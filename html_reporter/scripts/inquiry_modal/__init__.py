# html_reporter/scripts/inquiry_modal/__init__.py
"""
문의 상세보기 모달 스크립트 모듈 패키지
기능별로 분리된 스크립트들을 통합하여 제공
"""

from .core import get_core_scripts
from .data_loader import get_data_loader_scripts
from .filters import get_filters_scripts
from .sorting import get_sorting_scripts
from .pagination import get_pagination_scripts

def get_inquiry_modal_scripts():
    """모든 문의 모달 스크립트를 통합하여 반환"""
    
    # 스크립트 로딩 시작 메시지
    init_script = """
console.log('🚀 문의 상세보기 모달 시스템 로딩 시작 - v1.0');
"""
    
    # 모든 스크립트 모듈 통합
    scripts = [
        init_script,
        get_core_scripts(),           # 모달 열기/닫기 핵심 기능
        get_data_loader_scripts(),    # 데이터 로딩 및 카테고리 매칭
        get_filters_scripts(),        # 검색 및 필터링
        get_sorting_scripts(),        # 정렬 기능
        get_pagination_scripts(),     # 페이지네이션
    ]
    
    return '\n'.join(scripts)

# 개별 기능별 접근을 위한 함수들
def get_core_only():
    """핵심 모달 기능만"""
    return get_core_scripts()

def get_data_only():
    """데이터 로딩 기능만"""
    return get_data_loader_scripts()

def get_filters_only():
    """필터링 기능만"""
    return get_filters_scripts()

def get_sorting_only():
    """정렬 기능만"""
    return get_sorting_scripts()

def get_pagination_only():
    """페이지네이션 기능만"""
    return get_pagination_scripts()

__all__ = [
    'get_inquiry_modal_scripts',
    'get_core_only',
    'get_data_only',
    'get_filters_only',
    'get_sorting_only',
    'get_pagination_only',
    'get_core_scripts',
    'get_data_loader_scripts',
    'get_filters_scripts',
    'get_sorting_scripts',
    'get_pagination_scripts'
]