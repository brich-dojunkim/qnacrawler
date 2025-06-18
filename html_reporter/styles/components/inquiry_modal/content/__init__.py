# styles/components/inquiry_modal/content/__init__.py
"""
문의 상세보기 모달 콘텐츠 스타일 모듈 패키지
기능별로 분리된 스타일들을 통합하여 제공
"""

from .list import get_list_styles
from .card_base import get_card_base_styles
from .card_header import get_card_header_styles
from .card_body import get_card_body_styles
from .card_footer import get_card_footer_styles
from .badges import get_badges_styles
from .actions import get_actions_styles
from .states import get_states_styles
from .responsive import get_responsive_styles

def get_content_styles():
    """모든 콘텐츠 스타일을 통합하여 반환"""
    
    styles = [
        # 기본 구조
        get_list_styles(),           # 문의 목록 컨테이너
        get_card_base_styles(),      # 기본 카드 구조
        
        # 카드 세부 영역
        get_card_header_styles(),    # 카드 헤더 (메타정보)
        get_card_body_styles(),      # 카드 본문 (내용, 답변)
        get_card_footer_styles(),    # 카드 푸터 (통계, 버튼)
        
        # UI 컴포넌트
        get_badges_styles(),         # 배지 스타일
        get_actions_styles(),        # 액션 버튼
        
        # 상태 및 특수 케이스
        get_states_styles(),         # 로딩, 빈 상태
        
        # 반응형 (마지막에 적용)
        get_responsive_styles(),     # 모든 반응형 처리
    ]
    
    return '\n'.join(styles)

# 개별 기능별 접근을 위한 함수들
def get_card_structure_only():
    """카드 구조만 (기본 + 헤더 + 본문 + 푸터)"""
    return '\n'.join([
        get_card_base_styles(),
        get_card_header_styles(),
        get_card_body_styles(),
        get_card_footer_styles()
    ])

def get_ui_components_only():
    """UI 컴포넌트만 (배지 + 액션)"""
    return '\n'.join([
        get_badges_styles(),
        get_actions_styles()
    ])

def get_layout_only():
    """레이아웃만 (목록 + 기본 카드)"""
    return '\n'.join([
        get_list_styles(),
        get_card_base_styles()
    ])

def get_interactive_only():
    """인터랙티브 요소만 (액션 + 상태)"""
    return '\n'.join([
        get_actions_styles(),
        get_states_styles()
    ])

# 레거시 호환성을 위한 함수들
def get_card_styles():
    """레거시: 전체 카드 스타일"""
    return get_card_structure_only()

def get_badge_styles():
    """레거시: 배지 스타일"""
    return get_badges_styles()

def get_button_styles():
    """레거시: 버튼 스타일"""
    return get_actions_styles()

__all__ = [
    # 메인 통합 함수
    'get_content_styles',
    
    # 기능별 조합 함수들
    'get_card_structure_only',
    'get_ui_components_only',
    'get_layout_only',
    'get_interactive_only',
    
    # 개별 모듈 함수들
    'get_list_styles',
    'get_card_base_styles',
    'get_card_header_styles',
    'get_card_body_styles',
    'get_card_footer_styles',
    'get_badges_styles',
    'get_actions_styles',
    'get_states_styles',
    'get_responsive_styles',
    
    # 레거시 호환성 함수들
    'get_card_styles',
    'get_badge_styles',
    'get_button_styles',
]