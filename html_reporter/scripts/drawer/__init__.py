# html_reporter/scripts/drawer/__init__.py
"""
드로어 스크립트 모듈 패키지
기능별로 분리된 스크립트들을 통합하여 제공
"""

from .base import get_drawer_base_scripts
from .controls import get_drawer_control_scripts
from .rendering import get_drawer_rendering_scripts
from .search import get_drawer_search_scripts
from .events import get_drawer_event_scripts

def get_drawer_scripts():
    """모든 드로어 스크립트를 통합하여 반환"""
    
    # 스크립트 로딩 시작 메시지
    init_script = """
// ═══════════════════════════════════════════════════════════
// 사이드 드로어 시스템 v1.1 (모듈화)
// ═══════════════════════════════════════════════════════════
console.log('🚀 사이드 드로어 시스템 로딩 중 (모듈화)...');
"""
    
    # 모든 스크립트 모듈 통합
    scripts = [
        init_script,
        get_drawer_base_scripts(),      # 기본 열기/닫기 기능
        get_drawer_control_scripts(),   # 헤더 업데이트 및 컨트롤
        get_drawer_rendering_scripts(), # 렌더링 및 상세보기
        get_drawer_search_scripts(),    # 검색 및 필터링
        get_drawer_event_scripts(),     # 이벤트 처리 및 초기화
    ]
    
    return '\n'.join(scripts)

# 개별 기능별 접근을 위한 함수들
def get_base_only():
    """기본 드로어 기능만"""
    return get_drawer_base_scripts()

def get_controls_only():
    """컨트롤 기능만"""
    return get_drawer_control_scripts()

def get_rendering_only():
    """렌더링 기능만"""
    return get_drawer_rendering_scripts()

def get_search_only():
    """검색 기능만"""
    return get_drawer_search_scripts()

def get_events_only():
    """이벤트 처리만"""
    return get_drawer_event_scripts()

__all__ = [
    'get_drawer_scripts',
    'get_base_only',
    'get_controls_only',
    'get_rendering_only',
    'get_search_only',
    'get_events_only',
    'get_drawer_base_scripts',
    'get_drawer_control_scripts',
    'get_drawer_rendering_scripts',
    'get_drawer_search_scripts',
    'get_drawer_event_scripts'
]