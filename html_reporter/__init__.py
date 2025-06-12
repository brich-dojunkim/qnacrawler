# html_reporter/__init__.py (import 경로 수정)
"""HTML 리포터 패키지 - 사용하는 것만 안전하게 import"""

# === 필수 템플릿 함수들 ===
try:
    from .templates.base import get_base_template, get_header_template, get_footer_template
except ImportError as e:
    print(f"Warning: base templates import 오류: {e}")
    def get_base_template(): return ""
    def get_header_template(): return ""
    def get_footer_template(): return ""

try:
    from .templates.overview import get_overview_template
except ImportError as e:
    print(f"Warning: overview template import 오류: {e}")
    def get_overview_template(): return ""

try:
    from .templates.category import get_modal_template
except ImportError as e:
    print(f"Warning: category modal template import 오류: {e}")
    def get_modal_template(): return ""

try:
    from .templates.category_table import get_category_table_row_template, get_team_filter_options
except ImportError as e:
    print(f"Warning: category_table templates import 오류: {e}")
    def get_category_table_row_template(): return ""
    def get_team_filter_options(teams): return ""

# === 스크립트 함수들 ===
try:
    from .scripts import get_main_scripts
except ImportError as e:
    print(f"Warning: scripts import 오류: {e}")
    def get_main_scripts(): return ""

# === 스타일 함수들 ===
try:
    from .styles import get_main_styles
except ImportError as e:
    print(f"Warning: styles import 오류: {e}")
    def get_main_styles(): return ""

# === 사용하는 유틸리티 함수들만 ===
try:
    from .utils import (
        process_overview_data, process_category_data,
        generate_team_options
    )
except ImportError as e:
    print(f"Warning: utils import 오류: {e}")
    def process_overview_data(data): return {}
    def process_category_data(data): return []
    def generate_team_options(data): return ""

# === 패키지 내 사용하는 함수 목록만 ===
__all__ = [
    # 필수 템플릿 함수들
    'get_base_template',
    'get_header_template', 
    'get_footer_template',
    'get_overview_template',
    'get_modal_template',
    'get_category_table_row_template',
    'get_team_filter_options',
    
    # 스크립트 함수들
    'get_main_scripts',
    
    # 스타일 함수들
    'get_main_styles',
    
    # 사용하는 유틸리티 함수들만
    'process_overview_data',
    'process_category_data',
    'generate_team_options'
]