# html_reporter/styles/components/inquiry_modal/__init__.py
"""
문의 상세보기 모달 스타일 모듈 패키지
기능별로 분리된 스타일들을 통합하여 제공
"""

from .layout import get_layout_styles
from .header import get_header_styles
from .filters import get_filters_styles
from .content import get_content_styles

def get_inquiry_modal_styles():
    """모든 문의 모달 스타일을 통합하여 반환"""
    
    styles = [
        get_layout_styles(),        # 모달 레이아웃 및 오버레이
        get_header_styles(),        # 헤더 및 통계 영역
        get_filters_styles(),       # 필터 바 스타일
        get_content_styles(),       # 문의 목록 및 카드 스타일
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
    """콘텐츠 스타일만"""
    return get_content_styles()

__all__ = [
    'get_inquiry_modal_styles',
    'get_layout_only',
    'get_header_only',
    'get_filters_only',
    'get_content_only',
    'get_layout_styles',
    'get_header_styles',
    'get_filters_styles',
    'get_content_styles'
]