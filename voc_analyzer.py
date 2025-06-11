# voc_analyzer.py (import 경로 수정)
import json
import pandas as pd
import numpy as np
from collections import Counter
from datetime import datetime
from typing import Dict, List, Tuple
import warnings
warnings.filterwarnings('ignore')

from output_manager import setup_output_dirs, get_analysis_filename

class CategoryBasedVoCAnalyzer:
    def __init__(self, json_file_path: str):
        """
        카테고리 기반 VoC 분석기 초기화
        
        Args:
            json_file_path: 크롤링된 JSON 파일 경로
        """
        self.json_file_path = json_file_path
        self.df = None
        
        # 유저 여정별 카테고리 매핑
        self.user_journey_mapping = {
            '계정·입점': [
                '입점관리', '스토어관리', '플랜관리', '신규회원가입',
                '사업자정보/양도양수', '탈퇴/재가입', '브랜드권한신청'
            ],
            '상품·콘텐츠': [
                '상품등록', '상품등록 실패', '상품 조회 및 수정', '채널상품연동',
                '브리치 기획전신청', '채널딜 진행관리', '상품문의(브리치)', '상품문의(채널)'
            ],
            '주문·배송': [
                '발주/발송관리', '배송현황관리', '배송지연 관리 (결품취소)',
                '송장등록 실패/ 송장번호 수정', '주문조회', '긴급문의', '배송정책 관리'
            ],
            '반품·취소': [
                '취소관리', '교환관리/교환철회', '반품관리/환불보류'
            ],
            '정산': [
                '구매확정관리', '정산통합', '특약매입정산', '판매대행정산'
            ]
        }
        
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
            
            if len(team_data) < 1:
                continue
            
            # 기본 정보
            basic_info = {
                'total_inquiries': len(team_data),
                'urgent_count': team_data['is_urgent'].sum() if 'is_urgent' in team_data.columns else 0,
                'answered_count': len(team_data[team_data['answer_status'] == '답변완료']) if 'answer_status' in team_data.columns else 0,
                'avg_content_length': round(team_data['content_length'].mean(), 1) if 'content_length' in team_data.columns else 0
            }
            
            # 대표 문의 사례들
            samples = []
            if 'content_length' in team_data.columns:
                sorted_data = team_data.sort_values('content_length')
                
                for quantile in [0.3, 0.7]:
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
                sub_cat_counts = team_data['sub_category'].value_counts().head(5)
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
            
            # 대표 문의 사례들
            samples = []
            sample_count = min(2, len(cat_data))
            for i in range(sample_count):
                sample = cat_data.iloc[i]
                samples.append({
                    'inquiry_id': sample.get('inquiry_id', 'N/A'),
                    'content': sample['question_content'][:150] + '...' if len(sample['question_content']) > 150 else sample['question_content'],
                    'assigned_team': sample.get('assigned_team', 'N/A'),
                    'length': sample.get('content_length', 0),
                    'is_urgent': sample.get('is_urgent', False)
                })
            
            category_analysis[category] = {
                'basic_info': basic_info,
                'team_distribution': team_distribution,
                'sample_inquiries': samples
            }
        
        return category_analysis

    def analyze_by_user_journey(self) -> Dict:
        """user_journey 기준 분석"""
        print("🎯 유저 여정별 실제 문의 내용 분석 중...")
        
        if 'sub_category' not in self.df.columns or 'question_content' not in self.df.columns:
            return {"error": "필요한 컬럼이 없습니다."}
        
        # 유저 여정별로 sub_category 매핑
        self.df['user_journey'] = self.df['sub_category'].apply(self._map_to_user_journey)
        
        journey_analysis = {}
        
        for journey in self.user_journey_mapping.keys():
            journey_data = self.df[self.df['user_journey'] == journey]
            
            if len(journey_data) < 1:
                continue
            
            # 기본 정보
            basic_info = {
                'total_inquiries': len(journey_data),
                'urgent_count': journey_data['is_urgent'].sum() if 'is_urgent' in journey_data.columns else 0,
                'answered_count': len(journey_data[journey_data['answer_status'] == '답변완료']) if 'answer_status' in journey_data.columns else 0,
                'avg_content_length': round(journey_data['content_length'].mean(), 1) if 'content_length' in journey_data.columns else 0
            }
            
            # 대표 문의 사례들
            samples = []
            if 'content_length' in journey_data.columns:
                sorted_data = journey_data.sort_values('content_length')
                
                for quantile in [0.3, 0.7]:
                    idx = int(len(sorted_data) * quantile)
                    if idx < len(sorted_data):
                        sample = sorted_data.iloc[idx]
                        samples.append({
                            'inquiry_id': sample.get('inquiry_id', 'N/A'),
                            'content': sample['question_content'],
                            'length': sample['content_length'],
                            'sub_category': sample.get('sub_category', 'N/A'),
                            'assigned_team': sample.get('assigned_team', 'N/A'),
                            'is_urgent': sample.get('is_urgent', False)
                        })
            
            # 세부 카테고리 분포
            sub_categories = {}
            if 'sub_category' in journey_data.columns:
                sub_cat_counts = journey_data['sub_category'].value_counts().head(5)
                sub_categories = sub_cat_counts.to_dict()
            
            # 담당팀 분포
            team_distribution = {}
            if 'assigned_team' in journey_data.columns:
                team_counts = journey_data['assigned_team'].value_counts()
                team_distribution = team_counts.to_dict()
            
            journey_analysis[journey] = {
                'basic_info': basic_info,
                'sample_inquiries': samples,
                'sub_categories': sub_categories,
                'team_distribution': team_distribution
            }
        
        return journey_analysis
    
    def _map_to_user_journey(self, sub_category):
        """세부 카테고리를 유저 여정으로 매핑"""
        if pd.isna(sub_category):
            return '기타'
        
        for journey, categories in self.user_journey_mapping.items():
            if sub_category in categories:
                return journey
        
        return '기타'

    def analyze_weekly_trends(self) -> Dict:
        """주간별 문의 트렌드"""
        print("📅 주간별 문의 트렌드 분석 중...")
        
        if 'registration_date' not in self.df.columns:
            return {"error": "registration_date 컬럼이 없습니다."}
        
        # 주간별 집계
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
        
        # 분석 실행
        if verbose:
            print("1️⃣ 팀별 분석...")
        results["team_analysis"] = self.analyze_by_assigned_team()
        
        if verbose:
            print("2️⃣ 세부 카테고리별 분석...")
        results["category_analysis"] = self.analyze_by_sub_category()
        
        if verbose:
            print("3️⃣ 유저 여정별 분석...")
        results["journey_analysis"] = self.analyze_by_user_journey()
        
        if verbose:
            print("4️⃣ 주간별 트렌드...")
        results["weekly_trends"] = self.analyze_weekly_trends()
        
        # 결과 저장 - output 폴더에!
        if verbose:
            output_file = get_analysis_filename()
            
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(results, f, ensure_ascii=False, indent=2, default=str)
            
            print(f"✅ 분석 결과 저장: {output_file}")
        
        return results

# 메인 실행 함수
def main():
    import os
    
    # output 폴더 설정
    setup_output_dirs()
    
    # JSON 파일 찾기 - 현재 폴더와 output/crawl_data/ 둘 다 확인
    json_files = []
    
    # 현재 폴더에서 찾기 (기존 파일들)
    current_files = [f for f in os.listdir('.') if f.endswith('.json') and 'qna' in f.lower()]
    json_files.extend(current_files)
    
    # output/crawl_data/ 폴더에서 찾기 (새로 생성된 파일들)
    crawl_dir = "output/crawl_data"
    if os.path.exists(crawl_dir):
        crawl_files = [os.path.join(crawl_dir, f) for f in os.listdir(crawl_dir) if f.endswith('.json')]
        json_files.extend(crawl_files)
    
    if not json_files:
        print("❌ Q&A JSON 파일을 찾을 수 없습니다.")
        return
    
    # 가장 최근 파일 선택
    json_file = max(json_files, key=os.path.getctime)
    print(f"📁 분석할 파일: {json_file}")
    
    try:
        # 분석기 초기화
        analyzer = CategoryBasedVoCAnalyzer(json_file)
        
        # 분석 실행
        results = analyzer.generate_category_voc_analysis(verbose=True)
        
        # HTML 보고서 생성 (수정된 import)
        try:
            from voc_html_reporter import CategoryVoCHTMLReporter
            
            html_reporter = CategoryVoCHTMLReporter(analyzer.df)
            html_filename = html_reporter.save_and_open_html_report(results)
            
            print(f"\n🎉 1단계 통합 분석 완료!")
            print(f"📊 분석 결과: output/analysis/")
            print(f"📄 HTML 보고서: output/reports/")
            
        except ImportError as e:
            print(f"HTML 리포터 import 오류: {e}")
            print("voc_html_reporter.py 파일이 있는지 확인해주세요.")
        
    except Exception as e:
        print(f"❌ 분석 중 오류: {e}")

if __name__ == "__main__":
    main()