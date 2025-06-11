# voc_html_reporter.py (모달 시스템 확인)
"""
카테고리 기반 VoC HTML 보고서 생성기 - 개별 모달 시스템
"""

import pandas as pd
import webbrowser
import os
from datetime import datetime

# 분리된 모듈들 임포트
from html_reporter import (
    get_base_template, get_header_template, get_overview_template,
    get_journey_section_template, get_journey_card_template,
    get_category_section_template, get_category_card_template,
    get_modal_template, get_footer_template,
    get_main_scripts,
    process_overview_data, process_journey_data, process_category_data,
    generate_team_options  
)
from html_reporter.templates.category_table import get_category_table_row_template, get_team_filter_options
from html_reporter.styles import get_main_styles
from output_manager import get_report_filename

class CategoryVoCHTMLReporter:
    """카테고리 기반 VoC HTML 보고서 생성기 - 개별 모달 시스템"""
    
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def generate_html_report(self, results: dict) -> str:
        """HTML 보고서 생성 - 개별 모달 시스템"""
        print("🌐 개별 모달 시스템 HTML 보고서 생성 중...")
        
        # 데이터 처리
        overview_data = process_overview_data(results)
        journey_cards = process_journey_data(results)
        category_cards = process_category_data(results)
        
        # 팀 옵션 동적 생성
        team_options = generate_team_options(results)
        
        # 카테고리 테이블 데이터 생성
        category_table_data = self._generate_category_table_data(results)
        
        # 2개 탭 기반 HTML 구조
        html_content = get_base_template().format(
            styles=get_main_styles(),
            header=get_header_template().format(**overview_data),
            content=self._generate_tab_content(overview_data, journey_cards, category_cards, team_options, category_table_data),
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

    def _generate_category_table_data(self, results: dict):
        """카테고리 테이블 로우 데이터 생성 - 개별 모달 확인"""
        if 'category_analysis' not in results:
            return {
                'category_table_rows': '',
                'team_filter_options': '',
                'modals_html': ''
            }
        
        category_cards = process_category_data(results)
        
        print(f"📋 카테고리 데이터 처리: {len(category_cards)}개 카테고리")
        
        # 테이블 로우 HTML 생성
        table_rows_html = ""
        modals_html = ""
        
        # 팀 목록 수집
        teams = set()
        if 'team_analysis' in results:
            teams.update(results['team_analysis'].keys())
        
        for category in category_cards:
            # 긴급률 레벨 계산
            urgent_rate = float(category['urgent_rate'])
            if urgent_rate >= 20:
                urgent_level = 'high'
            elif urgent_rate >= 10:
                urgent_level = 'medium'
            else:
                urgent_level = 'low'
            
            # 카테고리명을 소문자로 변환 (검색용)
            name_lower = category['name'].lower()
            
            print(f"  📝 카테고리 처리: {category['name']} (모달 ID: {category['modal_id']})")
            
            # 테이블 로우 생성
            table_rows_html += get_category_table_row_template().format(
                name=category['name'],
                name_lower=name_lower,
                main_team=category['main_team'],
                main_journey=category['main_journey'],
                total_inquiries=category['total_inquiries'],
                urgent_rate=category['urgent_rate'],
                urgent_level=urgent_level,
                modal_id=category['modal_id']
            )
            
            # 개별 모달 생성
            modal_content = category.get('modal_content', '<div>문의 내용이 없습니다.</div>')
            modals_html += get_modal_template().format(
                modal_id=category['modal_id'],
                title=f"{category['name']} - 전체 {category['total_inquiries']}건",
                content=modal_content
            )
            
            # 팀 정보 수집
            teams.add(category['main_team'])
        
        # 팀 필터 옵션 생성
        team_filter_options = get_team_filter_options(teams)
        
        print(f"✅ 생성 완료: {len(category_cards)}개 테이블 로우, {len(category_cards)}개 모달")
        
        return {
            'category_table_rows': table_rows_html,
            'team_filter_options': team_filter_options,
            'modals_html': modals_html
        }

    def _generate_tab_content(self, overview_data, journey_cards, category_cards, team_options, category_table_data):
        """2개 탭 컨텐츠 생성 - 개별 모달 포함"""
        
        # 개요 탭 (아코디언 + 인라인 드롭다운 테이블 뷰)
        overview_content = get_overview_template().format(
            **overview_data,
            team_filter_options=category_table_data['team_filter_options'],
            category_table_rows=category_table_data['category_table_rows']
        )
        
        # 유저 여정 탭
        journey_cards_html = ""
        for journey in journey_cards:
            journey_cards_html += get_journey_card_template().format(**journey)
        journey_content = get_journey_section_template().format(journey_cards=journey_cards_html)
        
        # 전체 컨텐츠 조합 (2개 탭 + 개별 모달들)
        all_content = f"""
            {overview_content}
            {journey_content}
            
            <!-- 개별 카테고리 모달들 -->
            {category_table_data['modals_html']}
        """
        
        return all_content

    def save_and_open_html_report(self, results: dict) -> str:
        """HTML 보고서 저장 및 브라우저에서 열기"""
        html_content = self.generate_html_report(results)
        
        # output/reports/ 폴더에 저장
        filename = get_report_filename()
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        file_path = os.path.abspath(filename)
        print(f"✅ 개별 모달 시스템 HTML 보고서 저장: {filename}")
        
        try:
            webbrowser.open(f'file://{file_path}')
            print("🌐 브라우저에서 개별 모달 시스템 보고서를 열었습니다.")
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
        
        print(f"✅ 개별 모달 시스템 HTML 보고서 저장: {filename}")
        return filename