# html_reporter/styles/system/__init__.py
"""스타일 시스템 모듈 - 기반, 레이아웃, 반응형"""

from .base import get_base_styles
from .layout import get_layout_styles
from .responsive import get_responsive_styles

def get_system_styles():
    """모든 시스템 스타일을 조합하여 반환"""
    styles = [
        get_base_styles(),
        get_layout_styles(),
        get_responsive_styles()
    ]
    
    return '\n'.join(styles)

def get_foundation_styles():
    """기본 기반 스타일만 (base + layout)"""
    styles = [
        get_base_styles(),
        get_layout_styles()
    ]
    
    return '\n'.join(styles)

__all__ = [
    'get_system_styles',
    'get_foundation_styles', 
    'get_base_styles',
    'get_layout_styles',
    'get_responsive_styles'
]