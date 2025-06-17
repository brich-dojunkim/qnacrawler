# html_reporter/scripts/__init__.py (문의 모달 추가)
"""
scripts 패키지 – 모듈화된 컴포넌트들만 사용 + 문의 모달 추가
"""

from .accordion import get_accordion_scripts
from .modal     import get_modal_scripts
from .tabs      import get_tab_scripts
from .bootstrap import get_bootstrap_scripts
from .category_table import get_category_table_scripts

# 새로 추가: 문의 모달 스크립트
try:
    from .inquiry_modal import get_inquiry_modal_scripts
except ImportError as e:
    print(f"Warning: inquiry_modal scripts import 오류: {e}")
    def get_inquiry_modal_scripts():
        return ""

def get_main_scripts() -> str:
    """
    템플릿에서 호출되는 통합 스크립트.
    모든 모듈화된 컴포넌트만 사용 + 문의 모달 추가.
    """
    return "\n".join([
        get_accordion_scripts(),        # 모듈화된 아코디언
        get_modal_scripts(),           # 기본 모달
        get_tab_scripts(),             # 탭
        get_category_table_scripts(),  # 모듈화된 카테고리 테이블
        get_inquiry_modal_scripts(),   # 문의 상세보기 모달
        get_bootstrap_scripts(),       # 부트스트랩 (항상 마지막)
    ])

def get_scripts_without_inquiry_modal() -> str:
    """문의 모달 제외한 기본 스크립트만"""
    return "\n".join([
        get_accordion_scripts(),
        get_modal_scripts(),
        get_tab_scripts(),
        get_category_table_scripts(),
        get_bootstrap_scripts(),
    ])

def get_inquiry_modal_only() -> str:
    """문의 모달 스크립트만"""
    return get_inquiry_modal_scripts()

__all__ = [
    'get_main_scripts',
    'get_scripts_without_inquiry_modal',
    'get_inquiry_modal_only',
    'get_accordion_scripts',
    'get_modal_scripts',
    'get_tab_scripts',
    'get_bootstrap_scripts',
    'get_category_table_scripts',
    'get_inquiry_modal_scripts',
]