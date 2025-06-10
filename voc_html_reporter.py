# voc_html_reporter.py (모던 디자인 적용 버전)
"""
카테고리 기반 VoC HTML 보고서 생성기 - 모던 디자인 적용
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
    get_main_scripts,
    process_overview_data, process_team_data, process_journey_data, process_category_data
)
from html_reporter.styles import get_main_styles
from output_manager import get_report_filename

class CategoryVoCHTMLReporter:
    """카테고리 기반 VoC HTML 보고서 생성기 - 모던 디자인"""
    
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def generate_html_report(self, results: dict) -> str:
        """HTML 보고서 생성 - 모던 탭 기반 레이아웃"""
        print("🌐 모던 HTML 보고서 생성 중...")
        
        # 데이터 처리
        overview_data = process_overview_data(results)
        team_cards = process_team_data(results)
        journey_cards = process_journey_data(results)
        category_cards = process_category_data(results)
        
        # 탭 기반 HTML 구조
        html_content = get_base_template().format(
            styles=get_main_styles(),
            header=get_header_template().format(**overview_data),
            content=self._generate_tab_content(overview_data, team_cards, journey_cards, category_cards),
            footer=get_footer_template().format(generated_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
            scripts=f"""
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
            """
        )
        
        return html_content

    def _generate_tab_content(self, overview_data, team_cards, journey_cards, category_cards):
        """탭 컨텐츠 생성"""
        
        # 개요 탭
        overview_content = get_overview_template().format(**overview_data)
        
        # 팀별 탭
        team_cards_html = ""
        for team in team_cards:
            team_cards_html += get_team_card_template().format(**team)
        team_content = get_team_section_template().format(team_cards=team_cards_html)
        
        # 유저 여정 탭
        journey_cards_html = ""
        for journey in journey_cards:
            journey_cards_html += get_journey_card_template().format(**journey)
        journey_content = get_journey_section_template().format(journey_cards=journey_cards_html)
        
        # 카테고리 탭 + 모달들
        category_cards_html = ""
        modals_html = ""
        for category in category_cards:
            category_cards_html += get_category_card_template().format(**category)
            modals_html += get_modal_template().format(
                modal_id=category['modal_id'],
                title=f"{category['name']} - 전체 {category['total_inquiries']}건",
                content=category['modal_content']
            )
        category_content = get_category_section_template().format(category_cards=category_cards_html)
        
        # 전체 컨텐츠 조합
        all_content = f"""
            {overview_content}
            {team_content}
            {journey_content}
            {category_content}
            
            <!-- 모달들 -->
            {modals_html}
        """
        
        return all_content

    def save_and_open_html_report(self, results: dict) -> str:
        """HTML 보고서 저장 및 브라우저에서 열기 - output 폴더에!"""
        html_content = self.generate_html_report(results)
        
        # output/reports/ 폴더에 저장
        filename = get_report_filename()
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        file_path = os.path.abspath(filename)
        print(f"✅ 모던 HTML 보고서 저장: {filename}")
        
        try:
            webbrowser.open(f'file://{file_path}')
            print("🌐 브라우저에서 모던 보고서를 열었습니다.")
        except Exception as e:
            print(f"브라우저 열기 실패: {e}")
        
        return filename

    def save_html_only(self, results: dict, filename: str = None) -> str:
        """HTML 보고서만 저장"""
        html_content = self.generate_html_report(results)
        
        if filename is None:
            filename = get_report_filename()
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ 모던 HTML 보고서 저장: {filename}")
        return filename