"""
scripts 패키지 – 모듈화된 컴포넌트들만 사용
"""

from .accordion import get_accordion_scripts
from .modal     import get_modal_scripts
from .tabs      import get_tab_scripts
from .bootstrap import get_bootstrap_scripts
from .category_table import get_category_table_scripts

def get_main_scripts() -> str:
    """
    템플릿에서 호출되는 통합 스크립트.
    모든 모듈화된 컴포넌트만 사용.
    """
    return "\n".join([
        get_accordion_scripts(),        # 모듈화된 아코디언
        get_modal_scripts(),           # 모달
        get_tab_scripts(),             # 탭
        get_category_table_scripts(),  # 모듈화된 카테고리 테이블
        get_bootstrap_scripts(),       # 부트스트랩
    ])