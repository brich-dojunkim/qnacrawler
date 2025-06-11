"""
scripts 패키지 – 개별 JS 문자열을 하나로 합쳐 반환
"""

from .accordion import get_accordion_scripts
from .filters   import get_filter_scripts
from .modal     import get_modal_scripts
from .tabs      import get_tab_scripts
from .bootstrap import get_bootstrap_scripts
from .category_table import get_category_table_scripts

def get_main_scripts() -> str:
    """
    템플릿에서 호출되는 통합 스크립트.
    카테고리 테이블 스크립트 추가.
    """
    return "\n".join([
        get_accordion_scripts(),
        get_filter_scripts(),
        get_modal_scripts(),
        get_tab_scripts(),
        get_category_table_scripts(),
        get_bootstrap_scripts(),
    ])