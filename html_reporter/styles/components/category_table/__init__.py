"""
카테고리 테이블 스타일 모듈 패키지
기능별로 분리된 스타일들을 통합하여 제공
"""

from .header import get_header_styles, get_filter_button_styles
from .body import get_table_container_styles, get_table_body_styles, get_accordion_table_styles
from .filters import get_dropdown_styles, get_control_styles
from .modal import get_modal_styles
from .responsive import get_responsive_styles

def get_category_table_styles():
    """모든 카테고리 테이블 스타일을 통합하여 반환"""
    
    styles = [
        # 테이블 컨테이너
        get_table_container_styles(),
        
        # 헤더 관련
        get_header_styles(),
        get_filter_button_styles(),
        
        # 테이블 본문 (메인 테이블과 아코디언 내부 테이블 공통)
        get_table_body_styles(),
        get_accordion_table_styles(),
        
        # 필터 및 드롭다운
        get_dropdown_styles(),
        get_control_styles(),
        
        # 모달
        get_modal_styles(),
        
        # 반응형
        get_responsive_styles(),
    ]
    
    return '\n'.join(styles)

# 개별 기능별 접근을 위한 함수들
def get_header_only():
    """헤더 스타일만"""
    return '\n'.join([
        get_header_styles(),
        get_filter_button_styles()
    ])

def get_body_only():
    """본문 스타일만"""
    return '\n'.join([
        get_table_container_styles(),
        get_table_body_styles(),
        get_accordion_table_styles()
    ])

def get_filters_only():
    """필터 스타일만"""
    return '\n'.join([
        get_dropdown_styles(),
        get_control_styles()
    ])

def get_modal_only():
    """모달 스타일만"""
    return get_modal_styles()

def get_responsive_only():
    """반응형 스타일만"""
    return get_responsive_styles()

__all__ = [
    'get_category_table_styles',
    'get_header_only',
    'get_body_only',
    'get_filters_only',
    'get_modal_only',
    'get_responsive_only',
    'get_header_styles',
    'get_filter_button_styles',
    'get_table_container_styles',
    'get_table_body_styles',
    'get_accordion_table_styles',
    'get_dropdown_styles',
    'get_control_styles',
    'get_modal_styles',
    'get_responsive_styles'
]