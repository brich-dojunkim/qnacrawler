import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import webbrowser
import os
from datetime import datetime
from typing import Dict

# 한글 폰트 설정
plt.rcParams['font.family'] = ['Malgun Gothic', 'AppleGothic', 'NanumGothic']
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
        
        # 1. 팀별 문의 건수 차트 (더 컴팩트하게)
        if 'team_analysis' in results:
            team_data = results['team_analysis']
            
            if team_data:
                fig, ax = plt.subplots(figsize=(10, 5))
                
                teams = list(team_data.keys())
                counts = [team_data[team]['basic_info']['total_inquiries'] for team in teams]
                
                bars = ax.bar(teams, counts, color='steelblue', alpha=0.8)
                ax.set_title('팀별 문의 건수', fontsize=12, fontweight='bold')
                ax.set_ylabel('건수')
                plt.xticks(rotation=45, ha='right')
                
                # 막대 위에 값 표시
                for bar in bars:
                    height = bar.get_height()
                    ax.text(bar.get_x() + bar.get_width()/2., height,
                           f'{int(height)}', ha='center', va='bottom', fontsize=10)
                
                plt.tight_layout()
                charts['team_overview'] = self.create_chart_base64(fig)

        # 2. 주간별 문의 트렌드
        if 'weekly_trends' in results:
            weekly_data = results['weekly_trends']
            
            if weekly_data:
                fig, ax = plt.subplots(figsize=(12, 4))
                
                weeks = list(weekly_data.keys())
                counts = [weekly_data[week]['total_inquiries'] for week in weeks]
                
                ax.plot(range(len(weeks)), counts, marker='o', linewidth=2, markersize=6, 
                       color='steelblue', markerfacecolor='orange')
                ax.fill_between(range(len(weeks)), counts, alpha=0.3, color='steelblue')
                ax.set_title('주간별 문의 건수 추이 (최근 12주)', fontsize=12, fontweight='bold')
                ax.set_ylabel('건수')
                ax.set_xlabel('주')
                
                # x축 라벨을 간소화 (주차 번호만)
                week_labels = [f'W{i+1}' for i in range(len(weeks))]
                ax.set_xticks(range(len(weeks)))
                ax.set_xticklabels(week_labels)
                ax.grid(True, alpha=0.3)
                
                plt.tight_layout()
                charts['weekly_trend'] = self.create_chart_base64(fig)

        # 3. 팀별 세부 카테고리 분포 시각화
        if 'team_analysis' in results:
            team_data = results['team_analysis']
            
            # 각 팀별로 세부 카테고리 분포 차트 생성
            team_category_charts = {}
            
            for team_name, team_info in team_data.items():
                if team_info['sub_categories']:
                    fig, ax = plt.subplots(figsize=(7, 5))
                    
                    categories = list(team_info['sub_categories'].keys())[:5]  # 상위 5개
                    values = list(team_info['sub_categories'].values())[:5]
                    
                    # 현대적인 색상 팔레트
                    colors = ['#2563eb', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6']
                    
                    wedges, texts, autotexts = ax.pie(values, labels=categories, autopct='%1.1f%%', 
                                                     colors=colors[:len(categories)], startangle=90)
                    
                    # 텍스트 스타일링
                    for autotext in autotexts:
                        autotext.set_color('white')
                        autotext.set_fontweight('bold')
                        autotext.set_fontsize(9)
                    
                    for text in texts:
                        text.set_fontsize(8)
                    
                    ax.set_title(f'{team_name} 세부 카테고리 분포', fontsize=11, fontweight='bold', pad=15)
                    
                    plt.tight_layout()
                    team_category_charts[team_name] = self.create_chart_base64(fig)
            
            charts['team_categories'] = team_category_charts

        return charts

    def generate_html_report(self, results: Dict) -> str:
        """HTML 보고서 생성"""
        print("🌐 카테고리 기반 HTML 보고서 생성 중...")
        
        # 차트 생성
        charts = self.generate_charts(results)
        
        # 기본 정보
        overall_summary = results.get('overall_summary', {})
        total_inquiries = overall_summary.get('total_inquiries', 0)
        analysis_date = results.get('analysis_timestamp', datetime.now().isoformat())
        
        html_template = f"""
        <!DOCTYPE html>
        <html lang="ko">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>카테고리 기반 VoC 분석 보고서</title>
            <link rel="preconnect" href="https://cdn.jsdelivr.net">
            <link href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" rel="stylesheet">
            <style>
                :root {{
                    --primary-color: #2563eb;
                    --primary-light: #3b82f6;
                    --secondary-color: #64748b;
                    --accent-color: #f59e0b;
                    --success-color: #10b981;
                    --warning-color: #f59e0b;
                    --danger-color: #ef4444;
                    --gray-50: #f8fafc;
                    --gray-100: #f1f5f9;
                    --gray-200: #e2e8f0;
                    --gray-300: #cbd5e1;
                    --gray-600: #475569;
                    --gray-800: #1e293b;
                    --gray-900: #0f172a;
                    --border-radius: 12px;
                    --border-radius-lg: 16px;
                    --shadow-sm: 0 1px 3px 0 rgb(0 0 0 / 0.1);
                    --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1);
                    --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1);
                    --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1);
                }}
                
                * {{
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }}
                
                body {{
                    font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, sans-serif;
                    line-height: 1.6;
                    color: var(--gray-800);
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    min-height: 100vh;
                    padding: 1rem;
                }}
                
                .container {{
                    max-width: 1400px;
                    margin: 0 auto;
                    background: white;
                    border-radius: var(--border-radius-lg);
                    box-shadow: var(--shadow-xl);
                    overflow: hidden;
                }}
                
                .header {{
                    background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-light) 100%);
                    color: white;
                    padding: 2rem;
                    text-align: center;
                }}
                
                .header h1 {{
                    font-size: 2rem;
                    font-weight: 700;
                    margin-bottom: 0.5rem;
                    letter-spacing: -0.025em;
                }}
                
                .header p {{
                    font-size: 1rem;
                    opacity: 0.9;
                    font-weight: 400;
                }}
                
                .main-content {{
                    padding: 2rem;
                }}
                
                .overview-grid {{
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    gap: 2rem;
                    margin-bottom: 3rem;
                }}
                
                .stats-section {{
                    display: grid;
                    grid-template-columns: repeat(2, 1fr);
                    gap: 1rem;
                }}
                
                .stat-card {{
                    background: var(--gray-50);
                    border: 1px solid var(--gray-200);
                    border-radius: var(--border-radius);
                    padding: 1.5rem;
                    text-align: center;
                    transition: all 0.2s ease;
                }}
                
                .stat-card:hover {{
                    background: white;
                    box-shadow: var(--shadow-md);
                    transform: translateY(-2px);
                }}
                
                .stat-value {{
                    font-size: 2rem;
                    font-weight: 700;
                    color: var(--primary-color);
                    display: block;
                    margin-bottom: 0.25rem;
                }}
                
                .stat-label {{
                    font-size: 0.875rem;
                    color: var(--gray-600);
                    font-weight: 500;
                }}
                
                .chart-section {{
                    background: white;
                    border: 1px solid var(--gray-200);
                    border-radius: var(--border-radius);
                    padding: 1.5rem;
                    box-shadow: var(--shadow-sm);
                }}
                
                .chart-section h3 {{
                    font-size: 1.125rem;
                    font-weight: 600;
                    color: var(--gray-800);
                    margin-bottom: 1rem;
                    display: flex;
                    align-items: center;
                    gap: 0.5rem;
                }}
                
                .chart-section h3::before {{
                    content: "📊";
                    font-size: 1rem;
                }}
                
                .chart-section img {{
                    width: 100%;
                    height: auto;
                    border-radius: var(--border-radius);
                }}
                
                .section {{
                    background: white;
                    border: 1px solid var(--gray-200);
                    border-radius: var(--border-radius);
                    margin-bottom: 2rem;
                    overflow: hidden;
                    box-shadow: var(--shadow-sm);
                }}
                
                .section-header {{
                    background: var(--gray-50);
                    padding: 1.5rem;
                    border-bottom: 1px solid var(--gray-200);
                }}
                
                .section-header h2 {{
                    font-size: 1.5rem;
                    font-weight: 600;
                    color: var(--gray-800);
                    display: flex;
                    align-items: center;
                    gap: 0.75rem;
                }}
                
                .section-content {{
                    padding: 1.5rem;
                }}
                
                .grid {{
                    display: grid;
                    gap: 1.5rem;
                }}
                
                .grid-2 {{
                    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
                }}
                
                .grid-3 {{
                    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                }}
                
                .card {{
                    background: white;
                    border: 1px solid var(--gray-200);
                    border-radius: var(--border-radius);
                    padding: 1.5rem;
                    transition: all 0.2s ease;
                }}
                
                .card:hover {{
                    box-shadow: var(--shadow-md);
                    transform: translateY(-2px);
                    border-color: var(--primary-color);
                }}
                
                .card-header {{
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    margin-bottom: 1rem;
                    padding-bottom: 0.75rem;
                    border-bottom: 1px solid var(--gray-200);
                }}
                
                .card-title {{
                    font-size: 1.125rem;
                    font-weight: 600;
                    color: var(--gray-800);
                }}
                
                .card-badge {{
                    background: var(--primary-color);
                    color: white;
                    padding: 0.25rem 0.75rem;
                    border-radius: 9999px;
                    font-size: 0.75rem;
                    font-weight: 500;
                }}
                
                .metrics-grid {{
                    display: grid;
                    grid-template-columns: repeat(4, 1fr);
                    gap: 1rem;
                    margin: 1rem 0;
                }}
                
                .metric {{
                    text-align: center;
                    padding: 0.75rem;
                    background: var(--gray-50);
                    border-radius: var(--border-radius);
                }}
                
                .metric-value {{
                    font-size: 1.25rem;
                    font-weight: 600;
                    color: var(--primary-color);
                }}
                
                .metric-label {{
                    font-size: 0.75rem;
                    color: var(--gray-600);
                    margin-top: 0.25rem;
                }}
                
                .inquiry-sample {{
                    background: var(--gray-50);
                    border-left: 4px solid var(--primary-color);
                    padding: 1rem;
                    margin: 0.75rem 0;
                    border-radius: 0 var(--border-radius) var(--border-radius) 0;
                    font-style: italic;
                    line-height: 1.5;
                }}
                
                .inquiry-meta {{
                    font-size: 0.8rem;
                    color: var(--gray-600);
                    margin-top: 0.5rem;
                    font-style: normal;
                }}
                
                .category-chart {{
                    text-align: center;
                    margin: 1rem 0;
                    background: var(--gray-50);
                    padding: 1rem;
                    border-radius: var(--border-radius);
                }}
                
                .category-chart img {{
                    max-width: 100%;
                    height: auto;
                    border-radius: var(--border-radius);
                }}
                
                .team-badges {{
                    display: flex;
                    flex-wrap: wrap;
                    gap: 0.5rem;
                    margin: 0.75rem 0;
                }}
                
                .team-badge {{
                    background: var(--accent-color);
                    color: white;
                    padding: 0.25rem 0.75rem;
                    border-radius: 9999px;
                    font-size: 0.75rem;
                    font-weight: 500;
                }}
                
                .footer {{
                    text-align: center;
                    padding: 2rem;
                    background: var(--gray-50);
                    border-top: 1px solid var(--gray-200);
                    color: var(--gray-600);
                    font-size: 0.875rem;
                }}
                
                @media (max-width: 768px) {{
                    .overview-grid {{
                        grid-template-columns: 1fr;
                        gap: 1.5rem;
                    }}
                    
                    .stats-section {{
                        grid-template-columns: 1fr;
                    }}
                    
                    .metrics-grid {{
                        grid-template-columns: repeat(2, 1fr);
                    }}
                    
                    .main-content {{
                        padding: 1rem;
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
                    <div class="overview-grid">
                        <div class="stats-section">
                            <div class="stat-card">
                                <span class="stat-value">{total_inquiries:,}</span>
                                <div class="stat-label">총 문의</div>
                            </div>
        """
        
        # 기본 통계 카드들 추가
        if 'teams' in overall_summary:
            team_count = overall_summary['teams']['count']
            html_template += f"""
                            <div class="stat-card">
                                <span class="stat-value">{team_count}</span>
                                <div class="stat-label">담당팀</div>
                            </div>
            """
        
        if 'categories' in overall_summary:
            cat_count = overall_summary['categories']['count']
            html_template += f"""
                            <div class="stat-card">
                                <span class="stat-value">{cat_count}</span>
                                <div class="stat-label">카테고리</div>
                            </div>
            """
        
        if 'urgent_count' in overall_summary:
            urgent_count = overall_summary['urgent_count']
            html_template += f"""
                            <div class="stat-card">
                                <span class="stat-value">{urgent_count}</span>
                                <div class="stat-label">긴급 문의</div>
                            </div>
            """
        
        html_template += """
                        </div>
                        <div class="chart-section">
        """
        
        # 주간별 트렌드 차트
        if 'weekly_trend' in charts:
            html_template += f"""
                            <h3>주간별 문의 트렌드</h3>
                            <img src="{charts['weekly_trend']}" alt="주간별 트렌드">
            """
        elif 'team_overview' in charts:
            html_template += f"""
                            <h3>팀별 문의 현황</h3>
                            <img src="{charts['team_overview']}" alt="팀별 현황">
            """
        
        html_template += """
                        </div>
                    </div>
        """
        
        # 팀별 분석 섹션
        if 'team_analysis' in results and results['team_analysis']:
            html_template += """
                    <div class="section">
                        <div class="section-header">
                            <h2>🏢 팀별 문의 내용 분석</h2>
                        </div>
                        <div class="section-content">
                            <div class="grid grid-2">
            """
            
            for team_name, team_info in results['team_analysis'].items():
                basic_info = team_info['basic_info']
                
                html_template += f"""
                                <div class="card">
                                    <div class="card-header">
                                        <h3 class="card-title">{team_name}</h3>
                                        <span class="card-badge">{basic_info['total_inquiries']}건</span>
                                    </div>
                                    
                                    <div class="metrics-grid">
                                        <div class="metric">
                                            <div class="metric-value">{basic_info['total_inquiries']}</div>
                                            <div class="metric-label">총 문의</div>
                                        </div>
                                        <div class="metric">
                                            <div class="metric-value">{basic_info['urgent_count']}</div>
                                            <div class="metric-label">긴급</div>
                                        </div>
                                        <div class="metric">
                                            <div class="metric-value">{basic_info['answered_count']}</div>
                                            <div class="metric-label">답변완료</div>
                                        </div>
                                        <div class="metric">
                                            <div class="metric-value">{basic_info['avg_content_length']:.0f}</div>
                                            <div class="metric-label">평균길이</div>
                                        </div>
                                    </div>
                """
                
                # 세부 카테고리 분포 차트
                if 'team_categories' in charts and team_name in charts['team_categories']:
                    html_template += f"""
                                    <div class="category-chart">
                                        <h4 style="margin-bottom: 1rem; color: var(--gray-700); font-size: 1rem; font-weight: 600;">세부 카테고리 분포</h4>
                                        <img src="{charts['team_categories'][team_name]}" alt="{team_name} 카테고리 분포">
                                    </div>
                    """
                
                # 대표 문의 사례
                html_template += """
                                    <div style="margin-top: 1.5rem;">
                                        <h4 style="margin-bottom: 1rem; color: var(--gray-700); font-size: 1rem; font-weight: 600;">📋 대표 문의 사례</h4>
                """
                
                for sample in team_info['sample_inquiries']:
                    content_preview = sample['content'][:100] + '...' if len(sample['content']) > 100 else sample['content']
                    html_template += f"""
                                        <div class="inquiry-sample">
                                            "{content_preview}"
                                            <div class="inquiry-meta">
                                                길이: {sample['length']}자 | {sample['sub_category']} 
                                                | {'긴급' if sample['is_urgent'] else '일반'}
                                            </div>
                                        </div>
                    """
                
                html_template += """
                                    </div>
                                </div>
                """
            
            html_template += """
                            </div>
                        </div>
                    </div>
            """
        
        # 세부 카테고리별 분석 섹션
        if 'category_analysis' in results and results['category_analysis']:
            # 상위 12개 카테고리만 표시
            sorted_categories = sorted(results['category_analysis'].items(), 
                                     key=lambda x: x[1]['basic_info']['total_inquiries'], 
                                     reverse=True)[:12]
            
            html_template += """
                    <div class="section">
                        <div class="section-header">
                            <h2>📂 세부 카테고리별 문의 내용</h2>
                        </div>
                        <div class="section-content">
                            <div class="grid grid-3">
            """
            
            for category_name, category_info in sorted_categories:
                basic_info = category_info['basic_info']
                
                html_template += f"""
                                <div class="card">
                                    <div class="card-header">
                                        <h3 class="card-title" style="font-size: 1rem; line-height: 1.4;">{category_name}</h3>
                                        <span class="card-badge">{basic_info['total_inquiries']}건</span>
                                    </div>
                                    
                                    <div class="metrics-grid" style="grid-template-columns: repeat(3, 1fr);">
                                        <div class="metric">
                                            <div class="metric-value">{basic_info['total_inquiries']}</div>
                                            <div class="metric-label">총 문의</div>
                                        </div>
                                        <div class="metric">
                                            <div class="metric-value">{basic_info['urgent_count']}</div>
                                            <div class="metric-label">긴급</div>
                                        </div>
                                        <div class="metric">
                                            <div class="metric-value">{basic_info['avg_content_length']:.0f}</div>
                                            <div class="metric-label">평균길이</div>
                                        </div>
                                    </div>
                                    
                                    <div style="margin: 1rem 0;">
                                        <h4 style="margin-bottom: 0.75rem; color: var(--gray-700); font-size: 0.875rem; font-weight: 600;">담당팀</h4>
                                        <div class="team-badges">
                """
                
                for team, count in list(category_info['team_distribution'].items())[:3]:
                    html_template += f'<span class="team-badge">{team}: {count}건</span>'
                
                html_template += """
                                        </div>
                                    </div>
                                    
                                    <div>
                                        <h4 style="margin-bottom: 0.75rem; color: var(--gray-700); font-size: 0.875rem; font-weight: 600;">대표 문의</h4>
                """
                
                for sample in category_info['sample_inquiries'][:1]:  # 1개만
                    content_preview = sample['content'][:80] + '...' if len(sample['content']) > 80 else sample['content']
                    html_template += f"""
                                        <div class="inquiry-sample" style="padding: 0.75rem; font-size: 0.875rem;">
                                            "{content_preview}"
                                            <div class="inquiry-meta">
                                                {sample['assigned_team']} | {sample['length']}자
                                            </div>
                                        </div>
                    """
                
                html_template += """
                                    </div>
                                </div>
                """
            
            html_template += """
                            </div>
                        </div>
                    </div>
            """
        
        # 주간별 트렌드 섹션 (간소화)
        if 'weekly_trends' in results and results['weekly_trends']:
            html_template += """
                <div class="section">
                    <div class="section-header">
                        <h2>📅 주간별 문의 트렌드</h2>
                    </div>
                    <div class="section-content">
            """
            
            if 'weekly_trend' in charts:
                html_template += f"""
                        <div class="chart-section">
                            <img src="{charts['weekly_trend']}" alt="주간별 트렌드">
                        </div>
                """
            
            html_template += """
                    </div>
                </div>
            """
        
        # 푸터
        html_template += f"""
                </div>
                
                <div class="footer">
                    <p>카테고리 기반 VoC 분석 보고서</p>
                    <p>생성일시: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Pretendard 폰트 적용</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        return html_template

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