"""
scripts 패키지 – 개별 JS 문자열을 하나로 합쳐 반환
"""

from .accordion import get_accordion_scripts
from .filters   import get_filter_scripts
from .modal     import get_modal_scripts
from .tabs      import get_tab_scripts
from .bootstrap import get_bootstrap_scripts

def get_main_scripts() -> str:
    """
    템플릿에서 호출되는 통합 스크립트.
    필요에 따라 순서를 바꾸거나 일부만 리턴할 수도 있습니다.
    """
    return "\n".join([
        get_accordion_scripts(),
        get_filter_scripts(),
        get_modal_scripts(),
        get_tab_scripts(),
        get_bootstrap_scripts(),
    ])
