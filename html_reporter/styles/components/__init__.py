# html_reporter/styles/components/__init__.py
"""컴포넌트 스타일 모듈 - 모든 UI 컴포넌트 통합"""

from .buttons import get_button_styles
from .badges import get_badge_styles
from .modals import get_modal_styles
from .cards import get_card_styles

def get_component_styles():
    """모든 UI 컴포넌트 스타일 조합"""
    styles = [
        get_card_styles(),       # 카드 컴포넌트
        get_button_styles(),     # 버튼 컴포넌트
        get_badge_styles(),      # 배지 컴포넌트
        get_modal_styles(),      # 모달 컴포넌트
    ]
    
    return '\n'.join(styles)

def get_ui_components_only():
    """기본 UI 컴포넌트만 (카드 + 버튼 + 배지)"""
    styles = [
        get_card_styles(),
        get_button_styles(),
        get_badge_styles()
    ]
    
    return '\n'.join(styles)

def get_modal_components_only():
    """모달 관련 컴포넌트만"""
    styles = [
        get_button_styles(),     # modal-trigger 포함
        get_modal_styles(),      # 모달 오버레이
        get_card_styles(),       # inquiry-card 포함
    ]
    
    return '\n'.join(styles)

__all__ = [
    'get_component_styles',
    'get_ui_components_only', 
    'get_modal_components_only',
    'get_card_styles',           # 추가됨
    'get_button_styles',
    'get_badge_styles',
    'get_modal_styles',
]