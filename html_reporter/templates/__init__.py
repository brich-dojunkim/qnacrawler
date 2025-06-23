# html_reporter/templates/__init__.py (컨트롤 바 모듈 추가)
"""템플릿 모듈 - 사용하는 것만 import + 문의 모달 + 컨트롤 바 추가"""

# 베이스 템플릿 (필수)
from .base import get_base_template, get_header_template, get_footer_template

# 개요 템플릿 (필수)
from .overview import get_overview_template

# 카테고리 모달 템플릿 (필수)  
from .category import get_modal_template

# 카테고리 테이블 템플릿 (필수) - 테이블 필터 헤더 포함
from .category_table import (
    get_category_table_row_template, 
    get_team_filter_options,
    get_table_filter_header_template,
    get_table_filter_status_template,
    get_complete_category_table_template
)

# 컨트롤 바 템플릿 (새로 추가)
try:
    from .controls import get_controls_bar_template
except ImportError as e:
    print(f"Warning: controls templates import 오류: {e}")
    def get_controls_bar_template():
        return ""

# 문의 모달 템플릿 (기존)
try:
    from .inquiry_modal import get_inquiry_modal_template, get_inquiry_modal_components
except ImportError as e:
    print(f"Warning: inquiry_modal templates import 오류: {e}")
    def get_inquiry_modal_template():
        return ""
    def get_inquiry_modal_components():
        return {}

__all__ = [
    'get_base_template',
    'get_header_template', 
    'get_footer_template',
    'get_overview_template',
    'get_modal_template',
    'get_category_table_row_template',
    'get_team_filter_options',
    'get_table_filter_header_template',      # 새로 추가
    'get_table_filter_status_template',      # 새로 추가
    'get_complete_category_table_template',  # 새로 추가
    'get_controls_bar_template',
    'get_inquiry_modal_template',
    'get_inquiry_modal_components'
]