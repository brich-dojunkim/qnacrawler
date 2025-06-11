# html_reporter/styles/components/__init__.py (아코디언 추가)
"""컴포넌트 스타일 모듈 - 아코디언 컴포넌트 추가"""

from .tabs import get_tab_styles
from .cards import get_card_styles
from .buttons import get_button_styles
from .badges import get_badge_styles
from .modals import get_modal_styles
from .stats import get_stats_styles
from .ranking import get_ranking_styles
from .accordion import get_accordion_styles

def get_component_styles():
    """모든 UI 컴포넌트 스타일 조합"""
    styles = [
        get_tab_styles(),        # 탭 컴포넌트
        get_card_styles(),       # 카드 컴포넌트
        get_button_styles(),     # 버튼 컴포넌트
        get_badge_styles(),      # 배지 컴포넌트
        get_modal_styles(),      # 모달 컴포넌트
        get_stats_styles(),      # 통계 컴포넌트
        get_ranking_styles(),    # 랭킹 컴포넌트
        get_accordion_styles(),  # 아코디언 컴포넌트 (새로 추가)
    ]
    
    return '\n'.join(styles)

def get_navigation_components():
    """네비게이션 관련 컴포넌트들"""
    styles = [
        get_tab_styles(),        # 탭 네비게이션
        get_button_styles(),     # 네비게이션 버튼들
        get_accordion_styles(),  # 아코디언 네비게이션
    ]
    
    return '\n'.join(styles)

def get_ui_components_only():
    """기본 UI 컴포넌트만 (카드 + 버튼 + 배지 + 탭 + 아코디언)"""
    styles = [
        get_tab_styles(),
        get_card_styles(),
        get_button_styles(),
        get_badge_styles(),
        get_accordion_styles()
    ]
    
    return '\n'.join(styles)

def get_overview_components():
    """개요 탭 컴포넌트들"""
    styles = [
        get_tab_styles(),        # 탭 네비게이션
        get_card_styles(),       # 분포 카드용
        get_stats_styles(),      # 통계 카드용
        get_ranking_styles(),    # 순위 아이템용
        get_accordion_styles(),  # 팀별 아코디언용
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
    'get_navigation_components',
    'get_ui_components_only', 
    'get_overview_components',
    'get_modal_components_only',
    'get_tab_styles',           
    'get_card_styles',
    'get_button_styles',
    'get_badge_styles',
    'get_modal_styles',
    'get_stats_styles',
    'get_ranking_styles',
    'get_accordion_styles',     # 새로 추가
]