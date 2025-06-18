# styles/components/inquiry_modal/__init__.py (content.py 제거 버전)
"""
문의 상세보기 모달 스타일 모듈 패키지
content.py는 제거하고 모듈화된 content 패키지만 사용
"""

from .layout import get_layout_styles
from .header import get_header_styles
from .filters import get_filters_styles
from .content import get_content_styles  # 모듈화된 패키지에서 가져오기

def get_inquiry_modal_styles():
    """모든 문의 모달 스타일을 통합하여 반환"""
    
    styles = [
        get_layout_styles(),        # 모달 레이아웃 및 오버레이
        get_header_styles(),        # 헤더 및 통계 영역
        get_filters_styles(),       # 필터 바 스타일
        get_content_styles(),       # 문의 목록 및 카드 스타일 (모듈화된 패키지)
    ]
    
    return '\n'.join(styles)

# 개별 기능별 접근을 위한 함수들
def get_layout_only():
    """레이아웃 스타일만"""
    return get_layout_styles()

def get_header_only():
    """헤더 스타일만"""
    return get_header_styles()

def get_filters_only():
    """필터 스타일만"""
    return get_filters_styles()

def get_content_only():
    """콘텐츠 스타일만 (모듈화된 패키지)"""
    return get_content_styles()

# content 패키지의 세부 기능에 대한 편의 함수들
def get_card_styles():
    """카드 구조 스타일만"""
    from .content import get_card_structure_only
    return get_card_structure_only()

def get_badge_styles():
    """배지 스타일만"""
    from .content import get_ui_components_only
    return get_ui_components_only()

def get_action_styles():
    """액션 버튼 스타일만"""
    from .content import get_interactive_only
    return get_interactive_only()

def get_list_layout_styles():
    """목록 레이아웃 스타일만"""
    from .content import get_layout_only as get_content_layout_only
    return get_content_layout_only()

__all__ = [
    # 메인 함수
    'get_inquiry_modal_styles',
    
    # 기본 영역별 함수들
    'get_layout_only',
    'get_header_only',
    'get_filters_only',
    'get_content_only',
    
    # content 패키지 편의 함수들
    'get_card_styles',
    'get_badge_styles', 
    'get_action_styles',
    'get_list_layout_styles',
    
    # 개별 모듈 함수들 (직접 접근)
    'get_layout_styles',
    'get_header_styles',
    'get_filters_styles',
    'get_content_styles',
]