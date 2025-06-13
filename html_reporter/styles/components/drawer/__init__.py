# html_reporter/styles/components/drawer/__init__.py
"""
드로어 스타일 모듈 패키지
기능별로 분리된 스타일들을 통합하여 제공
"""

from .base import get_drawer_base_styles, get_drawer_panel_styles
from .header import get_drawer_header_styles, get_drawer_search_styles
from .content import get_drawer_content_styles, get_drawer_view_styles
from .inquiry_list import get_inquiry_list_styles, get_inquiry_item_styles
from .inquiry_detail import get_inquiry_detail_styles, get_answer_styles
from .responsive import get_drawer_responsive_styles

def get_drawer_styles():
    """모든 드로어 스타일을 통합하여 반환"""
    styles = [
        # 기본 구조
        get_drawer_base_styles(),
        get_drawer_panel_styles(),
        
        # 헤더 및 검색
        get_drawer_header_styles(),
        get_drawer_search_styles(),
        
        # 콘텐츠 영역
        get_drawer_content_styles(),
        get_drawer_view_styles(),
        
        # 문의 목록
        get_inquiry_list_styles(),
        get_inquiry_item_styles(),
        
        # 문의 상세보기
        get_inquiry_detail_styles(),
        get_answer_styles(),
        
        # 반응형
        get_drawer_responsive_styles(),
    ]
    
    return '\n'.join(styles)

# 개별 기능별 스타일 조합
def get_drawer_layout_styles():
    """드로어 기본 레이아웃만"""
    return '\n'.join([
        get_drawer_base_styles(),
        get_drawer_panel_styles(),
    ])

def get_drawer_header_combined():
    """헤더 관련 스타일만"""
    return '\n'.join([
        get_drawer_header_styles(),
        get_drawer_search_styles(),
    ])

def get_drawer_content_combined():
    """콘텐츠 관련 스타일만"""
    return '\n'.join([
        get_drawer_content_styles(),
        get_drawer_view_styles(),
    ])

def get_drawer_inquiry_styles():
    """문의 관련 스타일만"""
    return '\n'.join([
        get_inquiry_list_styles(),
        get_inquiry_item_styles(),
        get_inquiry_detail_styles(),
        get_answer_styles(),
    ])

__all__ = [
    # 메인 통합 함수
    'get_drawer_styles',
    
    # 기능별 조합 함수들
    'get_drawer_layout_styles',
    'get_drawer_header_combined',
    'get_drawer_content_combined',
    'get_drawer_inquiry_styles',
    
    # 개별 모듈 함수들
    'get_drawer_base_styles',
    'get_drawer_panel_styles',
    'get_drawer_header_styles',
    'get_drawer_search_styles',
    'get_drawer_content_styles',
    'get_drawer_view_styles',
    'get_inquiry_list_styles',
    'get_inquiry_item_styles',
    'get_inquiry_detail_styles',
    'get_answer_styles',
    'get_drawer_responsive_styles',
]