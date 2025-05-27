import json
import pandas as pd
import numpy as np
from collections import Counter
from datetime import datetime
from typing import Dict, List, Tuple
import warnings
warnings.filterwarnings('ignore')

class CategoryBasedVoCAnalyzer:
    def __init__(self, json_file_path: str):
        """
        카테고리 기반 VoC 분석기 초기화
        
        Args:
            json_file_path: 크롤링된 JSON 파일 경로
        """
        self.json_file_path = json_file_path
        self.df = None
        self.load_and_preprocess_data()
        
    def load_and_preprocess_data(self):
        """데이터 로드 및 전처리"""
        try:
            with open(self.json_file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # 데이터 구조 확인
            if 'data' in data:
                qna_data = data['data']
            else:
                qna_data = data
            
            self.df = pd.DataFrame(qna_data)
            
            # 카테고리 정보 평탄화
            if 'category' in self.df.columns:
                category_df = pd.json_normalize(self.df['category'])
                self.df = pd.concat([self.df.drop('category', axis=1), category_df], axis=1)
            
            # 날짜 변환
            if 'registration_date' in self.df.columns:
                self.df['registration_date'] = pd.to_datetime(self.df['registration_date'], errors='coerce')
            
            # 텍스트 길이 계산
            if 'question_content' in self.df.columns:
                self.df['content_length'] = self.df['question_content'].str.len()
            
            print(f"✅ 데이터 로드 완료: {len(self.df)}개 문의")
            print(f"📊 사용 가능한 컬럼: {list(self.df.columns)}")
            
        except Exception as e:
            print(f"❌ 데이터 로드 실패: {e}")
            raise

    def analyze_by_assigned_team(self) -> Dict:
        """assigned_team 기준 분석"""
        print("🏢 팀별 실제 문의 내용 분석 중...")
        
        if 'assigned_team' not in self.df.columns or 'question_content' not in self.df.columns:
            return {"error": "필요한 컬럼이 없습니다."}
        
        team_analysis = {}
        
        for team in self.df['assigned_team'].dropna().unique():
            team_data = self.df[self.df['assigned_team'] == team]
            
            if len(team_data) < 3:  # 최소 3개 이상
                continue
            
            # 기본 정보
            basic_info = {
                'total_inquiries': len(team_data),
                'urgent_count': team_data['is_urgent'].sum() if 'is_urgent' in team_data.columns else 0,
                'answered_count': len(team_data[team_data['answer_status'] == '답변완료']) if 'answer_status' in team_data.columns else 0,
                'avg_content_length': round(team_data['content_length'].mean(), 1) if 'content_length' in team_data.columns else 0
            }
            
            # 대표 문의 사례들 (다양한 길이로 2개만)
            samples = []
            if 'content_length' in team_data.columns:
                sorted_data = team_data.sort_values('content_length')
                
                for quantile in [0.3, 0.7]:  # 2개만
                    idx = int(len(sorted_data) * quantile)
                    if idx < len(sorted_data):
                        sample = sorted_data.iloc[idx]
                        samples.append({
                            'inquiry_id': sample.get('inquiry_id', 'N/A'),
                            'content': sample['question_content'],
                            'length': sample['content_length'],
                            'sub_category': sample.get('sub_category', 'N/A'),
                            'is_urgent': sample.get('is_urgent', False)
                        })
            
            # 세부 카테고리 분포
            sub_categories = {}
            if 'sub_category' in team_data.columns:
                sub_cat_counts = team_data['sub_category'].value_counts().head(5)  # 상위 5개만
                sub_categories = sub_cat_counts.to_dict()
            
            team_analysis[team] = {
                'basic_info': basic_info,
                'sample_inquiries': samples,
                'sub_categories': sub_categories
            }
        
        return team_analysis

    def analyze_by_sub_category(self) -> Dict:
        """sub_category 기준 분석"""
        print("📂 세부 카테고리별 실제 문의 내용 분석 중...")
        
        if 'sub_category' not in self.df.columns or 'question_content' not in self.df.columns:
            return {"error": "필요한 컬럼이 없습니다."}
        
        category_analysis = {}
        
        for category in self.df['sub_category'].dropna().unique():
            cat_data = self.df[self.df['sub_category'] == category]
            
            if len(cat_data) < 3:
                continue
            
            # 기본 정보
            basic_info = {
                'total_inquiries': len(cat_data),
                'urgent_count': cat_data['is_urgent'].sum() if 'is_urgent' in cat_data.columns else 0,
                'avg_content_length': round(cat_data['content_length'].mean(), 1) if 'content_length' in cat_data.columns else 0
            }
            
            # 이 카테고리가 주로 어느 팀에서 처리되는지
            team_distribution = {}
            if 'assigned_team' in cat_data.columns:
                team_counts = cat_data['assigned_team'].value_counts()
                team_distribution = team_counts.to_dict()
            
            # 대표 문의 사례들 (2개만)
            samples = []
            for i in range(min(2, len(cat_data))):
                sample = cat_data.iloc[i]
                samples.append({
                    'inquiry_id': sample.get('inquiry_id', 'N/A'),
                    'content': sample['question_content'][:150] + '...' if len(sample['question_content']) > 150 else sample['question_content'],
                    'assigned_team': sample.get('assigned_team', 'N/A'),
                    'length': sample.get('content_length', 0)
                })
            
            category_analysis[category] = {
                'basic_info': basic_info,
                'team_distribution': team_distribution,
                'sample_inquiries': samples
            }
        
        return category_analysis

    def analyze_weekly_trends(self) -> Dict:
        """주간별 문의 트렌드"""
        print("📅 주간별 문의 트렌드 분석 중...")
        
        if 'registration_date' not in self.df.columns:
            return {"error": "registration_date 컬럼이 없습니다."}
        
        # 주간별 집계 (월요일 시작)
        self.df['year_week'] = self.df['registration_date'].dt.to_period('W-MON')
        weekly_stats = {}
        
        # 최근 12주간만 분석
        recent_weeks = self.df['year_week'].dropna().unique()
        recent_weeks = sorted(recent_weeks)[-12:]
        
        for week in recent_weeks:
            week_data = self.df[self.df['year_week'] == week]
            
            stats = {
                'total_inquiries': len(week_data),
                'urgent_count': week_data['is_urgent'].sum() if 'is_urgent' in week_data.columns else 0,
                'avg_content_length': round(week_data['content_length'].mean(), 1) if 'content_length' in week_data.columns else 0
            }
            
            # 팀별 분포 (상위 3개만)
            if 'assigned_team' in week_data.columns:
                team_dist = week_data['assigned_team'].value_counts().head(3).to_dict()
                stats['top_teams'] = team_dist
            
            weekly_stats[str(week)] = stats
        
        return weekly_stats

    def get_overall_summary(self) -> Dict:
        """전체 데이터 요약"""
        summary = {
            'total_inquiries': len(self.df),
            'date_range': {
                'start': str(self.df['registration_date'].min().date()) if 'registration_date' in self.df.columns else None,
                'end': str(self.df['registration_date'].max().date()) if 'registration_date' in self.df.columns else None
            }
        }
        
        # 팀 개수 및 목록
        if 'assigned_team' in self.df.columns:
            teams = self.df['assigned_team'].dropna().unique()
            summary['teams'] = {
                'count': len(teams),
                'list': teams.tolist()
            }
        
        # 카테고리 개수 및 목록
        if 'sub_category' in self.df.columns:
            categories = self.df['sub_category'].dropna().unique()
            summary['categories'] = {
                'count': len(categories),
                'list': categories.tolist()
            }
        
        # 기본 통계
        if 'is_urgent' in self.df.columns:
            summary['urgent_count'] = int(self.df['is_urgent'].sum())
        
        if 'answer_status' in self.df.columns:
            answer_stats = self.df['answer_status'].value_counts().to_dict()
            summary['answer_status_distribution'] = answer_stats
        
        if 'content_length' in self.df.columns:
            summary['content_length_stats'] = {
                'mean': round(self.df['content_length'].mean(), 1),
                'median': round(self.df['content_length'].median(), 1),
                'min': int(self.df['content_length'].min()),
                'max': int(self.df['content_length'].max())
            }
        
        return summary

    def generate_category_voc_analysis(self, verbose=False) -> Dict:
        """카테고리 기반 VoC 분석 실행"""
        if verbose:
            print("🎯 카테고리 기반 VoC 분석 시작...")
        
        results = {
            "analysis_timestamp": datetime.now().isoformat(),
            "data_source": self.json_file_path,
            "overall_summary": self.get_overall_summary()
        }
        
        # 1. 팀별 분석
        if verbose:
            print("1️⃣ 팀별 분석...")
        results["team_analysis"] = self.analyze_by_assigned_team()
        
        # 2. 세부 카테고리별 분석
        if verbose:
            print("2️⃣ 세부 카테고리별 분석...")
        results["category_analysis"] = self.analyze_by_sub_category()
        
        # 3. 주간별 트렌드
        if verbose:
            print("3️⃣ 주간별 트렌드...")
        results["weekly_trends"] = self.analyze_weekly_trends()
        
        # 결과 저장
        if verbose:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"category_voc_analysis_{timestamp}.json"
            
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(results, f, ensure_ascii=False, indent=2, default=str)
            
            print(f"✅ 카테고리 VoC 분석 결과 저장: {output_file}")
        
        return results

    def create_summary_dashboard(self) -> str:
        """간단한 요약 대시보드"""
        summary = self.get_overall_summary()
        
        dashboard = f"""
        ╔══════════════════════════════════════════════════════════════╗
        ║                📊 카테고리 기반 VoC 분석                        ║
        ╠══════════════════════════════════════════════════════════════╣
        ║ 📈 데이터 개요                                                ║
        ║   • 총 문의: {summary['total_inquiries']:,}건                      ║
        ║   • 분석 기간: {summary['date_range']['start']} ~ {summary['date_range']['end']} ║
        ║   • 담당팀: {summary.get('teams', {}).get('count', 0)}개                ║
        ║   • 세부카테고리: {summary.get('categories', {}).get('count', 0)}개          ║
        """
        
        if 'urgent_count' in summary:
            dashboard += f"║   • 긴급 문의: {summary['urgent_count']}건                        ║\n"
        
        if 'content_length_stats' in summary:
            avg_length = summary['content_length_stats']['mean']
            dashboard += f"║   • 평균 문의 길이: {avg_length}자                          ║\n"
        
        dashboard += """║                                                              ║
        ║ 🎯 분석 내용                                                  ║
        ║   • 팀별 실제 문의 내용 및 키워드                              ║
        ║   • 세부 카테고리별 문의 특성                                  ║
        ║   • 주간별 문의 트렌드                                        ║
        ║   • 대표 문의 사례                                            ║
        ╚══════════════════════════════════════════════════════════════╝
        """
        
        return dashboard

# 메인 실행 함수
def main():
    import os
    
    # JSON 파일 찾기
    json_files = [f for f in os.listdir('.') if f.endswith('.json') and 'qna' in f.lower()]
    
    if not json_files:
        print("❌ Q&A JSON 파일을 찾을 수 없습니다.")
        return
    
    # 가장 최근 파일 선택
    json_file = max(json_files, key=os.path.getctime)
    print(f"📁 분석할 파일: {json_file}")
    
    try:
        # 카테고리 기반 VoC 분석기 초기화
        analyzer = CategoryBasedVoCAnalyzer(json_file)
        
        # 대시보드 출력
        print(analyzer.create_summary_dashboard())
        
        # 카테고리 기반 VoC 분석 실행
        results = analyzer.generate_category_voc_analysis(verbose=True)
        
        # HTML 보고서 생성
        try:
            from voc_html_reporter import CategoryVoCHTMLReporter
            
            html_reporter = CategoryVoCHTMLReporter(analyzer.df)
            html_filename = html_reporter.save_and_open_html_report(results)
            
            print(f"\n🎉 카테고리 기반 VoC 분석 완료!")
            print(f"📄 HTML 보고서: {html_filename}")
            
        except ImportError:
            print("HTML 리포터를 찾을 수 없습니다. voc_html_reporter.py 파일을 확인해주세요.")
        
        print("\n💡 분석 결과 요약:")
        
        if 'team_analysis' in results:
            team_count = len(results['team_analysis'])
            print(f"📊 분석된 팀: {team_count}개")
            
            if results['team_analysis']:
                # 가장 문의가 많은 팀
                max_team = max(results['team_analysis'].items(), 
                             key=lambda x: x[1]['basic_info']['total_inquiries'])
                print(f"📈 최다 문의 팀: {max_team[0]} ({max_team[1]['basic_info']['total_inquiries']}건)")
        
        if 'category_analysis' in results:
            cat_count = len(results['category_analysis'])
            print(f"📂 분석된 세부카테고리: {cat_count}개")
        
        if 'weekly_trends' in results:
            week_count = len(results['weekly_trends'])
            print(f"📅 분석된 주간: {week_count}주")
        
    except Exception as e:
        print(f"❌ 분석 중 오류: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()