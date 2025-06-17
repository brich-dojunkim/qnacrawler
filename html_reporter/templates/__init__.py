# html_reporter/templates/__init__.py (문의 모달 추가된 버전)
"""템플릿 모듈 - 사용하는 것만 import + 문의 모달 추가"""

# 베이스 템플릿 (필수)
from .base import get_base_template, get_header_template, get_footer_template

# 개요 템플릿 (필수)
from .overview import get_overview_template

# 카테고리 모달 템플릿 (필수)  
from .category import get_modal_template

# 카테고리 테이블 템플릿 (필수)
from .category_table import get_category_table_row_template, get_team_filter_options

# 문의 모달 템플릿 (새로 추가)
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
    'get_inquiry_modal_template',      # 새로 추가
    'get_inquiry_modal_components'     # 새로 추가
]