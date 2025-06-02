# voc_html_reporter.py (새로운 메인 파일 - 깔끔해진 버전)
"""
카테고리 기반 VoC HTML 보고서 생성기 (모듈화 버전)
"""

import pandas as pd
import webbrowser
import os
from datetime import datetime

# 분리된 모듈들 임포트
from html_reporter import (
    get_base_template, get_header_template, get_overview_template,
    get_team_section_template, get_team_card_template, 
    get_journey_section_template, get_journey_card_template,
    get_category_section_template, get_category_card_template,
    get_modal_template, get_footer_template,
    get_main_styles, get_main_scripts,
    process_overview_data, process_team_data, process_journey_data, process_category_data
)

class CategoryVoCHTMLReporter:
    """카테고리 기반 VoC HTML 보고서 생성기 (모듈화 버전)"""
    
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def generate_html_report(self, results: dict) -> str:
        """HTML 보고서 생성 - 탭 기반 레이아웃"""
        print("🌐 카테고리 기반 HTML 보고서 생성 중...")
        
        # 데이터 처리
        overview_data = process_overview_data(results)
        team_cards = process_team_data(results)
        journey_cards = process_journey_data(results)
        category_cards = process_category_data(results)
        
        # 탭 기반 HTML 구조
        html_content = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>카테고리 기반 VoC 분석 보고서</title>
    <link href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" rel="stylesheet">
    <style>{get_main_styles()}</style>
    <style>
        /* 탭 스타일 추가 */
        .tab-navigation {{
            background: white;
            border-bottom: 1px solid #e2e8f0;
            padding: 0 2rem;
        }}
        
        .tab-nav {{
            display: flex;
            gap: 0;
        }}
        
        .tab-btn {{
            padding: 1rem 2rem;
            border: none;
            background: none;
            font-size: 1rem;
            font-weight: 600;
            color: #64748b;
            cursor: pointer;
            border-bottom: 3px solid transparent;
            transition: all 0.3s ease;
        }}
        
        .tab-btn.active {{
            color: #2563eb;
            border-bottom-color: #2563eb;
            background: #f8fafc;
        }}
        
        .tab-btn:hover:not(.active) {{
            color: #374151;
            background: #f1f5f9;
        }}
        
        .tab-content {{
            display: none;
            padding: 2rem;
        }}
        
        .tab-content.active {{
            display: block;
        }}
        
        @media (max-width: 768px) {{
            .tab-nav {{
                flex-wrap: wrap;
            }}
            
            .tab-btn {{
                flex: 1;
                padding: 0.75rem 1rem;
                font-size: 0.9rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        {get_header_template().format(**overview_data)}
        
        <!-- 탭 네비게이션 -->
        <div class="tab-navigation">
            <div class="tab-nav">
                <button class="tab-btn active" onclick="switchTab('overview')">📊 분석 개요</button>
                <button class="tab-btn" onclick="switchTab('teams')">👥 팀별 분석</button>
                <button class="tab-btn" onclick="switchTab('journey')">🎯 유저 여정</button>
                <button class="tab-btn" onclick="switchTab('categories')">📂 세부 카테고리</button>
            </div>
        </div>
        
        <div class="main-content">
            <!-- 분석 개요 탭 -->
            <div id="overview" class="tab-content active">
                {get_overview_template().format(**overview_data)}
            </div>
            
            <!-- 팀별 분석 탭 -->
            <div id="teams" class="tab-content">"""
        
        # 팀별 섹션 내용
        team_cards_html = ""
        for team in team_cards:
            team_cards_html += get_team_card_template().format(**team)
        html_content += get_team_section_template().format(team_cards=team_cards_html).replace('<div class="major-section">', '').replace('</div>', '', 1)
        
        html_content += """
            </div>
            
            <!-- 유저 여정 탭 -->
            <div id="journey" class="tab-content">"""
        
        # 유저 여정별 섹션 내용  
        journey_cards_html = ""
        for journey in journey_cards:
            journey_cards_html += get_journey_card_template().format(**journey)
        html_content += get_journey_section_template().format(journey_cards=journey_cards_html).replace('<div class="major-section">', '').replace('</div>', '', 1)
        
        html_content += """
            </div>
            
            <!-- 세부 카테고리 탭 -->
            <div id="categories" class="tab-content">"""
        
        # 카테고리별 섹션 내용
        category_cards_html = ""
        modals_html = ""
        for category in category_cards:
            category_cards_html += get_category_card_template().format(**category)
            modals_html += get_modal_template().format(
                modal_id=category['modal_id'],
                title=f"{category['name']} - 전체 {category['total_inquiries']}건",
                content=category['modal_content']
            )
        html_content += get_category_section_template().format(category_cards=category_cards_html).replace('<div class="major-section">', '').replace('</div>', '', 1)
        
        html_content += f"""
            </div>
        </div>
        
        {get_footer_template().format(generated_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))}
        
        <!-- 모달들 -->
        {modals_html}
    </div>
    
    <script>
        {get_main_scripts()}
        
        function switchTab(tabName) {{
            // 모든 탭 컨텐츠 숨기기
            document.querySelectorAll('.tab-content').forEach(tab => {{
                tab.classList.remove('active');
            }});
            
            // 모든 탭 버튼 비활성화
            document.querySelectorAll('.tab-btn').forEach(btn => {{
                btn.classList.remove('active');
            }});
            
            // 선택된 탭 활성화
            document.getElementById(tabName).classList.add('active');
            event.target.classList.add('active');
        }}
    </script>
</body>
</html>"""
        
        return html_content

    def save_and_open_html_report(self, results: dict) -> str:
        """HTML 보고서 저장 및 브라우저에서 열기"""
        html_content = self.generate_html_report(results)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"category_voc_report_{timestamp}.html"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        file_path = os.path.abspath(filename)
        print(f"✅ HTML 보고서 저장: {filename}")
        
        try:
            webbrowser.open(f'file://{file_path}')
            print("🌐 브라우저에서 보고서를 열었습니다.")
        except Exception as e:
            print(f"브라우저 열기 실패: {e}")
        
        return filename

    def save_html_only(self, results: dict, filename: str = None) -> str:
        """HTML 보고서만 저장 (브라우저 열기 없음)"""
        html_content = self.generate_html_report(results)
        
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"category_voc_report_{timestamp}.html"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ HTML 보고서 저장: {filename}")
        return filename