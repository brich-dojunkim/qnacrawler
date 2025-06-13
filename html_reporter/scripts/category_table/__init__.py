"""
카테고리 테이블 스크립트 모듈 패키지
기능별로 분리된 스크립트들을 통합하여 제공
"""

from .modal import get_modal_scripts
from .filters import get_filter_scripts
from .sorting import get_sorting_scripts
from .state import get_state_scripts
from .events import get_event_scripts

def get_category_table_scripts():
    """모든 카테고리 테이블 스크립트를 통합하여 반환"""
    
    # 스크립트 로딩 시작 메시지
    init_script = """
// ═══════════════════════════════════════════════════════════
// 카테고리 테이블 필터링 및 정렬 스크립트 - 모듈화 v1.0
// ═══════════════════════════════════════════════════════════
console.log('🚀 카테고리 테이블 시스템 로딩 시작 (모듈화)');
"""
    
    # 모든 스크립트 모듈 통합
    scripts = [
        init_script,
        get_state_scripts(),           # 상태 관리 (tableFilters 변수 포함)
        get_modal_scripts(),           # 모달 시스템
        get_filter_scripts(),          # 필터링 시스템
        get_sorting_scripts(),         # 정렬 시스템
        get_event_scripts(),           # 이벤트 처리 및 초기화
    ]
    
    return '\n'.join(scripts)

# 개별 기능별 접근을 위한 함수들
def get_modal_only():
    """모달 기능만"""
    return get_modal_scripts()

def get_filters_only():
    """필터링 기능만"""
    return get_filter_scripts()

def get_sorting_only():
    """정렬 기능만"""
    return get_sorting_scripts()

def get_state_only():
    """상태 관리만"""
    return get_state_scripts()

def get_events_only():
    """이벤트 처리만"""
    return get_event_scripts()

__all__ = [
    'get_category_table_scripts',
    'get_modal_only',
    'get_filters_only',
    'get_sorting_only',
    'get_state_only',
    'get_events_only',
    'get_modal_scripts',
    'get_filter_scripts',
    'get_sorting_scripts',
    'get_state_scripts',
    'get_event_scripts'
]