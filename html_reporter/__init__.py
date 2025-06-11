# html_reporter/__init__.py (안전한 import 적용)
"""HTML 리포터 패키지 - 안전한 import 구조"""

# === 템플릿 함수들 ===
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
    from .templates.team import get_team_section_template, get_team_card_template
except ImportError as e:
    print(f"Warning: team templates import 오류: {e}")
    def get_team_section_template(): return ""
    def get_team_card_template(): return ""

try:
    from .templates.journey import get_journey_section_template, get_journey_card_template
except ImportError as e:
    print(f"Warning: journey templates import 오류: {e}")
    def get_journey_section_template(): return ""
    def get_journey_card_template(): return ""

try:
    from .templates.category import get_category_section_template, get_category_card_template, get_modal_template
except ImportError as e:
    print(f"Warning: category templates import 오류: {e}")
    def get_category_section_template(): return ""
    def get_category_card_template(): return ""
    def get_modal_template(): return ""

# === 새로 추가된 카테고리 테이블 템플릿 ===
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

# === 유틸리티 함수들 ===
try:
    from .utils import (
        process_overview_data, process_team_data, process_journey_data, process_category_data,
        generate_team_options, generate_rank_tables, generate_sub_categories_html
    )
except ImportError as e:
    print(f"Warning: utils import 오류: {e}")
    def process_overview_data(data): return {}
    def process_team_data(data): return []
    def process_journey_data(data): return []
    def process_category_data(data): return []
    def generate_team_options(data): return ""
    def generate_rank_tables(data): return ""
    def generate_sub_categories_html(data, max_items=5): return ""

# === 패키지 내 모든 함수 목록 ===
__all__ = [
    # 템플릿 함수들
    'get_base_template',
    'get_header_template', 
    'get_footer_template',
    'get_overview_template',
    'get_team_section_template',
    'get_team_card_template',
    'get_journey_section_template',
    'get_journey_card_template',
    'get_category_section_template',
    'get_category_card_template',
    'get_modal_template',
    
    # 새로 추가된 템플릿
    'get_category_table_row_template',
    'get_team_filter_options',
    
    # 스크립트 함수들
    'get_main_scripts',
    
    # 스타일 함수들
    'get_main_styles',
    
    # 유틸리티 함수들
    'process_overview_data',
    'process_team_data',
    'process_journey_data',
    'process_category_data',
    'generate_team_options',
    'generate_rank_tables',
    'generate_sub_categories_html'
]