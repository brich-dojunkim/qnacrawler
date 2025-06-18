# html_reporter/scripts/inquiry_modal/modal_actions.py
"""
문의 모달 열기/닫기 및 액션 처리 - 답변 관련 함수 제거
"""

def get_modal_actions_scripts():
    """모달 액션 스크립트 - 답변 관련 함수 제거"""
    return """
// ─────────── 모달 액션 시스템 ───────────
console.log('🎬 모달 액션 시스템 로딩 중...');

// ─────────── 모달 열기 메인 함수 ───────────
window.openInquiryModal = function(categoryType, categoryName) {
    console.log(`🎯 문의 모달 열기: ${categoryType} - ${categoryName}`);
    
    try {
        setCurrentCategory(categoryType, categoryName);
        setCurrentPage(1);
        
        const modal = document.getElementById('inquiry-detail-modal');
        if (modal) {
            modal.classList.add('active');
            document.body.style.overflow = 'hidden';
            updateModalState({ isOpen: true });
            
            updateModalTitle(categoryType, categoryName);
            
            setTimeout(() => {
                debugInquiryModalDOM();
            }, 100);
            
            showInquiryLoading();
            
            setTimeout(() => {
                if (typeof loadCategoryInquiries === 'function') {
                    loadCategoryInquiries(categoryName);
                } else {
                    console.error('❌ loadCategoryInquiries 함수를 찾을 수 없습니다.');
                    hideInquiryLoading();
                    showEmptyState();
                }
            }, 300);
            
        } else {
            console.error('❌ 문의 모달 요소를 찾을 수 없습니다.');
        }
        
    } catch (error) {
        console.error('❌ 문의 모달 열기 오류:', error);
        hideInquiryLoading();
        alert('문의 목록을 불러오는 중 오류가 발생했습니다.');
    }
};

// ─────────── 모달 닫기 ───────────
window.closeInquiryModal = function() {
    console.log('🔒 문의 모달 닫기');
    
    try {
        const modal = document.getElementById('inquiry-detail-modal');
        if (modal) {
            modal.classList.remove('active');
            document.body.style.overflow = 'auto';
            updateModalState({ isOpen: false });
            
            resetModalState();
        }
        
    } catch (error) {
        console.error('❌ 문의 모달 닫기 오류:', error);
    }
};

// ─────────── 새로고침 함수 ───────────
window.refreshInquiryModal = function() {
    console.log('🔄 문의 모달 새로고침');
    
    const state = getCurrentState();
    if (state.currentCategory) {
        showInquiryLoading();
        setTimeout(() => {
            if (typeof loadCategoryInquiries === 'function') {
                loadCategoryInquiries(state.currentCategory);
            }
        }, 300);
    }
};

// ─────────── 문의 상세보기 함수 ───────────
window.showInquiryDetail = function(inquiryId) {
    console.log(`🔍 문의 상세보기: ${inquiryId}`);
    
    const state = getCurrentState();
    const inquiry = state.allInquiries.find(inq => inq.inquiry_id === inquiryId);
    if (inquiry) {
        alert(`문의 ID: ${inquiryId}\\n내용: ${inquiry.question_content?.substring(0, 200)}...`);
    }
};

// ─────────── 연락처 정보 보기 ───────────
window.showAuthorInfo = function(email, phone, name) {
    const info = `📞 ${name} 연락처\\n\\n📧 이메일: ${email}\\n📱 전화: ${phone}`;
    alert(info);
};

// ─────────── 전체 내용 토글 ───────────
window.toggleFullContent = function(button) {
    const card = button.closest('.inquiry-card');
    const preview = card.querySelector('.content-preview');
    const fullContent = card.querySelector('.full-content');
    const expandText = button.querySelector('.expand-text');
    const collapseText = button.querySelector('.collapse-text');
    const expandIcon = button.querySelector('.expand-icon');
    
    if (fullContent.style.display === 'none') {
        preview.style.display = 'none';
        fullContent.style.display = 'block';
        expandText.style.display = 'none';
        collapseText.style.display = 'inline';
        expandIcon.style.transform = 'rotate(180deg)';
    } else {
        preview.style.display = 'block';
        fullContent.style.display = 'none';
        expandText.style.display = 'inline';
        collapseText.style.display = 'none';
        expandIcon.style.transform = 'rotate(0deg)';
    }
};

// ─────────── 전체 답변 토글 ───────────
window.toggleFullAnswer = function(button) {
    const answerSection = button.closest('.answer-section');
    const preview = answerSection.querySelector('.answer-preview');
    const fullAnswer = answerSection.querySelector('.full-answer');
    const expandText = button.querySelector('.expand-text');
    const collapseText = button.querySelector('.collapse-text');
    
    if (fullAnswer.style.display === 'none') {
        preview.style.display = 'none';
        fullAnswer.style.display = 'block';
        expandText.style.display = 'none';
        collapseText.style.display = 'inline';
    } else {
        preview.style.display = 'block';
        fullAnswer.style.display = 'none';
        expandText.style.display = 'inline';
        collapseText.style.display = 'none';
    }
};

// ─────────── 키보드 이벤트 처리 ───────────
document.addEventListener('keydown', function(event) {
    const state = getCurrentState();
    if (event.key === 'Escape' && state.isOpen) {
        closeInquiryModal();
    }
});

// ─────────── 모달 외부 클릭으로 닫기 ───────────
document.addEventListener('click', function(event) {
    const state = getCurrentState();
    if (event.target.classList.contains('inquiry-modal-overlay') && state.isOpen) {
        closeInquiryModal();
    }
});

console.log('✅ 모달 액션 시스템 로딩 완료');
"""