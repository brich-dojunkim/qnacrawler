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
    get_category_section_template, get_category_card_template,
    get_modal_template, get_footer_template,
    get_main_styles, get_main_scripts,
    process_overview_data, process_team_data, process_category_data
)

class CategoryVoCHTMLReporter:
    """카테고리 기반 VoC HTML 보고서 생성기 (모듈화 버전)"""
    
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def generate_html_report(self, results: dict) -> str:
        """HTML 보고서 생성"""
        print("🌐 카테고리 기반 HTML 보고서 생성 중...")
        
        # 데이터 처리
        overview_data = process_overview_data(results)
        team_cards = process_team_data(results)
        category_cards = process_category_data(results)
        
        # HTML 조각들 생성
        header_html = get_header_template().format(**overview_data)
        overview_html = get_overview_template().format(**overview_data, rank_tables="")
        
        # 팀별 섹션
        team_cards_html = ""
        for team in team_cards:
            team_cards_html += get_team_card_template().format(**team)
        team_section_html = get_team_section_template().format(team_cards=team_cards_html)
        
        # 카테고리별 섹션
        category_cards_html = ""
        modals_html = ""
        for category in category_cards:
            category_cards_html += get_category_card_template().format(**category)
            modals_html += get_modal_template().format(
                modal_id=category['modal_id'],
                title=f"{category['name']} - 전체 {category['total_inquiries']}건",
                content=category['modal_content']
            )
        category_section_html = get_category_section_template().format(category_cards=category_cards_html)
        
        # 푸터
        footer_html = get_footer_template().format(
            generated_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )
        
        # 전체 콘텐츠 조합
        content = overview_html + team_section_html + category_section_html + modals_html
        
        # 최종 HTML 조합
        final_html = get_base_template().format(
            styles=get_main_styles(),
            header=header_html,
            content=content,
            footer=footer_html,
            scripts=f"<script>{get_main_scripts()}</script>"
        )
        
        return final_html

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