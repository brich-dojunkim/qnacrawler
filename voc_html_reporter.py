# voc_html_reporter.py (문의 모달 템플릿 import 방식)
"""
카테고리 기반 VoC HTML 보고서 생성기 - 완료율 칼럼 지원 + 드로어 통합 + 데이터 변환 개선
"""

import pandas as pd
import webbrowser
import os
import json
import traceback
from datetime import datetime

# 실제로 사용하는 것만 import (드로어와 문의 모달은 직접 import)
from html_reporter import (
    get_base_template, get_header_template, get_overview_template,
    get_modal_template, get_footer_template,
    get_main_scripts,
    process_overview_data, process_category_data,
    generate_team_options  
)
from html_reporter.templates.category_table import get_category_table_row_template, get_team_filter_options

# 🚨 직접 import 방식으로 변경
try:
    from html_reporter.templates.inquiry_modal import get_inquiry_modal_template
    print("✅ 문의 모달 템플릿 import 성공")
except ImportError as e:
    print(f"❌ 문의 모달 템플릿 import 실패: {e}")
    def get_inquiry_modal_template():
        return ""

from html_reporter.styles import get_main_styles
from output_manager import get_report_filename

class CategoryVoCHTMLReporter:
    """카테고리 기반 VoC HTML 보고서 생성기 - 단일 페이지 + 드로어 + 문의 모달"""
    
    def __init__(self, df: pd.DataFrame, json_path: str = None):
        self.df = df
        self.json_path = json_path  # 원본 JSON 파일 경로

    def generate_html_report(self, results: dict) -> str:
        """HTML 보고서 생성 - 단일 페이지 + 드로어 + 문의 모달"""
        print("🌐 단일 페이지 HTML 보고서 생성 중... (드로어 + 문의 모달 포함)")
        
        # 데이터 처리 (사용하는 것만)
        overview_data = process_overview_data(results)
        
        # 팀 옵션 동적 생성
        team_options = generate_team_options(results)
        
        # 카테고리 테이블 데이터 생성
        category_table_data = self._generate_category_table_data(results)
        
        # 원본 문의 데이터를 JSON으로 변환 (드로어에서 사용)
        raw_data_json = self._prepare_raw_data_json()
        
        # 🔧 문의 모달 템플릿 가져오기 (이미 import에서 처리됨)
        inquiry_modal_template = get_inquiry_modal_template()
                
        # 단일 페이지 HTML 구조 + 드로어 + 문의 모달
        html_content = get_base_template().format(
            styles=get_main_styles(),
            header=get_header_template().format(**overview_data),
            content=get_overview_template().format(
                **overview_data,
                team_filter_options=category_table_data['team_filter_options'],
                category_table_rows=category_table_data['category_table_rows'],
                inquiry_modal_template=inquiry_modal_template  # 🚨 문의 모달 템플릿
            ) + category_table_data['modals_html'],
            footer=get_footer_template().format(generated_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
            scripts=f"""
            <script>
                // 원본 문의 데이터를 전역 변수로 저장 (드로어 + 문의 모달에서 사용)
                window.rawInquiryData = {raw_data_json};
                
                {get_main_scripts()}
            </script>
            """
        )
        
        print("🎉 HTML 보고서 생성 완료 (드로어 + 문의 모달 통합)")
        return html_content

    def _prepare_raw_data_json(self):
        """원본 문의 데이터를 드로어 + 문의 모달에서 사용할 수 있도록 JSON으로 변환 (강화된 디버깅)"""
        try:
            # 원본 JSON 파일 직접 사용 시도
            if self.json_path and os.path.exists(self.json_path):
                print(f"📁 원본 JSON 파일 직접 사용 시도: {self.json_path}")
                try:
                    with open(self.json_path, 'r', encoding='utf-8') as f:
                        raw_data = json.load(f)
                    print(f"✅ 원본 JSON 파일 로드 성공: {len(raw_data)}건")
                    return json.dumps(raw_data, ensure_ascii=False)
                except Exception as json_error:
                    print(f"❌ 원본 JSON 파일 로드 실패: {json_error}")
                    # DataFrame 방식으로 fallback
            
            print(f"🔍 DataFrame 정보:")
            print(f"   - 행 수: {len(self.df)}")
            print(f"   - 컬럼: {list(self.df.columns)}")
            
            if len(self.df) == 0:
                print("❌ DataFrame이 비어있습니다!")
                return "[]"
            
            # 첫 번째 행 구조 확인
            first_row = self.df.iloc[0]
            print(f"📋 첫 번째 행 구조:")
            for col, value in first_row.items():
                value_str = str(value)[:100] + "..." if len(str(value)) > 100 else str(value)
                print(f"   {col}: {type(value).__name__} = {value_str}")
            
            # 간단한 변환 시도
            print("🔄 데이터 변환 시작...")
            
            # 1단계: to_dict 테스트
            try:
                raw_data = self.df.to_dict('records')
                print(f"✅ to_dict 성공: {len(raw_data)}개 레코드")
            except Exception as e:
                print(f"❌ to_dict 실패: {e}")
                return "[]"
            
            # 2단계: 첫 번째 레코드 구조 확인
            if raw_data:
                first_record = raw_data[0]
                print(f"📊 첫 번째 레코드:")
                for key, value in first_record.items():
                    value_type = type(value).__name__
                    value_str = str(value)[:50] + "..." if len(str(value)) > 50 else str(value)
                    print(f"   {key}: {value_type} = {value_str}")
            
            # 3단계: JSON 직렬화 테스트
            try:
                # 일단 첫 번째 레코드만 시도
                test_json = json.dumps([raw_data[0]], ensure_ascii=False, default=str)
                print(f"✅ JSON 직렬화 테스트 성공: {len(test_json)} 문자")
            except Exception as e:
                print(f"❌ JSON 직렬화 테스트 실패: {e}")
                
                # 문제가 되는 필드 찾기
                problematic_fields = []
                for key, value in raw_data[0].items():
                    try:
                        json.dumps(value, default=str)
                    except:
                        problematic_fields.append(key)
                print(f"🚫 문제 필드들: {problematic_fields}")
            
            # 4단계: 안전한 변환
            print("🛠 안전한 데이터 변환 수행...")
            safe_data = []
            
            for i, record in enumerate(raw_data[:5]):  # 처음 5개만 테스트
                safe_record = {}
                for key, value in record.items():
                    try:
                        if pd.isna(value):
                            safe_record[key] = None
                        elif isinstance(value, pd.Timestamp):
                            safe_record[key] = str(value)
                        elif key == 'answers' and isinstance(value, list):
                            # answers 필드 특별 처리
                            safe_record[key] = value
                        elif key == 'author_info' and isinstance(value, dict):
                            # author_info 필드 특별 처리
                            safe_record[key] = value
                        elif key == 'category' and isinstance(value, dict):
                            # category 필드 특별 처리 
                            safe_record[key] = value
                        else:
                            # JSON 직렬화 테스트
                            json.dumps(value, default=str)
                            safe_record[key] = value
                    except Exception as field_error:
                        print(f"⚠️ 필드 {key} 변환 실패: {field_error}")
                        safe_record[key] = str(value) if value is not None else None
                
                safe_data.append(safe_record)
                print(f"✅ 레코드 {i+1} 변환 완료")
            
            # 전체 데이터 변환
            if len(safe_data) == 5:  # 테스트가 성공하면 전체 변환
                print("🚀 전체 데이터 변환 시작...")
                safe_data = []
                for record in raw_data:
                    safe_record = {}
                    for key, value in record.items():
                        try:
                            if pd.isna(value):
                                safe_record[key] = None
                            elif isinstance(value, pd.Timestamp):
                                safe_record[key] = str(value)
                            elif key in ['answers', 'author_info', 'category'] and isinstance(value, (list, dict)):
                                # 복합 필드 특별 처리
                                safe_record[key] = value
                            else:
                                json.dumps(value, default=str)
                                safe_record[key] = value
                        except:
                            safe_record[key] = str(value) if value is not None else None
                    safe_data.append(safe_record)
            
            final_json = json.dumps(safe_data, ensure_ascii=False, default=str)
            print(f"🎉 최종 변환 완료: {len(safe_data)}개 레코드, {len(final_json)} 문자")
            
            return final_json
            
        except Exception as e:
            print(f"💥 전체 변환 실패: {e}")
            print(f"   오류 타입: {type(e).__name__}")
            print(f"   스택 트레이스: {traceback.format_exc()}")
            
            # 최후의 fallback
            return "[]"

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
            
            # 🔧 테이블 로우 생성 - 이제 openInquiryModal 함수 사용
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
            
            # 🔧 기존 모달은 레거시 호환성을 위해 유지 (일부 기능에서 아직 사용할 수 있음)
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
        
        print(f"✅ 생성 완료: {len(category_cards)}개 테이블 로우, {len(category_cards)}개 기존 모달 + 1개 문의 모달")
        
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
        print(f"✅ 단일 페이지 HTML 보고서 저장: {filename} (드로어 + 문의 모달 포함)")
        
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
        
        print(f"✅ 단일 페이지 HTML 보고서 저장: {filename} (드로어 + 문의 모달 포함)")
        return filename