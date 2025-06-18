# html_reporter/scripts/inquiry_modal/core.py (최소화된 버전)
"""
문의 상세보기 모달 핵심 기능 - 레거시 호환성용 최소 기능만
대부분의 기능이 새로운 모듈들로 분리되었습니다.
"""

def get_core_scripts():
    """모달 핵심 기능 - 레거시 호환성용 (새 모듈들을 조합)"""
    return """
// ═══════════════════════════════════════════════════════════
// 📌 레거시 호환성 - 기존 core.py 인터페이스 유지
// 실제 기능들은 새로운 모듈들로 분리되었습니다.
// ═══════════════════════════════════════════════════════════
console.log('📋 문의 모달 핵심 기능 로딩 중... (레거시 호환성)');

// ⚠️ 주의: 이 파일은 레거시 호환성을 위해 유지됩니다.
// 새로운 기능들은 다음 모듈들에서 제공됩니다:
// - modal_state.py: 상태 관리
// - dom_utils.py: DOM 조작
// - modal_actions.py: 모달 열기/닫기
// - card_factory.py: 카드 생성
// - data_matcher.py: 데이터 매칭
// - stats_calculator.py: 통계 계산
// - main_loader.py: 데이터 로딩

// 기본적인 호환성 함수들만 여기에 남겨둡니다.

// ─────────── 레거시 호환성 함수들 ───────────
function legacyCompatibilityCheck() {
    const requiredFunctions = [
        'updateModalState',
        'resetModalState', 
        'openInquiryModal',
        'closeInquiryModal',
        'createInquiryCard',
        'loadCategoryInquiries',
        'calculateInquiryStats'
    ];
    
    const missingFunctions = requiredFunctions.filter(funcName => {
        return typeof window[funcName] !== 'function';
    });
    
    if (missingFunctions.length > 0) {
        console.error('❌ 필수 함수들이 누락되었습니다:', missingFunctions);
        console.log('💡 새로운 모듈들이 올바르게 로드되었는지 확인하세요.');
        return false;
    }
    
    console.log('✅ 레거시 호환성 확인 완료');
    return true;
}

// ─────────── 통합 초기화 ───────────
function initializeInquiryModal() {
    console.log('🎯 문의 모달 시스템 초기화...');
    
    // 호환성 확인
    if (!legacyCompatibilityCheck()) {
        console.error('❌ 초기화 실패: 필수 컴포넌트 누락');
        return false;
    }
    
    // 기본 상태 초기화 (새 모듈에서 제공)
    if (typeof resetModalState === 'function') {
        resetModalState();
    }
    
    console.log('✅ 문의 모달 시스템 초기화 완료');
    return true;
}

// ─────────── 시스템 상태 확인 ───────────
window.checkInquiryModalSystem = function() {
    console.log('🔍 문의 모달 시스템 상태 확인:');
    
    const systemStatus = {
        stateManager: typeof updateModalState === 'function',
        domUtils: typeof ensureInquiryListElement === 'function', 
        modalActions: typeof openInquiryModal === 'function',
        cardFactory: typeof createInquiryCard === 'function',
        dataLoader: typeof loadCategoryInquiries === 'function',
        stats: typeof calculateInquiryStats === 'function',
        filters: typeof applyAllFiltersAndRender === 'function'
    };
    
    console.log('📊 시스템 모듈 상태:', systemStatus);
    
    const allLoaded = Object.values(systemStatus).every(status => status === true);
    console.log(allLoaded ? '✅ 모든 모듈 정상 로드됨' : '❌ 일부 모듈 누락됨');
    
    return systemStatus;
};

// 페이지 로드 완료 시 자동 초기화
setTimeout(() => {
    initializeInquiryModal();
}, 100);

console.log('✅ 문의 모달 핵심 기능 로딩 완료 (레거시 호환성)');
"""