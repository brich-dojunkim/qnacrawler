# html_reporter/scripts/inquiry_modal/__init__.py (완전 모듈화 버전)
"""
문의 상세보기 모달 스크립트 모듈 패키지 - 완전 모듈화 버전
기능별로 세분화된 모듈들을 통합하여 제공
"""

# === 새로 모듈화된 기능들 ===
from .modal_state import get_modal_state_scripts
from .dom_utils import get_dom_utils_scripts
from .modal_actions import get_modal_actions_scripts
from .card_factory import get_card_factory_scripts
from .data_matcher import get_data_matcher_scripts
from .stats_calculator import get_stats_calculator_scripts
from .main_loader import get_main_loader_scripts

# === 기존 모듈들 ===
from .filters import get_filters_scripts
from .sorting import get_sorting_scripts
from .pagination import get_pagination_scripts

def get_inquiry_modal_scripts():
    """모든 문의 모달 스크립트를 통합하여 반환 - 완전 모듈화 버전"""
    
    # 스크립트 로딩 시작 메시지
    init_script = """
console.log('🚀 문의 상세보기 모달 시스템 로딩 시작 - v2.0 (완전 모듈화)');
"""
    
    # 모든 스크립트 모듈 통합 (의존성 순서 고려)
    scripts = [
        init_script,
        
        # === 1단계: 기반 시스템 ===
        get_modal_state_scripts(),        # 상태 관리 (다른 모듈들이 의존)
        get_dom_utils_scripts(),          # DOM 유틸리티 (UI 조작 기반)
        
        # === 2단계: 데이터 처리 ===
        get_data_matcher_scripts(),       # 데이터 매칭 시스템
        get_stats_calculator_scripts(),   # 통계 계산 시스템
        get_main_loader_scripts(),        # 메인 데이터 로더
        
        # === 3단계: UI 컴포넌트 ===
        get_card_factory_scripts(),       # 카드 생성 팩토리
        get_modal_actions_scripts(),      # 모달 액션 (카드 팩토리 이후)
        
        # === 4단계: 인터랙션 ===
        get_filters_scripts(),            # 필터링 시스템
        get_sorting_scripts(),            # 정렬 시스템
        get_pagination_scripts(),         # 페이지네이션 (마지막)
    ]
    
    return '\n'.join(scripts)

# 개별 기능별 접근을 위한 함수들
def get_core_systems_only():
    """핵심 시스템만 (상태 관리 + DOM 유틸리티)"""
    return '\n'.join([
        get_modal_state_scripts(),
        get_dom_utils_scripts()
    ])

def get_data_systems_only():
    """데이터 처리 시스템만"""
    return '\n'.join([
        get_data_matcher_scripts(),
        get_stats_calculator_scripts(),
        get_main_loader_scripts()
    ])

def get_ui_systems_only():
    """UI 시스템만"""
    return '\n'.join([
        get_card_factory_scripts(),
        get_modal_actions_scripts()
    ])

def get_interaction_systems_only():
    """인터랙션 시스템만"""
    return '\n'.join([
        get_filters_scripts(),
        get_sorting_scripts(),
        get_pagination_scripts()
    ])

def get_minimal_modal():
    """최소한의 모달 기능만"""
    return '\n'.join([
        get_modal_state_scripts(),
        get_dom_utils_scripts(),
        get_modal_actions_scripts(),
        get_card_factory_scripts()
    ])

# 레거시 호환성을 위한 함수들
def get_core_only():
    """레거시: 핵심 기능만"""
    return get_minimal_modal()

def get_data_only():
    """레거시: 데이터 기능만"""
    return get_data_systems_only()

def get_filters_only():
    """레거시: 필터링 기능만"""
    return get_filters_scripts()

def get_sorting_only():
    """레거시: 정렬 기능만"""
    return get_sorting_scripts()

def get_pagination_only():
    """레거시: 페이지네이션 기능만"""
    return get_pagination_scripts()

__all__ = [
    # === 메인 함수 ===
    'get_inquiry_modal_scripts',
    
    # === 새로운 모듈화된 기능별 접근 ===
    'get_core_systems_only',
    'get_data_systems_only',
    'get_ui_systems_only',
    'get_interaction_systems_only',
    'get_minimal_modal',
    
    # === 개별 모듈 함수들 ===
    'get_modal_state_scripts',
    'get_dom_utils_scripts',
    'get_modal_actions_scripts',
    'get_card_factory_scripts',
    'get_data_matcher_scripts',
    'get_stats_calculator_scripts',
    'get_main_loader_scripts',
    'get_filters_scripts',
    'get_sorting_scripts',
    'get_pagination_scripts',
    
    # === 레거시 호환성 함수들 ===
    'get_core_only',
    'get_data_only',
    'get_filters_only',
    'get_sorting_only',
    'get_pagination_only',
]