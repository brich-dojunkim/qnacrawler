import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import webbrowser
import os
from datetime import datetime
from typing import Dict

# 한글 폰트 설정
plt.rcParams['font.family'] = ['DejaVu Sans', 'Arial Unicode MS', 'AppleGothic']
plt.rcParams['axes.unicode_minus'] = False

class CategoryVoCHTMLReporter:
    def __init__(self, df: pd.DataFrame):
        """
        카테고리 기반 VoC HTML 보고서 생성기 초기화
        
        Args:
            df: VoC 분석이 완료된 DataFrame
        """
        self.df = df

    def create_chart_base64(self, fig) -> str:
        """matplotlib 차트를 base64 인코딩된 이미지로 변환"""
        buffer = BytesIO()
        fig.savefig(buffer, format='png', dpi=150, bbox_inches='tight')
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.getvalue()).decode()
        buffer.close()
        plt.close(fig)
        return f"data:image/png;base64,{image_base64}"

    def generate_charts(self, results: Dict) -> Dict:
        """분석 결과를 위한 차트들 생성"""
        charts = {}
        
        # 1. 팀별 문의 건수 차트 (세로 바차트)
        if 'team_analysis' in results:
            team_data = results['team_analysis']
            
            if team_data:
                fig, ax = plt.subplots(figsize=(8, 5))
                
                teams = list(team_data.keys())
                counts = [team_data[team]['basic_info']['total_inquiries'] for team in teams]
                
                bars = ax.bar(range(len(teams)), counts, color='steelblue', alpha=0.8, edgecolor='navy', linewidth=0.5)
                
                # 막대 위에 값 표시
                for i, bar in enumerate(bars):
                    height = bar.get_height()
                    ax.text(bar.get_x() + bar.get_width()/2., height,
                           f'{int(height)}', ha='center', va='bottom', fontsize=10, fontweight='bold')
                
                ax.set_title('팀별 문의 분포', fontsize=12, fontweight='bold', pad=15)
                ax.set_ylabel('건수', fontsize=11)
                ax.set_xlabel('팀', fontsize=11)
                
                # x축 라벨 설정
                ax.set_xticks(range(len(teams)))
                ax.set_xticklabels(teams, rotation=45, ha='right', fontsize=10)
                ax.grid(True, alpha=0.3, axis='y')
                
                # y축 시작을 0으로 설정
                ax.set_ylim(bottom=0)
                
                plt.tight_layout()
                charts['team_overview'] = self.create_chart_base64(fig)

        # 1-2. 유저 여정별 문의 건수 차트 (세로 바차트)
        if 'journey_analysis' in results:
            journey_data = results['journey_analysis']
            
            if journey_data:
                fig, ax = plt.subplots(figsize=(8, 5))
                
                journeys = list(journey_data.keys())
                counts = [journey_data[journey]['basic_info']['total_inquiries'] for journey in journeys]
                
                bars = ax.bar(range(len(journeys)), counts, color='#10b981', alpha=0.8, edgecolor='#059669', linewidth=0.5)
                
                # 막대 위에 값 표시
                for i, bar in enumerate(bars):
                    height = bar.get_height()
                    ax.text(bar.get_x() + bar.get_width()/2., height,
                           f'{int(height)}', ha='center', va='bottom', fontsize=10, fontweight='bold')
                
                ax.set_title('유저 여정별 문의 분포', fontsize=12, fontweight='bold', pad=15)
                ax.set_ylabel('건수', fontsize=11)
                ax.set_xlabel('유저 여정', fontsize=11)
                
                # x축 라벨 설정
                ax.set_xticks(range(len(journeys)))
                ax.set_xticklabels(journeys, rotation=45, ha='right', fontsize=10)
                ax.grid(True, alpha=0.3, axis='y')
                
                # y축 시작을 0으로 설정
                ax.set_ylim(bottom=0)
                
                plt.tight_layout()
                charts['journey_overview'] = self.create_chart_base64(fig)

        # 2. 주간별 문의 트렌드 (세로 바 차트로 변경)
        if 'weekly_trends' in results:
            weekly_data = results['weekly_trends']
            
            if weekly_data:
                fig, ax = plt.subplots(figsize=(10, 5))
                
                weeks = list(weekly_data.keys())
                counts = [weekly_data[week]['total_inquiries'] for week in weeks]
                
                # 실제 날짜 라벨 생성
                date_labels = []
                for week_str in weeks:
                    try:
                        # Period 문자열을 파싱하여 실제 날짜로 변환
                        week_period = pd.Period(week_str, freq='W-MON')
                        start_date = week_period.start_time
                        end_date = week_period.end_time
                        date_labels.append(f"{start_date.strftime('%m/%d')}-{end_date.strftime('%m/%d')}")
                    except:
                        # 파싱 실패시 기존 방식
                        date_labels.append(f'W{len(date_labels)+1}')
                
                # 세로 바 차트 생성
                bars = ax.bar(range(len(weeks)), counts, color='steelblue', alpha=0.8, edgecolor='navy', linewidth=0.5)
                
                # 막대 위에 값 표시
                for i, bar in enumerate(bars):
                    height = bar.get_height()
                    ax.text(bar.get_x() + bar.get_width()/2., height,
                           f'{int(height)}', ha='center', va='bottom', fontsize=9, fontweight='bold')
                
                ax.set_title('주간별 문의 건수 추이', fontsize=12, fontweight='bold', pad=15)
                ax.set_ylabel('건수', fontsize=11)
                ax.set_xlabel('주간', fontsize=11)
                
                # x축 라벨을 실제 날짜로 설정
                ax.set_xticks(range(len(weeks)))
                ax.set_xticklabels(date_labels, rotation=45, ha='right', fontsize=9)
                ax.grid(True, alpha=0.3, axis='y')
                
                # y축 시작을 0으로 설정
                ax.set_ylim(bottom=0)
                
                plt.tight_layout()
                charts['weekly_trend'] = self.create_chart_base64(fig)

        # 3. 팀별 세부 카테고리 분포 시각화 (세로 바차트로 변경)
        if 'team_analysis' in results:
            team_data = results['team_analysis']
            
            # 각 팀별로 세부 카테고리 분포 차트 생성
            team_category_charts = {}
            
            for team_name, team_info in team_data.items():
                if team_info['sub_categories']:
                    fig, ax = plt.subplots(figsize=(8, 5))
                    
                    categories = list(team_info['sub_categories'].keys())[:5]  # 상위 5개
                    values = list(team_info['sub_categories'].values())[:5]
                    
                    # 세로 바 차트 생성
                    bars = ax.bar(range(len(categories)), values, color='steelblue', alpha=0.8, edgecolor='navy', linewidth=0.5)
                    
                    # 막대 위에 값 표시
                    for i, bar in enumerate(bars):
                        height = bar.get_height()
                        ax.text(bar.get_x() + bar.get_width()/2., height,
                               f'{int(height)}', ha='center', va='bottom', fontsize=9, fontweight='bold')
                    
                    ax.set_title(f'세부 카테고리 분포', fontsize=11, fontweight='bold', pad=15)
                    ax.set_ylabel('건수', fontsize=10)
                    ax.set_xlabel('카테고리', fontsize=10)
                    
                    # x축 라벨 설정
                    ax.set_xticks(range(len(categories)))
                    ax.set_xticklabels(categories, rotation=45, ha='right', fontsize=9)
                    ax.grid(True, alpha=0.3, axis='y')
                    
                    # y축 시작을 0으로 설정
                    ax.set_ylim(bottom=0)
                    
                    plt.tight_layout()
                    team_category_charts[team_name] = self.create_chart_base64(fig)
            
            charts['team_categories'] = team_category_charts

        # 4. 유저 여정별 세부 카테고리 분포 시각화 (세로 바차트)
        if 'journey_analysis' in results:
            journey_data = results['journey_analysis']
            
            # 각 여정별로 세부 카테고리 분포 차트 생성
            journey_category_charts = {}
            
            for journey_name, journey_info in journey_data.items():
                if journey_info['sub_categories']:
                    fig, ax = plt.subplots(figsize=(8, 5))
                    
                    categories = list(journey_info['sub_categories'].keys())[:5]  # 상위 5개
                    values = list(journey_info['sub_categories'].values())[:5]
                    
                    # 세로 바 차트 생성
                    bars = ax.bar(range(len(categories)), values, color='#10b981', alpha=0.8, edgecolor='#059669', linewidth=0.5)
                    
                    # 막대 위에 값 표시
                    for i, bar in enumerate(bars):
                        height = bar.get_height()
                        ax.text(bar.get_x() + bar.get_width()/2., height,
                               f'{int(height)}', ha='center', va='bottom', fontsize=9, fontweight='bold')
                    
                    ax.set_title(f'세부 카테고리 분포', fontsize=11, fontweight='bold', pad=15)
                    ax.set_ylabel('건수', fontsize=10)
                    ax.set_xlabel('카테고리', fontsize=10)
                    
                    # x축 라벨 설정
                    ax.set_xticks(range(len(categories)))
                    ax.set_xticklabels(categories, rotation=45, ha='right', fontsize=9)
                    ax.grid(True, alpha=0.3, axis='y')
                    
                    # y축 시작을 0으로 설정
                    ax.set_ylim(bottom=0)
                    
                    plt.tight_layout()
                    journey_category_charts[journey_name] = self.create_chart_base64(fig)
            
            charts['journey_categories'] = journey_category_charts

        return charts

    def _get_journey_for_category(self, category_name):
        """세부 카테고리를 유저 여정으로 매핑하는 간단한 함수"""
        journey_mapping = {
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
        
        for journey, categories in journey_mapping.items():
            if category_name in categories:
                return journey
        
        return '기타'

    def generate_html_report(self, results: Dict) -> str:
        """HTML 보고서 생성"""
        print("🌐 카테고리 기반 HTML 보고서 생성 중...")
        
        # 차트 생성
        charts = self.generate_charts(results)
        
        # 기본 정보
        overall_summary = results.get('overall_summary', {})
        total_inquiries = overall_summary.get('total_inquiries', 0)
        analysis_date = results.get('analysis_timestamp', datetime.now().isoformat())
        
        # HTML 시작
        html_parts = []
        
        # HTML 헤더
        html_parts.append("""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>카테고리 기반 VoC 분석 보고서</title>
    <link href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" rel="stylesheet">
    <style>
        body {
            font-family: 'Pretendard', -apple-system, sans-serif;
            margin: 0;
            padding: 1rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        .container {
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 16px;
            box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1);
            overflow: hidden;
        }
        .header {
            background: linear-gradient(135deg, #2563eb 0%, #3b82f6 100%);
            color: white;
            padding: 2rem;
            text-align: center;
        }
        .header h1 {
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }
        .main-content {
            padding: 2rem;
        }
        .major-section {
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            margin-bottom: 2rem;
            box-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1);
        }
        .major-section-header {
            background: #f8fafc;
            padding: 1.5rem;
            border-bottom: 1px solid #e2e8f0;
        }
        .major-section-header h2 {
            font-size: 1.5rem;
            font-weight: 600;
            margin: 0;
        }
        .major-section-content {
            padding: 1.5rem;
        }
        .entity-card {
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 1.5rem;
            transition: all 0.2s ease;
        }
        .entity-card:hover {
            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
            transform: translateY(-2px);
        }
        .entity-card-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 1rem;
            padding-bottom: 0.75rem;
            border-bottom: 1px solid #e2e8f0;
        }
        .entity-card-title {
            font-size: 1.125rem;
            font-weight: 600;
            margin: 0;
        }
        .entity-card-badge {
            background: #2563eb;
            color: white;
            padding: 0.25rem 0.75rem;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: 500;
        }
        .grid {
            display: grid;
            gap: 1.5rem;
        }
        .grid-3 {
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        }
        .grid-4 {
            grid-template-columns: repeat(4, 1fr);
        }
        .grid-5 {
            grid-template-columns: repeat(5, 1fr);
        }
        .stats-list {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        .stats-list li {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0.75rem 0;
            border-bottom: 1px solid #e2e8f0;
        }
        .stats-list li:last-child {
            border-bottom: none;
        }
        .stat-name {
            font-size: 0.875rem;
            color: #475569;
        }
        .stat-number {
            font-size: 1.25rem;
            font-weight: 700;
            color: #2563eb;
        }
        .metrics-list {
            list-style: none;
            padding: 0;
            margin: 1rem 0;
        }
        .metrics-list li {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0.5rem 0;
            border-bottom: 1px solid #f1f5f9;
        }
        .metrics-list li:last-child {
            border-bottom: none;
        }
        .metric-name {
            font-size: 0.8rem;
            color: #64748b;
        }
        .metric-number {
            font-size: 1rem;
            font-weight: 600;
            color: #2563eb;
        }
        .modal-trigger {
            width: 100%;
            background: #2563eb;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.75rem;
            margin-top: 1rem;
            font-size: 0.875rem;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .modal-trigger:hover {
            background: #1d4ed8;
        }
        .modal-overlay {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.5);
            z-index: 1000;
            justify-content: center;
            align-items: center;
        }
        .modal-overlay.active {
            display: flex;
        }
        .modal-content {
            background: white;
            border-radius: 12px;
            width: 90%;
            max-width: 800px;
            max-height: 80vh;
            overflow: hidden;
            box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1);
        }
        .modal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1.5rem;
            border-bottom: 1px solid #e2e8f0;
            background: #f8fafc;
        }
        .modal-title {
            font-size: 1.25rem;
            font-weight: 600;
            color: #374151;
        }
        .modal-close {
            background: none;
            border: none;
            font-size: 1.5rem;
            cursor: pointer;
            color: #6b7280;
            padding: 0.25rem;
        }
        .modal-close:hover {
            color: #374151;
        }
        .modal-body {
            padding: 1.5rem;
            max-height: 60vh;
            overflow-y: auto;
        }
        .inquiry-card {
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 1rem;
            margin-bottom: 1rem;
            background: #f8fafc;
        }
        .inquiry-card:last-child {
            margin-bottom: 0;
        }
        .inquiry-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 0.75rem;
            font-size: 0.875rem;
            color: #6b7280;
        }
        .inquiry-content {
            color: #374151;
            line-height: 1.5;
            font-size: 0.95rem;
        }
        .urgency-badge {
            padding: 0.25rem 0.5rem;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: 500;
        }
        .urgency-urgent {
            background: #fee2e2;
            color: #dc2626;
        }
        .urgency-normal {
            background: #f0f9ff;
            color: #0369a1;
        }
        .filter-buttons {
            display: flex;
            gap: 0.5rem;
            margin-bottom: 1.5rem;
            justify-content: center;
        }
        .filter-btn {
            padding: 0.5rem 1rem;
            border: 2px solid #e2e8f0;
            background: white;
            border-radius: 8px;
            cursor: pointer;
            font-size: 0.875rem;
            font-weight: 500;
            color: #475569;
            transition: all 0.2s ease;
        }
        .filter-btn:hover {
            border-color: #2563eb;
            color: #2563eb;
        }
        .filter-btn.active {
            background: #2563eb;
            border-color: #2563eb;
            color: white;
        }
        .journey-badge {
            background: #10b981;
            color: white;
            padding: 0.25rem 0.5rem;
            border-radius: 9999px;
            font-size: 0.75rem;
        }
        .chart-container {
            text-align: center;
            background: white;
            border-radius: 12px;
            padding: 1rem;
            border: 1px solid #e2e8f0;
        }
        .chart-container img {
            max-width: 100%;
            height: auto;
            border-radius: 12px;
        }
        .sub-card {
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
        }
        .subsection-title {
            font-size: 1rem;
            font-weight: 600;
            margin-bottom: 1rem;
        }
        .small-subsection-title {
            font-size: 0.875rem;
            font-weight: 600;
            margin-bottom: 0.75rem;
        }
        .team-badges {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin: 0.75rem 0;
        }
        .team-badge {
            background: #f59e0b;
            color: white;
            padding: 0.25rem 0.75rem;
            border-radius: 9999px;
            font-size: 0.75rem;
        }
        .inquiry-sample {
            background: #f8fafc;
            border-left: 4px solid #2563eb;
            padding: 1rem;
            margin: 0.75rem 0;
            border-radius: 0 12px 12px 0;
            font-style: italic;
        }
        .inquiry-meta {
            font-size: 0.8rem;
            color: #475569;
            margin-top: 0.5rem;
            font-style: normal;
        }
        .footer {
            text-align: center;
            padding: 2rem;
            background: #f8fafc;
            border-top: 1px solid #e2e8f0;
            color: #475569;
            font-size: 0.875rem;
        }
        @media (max-width: 1200px) {
            .grid-4 { grid-template-columns: repeat(2, 1fr); }
            .grid-5 { grid-template-columns: repeat(3, 1fr); }
        }
        @media (max-width: 768px) {
            .main-content { padding: 1rem; }
            .grid-3, .grid-4, .grid-5 { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>카테고리 기반 VoC 분석</h1>
            <p>고객 문의 데이터의 카테고리별 분석 결과</p>""")
        
        # 날짜 추가
        formatted_date = analysis_date[:19].replace('T', ' ')
        html_parts.append(f'            <p>{formatted_date}</p>')
        
        html_parts.append("""        </div>
        <div class="main-content">
            <div class="major-section">
                <div class="major-section-header">
                    <h2>분석 개요</h2>
                </div>
                <div class="major-section-content">
                    <div class="grid grid-4">
                        <div class="entity-card">
                            <div class="entity-card-header">
                                <h3 class="entity-card-title">데이터 현황</h3>""")
        
        # 총 문의 수 배지
        html_parts.append(f'                                <span class="entity-card-badge">{total_inquiries:,}건</span>')
        
        html_parts.append("""                            </div>
                            <ul class="stats-list">""")
        
        # 기본 통계
        html_parts.append(f"""                                <li>
                                    <span class="stat-name">총 문의</span>
                                    <span class="stat-number">{total_inquiries:,}</span>
                                </li>""")
        
        if 'teams' in overall_summary:
            team_count = overall_summary['teams']['count']
            html_parts.append(f"""                                <li>
                                    <span class="stat-name">담당팀</span>
                                    <span class="stat-number">{team_count}</span>
                                </li>""")
        
        if 'categories' in overall_summary:
            cat_count = overall_summary['categories']['count']
            html_parts.append(f"""                                <li>
                                    <span class="stat-name">카테고리</span>
                                    <span class="stat-number">{cat_count}</span>
                                </li>""")
        
        if 'urgent_count' in overall_summary:
            urgent_count = overall_summary['urgent_count']
            html_parts.append(f"""                                <li>
                                    <span class="stat-name">긴급 문의</span>
                                    <span class="stat-number">{urgent_count}</span>
                                </li>""")
        
        html_parts.append("""                            </ul>
                        </div>
                        <div class="entity-card">
                            <div class="entity-card-header">
                                <h3 class="entity-card-title">주간별 트렌드</h3>
                                <span class="entity-card-badge">최근 12주</span>
                            </div>
                            <ul class="stats-list" style="margin-bottom: 1rem;">""")
        
        # 주간별 트렌드 통계
        if 'weekly_trends' in results:
            weekly_data = results['weekly_trends']
            week_counts = [weekly_data[week]['total_inquiries'] for week in weekly_data.keys()]
            if week_counts:
                avg_weekly = sum(week_counts) / len(week_counts)
                max_weekly = max(week_counts)
                html_parts.append(f"""                                <li>
                                    <span class="stat-name">주간 평균</span>
                                    <span class="stat-number">{avg_weekly:.0f}</span>
                                </li>
                                <li>
                                    <span class="stat-name">최대 주간</span>
                                    <span class="stat-number">{max_weekly}</span>
                                </li>""")
        
        html_parts.append("""                            </ul>
                            <div class="chart-container">""")
        
        # 주간별 트렌드 차트
        if 'weekly_trend' in charts:
            html_parts.append(f'                                <img src="{charts["weekly_trend"]}" alt="주간별 트렌드">')
        
        html_parts.append("""                            </div>
                        </div>
                        <div class="entity-card">
                            <div class="entity-card-header">
                                <h3 class="entity-card-title">팀별 분포</h3>""")
        
        # 팀 개수 배지
        if 'teams' in overall_summary:
            team_count = overall_summary['teams']['count']
            html_parts.append(f'                                <span class="entity-card-badge">{team_count}개 팀</span>')
        
        html_parts.append("""                            </div>
                            <ul class="stats-list" style="margin-bottom: 1rem;">""")
        
        # 팀별 분포 통계
        if 'team_analysis' in results:
            team_data = results['team_analysis']
            if team_data:
                team_counts = [team_data[team]['basic_info']['total_inquiries'] for team in team_data.keys()]
                avg_team = sum(team_counts) / len(team_counts)
                max_team = max(team_counts)
                html_parts.append(f"""                                <li>
                                    <span class="stat-name">팀 평균</span>
                                    <span class="stat-number">{avg_team:.0f}</span>
                                </li>
                                <li>
                                    <span class="stat-name">최대 팀</span>
                                    <span class="stat-number">{max_team}</span>
                                </li>""")
        
        html_parts.append("""                            </ul>
                            <div class="chart-container">""")
        
        # 팀별 분포 차트
        if 'team_overview' in charts:
            html_parts.append(f'                                <img src="{charts["team_overview"]}" alt="팀별 분포">')

        html_parts.append("""                            </div>
                        </div>
                        <div class="entity-card">
                            <div class="entity-card-header">
                                <h3 class="entity-card-title">유저 여정별 분포</h3>""")
        
        # 유저 여정 개수 배지
        if 'journey_analysis' in results:
            journey_count = len(results['journey_analysis'])
            html_parts.append(f'                                <span class="entity-card-badge">{journey_count}개 여정</span>')
        
        html_parts.append("""                            </div>
                            <ul class="stats-list" style="margin-bottom: 1rem;">""")
        
        # 유저 여정별 분포 통계
        if 'journey_analysis' in results:
            journey_data = results['journey_analysis']
            if journey_data:
                journey_counts = [journey_data[journey]['basic_info']['total_inquiries'] for journey in journey_data.keys()]
                avg_journey = sum(journey_counts) / len(journey_counts)
                max_journey = max(journey_counts)
                html_parts.append(f"""                                <li>
                                    <span class="stat-name">여정 평균</span>
                                    <span class="stat-number">{avg_journey:.0f}</span>
                                </li>
                                <li>
                                    <span class="stat-name">최대 여정</span>
                                    <span class="stat-number">{max_journey}</span>
                                </li>""")
        
        html_parts.append("""                            </ul>
                            <div class="chart-container">""")
        
        # 유저 여정별 분포 차트
        if 'journey_overview' in charts:
            html_parts.append(f'                                <img src="{charts["journey_overview"]}" alt="유저 여정별 분포">')
        
        html_parts.append("""                            </div>
                        </div>
                    </div>
                </div>
            </div>""")
        
        # 팀별 분석 섹션
        if 'team_analysis' in results and results['team_analysis']:
            html_parts.append("""            <div class="major-section">
                <div class="major-section-header">
                    <h2>팀별 문의 내용 분석</h2>
                </div>
                <div class="major-section-content">
                    <div class="grid grid-4">""")
            
            for team_name, team_info in results['team_analysis'].items():
                basic_info = team_info['basic_info']
                
                html_parts.append(f"""                        <div class="entity-card">
                            <div class="entity-card-header">
                                <h3 class="entity-card-title">{team_name}</h3>
                                <span class="entity-card-badge">{basic_info['total_inquiries']}건</span>
                            </div>
                            <ul class="metrics-list">
                                <li>
                                    <span class="metric-name">총 문의</span>
                                    <span class="metric-number">{basic_info['total_inquiries']}</span>
                                </li>
                                <li>
                                    <span class="metric-name">긴급</span>
                                    <span class="metric-number">{basic_info['urgent_count']}</span>
                                </li>
                                <li>
                                    <span class="metric-name">답변완료</span>
                                    <span class="metric-number">{basic_info['answered_count']}</span>
                                </li>
                                <li>
                                    <span class="metric-name">평균길이</span>
                                    <span class="metric-number">{basic_info['avg_content_length']:.0f}</span>
                                </li>
                            </ul>""")
                
                # 세부 카테고리 분포 차트 (별도 카드 없이)
                if 'team_categories' in charts and team_name in charts['team_categories']:
                    html_parts.append(f"""                            <div style="margin-top: 1rem;">
                                <h4 style="font-size: 0.9rem; font-weight: 600; margin-bottom: 0.75rem;">세부 카테고리 분포</h4>
                                <div class="chart-container" style="margin: 0; padding: 0.5rem;">
                                    <img src="{charts['team_categories'][team_name]}" alt="{team_name} 카테고리 분포">
                                </div>
                            </div>""")
                
                html_parts.append("""                        </div>""")
            
            html_parts.append("""                    </div>
                </div>
            </div>""")
            
            # 유저 여정별 모달들 추가
            for journey_name, journey_info in results['journey_analysis'].items():
                basic_info = journey_info['basic_info']
                modal_id = f"journey-modal-{journey_name.replace(' ', '-').replace('·', '-')}"
                
                html_parts.append(f"""            <div class="modal-overlay" id="{modal_id}" onclick="closeModal('{modal_id}')">
                <div class="modal-content" onclick="event.stopPropagation()">
                    <div class="modal-header">
                        <h3 class="modal-title">{journey_name} - 전체 {basic_info['total_inquiries']}건</h3>
                        <button class="modal-close" onclick="closeModal('{modal_id}')">&times;</button>
                    </div>
                    <div class="modal-body">""")
                
                # 전체 문의 내용 표시 (샘플 데이터 사용)
                for i, sample in enumerate(journey_info['sample_inquiries']):
                    urgency_class = "urgency-urgent" if sample.get('is_urgent', False) else "urgency-normal"
                    urgency_text = "긴급" if sample.get('is_urgent', False) else "일반"
                    
                    html_parts.append(f"""                        <div class="inquiry-card">
                            <div class="inquiry-header">
                                <span>{sample['assigned_team']} | {sample['sub_category']}</span>
                                <span class="urgency-badge {urgency_class}">{urgency_text}</span>
                            </div>
                            <div class="inquiry-content">{sample['content']}</div>
                        </div>""")
                
                # 더 많은 데이터가 있는 경우 표시
                if basic_info['total_inquiries'] > len(journey_info['sample_inquiries']):
                    remaining = basic_info['total_inquiries'] - len(journey_info['sample_inquiries'])
                    html_parts.append(f"""                        <div style="text-align: center; padding: 1rem; color: #6b7280; font-style: italic;">
                            ... 및 {remaining}건의 추가 문의가 있습니다
                        </div>""")
                
                html_parts.append("""                    </div>
                </div>
            </div>""")
        
        # 유저 여정별 분석 섹션
        if 'journey_analysis' in results and results['journey_analysis']:
            html_parts.append("""            <div class="major-section">
                <div class="major-section-header">
                    <h2>유저 여정별 문의 내용 분석</h2>
                </div>
                <div class="major-section-content">
                    <div class="grid grid-3">""")
            
            for journey_name, journey_info in results['journey_analysis'].items():
                basic_info = journey_info['basic_info']
                
                html_parts.append(f"""                        <div class="entity-card">
                            <div class="entity-card-header">
                                <h3 class="entity-card-title">{journey_name}</h3>
                                <span class="entity-card-badge">{basic_info['total_inquiries']}건</span>
                            </div>
                            <ul class="metrics-list">
                                <li>
                                    <span class="metric-name">총 문의</span>
                                    <span class="metric-number">{basic_info['total_inquiries']}</span>
                                </li>
                                <li>
                                    <span class="metric-name">긴급</span>
                                    <span class="metric-number">{basic_info['urgent_count']}</span>
                                </li>
                                <li>
                                    <span class="metric-name">답변완료</span>
                                    <span class="metric-number">{basic_info['answered_count']}</span>
                                </li>
                                <li>
                                    <span class="metric-name">평균길이</span>
                                    <span class="metric-number">{basic_info['avg_content_length']:.0f}</span>
                                </li>
                            </ul>""")
                
                # 세부 카테고리 분포 차트 (별도 카드 없이)
                if 'journey_categories' in charts and journey_name in charts['journey_categories']:
                    html_parts.append(f"""                            <div style="margin-top: 1rem;">
                                <h4 style="font-size: 0.9rem; font-weight: 600; margin-bottom: 0.75rem;">세부 카테고리 분포</h4>
                                <div class="chart-container" style="margin: 0; padding: 0.5rem;">
                                    <img src="{charts['journey_categories'][journey_name]}" alt="{journey_name} 카테고리 분포">
                                </div>
                            </div>""")
                
                # 모달 버튼 추가
                journey_modal_id = f"journey-modal-{journey_name.replace(' ', '-').replace('·', '-')}"
                html_parts.append(f"""                            <button class="modal-trigger" onclick="openModal('{journey_modal_id}')">
                                문의 내용 보기 ({basic_info['total_inquiries']}건)
                            </button>
                        </div>""")
            
            html_parts.append("""                    </div>
                </div>
            </div>""")
        
        # 세부 카테고리별 분석 섹션
        if 'category_analysis' in results and results['category_analysis']:
            sorted_categories = sorted(results['category_analysis'].items(), 
                                     key=lambda x: x[1]['basic_info']['total_inquiries'], 
                                     reverse=True)[:12]
            
            html_parts.append("""            <div class="major-section">
                <div class="major-section-header">
                    <h2>세부 카테고리별 문의 내용</h2>
                </div>
                <div class="major-section-content">
                    <div class="grid grid-3">""")
            
            for category_name, category_info in sorted_categories:
                basic_info = category_info['basic_info']
                
                html_parts.append(f"""                        <div class="entity-card">
                            <div class="entity-card-header">
                                <h3 class="entity-card-title" style="font-size: 1rem; line-height: 1.4;">{category_name}</h3>
                                <span class="entity-card-badge">{basic_info['total_inquiries']}건</span>
                            </div>
                            <ul class="metrics-list">
                                <li>
                                    <span class="metric-name">총 문의</span>
                                    <span class="metric-number">{basic_info['total_inquiries']}</span>
                                </li>
                                <li>
                                    <span class="metric-name">긴급</span>
                                    <span class="metric-number">{basic_info['urgent_count']}</span>
                                </li>
                                <li>
                                    <span class="metric-name">평균길이</span>
                                    <span class="metric-number">{basic_info['avg_content_length']:.0f}</span>
                                </li>
                            </ul>
                            <div style="margin: 1rem 0;">
                                <h4 class="small-subsection-title">담당팀</h4>
                                <div class="team-badges">""")
                
                for team, count in list(category_info['team_distribution'].items())[:3]:
                    html_parts.append(f'                                    <span class="team-badge">{team}: {count}건</span>')
                
                # 모달 버튼 추가
                modal_id = f"modal-{category_name.replace(' ', '-').replace('/', '-')}"
                html_parts.append(f"""                                </div>
                            </div>
                            <button class="modal-trigger" onclick="openModal('{modal_id}')">
                                문의 내용 보기 ({basic_info['total_inquiries']}건)
                            </button>
                        </div>""")
            
            html_parts.append("""                    </div>
                </div>
            </div>""")
            
            # 모달들 추가
            for category_name, category_info in sorted_categories:
                basic_info = category_info['basic_info']
                modal_id = f"modal-{category_name.replace(' ', '-').replace('/', '-')}"
                
                html_parts.append(f"""            <div class="modal-overlay" id="{modal_id}" onclick="closeModal('{modal_id}')">
                <div class="modal-content" onclick="event.stopPropagation()">
                    <div class="modal-header">
                        <h3 class="modal-title">{category_name} - 전체 {basic_info['total_inquiries']}건</h3>
                        <button class="modal-close" onclick="closeModal('{modal_id}')">&times;</button>
                    </div>
                    <div class="modal-body">""")
                
                # 전체 문의 내용 표시 (샘플 데이터 사용, 실제로는 모든 문의를 표시)
                for i, sample in enumerate(category_info['sample_inquiries']):
                    urgency_class = "urgency-urgent" if sample.get('is_urgent', False) else "urgency-normal"
                    urgency_text = "긴급" if sample.get('is_urgent', False) else "일반"
                    
                    html_parts.append(f"""                        <div class="inquiry-card">
                            <div class="inquiry-header">
                                <span>{sample['assigned_team']}</span>
                                <span class="urgency-badge {urgency_class}">{urgency_text}</span>
                            </div>
                            <div class="inquiry-content">{sample['content']}</div>
                        </div>""")
                
                # 더 많은 데이터가 있는 경우 표시
                if basic_info['total_inquiries'] > len(category_info['sample_inquiries']):
                    remaining = basic_info['total_inquiries'] - len(category_info['sample_inquiries'])
                    html_parts.append(f"""                        <div style="text-align: center; padding: 1rem; color: #6b7280; font-style: italic;">
                            ... 및 {remaining}건의 추가 문의가 있습니다
                        </div>""")
                
                html_parts.append("""                    </div>
                </div>
            </div>""")
            
        # JavaScript 추가
        html_parts.append("""        <script>
            function openModal(modalId) {
                document.getElementById(modalId).classList.add('active');
                document.body.style.overflow = 'hidden';
            }
            
            function closeModal(modalId) {
                document.getElementById(modalId).classList.remove('active');
                document.body.style.overflow = 'auto';
            }
            
            function filterCategories(type) {
                // 활성 버튼 업데이트
                document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
                event.target.classList.add('active');
                
                const container = document.getElementById('categories-container');
                const cards = Array.from(container.children);
                
                // 정렬 함수
                let sortFunction;
                switch(type) {
                    case 'team':
                        sortFunction = (a, b) => {
                            const teamA = a.getAttribute('data-team');
                            const teamB = b.getAttribute('data-team');
                            return teamA.localeCompare(teamB);
                        };
                        break;
                    case 'journey':
                        sortFunction = (a, b) => {
                            const journeyA = a.getAttribute('data-journey');
                            const journeyB = b.getAttribute('data-journey');
                            return journeyA.localeCompare(journeyB);
                        };
                        break;
                    default: // 'all'
                        sortFunction = (a, b) => {
                            const countA = parseInt(a.getAttribute('data-count'));
                            const countB = parseInt(b.getAttribute('data-count'));
                            return countB - countA; // 내림차순
                        };
                }
                
                // 정렬 및 재배치
                cards.sort(sortFunction);
                cards.forEach(card => container.appendChild(card));
            }
            
            // ESC 키로 모달 닫기
            document.addEventListener('keydown', function(event) {
                if (event.key === 'Escape') {
                    const activeModal = document.querySelector('.modal-overlay.active');
                    if (activeModal) {
                        activeModal.classList.remove('active');
                        document.body.style.overflow = 'auto';
                    }
                }
            });
        </script>""")
        
        # 푸터
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        html_parts.append(f"""        </div>
        <div class="footer">
            <p>카테고리 기반 VoC 분석 보고서</p>
            <p>생성일시: {current_time} | Pretendard 폰트 적용</p>
        </div>
    </div>
</body>
</html>""")
        
        return ''.join(html_parts)

    def save_and_open_html_report(self, results: Dict) -> str:
        """HTML 보고서 저장 및 브라우저에서 열기"""
        html_content = self.generate_html_report(results)
        
        # 파일명 생성
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"category_voc_report_{timestamp}.html"
        
        # HTML 파일 저장
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # 절대 경로로 변환
        file_path = os.path.abspath(filename)
        
        print(f"✅ HTML 보고서 저장: {filename}")
        
        # 브라우저에서 열기
        try:
            webbrowser.open(f'file://{file_path}')
            print("🌐 브라우저에서 보고서를 열었습니다.")
        except Exception as e:
            print(f"브라우저 열기 실패: {e}")
            print(f"수동으로 파일을 열어주세요: {filename}")
        
        return filename

    def save_html_only(self, results: Dict, filename: str = None) -> str:
        """HTML 보고서만 저장 (브라우저 열기 없음)"""
        html_content = self.generate_html_report(results)
        
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"category_voc_report_{timestamp}.html"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ HTML 보고서 저장: {filename}")
        return filename