# html_reporter/styles/components/accordion/__init__.py
"""
아코디언 컴포넌트 모듈 패키지
각 기능별로 분리된 스타일을 통합하여 제공
"""

from .base import get_accordion_base_layout, get_accordion_item_structure
from .controls import get_controls_bar_styles, get_view_toggle_styles
from .headers import (
    get_accordion_header_styles, 
    get_summary_info_styles, 
    get_progress_bar_styles, 
    get_toggle_button_styles
)
from .metrics import (
    get_metrics_grid_styles, 
    get_metric_item_base_styles, 
    get_metric_item_border_styles
)
from .sub_table import (
    get_sub_table_container_styles,
    get_sub_table_header_styles,
    get_sub_table_body_styles,
    get_sub_table_content_styles,
    get_sub_table_action_styles
)
from .responsive import (
    get_tablet_responsive_styles,
    get_mobile_responsive_styles,
    get_sub_table_responsive_styles
)

def get_accordion_styles():
    """모든 아코디언 스타일을 통합하여 반환"""
    styles = [
        # 기본 구조
        get_accordion_base_layout(),
        get_accordion_item_structure(),
        
        # 컨트롤 바
        get_controls_bar_styles(),
        get_view_toggle_styles(),
        
        # 헤더 및 정보 표시
        get_accordion_header_styles(),
        get_summary_info_styles(),
        get_progress_bar_styles(),
        get_toggle_button_styles(),
        
        # 메트릭 카드
        get_metrics_grid_styles(),
        get_metric_item_base_styles(),
        get_metric_item_border_styles(),
        
        # 세부카테고리 테이블
        get_sub_table_container_styles(),
        get_sub_table_header_styles(),
        get_sub_table_body_styles(),
        get_sub_table_content_styles(),
        get_sub_table_action_styles(),
        
        # 반응형
        get_tablet_responsive_styles(),
        get_mobile_responsive_styles(),
        get_sub_table_responsive_styles(),
    ]
    
    return '\n'.join(styles)

# 개별 기능별 스타일 조합
def get_accordion_base_styles():
    """기본 아코디언 구조만"""
    return '\n'.join([
        get_accordion_base_layout(),
        get_accordion_item_structure(),
    ])

def get_accordion_control_styles():
    """컨트롤 관련 스타일만"""
    return '\n'.join([
        get_controls_bar_styles(),
        get_view_toggle_styles(),
    ])

def get_accordion_header_styles_combined():
    """헤더 관련 스타일만"""
    return '\n'.join([
        get_accordion_header_styles(),
        get_summary_info_styles(),
        get_progress_bar_styles(),
        get_toggle_button_styles(),
    ])

def get_accordion_metrics_styles():
    """메트릭 관련 스타일만"""
    return '\n'.join([
        get_metrics_grid_styles(),
        get_metric_item_base_styles(),
        get_metric_item_border_styles(),
    ])

def get_accordion_sub_table_styles():
    """세부카테고리 테이블 스타일만"""
    return '\n'.join([
        get_sub_table_container_styles(),
        get_sub_table_header_styles(),
        get_sub_table_body_styles(),
        get_sub_table_content_styles(),
        get_sub_table_action_styles(),
    ])

def get_accordion_responsive_styles():
    """반응형 스타일만"""
    return '\n'.join([
        get_tablet_responsive_styles(),
        get_mobile_responsive_styles(),
        get_sub_table_responsive_styles(),
    ])

# 하위 호환성을 위한 함수들
def get_accordion_layout_styles():
    """레이아웃 스타일 (하위 호환성)"""
    return get_accordion_base_layout()

def get_accordion_item_styles():
    """아이템 스타일 (하위 호환성)"""
    return get_accordion_item_structure()

__all__ = [
    # 메인 통합 함수
    'get_accordion_styles',
    
    # 기능별 조합 함수들
    'get_accordion_base_styles',
    'get_accordion_control_styles', 
    'get_accordion_header_styles_combined',
    'get_accordion_metrics_styles',
    'get_accordion_sub_table_styles',
    'get_accordion_responsive_styles',
    
    # 개별 모듈 함수들
    'get_accordion_base_layout',
    'get_accordion_item_structure',
    'get_controls_bar_styles',
    'get_view_toggle_styles',
    'get_accordion_header_styles',
    'get_summary_info_styles',
    'get_progress_bar_styles',
    'get_toggle_button_styles',
    'get_metrics_grid_styles',
    'get_metric_item_base_styles',
    'get_metric_item_border_styles',
    'get_sub_table_container_styles',
    'get_sub_table_header_styles',
    'get_sub_table_body_styles',
    'get_sub_table_content_styles',
    'get_sub_table_action_styles',
    'get_tablet_responsive_styles',
    'get_mobile_responsive_styles',
    'get_sub_table_responsive_styles',
    
    # 하위 호환성 함수들
    'get_accordion_layout_styles',
    'get_accordion_item_styles',
]