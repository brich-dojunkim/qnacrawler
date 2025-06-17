# html_reporter/templates/inquiry_modal/__init__.py
"""
문의 상세보기 모달 템플릿 모듈 패키지
기능별로 분리된 템플릿들을 통합하여 제공
"""

from .layout import get_inquiry_modal_layout
from .inquiry_card import get_inquiry_card_template, get_inquiry_list_template, get_loading_template, get_empty_state_template

def get_inquiry_modal_template():
    """완전한 문의 모달 템플릿 반환"""
    return get_inquiry_modal_layout()

def get_inquiry_modal_components():
    """모든 모달 컴포넌트를 딕셔너리로 반환"""
    return {
        'layout': get_inquiry_modal_layout(),
        'card_template': get_inquiry_card_template(),
        'list_template': get_inquiry_list_template(),
        'loading_template': get_loading_template(),
        'empty_state_template': get_empty_state_template()
    }

__all__ = [
    'get_inquiry_modal_template',
    'get_inquiry_modal_components',
    'get_inquiry_modal_layout',
    'get_inquiry_card_template',
    'get_inquiry_list_template',
    'get_loading_template',
    'get_empty_state_template'
]