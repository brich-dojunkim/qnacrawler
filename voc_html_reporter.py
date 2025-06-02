import pandas as pd
import webbrowser
import os
from datetime import datetime
from typing import Dict

class CategoryVoCHTMLReporter:
    def __init__(self, df: pd.DataFrame):
        """
        카테고리 기반 VoC HTML 보고서 생성기 초기화
        
        Args:
            df: VoC 분석이 완료된 DataFrame
        """
        self.df = df

    def generate_text_tables(self, results: Dict) -> Dict:
        """분석 결과를 위한 텍스트 표들 생성"""
        text_tables = {}
        
        # 1. 팀별 문의 분포 텍스트 표 (카드 컴포넌트 없이)
        if 'team_analysis' in results:
            team_data = results['team_analysis']
            
            if team_data:
                # 데이터 정렬 (문의 건수 기준 내림차순)
                sorted_teams = sorted(team_data.items(), 
                                    key=lambda x: x[1]['basic_info']['total_inquiries'], 
                                    reverse=True)
                
                total_inquiries = sum(team_data[team]['basic_info']['total_inquiries'] for team in team_data.keys())
                
                team_table_html = '<h4 class="rank-table-title">팀별 문의 분포</h4>'
                
                for idx, (team_name, team_info) in enumerate(sorted_teams, 1):
                    count = team_info['basic_info']['total_inquiries']
                    percentage = (count / total_inquiries * 100) if total_inquiries > 0 else 0
                    
                    team_table_html += f'''
                    <div class="rank-row">
                        <div class="rank-number">{idx}</div>
                        <div class="rank-name">{team_name}</div>
                        <div class="rank-value">{count}건 ({percentage:.1f}%)</div>
                    </div>'''
                
                text_tables['team_overview'] = team_table_html

        # 2. 유저 여정별 문의 분포 텍스트 표 (카드 컴포넌트 없이)
        if 'journey_analysis' in results:
            journey_data = results['journey_analysis']
            
            if journey_data:
                # 문의 건수로 정렬 (순위표이므로)
                sorted_journeys = sorted(journey_data.items(), 
                                       key=lambda x: x[1]['basic_info']['total_inquiries'], 
                                       reverse=True)
                
                total_inquiries = sum(data['basic_info']['total_inquiries'] for _, data in sorted_journeys)
                
                journey_table_html = '<h4 class="rank-table-title">유저 여정별 문의 분포</h4>'
                
                for idx, (journey_name, journey_info) in enumerate(sorted_journeys, 1):
                    count = journey_info['basic_info']['total_inquiries']
                    percentage = (count / total_inquiries * 100) if total_inquiries > 0 else 0
                    
                    journey_table_html += f'''
                    <div class="rank-row">
                        <div class="rank-number">{idx}</div>
                        <div class="rank-name">{journey_name}</div>
                        <div class="rank-value">{count}건 ({percentage:.1f}%)</div>
                    </div>'''
                
                text_tables['journey_overview'] = journey_table_html

        # 3. 주간별 문의 트렌드 텍스트 표 (카드 컴포넌트 없이)
        if 'weekly_trends' in results:
            weekly_data = results['weekly_trends']
            
            if weekly_data:
                # 주간 데이터 정렬 (최신순)
                sorted_weeks = sorted(weekly_data.items())
                
                avg_weekly = sum(weekly_data[week]['total_inquiries'] for week in weekly_data.keys()) / len(weekly_data) if weekly_data else 0
                
                weekly_table_html = '<h4 class="rank-table-title">주간별 문의 트렌드 (최근 8주)</h4>'
                
                # 최근 8주만 표시
                recent_weeks = sorted_weeks[-8:]
                
                for week_str, week_info in recent_weeks:
                    count = week_info['total_inquiries']
                    
                    # 주간 라벨 생성
                    try:
                        week_period = pd.Period(week_str, freq='W-MON')
                        start_date = week_period.start_time
                        end_date = week_period.end_time
                        week_label = f"{start_date.strftime('%m/%d')}-{end_date.strftime('%m/%d')}"
                    except:
                        week_label = week_str
                    
                    # 트렌드 텍스트
                    if count > avg_weekly * 1.1:
                        trend_text = "상승"
                    elif count < avg_weekly * 0.9:
                        trend_text = "하락"
                    else:
                        trend_text = "평균"
                    
                    weekly_table_html += f'''
                    <div class="rank-row">
                        <div class="rank-number">{trend_text}</div>
                        <div class="rank-name">{week_label}</div>
                        <div class="rank-value">{count}건</div>
                    </div>'''
                
                # 요약 정보 추가
                max_weekly = max(weekly_data[week]['total_inquiries'] for week in weekly_data.keys())
                min_weekly = min(weekly_data[week]['total_inquiries'] for week in weekly_data.keys())
                
                weekly_table_html += f'''
                <div class="rank-summary">
                    <span>평균: {avg_weekly:.0f}건</span>
                    <span>최고: {max_weekly}건</span>
                    <span>최저: {min_weekly}건</span>
                </div>'''
                
                text_tables['weekly_trend'] = weekly_table_html

        # 4. 팀별 세부 카테고리 분포 - 단순한 목록
        if 'team_analysis' in results:
            team_data = results['team_analysis']
            team_category_tables = {}
            
            for team_name, team_info in team_data.items():
                if team_info['sub_categories']:
                    # 카테고리를 건수 기준으로 정렬
                    categories = sorted(team_info['sub_categories'].items(), 
                                      key=lambda x: x[1], reverse=True)[:5]  # 상위 5개
                    
                    table_html = '<div class="simple-list">'
                    table_html += f'<h5 class="simple-list-title">세부 카테고리 분포</h5>'
                    
                    for idx, (category, count) in enumerate(categories, 1):
                        table_html += f'''
                        <div class="simple-item">
                            <span class="simple-rank">{idx}</span>
                            <span class="simple-name">{category}</span>
                            <span class="simple-value">{count}건</span>
                        </div>'''
                    
                    table_html += '</div>'
                    team_category_tables[team_name] = table_html
            
            text_tables['team_categories'] = team_category_tables

        # 5. 유저 여정별 세부 카테고리 분포 - 단순한 목록
        if 'journey_analysis' in results:
            journey_data = results['journey_analysis']
            journey_category_tables = {}
            
            for journey_name, journey_info in journey_data.items():
                if journey_info['sub_categories']:
                    # 카테고리를 건수 기준으로 정렬
                    categories = sorted(journey_info['sub_categories'].items(), 
                                      key=lambda x: x[1], reverse=True)[:5]  # 상위 5개
                    
                    table_html = '<div class="simple-list">'
                    table_html += f'<h5 class="simple-list-title">세부 카테고리 분포</h5>'
                    
                    for idx, (category, count) in enumerate(categories, 1):
                        table_html += f'''
                        <div class="simple-item">
                            <span class="simple-rank">{idx}</span>
                            <span class="simple-name">{category}</span>
                            <span class="simple-value">{count}건</span>
                        </div>'''
                    
                    table_html += '</div>'
                    journey_category_tables[journey_name] = table_html
            
            text_tables['journey_categories'] = journey_category_tables

        return text_tables

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
        
        # 텍스트 표 생성
        text_tables = self.generate_text_tables(results)
        
        # 기본 정보
        overall_summary = results.get('overall_summary', {})
        total_inquiries = overall_summary.get('total_inquiries', 0)
        urgent_count = overall_summary.get('urgent_count', 0)
        analysis_date = results.get('analysis_timestamp', datetime.now().isoformat())
        
        # HTML 생성
        html_content = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>카테고리 기반 VoC 분석 보고서</title>
    <link href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" rel="stylesheet">
    <style>
        body {{
            font-family: 'Pretendard', -apple-system, sans-serif;
            margin: 0;
            padding: 1rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }}
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 16px;
            box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #2563eb 0%, #3b82f6 100%);
            color: white;
            padding: 2rem;
            text-align: center;
        }}
        .header h1 {{
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }}
        .main-content {{
            padding: 2rem;
        }}
        .major-section {{
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            margin-bottom: 2rem;
            box-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1);
        }}
        .major-section-header {{
            background: #f8fafc;
            padding: 1.5rem;
            border-bottom: 1px solid #e2e8f0;
        }}
        .major-section-header h2 {{
            font-size: 1.5rem;
            font-weight: 600;
            margin: 0;
        }}
        .major-section-content {{
            padding: 1.5rem;
        }}
        .entity-card {{
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 1.5rem;
            transition: all 0.2s ease;
        }}
        .entity-card:hover {{
            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
            transform: translateY(-2px);
        }}
        .entity-card-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 1rem;
            padding-bottom: 0.75rem;
            border-bottom: 1px solid #e2e8f0;
        }}
        .entity-card-title {{
            font-size: 1.125rem;
            font-weight: 600;
            margin: 0;
        }}
        .entity-card-badge {{
            background: #2563eb;
            color: white;
            padding: 0.25rem 0.75rem;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: 500;
        }}
        
        /* 데이터 현황 가로 배치 */
        .data-overview {{
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            transition: all 0.2s ease;
        }}
        .data-overview:hover {{
            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
            transform: translateY(-2px);
        }}
        .data-overview-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 1rem;
            padding-bottom: 0.75rem;
            border-bottom: 1px solid #e2e8f0;
        }}
        .data-stats {{
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 4rem;
            margin: 0;
            padding: 1rem 0;
        }}
        .data-stat {{
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
        }}
        .data-stat-name {{
            font-size: 0.85rem;
            color: #475569;
            margin-bottom: 0.25rem;
        }}
        .data-stat-number {{
            font-size: 1.5rem;
            font-weight: 700;
            color: #2563eb;
        }}
        
        .grid {{
            display: grid;
            gap: 1.5rem;
        }}
        .grid-3 {{
            grid-template-columns: repeat(3, 1fr);
        }}
        .grid-4 {{
            grid-template-columns: repeat(4, 1fr);
        }}
        .grid-5 {{
            grid-template-columns: repeat(5, 1fr);
        }}
        .stats-list {{
            list-style: none;
            padding: 0;
            margin: 0;
        }}
        .stats-list li {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0.75rem 0;
            border-bottom: 1px solid #e2e8f0;
        }}
        .stats-list li:last-child {{
            border-bottom: none;
        }}
        .stat-name {{
            font-size: 0.875rem;
            color: #475569;
        }}
        .stat-number {{
            font-size: 1.25rem;
            font-weight: 700;
            color: #2563eb;
        }}
        .metrics-list {{
            list-style: none;
            padding: 0;
            margin: 1rem 0;
        }}
        .metrics-list li {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0.5rem 0;
            border-bottom: 1px solid #f1f5f9;
        }}
        .metrics-list li:last-child {{
            border-bottom: none;
        }}
        .metric-name {{
            font-size: 0.8rem;
            color: #64748b;
        }}
        .metric-number {{
            font-size: 1rem;
            font-weight: 600;
            color: #2563eb;
        }}
        .modal-trigger {{
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
        }}
        .modal-trigger:hover {{
            background: #1d4ed8;
        }}
        .modal-overlay {{
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
        }}
        .modal-overlay.active {{
            display: flex;
        }}
        .modal-content {{
            background: white;
            border-radius: 12px;
            width: 90%;
            max-width: 800px;
            max-height: 80vh;
            overflow: hidden;
            box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1);
        }}
        .modal-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1.5rem;
            border-bottom: 1px solid #e2e8f0;
            background: #f8fafc;
        }}
        .modal-title {{
            font-size: 1.25rem;
            font-weight: 600;
            color: #374151;
        }}
        .modal-close {{
            background: none;
            border: none;
            font-size: 1.5rem;
            cursor: pointer;
            color: #6b7280;
            padding: 0.25rem;
        }}
        .modal-close:hover {{
            color: #374151;
        }}
        .modal-body {{
            padding: 1.5rem;
            max-height: 60vh;
            overflow-y: auto;
        }}
        .inquiry-card {{
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 1rem;
            margin-bottom: 1rem;
            background: #f8fafc;
        }}
        .inquiry-card:last-child {{
            margin-bottom: 0;
        }}
        .inquiry-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 0.75rem;
            font-size: 0.875rem;
            color: #6b7280;
        }}
        .inquiry-content {{
            color: #374151;
            line-height: 1.5;
            font-size: 0.95rem;
        }}
        .urgency-badge {{
            padding: 0.25rem 0.5rem;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: 500;
        }}
        .urgency-urgent {{
            background: #fee2e2;
            color: #dc2626;
        }}
        .urgency-normal {{
            background: #f0f9ff;
            color: #0369a1;
        }}
        .filter-buttons {{
            display: flex;
            gap: 0.5rem;
            margin-bottom: 1.5rem;
            justify-content: center;
        }}
        .filter-btn {{
            padding: 0.5rem 1rem;
            border: 2px solid #e2e8f0;
            background: white;
            border-radius: 8px;
            cursor: pointer;
            font-size: 0.875rem;
            font-weight: 500;
            color: #475569;
            transition: all 0.2s ease;
        }}
        .filter-btn:hover {{
            border-color: #2563eb;
            color: #2563eb;
        }}
        .filter-btn.active {{
            background: #2563eb;
            border-color: #2563eb;
            color: white;
        }}
        .journey-badge {{
            background: #10b981;
            color: white;
            padding: 0.25rem 0.5rem;
            border-radius: 9999px;
            font-size: 0.75rem;
        }}
        .team-badges {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin: 0.75rem 0;
        }}
        .team-badge {{
            background: #f59e0b;
            color: white;
            padding: 0.25rem 0.75rem;
            border-radius: 9999px;
            font-size: 0.75rem;
        }}
        .small-subsection-title {{
            font-size: 0.875rem;
            font-weight: 600;
            margin-bottom: 0.75rem;
        }}
        
        /* 순위표 스타일 (컴팩트) */
        .rank-table-title {{
            font-size: 0.95rem;
            font-weight: 600;
            margin-bottom: 0.75rem;
            color: #374151;
        }}
        .rank-row {{
            display: flex;
            align-items: center;
            margin-bottom: 0.5rem;
            padding: 0.3rem;
            background: white;
            border-radius: 6px;
            border: 1px solid #e2e8f0;
            transition: all 0.2s ease;
        }}
        .rank-row:hover {{
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }}
        .rank-number {{
            min-width: 40px;
            font-size: 0.8rem;
            font-weight: 600;
            color: #2563eb;
            text-align: center;
        }}
        .rank-name {{
            flex: 1;
            font-size: 0.8rem;
            font-weight: 500;
            color: #374151;
            margin-left: 0.75rem;
        }}
        .rank-value {{
            min-width: 80px;
            text-align: right;
            font-size: 0.8rem;
            font-weight: 600;
            color: #2563eb;
        }}
        .rank-summary {{
            margin-top: 0.75rem;
            padding-top: 0.75rem;
            border-top: 1px solid #e2e8f0;
            display: flex;
            gap: 1.5rem;
            font-size: 0.7rem;
            color: #6b7280;
            justify-content: center;
        }}
        
        /* 단순한 목록 스타일 */
        .simple-list {{
            margin: 1rem 0;
        }}
        .simple-list-title {{
            font-size: 0.8rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
            color: #374151;
        }}
        .simple-item {{
            display: flex;
            align-items: center;
            margin-bottom: 0.25rem;
            padding: 0.2rem 0;
            font-size: 0.75rem;
        }}
        .simple-rank {{
            min-width: 20px;
            font-weight: 600;
            color: #6b7280;
        }}
        .simple-name {{
            flex: 1;
            margin-left: 0.5rem;
            color: #374151;
        }}
        .simple-value {{
            min-width: 50px;
            text-align: right;
            font-weight: 600;
            color: #2563eb;
        }}
        
        .footer {{
            text-align: center;
            padding: 2rem;
            background: #f8fafc;
            border-top: 1px solid #e2e8f0;
            color: #475569;
            font-size: 0.875rem;
        }}
        
        @media (max-width: 1200px) {{
            .grid-4 {{ grid-template-columns: repeat(2, 1fr); }}
            .grid-5 {{ grid-template-columns: repeat(3, 1fr); }}
        }}
        @media (max-width: 768px) {{
            .main-content {{ padding: 1rem; }}
            .grid-3, .grid-4, .grid-5 {{ grid-template-columns: 1fr; }}
            .data-stats {{
                flex-direction: column;
                gap: 1rem;
            }}
            .rank-row {{
                flex-direction: column;
                align-items: stretch;
                gap: 0.25rem;
            }}
            .rank-number {{
                min-width: auto;
                text-align: left;
            }}
            .rank-name {{
                margin-left: 0;
            }}
            .rank-value {{
                text-align: left;
                min-width: auto;
            }}
            .rank-summary {{
                flex-direction: column;
                gap: 0.25rem;
                text-align: center;
            }}
            .simple-item {{
                flex-direction: column;
                align-items: flex-start;
                gap: 0.1rem;
            }}
            .simple-rank, .simple-name, .simple-value {{
                min-width: auto;
                text-align: left;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>카테고리 기반 VoC 분석</h1>
            <p>고객 문의 데이터의 카테고리별 분석 결과</p>
            <p>{analysis_date[:19].replace('T', ' ')}</p>
        </div>
        <div class="main-content">
            <div class="major-section">
                <div class="major-section-header">
                    <h2>분석 개요</h2>
                </div>
                <div class="major-section-content">
                    <!-- 데이터 현황을 가로로 길게 배치 -->
                    <div class="data-overview">
                        <div class="data-overview-header">
                            <h3 class="entity-card-title">데이터 현황</h3>
                            <span class="entity-card-badge">{total_inquiries:,}건</span>
                        </div>
                        <div class="data-stats">
                            <div class="data-stat">
                                <div class="data-stat-name">총문의</div>
                                <div class="data-stat-number">{total_inquiries:,}</div>
                            </div>
                            <div class="data-stat">
                                <div class="data-stat-name">긴급문의</div>
                                <div class="data-stat-number">{urgent_count}</div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- 나머지 3개 카드를 3등분으로 배치 -->
                    <div class="grid grid-3">"""
        
        # 주간별 트렌드 카드
        if 'weekly_trends' in results:
            weekly_data = results['weekly_trends']
            week_counts = [weekly_data[week]['total_inquiries'] for week in weekly_data.keys()]
            if week_counts:
                avg_weekly = sum(week_counts) / len(week_counts)
                max_weekly = max(week_counts)
                
                html_content += f"""
                        <div class="entity-card">
                            <div class="entity-card-header">
                                <h3 class="entity-card-title">주간별 트렌드</h3>
                                <span class="entity-card-badge">최근 12주</span>
                            </div>
                            <ul class="stats-list" style="margin-bottom: 1rem;">
                                <li>
                                    <span class="stat-name">주간 평균</span>
                                    <span class="stat-number">{avg_weekly:.0f}</span>
                                </li>
                                <li>
                                    <span class="stat-name">최대 주간</span>
                                    <span class="stat-number">{max_weekly}</span>
                                </li>
                            </ul>
                            {text_tables.get('weekly_trend', '')}
                        </div>"""
        
        # 팀별 분포 카드
        if 'team_analysis' in results:
            team_data = results['team_analysis']
            if team_data:
                team_counts = [team_data[team]['basic_info']['total_inquiries'] for team in team_data.keys()]
                avg_team = sum(team_counts) / len(team_counts)
                max_team = max(team_counts)
                team_count = len(team_data)
                
                html_content += f"""
                        <div class="entity-card">
                            <div class="entity-card-header">
                                <h3 class="entity-card-title">팀별 분포</h3>
                                <span class="entity-card-badge">{team_count}개 팀</span>
                            </div>
                            <ul class="stats-list" style="margin-bottom: 1rem;">
                                <li>
                                    <span class="stat-name">팀 평균</span>
                                    <span class="stat-number">{avg_team:.0f}</span>
                                </li>
                                <li>
                                    <span class="stat-name">최대 팀</span>
                                    <span class="stat-number">{max_team}</span>
                                </li>
                            </ul>
                            {text_tables.get('team_overview', '')}
                        </div>"""
        
        # 유저 여정별 분포 카드
        if 'journey_analysis' in results:
            journey_data = results['journey_analysis']
            if journey_data:
                journey_counts = [journey_data[journey]['basic_info']['total_inquiries'] for journey in journey_data.keys()]
                avg_journey = sum(journey_counts) / len(journey_counts)
                max_journey = max(journey_counts)
                journey_count = len(journey_data)
                
                html_content += f"""
                        <div class="entity-card">
                            <div class="entity-card-header">
                                <h3 class="entity-card-title">유저 여정별 분포</h3>
                                <span class="entity-card-badge">{journey_count}개 여정</span>
                            </div>
                            <ul class="stats-list" style="margin-bottom: 1rem;">
                                <li>
                                    <span class="stat-name">여정 평균</span>
                                    <span class="stat-number">{avg_journey:.0f}</span>
                                </li>
                                <li>
                                    <span class="stat-name">최대 여정</span>
                                    <span class="stat-number">{max_journey}</span>
                                </li>
                            </ul>
                            {text_tables.get('journey_overview', '')}
                        </div>"""
        
        html_content += """
                    </div>
                </div>
            </div>"""
        
        # 팀별 분석 섹션 (grid-4 유지)
        if 'team_analysis' in results and results['team_analysis']:
            html_content += """
            <div class="major-section">
                <div class="major-section-header">
                    <h2>팀별 문의 내용 분석</h2>
                </div>
                <div class="major-section-content">
                    <div class="grid grid-4">"""
            
            for team_name, team_info in results['team_analysis'].items():
                basic_info = team_info['basic_info']
                
                html_content += f"""
                        <div class="entity-card">
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
                            </ul>"""
                
                # 세부 카테고리 분포 텍스트 표 (별도 카드 없이)
                if 'team_categories' in text_tables and team_name in text_tables['team_categories']:
                    html_content += text_tables['team_categories'][team_name]
                
                html_content += """
                        </div>"""
            
            html_content += """
                    </div>
                </div>
            </div>"""
        
        # 유저 여정별 분석 섹션 (grid-5로 변경)
        if 'journey_analysis' in results and results['journey_analysis']:
            html_content += """
            <div class="major-section">
                <div class="major-section-header">
                    <h2>유저 여정별 문의 내용 분석</h2>
                </div>
                <div class="major-section-content">
                    <div class="grid grid-5">"""
            
            for journey_name, journey_info in results['journey_analysis'].items():
                basic_info = journey_info['basic_info']
                
                html_content += f"""
                        <div class="entity-card">
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
                            </ul>"""
                
                # 세부 카테고리 분포 텍스트 표 (별도 카드 없이)
                if 'journey_categories' in text_tables and journey_name in text_tables['journey_categories']:
                    html_content += text_tables['journey_categories'][journey_name]
                
                html_content += """
                        </div>"""
            
            html_content += """
                    </div>
                </div>
            </div>"""
        
        # 세부 카테고리별 분석 섹션 (필터 기능 추가)
        if 'category_analysis' in results and results['category_analysis']:
            sorted_categories = sorted(results['category_analysis'].items(), 
                                     key=lambda x: x[1]['basic_info']['total_inquiries'], 
                                     reverse=True)
            
            html_content += """
            <div class="major-section">
                <div class="major-section-header">
                    <h2>세부 카테고리별 문의 내용</h2>
                </div>
                <div class="major-section-content">
                    <!-- 필터 버튼 추가 -->
                    <div class="filter-buttons">
                        <button class="filter-btn active" onclick="filterCategories('all')">전체</button>
                        <button class="filter-btn" onclick="filterCategories('team')">팀별</button>
                        <button class="filter-btn" onclick="filterCategories('journey')">유저여정별</button>
                    </div>
                    <div class="grid grid-3" id="categories-container">"""
            
            for category_name, category_info in sorted_categories:
                basic_info = category_info['basic_info']
                
                # 가장 많은 담당팀과 유저 여정 추출
                main_team = list(category_info['team_distribution'].keys())[0] if category_info['team_distribution'] else '기타'
                main_journey = self._get_journey_for_category(category_name)
                
                # data 속성 추가
                html_content += f"""
                        <div class="entity-card" 
                             data-team="{main_team}" 
                             data-journey="{main_journey}" 
                             data-count="{basic_info['total_inquiries']}">
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
                                <div class="team-badges">"""
                
                # 담당팀 배지 (건수 제거)
                for team, count in list(category_info['team_distribution'].items())[:3]:
                    html_content += f'                                    <span class="team-badge">{team}</span>'
                
                html_content += """                                </div>
                                <h4 class="small-subsection-title">유저 여정</h4>
                                <div style="margin: 0.5rem 0;">"""
                
                # 유저 여정 배지 추가
                html_content += f'                                    <span class="journey-badge">{main_journey}</span>'
                
                # 모달 버튼 추가
                modal_id = f"modal-{category_name.replace(' ', '-').replace('/', '-').replace('(', '').replace(')', '')}"
                html_content += f"""                                </div>
                            </div>
                            <button class="modal-trigger" onclick="openModal('{modal_id}')">
                                문의 내용 보기 ({basic_info['total_inquiries']}건)
                            </button>
                        </div>"""
            
            html_content += """
                    </div>
                </div>
            </div>"""
            
            # 모달들 추가
            for category_name, category_info in sorted_categories:
                basic_info = category_info['basic_info']
                modal_id = f"modal-{category_name.replace(' ', '-').replace('/', '-').replace('(', '').replace(')', '')}"
                
                html_content += f"""
            <div class="modal-overlay" id="{modal_id}" onclick="closeModal('{modal_id}')">
                <div class="modal-content" onclick="event.stopPropagation()">
                    <div class="modal-header">
                        <h3 class="modal-title">{category_name} - 전체 {basic_info['total_inquiries']}건</h3>
                        <button class="modal-close" onclick="closeModal('{modal_id}')">&times;</button>
                    </div>
                    <div class="modal-body">"""
                
                # 전체 문의 내용 표시 (샘플 데이터 사용)
                for i, sample in enumerate(category_info['sample_inquiries']):
                    urgency_class = "urgency-urgent" if sample.get('is_urgent', False) else "urgency-normal"
                    urgency_text = "긴급" if sample.get('is_urgent', False) else "일반"
                    
                    html_content += f"""
                        <div class="inquiry-card">
                            <div class="inquiry-header">
                                <span>{sample['assigned_team']}</span>
                                <span class="urgency-badge {urgency_class}">{urgency_text}</span>
                            </div>
                            <div class="inquiry-content">{sample['content']}</div>
                        </div>"""
                
                # 더 많은 데이터가 있는 경우 표시
                if basic_info['total_inquiries'] > len(category_info['sample_inquiries']):
                    remaining = basic_info['total_inquiries'] - len(category_info['sample_inquiries'])
                    html_content += f"""
                        <div style="text-align: center; padding: 1rem; color: #6b7280; font-style: italic;">
                            ... 및 {remaining}건의 추가 문의가 있습니다
                        </div>"""
                
                html_content += """
                    </div>
                </div>
            </div>"""
        
        # JavaScript 추가 (필터 기능 구현)
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        html_content += f"""
        <script>
            function openModal(modalId) {{
                document.getElementById(modalId).classList.add('active');
                document.body.style.overflow = 'hidden';
            }}
            
            function closeModal(modalId) {{
                document.getElementById(modalId).classList.remove('active');
                document.body.style.overflow = 'auto';
            }}
            
            function filterCategories(type) {{
                // 활성 버튼 업데이트
                document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
                event.target.classList.add('active');
                
                const container = document.getElementById('categories-container');
                const cards = Array.from(container.children);
                
                // 정렬 함수
                let sortFunction;
                switch(type) {{
                    case 'team':
                        sortFunction = (a, b) => {{
                            const teamA = a.getAttribute('data-team');
                            const teamB = b.getAttribute('data-team');
                            return teamA.localeCompare(teamB);
                        }};
                        break;
                    case 'journey':
                        // 유저 여정 순서 정의
                        const journeyOrder = ['계정·입점', '상품·콘텐츠', '주문·배송', '반품·취소', '정산', '기타'];
                        sortFunction = (a, b) => {{
                            const journeyA = a.getAttribute('data-journey');
                            const journeyB = b.getAttribute('data-journey');
                            const indexA = journeyOrder.indexOf(journeyA);
                            const indexB = journeyOrder.indexOf(journeyB);
                            
                            // 정의된 순서가 없으면 기타로 처리
                            const finalIndexA = indexA === -1 ? journeyOrder.length : indexA;
                            const finalIndexB = indexB === -1 ? journeyOrder.length : indexB;
                            
                            return finalIndexA - finalIndexB;
                        }};
                        break;
                    default: // 'all'
                        sortFunction = (a, b) => {{
                            const countA = parseInt(a.getAttribute('data-count'));
                            const countB = parseInt(b.getAttribute('data-count'));
                            return countB - countA; // 내림차순
                        }};
                }}
                
                // 정렬 및 재배치
                cards.sort(sortFunction);
                cards.forEach(card => container.appendChild(card));
            }}
            
            // ESC 키로 모달 닫기
            document.addEventListener('keydown', function(event) {{
                if (event.key === 'Escape') {{
                    const activeModal = document.querySelector('.modal-overlay.active');
                    if (activeModal) {{
                        activeModal.classList.remove('active');
                        document.body.style.overflow = 'auto';
                    }}
                }}
            }});
        </script>
        </div>
        <div class="footer">
            <p>카테고리 기반 VoC 분석 보고서</p>
            <p>생성일시: {current_time} | Pretendard 폰트 적용</p>
        </div>
    </div>
</body>
</html>"""
        
        return html_content

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