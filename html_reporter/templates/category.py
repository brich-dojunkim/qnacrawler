# html_reporter/templates/category.py (수정된 버전)
"""카테고리별 분석 템플릿들 - 필수 함수만 유지"""

def get_category_section_template():
    """사용되지 않음 - 호환성을 위해 빈 문자열 반환"""
    return ""

def get_category_card_template():
    """사용되지 않음 - 호환성을 위해 빈 문자열 반환"""
    return ""

def get_modal_template():
    """모달 템플릿"""
    return """<div id="{modal_id}" class="modal-overlay">
    <div class="modal-content">
        <div class="modal-header">
            <h3 class="modal-title">{title}</h3>
            <button class="modal-close" onclick="closeModal('{modal_id}')">&times;</button>
        </div>
        <div class="modal-body">
            {content}
        </div>
    </div>
</div>"""