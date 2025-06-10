# html_reporter/styles/__init__.py
"""스타일 모듈 패키지 - 시스템 + 컴포넌트 통합"""

from .system import get_system_styles
from .components import get_component_styles

def get_main_styles():
    """모든 스타일을 조합하여 반환"""
    styles = [
        get_system_styles(),      # 시스템 스타일 (base, layout, responsive)
        get_component_styles()    # 컴포넌트 스타일 (모든 UI 요소들)
    ]
    
    return '\n'.join(styles)

def get_minimal_styles():
    """최소한의 스타일만 (시스템 기반 + 기본 컴포넌트)"""
    from .system import get_foundation_styles
    from .components import get_ui_components_only
    
    styles = [
        get_foundation_styles(),  # base + layout (responsive 제외)
        get_ui_components_only()  # 기본 UI 컴포넌트들
    ]
    
    return '\n'.join(styles)

def get_overview_only_styles():
    """개요 탭만 사용할 때"""
    from .system import get_system_styles
    from .components import get_overview_components
    
    styles = [
        get_system_styles(),      # 전체 시스템 스타일
        get_overview_components() # 개요 탭 전용 컴포넌트들
    ]
    
    return '\n'.join(styles)

# ===== 하위 호환성 함수들 =====

def get_base_styles():
    """기본 스타일만 (하위 호환성)"""
    from .system import get_base_styles as _get_base_styles
    return _get_base_styles()

def get_layout_styles():
    """레이아웃 스타일만 (하위 호환성)"""
    from .system import get_layout_styles as _get_layout_styles
    return _get_layout_styles()

def get_responsive_styles():
    """반응형 스타일만 (하위 호환성)"""
    from .system import get_responsive_styles as _get_responsive_styles
    return _get_responsive_styles()

def get_tab_styles():
    """탭 스타일만 (하위 호환성)"""
    from .components import get_tab_styles as _get_tab_styles
    return _get_tab_styles()

def get_card_styles():
    """카드 스타일만 (하위 호환성)"""
    from .components import get_card_styles as _get_card_styles
    return _get_card_styles()

def get_overview_styles():
    """개요 스타일 (하위 호환성)"""
    from .components import get_overview_components
    return get_overview_components()

def get_component_styles():
    """컴포넌트 스타일 (직접 접근용)"""
    from .components import get_component_styles as _get_component_styles
    return _get_component_styles()

def get_system_styles():
    """시스템 스타일 (직접 접근용)"""
    from .system import get_system_styles as _get_system_styles
    return _get_system_styles()

__all__ = [
    # 메인 함수들
    'get_main_styles',
    'get_minimal_styles',
    'get_overview_only_styles',
    
    # 직접 접근
    'get_system_styles',
    'get_component_styles',
    
    # 하위 호환성 함수들
    'get_base_styles',
    'get_layout_styles', 
    'get_responsive_styles',
    'get_tab_styles',
    'get_card_styles',
    'get_overview_styles'
]