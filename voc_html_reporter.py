# voc_html_reporter.py (완료율 필드 추가된 버전)
"""
카테고리 기반 VoC HTML 보고서 생성기 - 완료율 칼럼 지원
"""

import pandas as pd
import webbrowser
import os
from datetime import datetime

# 실제로 사용하는 것만 import
from html_reporter import (
    get_base_template, get_header_template, get_overview_template,
    get_modal_template, get_footer_template,
    get_main_scripts,
    process_overview_data, process_category_data,
    generate_team_options  
)
from html_reporter.templates.category_table import get_category_table_row_template, get_team_filter_options
from html_reporter.styles import get_main_styles
from output_manager import get_report_filename

class CategoryVoCHTMLReporter:
    """카테고리 기반 VoC HTML 보고서 생성기 - 단일 페이지"""
    
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def generate_html_report(self, results: dict) -> str:
        """HTML 보고서 생성 - 단일 페이지"""
        print("🌐 단일 페이지 HTML 보고서 생성 중...")
        
        # 데이터 처리 (사용하는 것만)
        overview_data = process_overview_data(results)
        
        # 팀 옵션 동적 생성
        team_options = generate_team_options(results)
        
        # 카테고리 테이블 데이터 생성
        category_table_data = self._generate_category_table_data(results)
        
        # 단일 페이지 HTML 구조
        html_content = get_base_template().format(
            styles=get_main_styles(),
            header=get_header_template().format(**overview_data),
            content=get_overview_template().format(
                **overview_data,
                team_filter_options=category_table_data['team_filter_options'],
                category_table_rows=category_table_data['category_table_rows']
            ) + category_table_data['modals_html'],
            footer=get_footer_template().format(generated_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
            scripts=f"""
            <script>
                {get_main_scripts()}
            </script>
            """
        )
        
        return html_content

    def _generate_category_table_data(self, results: dict):
            """카테고리 테이블 로우 데이터 생성 - 문의율 필드 포함"""
            if 'category_analysis' not in results:
                return {
                    'category_table_rows': '',
                    'team_filter_options': '',
                    'modals_html': ''
                }
            
            category_cards = process_category_data(results)
            
            # 전체 문의 수 계산 (비율 계산용)
            total_inquiries_for_percentage = 0
            if 'overall_summary' in results:
                total_inquiries_for_percentage = results['overall_summary'].get('total_inquiries', 1)
            else:
                # 전체 문의 수를 구할 수 없으면 카테고리별 문의 수의 합으로 계산
                total_inquiries_for_percentage = sum(card['total_inquiries'] for card in category_cards)
            
            print(f"📋 카테고리 데이터 처리: {len(category_cards)}개 카테고리, 전체 문의: {total_inquiries_for_percentage}건")
            
            # 테이블 로우 HTML 생성
            table_rows_html = ""
            modals_html = ""
            
            # 팀 목록 수집
            teams = set()
            if 'team_analysis' in results:
                teams.update(results['team_analysis'].keys())
            
            for category in category_cards:
                # 문의율 계산 (전체 대비 비율)
                inquiry_rate = round((category['total_inquiries'] / total_inquiries_for_percentage * 100), 1) if total_inquiries_for_percentage > 0 else 0
                
                # 긴급률 레벨 계산
                urgent_rate = float(category['urgent_rate'])
                if urgent_rate >= 20:
                    urgent_level = 'high'
                elif urgent_rate >= 10:
                    urgent_level = 'medium'
                else:
                    urgent_level = 'low'
                
                # 완료율 레벨 계산
                answer_rate = float(category.get('answer_rate', 0))  # 기본값 0
                if answer_rate >= 80:
                    complete_level = 'high'
                elif answer_rate >= 50:
                    complete_level = 'medium'
                else:
                    complete_level = 'low'
                
                # 카테고리명을 소문자로 변환 (검색용)
                name_lower = category['name'].lower()
                
                print(f"  📝 카테고리 처리: {category['name']} (문의율: {inquiry_rate}%, 완료율: {answer_rate}%, 모달 ID: {category['modal_id']})")
                
                # 테이블 로우 생성 (문의율 필드 추가)
                table_rows_html += get_category_table_row_template().format(
                    name=category['name'],
                    name_lower=name_lower,
                    main_team=category['main_team'],
                    main_journey=category['main_journey'],
                    total_inquiries=category['total_inquiries'],
                    inquiry_rate=inquiry_rate,  # 문의율 추가
                    urgent_rate=category['urgent_rate'],
                    urgent_level=urgent_level,
                    answer_rate=answer_rate,  # 완료율 추가
                    complete_level=complete_level,  # 완료율 레벨 추가
                    modal_id=category['modal_id']
                )
                
                # 개별 모달 생성
                modal_content = category.get('modal_content', '<div>문의 내용이 없습니다.</div>')
                modals_html += get_modal_template().format(
                    modal_id=category['modal_id'],
                    title=f"{category['name']} - 전체 {category['total_inquiries']}건 ({inquiry_rate}%)",
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

    def save_and_open_html_report(self, results: dict) -> str:
        """HTML 보고서 저장 및 브라우저에서 열기"""
        html_content = self.generate_html_report(results)
        
        # output/reports/ 폴더에 저장
        filename = get_report_filename()
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        file_path = os.path.abspath(filename)
        print(f"✅ 단일 페이지 HTML 보고서 저장: {filename}")
        
        try:
            webbrowser.open(f'file://{file_path}')
            print("🌐 브라우저에서 단일 페이지 보고서를 열었습니다.")
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
        
        print(f"✅ 단일 페이지 HTML 보고서 저장: {filename}")
        return filename