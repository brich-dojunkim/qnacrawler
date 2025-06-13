"""
아코디언 스크립트 모듈 패키지
기능별로 분리된 스크립트들을 통합하여 제공
"""

from .base import get_accordion_base_scripts
from .bulk_controls import get_bulk_control_scripts
from .sorting import get_sorting_scripts
from .header_updates import get_header_update_scripts
from .events import get_event_scripts

def get_accordion_scripts():
    """모든 아코디언 스크립트를 통합하여 반환"""
    
    # 스크립트 로딩 시작 메시지
    init_script = """
console.log('🚀 아코디언 스크립트 로딩 시작 - v2.1 (모듈화)');
"""
    
    # 모든 스크립트 모듈 통합
    scripts = [
        init_script,
        get_accordion_base_scripts(),       # 기본 토글 기능
        get_bulk_control_scripts(),         # 전체 펼치기/접기
        get_sorting_scripts(),              # 정렬 기능
        get_header_update_scripts(),        # 헤더 업데이트
        get_event_scripts(),                # 이벤트 처리 및 초기화
    ]
    
    return '\n'.join(scripts)

# 개별 기능별 접근을 위한 함수들
def get_base_only():
    """기본 토글 기능만"""
    return get_accordion_base_scripts()

def get_sorting_only():
    """정렬 기능만"""
    return get_sorting_scripts()

def get_header_updates_only():
    """헤더 업데이트 기능만"""
    return get_header_update_scripts()

def get_bulk_controls_only():
    """벌크 제어 기능만"""
    return get_bulk_control_scripts()

__all__ = [
    'get_accordion_scripts',
    'get_base_only',
    'get_sorting_only', 
    'get_header_updates_only',
    'get_bulk_controls_only',
    'get_accordion_base_scripts',
    'get_bulk_control_scripts',
    'get_sorting_scripts',
    'get_header_update_scripts',
    'get_event_scripts'
]