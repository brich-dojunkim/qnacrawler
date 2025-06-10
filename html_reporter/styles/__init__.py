# html_reporter/styles/__init__.py
"""스타일 모듈 패키지 - 메인 진입점"""

from .base import get_base_styles
from .tabs import get_tab_styles  
from .overview import get_overview_styles
from .layout import get_layout_styles
from .components import get_component_styles
from .responsive import get_responsive_styles

def get_main_styles():
    """모든 스타일을 조합하여 반환"""
    styles = [
        get_base_styles(),
        get_tab_styles(),
        get_overview_styles(),
        get_layout_styles(),
        get_component_styles(),
        get_responsive_styles()
    ]
    
    return '\n'.join(styles)

def get_minimal_styles():
    """최소한의 스타일만 (기본 기능용)"""
    styles = [
        get_base_styles(),
        get_tab_styles(),
        get_layout_styles()
    ]
    
    return '\n'.join(styles)

def get_overview_only_styles():
    """개요 탭만 사용할 때"""
    styles = [
        get_base_styles(),
        get_tab_styles(),
        get_overview_styles(),
        get_responsive_styles()
    ]
    
    return '\n'.join(styles)

__all__ = [
    'get_base_styles',
    'get_tab_styles',
    'get_card_styles',
    'get_overview_styles',
    'get_layout_styles',
    'get_component_styles',
    'get_responsive_styles',
    'get_main_styles',
    'get_minimal_styles',
    'get_overview_only_styles'
]