# html_reporter/scripts/inquiry_modal/modal_actions.py
"""
문의 모달 열기/닫기 및 액션 처리 - 답변 관련 함수 제거
"""

def get_modal_actions_scripts():
    """모달 액션 스크립트 - 답변 관련 함수 제거"""
    return """
// ─────────── 모달 액션 시스템 ───────────
console.log('🎬 모달 액션 시스템 로딩 중...');

// ─────────── 모달 열기 메인 함수 (헤더 정보 업데이트 추가) ───────────
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
            
            // 🚨 중요: 모달 제목과 헤더 정보 업데이트
            updateModalHeaderInfo(categoryType, categoryName);
            
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

// ─────────── 모달 헤더 정보 업데이트 ───────────
function updateModalHeaderInfo(categoryType, categoryName) {
    console.log(`🔄 모달 헤더 정보 업데이트: ${categoryType} - ${categoryName}`);
    
    // 제목 업데이트
    const titleElement = document.getElementById('inquiry-modal-title');
    if (titleElement) {
        const typeText = categoryType === 'category' ? '카테고리' : '세부카테고리';
        titleElement.innerHTML = `📂 ${categoryName} 문의 목록`;
        titleElement.setAttribute('title', `${typeText}: ${categoryName}`);
    }
    
    // 팀/여정 정보 가져오기 및 추가
    const categoryInfo = getCategoryInfo(categoryName);
    if (categoryInfo) {
        addTeamJourneyToHeader(categoryInfo);
    }
}

// ─────────── 카테고리 정보 가져오기 ───────────
function getCategoryInfo(categoryName) {
    // 전역 결과 데이터에서 카테고리 정보 검색
    if (window.categoryAnalysisData && window.categoryAnalysisData[categoryName]) {
        return window.categoryAnalysisData[categoryName];
    }
    
    // 매핑 함수로 기본 정보 생성
    return {
        main_team: getMainTeamForCategory(categoryName),
        main_journey: getMainJourneyForCategory(categoryName)
    };
}

// ─────────── 팀/여정 정보를 헤더에 추가 ───────────
function addTeamJourneyToHeader(categoryInfo) {
    const statsContainer = document.getElementById('inquiry-modal-stats');
    if (!statsContainer) return;
    
    // 기존 팀/여정 배지 제거
    const existingBadges = statsContainer.querySelectorAll('.team-journey-badge');
    existingBadges.forEach(badge => badge.remove());
    
    // 새로운 팀/여정 배지 추가
    const teamBadgeHtml = `
        <span class="stat-item team-journey-badge">
            <span class="stat-icon">👥</span>
            <span class="stat-label">담당팀:</span>
            <span class="stat-value">${categoryInfo.main_team || '미분류'}</span>
        </span>
    `;
    
    const journeyBadgeHtml = `
        <span class="stat-item team-journey-badge">
            <span class="stat-icon">🎯</span>
            <span class="stat-label">여정:</span>
            <span class="stat-value">${categoryInfo.main_journey || '기타'}</span>
        </span>
    `;
    
    // 기존 통계 뒤에 추가
    statsContainer.insertAdjacentHTML('beforeend', teamBadgeHtml);
    statsContainer.insertAdjacentHTML('beforeend', journeyBadgeHtml);
}

// ─────────── 카테고리별 팀/여정 매핑 함수들 ───────────
function getMainTeamForCategory(categoryName) {
    // 유저 여정 매핑에서 팀 정보 추출
    const teamMapping = {
        '입점관리': 'MD팀',
        '스토어관리': 'MD팀', 
        '상품등록': '상품팀',
        '상품등록 실패': '상품팀',
        '발주/발송관리': '주문팀',
        '배송현황관리': '주문팀',
        '취소관리': 'CS팀',
        '반품관리/환불보류': 'CS팀',
        '정산통합': '정산팀'
        // 더 많은 매핑 추가...
    };
    
    return teamMapping[categoryName] || '미분류';
}

function getMainJourneyForCategory(categoryName) {
    // 기존 유저 여정 매핑 사용
    const journeyMapping = {
        '계정·입점': ['입점관리', '스토어관리', '플랜관리', '신규회원가입', '사업자정보/양도양수', '탈퇴/재가입', '브랜드권한신청'],
        '상품·콘텐츠': ['상품등록', '상품등록 실패', '상품 조회 및 수정', '채널상품연동', '브리치 기획전신청', '채널딜 진행관리', '상품문의(브리치)', '상품문의(채널)'],
        '주문·배송': ['발주/발송관리', '배송현황관리', '배송지연 관리 (결품취소)', '송장등록 실패/ 송장번호 수정', '주문조회', '긴급문의', '배송정책 관리'],
        '반품·취소': ['취소관리', '교환관리/교환철회', '반품관리/환불보류'],
        '정산': ['구매확정관리', '정산통합', '특약매입정산', '판매대행정산']
    };
    
    for (const [journey, categories] of Object.entries(journeyMapping)) {
        if (categories.includes(categoryName)) {
            return journey;
        }
    }
    
    return '기타';
}

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