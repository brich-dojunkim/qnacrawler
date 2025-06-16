# html_reporter/templates/__init__.py (정리된 버전 - 드로어 추가)
"""템플릿 모듈 - 사용하는 것만 import + 드로어 추가"""

# 베이스 템플릿 (필수)
from .base import get_base_template, get_header_template, get_footer_template

# 개요 템플릿 (필수)
from .overview import get_overview_template

# 카테고리 모달 템플릿 (필수)  
from .category import get_modal_template

# 카테고리 테이블 템플릿 (필수)
from .category_table import get_category_table_row_template, get_team_filter_options

__all__ = [
    'get_base_template',
    'get_header_template', 
    'get_footer_template',
    'get_overview_template',
    'get_modal_template',
    'get_category_table_row_template',
    'get_team_filter_options',
    'get_drawer_template'  # 새로 추가
]