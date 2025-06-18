# html_reporter/scripts/inquiry_modal/data_loader.py (최소화된 레거시 버전)
"""
문의 데이터 로딩 - 레거시 호환성용 최소 기능만
대부분의 기능이 새로운 모듈들로 분리되었습니다.
"""

def get_data_loader_scripts():
    """데이터 로딩 관련 스크립트 - 레거시 호환성용"""
    return """
// ═══════════════════════════════════════════════════════════
// 📌 레거시 호환성 - 기존 data_loader.py 인터페이스 유지  
// 실제 기능들은 새로운 모듈들로 분리되었습니다.
// ═══════════════════════════════════════════════════════════
console.log('📊 데이터 로더 시스템 로딩 중... (레거시 호환성)');

// ⚠️ 주의: 이 파일은 레거시 호환성을 위해 유지됩니다.
// 새로운 기능들은 다음 모듈들에서 제공됩니다:
// - main_loader.py: 메인 데이터 로딩 로직
// - data_matcher.py: 카테고리 매칭 시스템
// - stats_calculator.py: 통계 계산 시스템

// ─────────── 레거시 래퍼 함수들 ───────────

// 메인 로더 함수는 main_loader.py에서 제공됩니다
// window.loadCategoryInquiries는 이미 정의되어 있어야 합니다.

// ─────────── 호환성 확인 함수 ───────────
function checkDataLoaderCompatibility() {
    const requiredFunctions = [
        'loadCategoryInquiries',      // main_loader.py에서 제공
        'filterInquiriesByCategory',  // data_matcher.py에서 제공
        'calculateInquiryStats',      // stats_calculator.py에서 제공
        'updateTeamFilterOptions'     // stats_calculator.py에서 제공
    ];
    
    const missingFunctions = requiredFunctions.filter(funcName => {
        return typeof window[funcName] !== 'function';
    });
    
    if (missingFunctions.length > 0) {
        console.error('❌ 데이터 로더 필수 함수들이 누락되었습니다:', missingFunctions);
        return false;
    }
    
    console.log('✅ 데이터 로더 호환성 확인 완료');
    return true;
}

// ─────────── 레거시 헬퍼 함수들 ───────────
window.debugInquiryData = function() {
    console.log('🔍 문의 데이터 디버깅 정보 (레거시):');
    
    // 새로운 디버깅 함수가 있으면 그것을 호출
    if (typeof window.debugDataLoading === 'function') {
        return window.debugDataLoading();
    }
    
    // 기본 디버깅 정보
    const state = window.inquiryModalState || {};
    console.log(`📦 전체 원본 데이터: ${window.rawInquiryData?.length || 0}건`);
    console.log(`🎯 현재 카테고리: ${state.currentCategory || 'N/A'}`);
    console.log(`📊 필터링된 문의: ${state.allInquiries?.length || 0}건`);
    console.log(`📄 현재 페이지 문의: ${state.currentPageInquiries?.length || 0}건`);
};

// ─────────── 검색어 하이라이팅 (레거시 지원) ───────────
if (typeof window.highlightSearchTerm !== 'function') {
    window.highlightSearchTerm = function(text, searchTerm) {
        if (!searchTerm || !text) return text;
        
        try {
            const regex = new RegExp(`(${searchTerm.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\window.debugInquiryData = function() {
    console.log('🔍 문의 데이터 디버깅 정보 (레거시):')})`, 'gi');
            return text.replace(regex, '<mark class="search-highlight">$1</mark>');
        } catch (error) {
            console.warn('⚠️ 검색어 하이라이팅 오류 (레거시):', error);
            return text;
        }
    };
}

// ─────────── 초기화 및 호환성 확인 ───────────
setTimeout(() => {
    if (checkDataLoaderCompatibility()) {
        console.log('✅ 데이터 로더 시스템 준비 완료 (레거시 호환성)');
    } else {
        console.error('❌ 데이터 로더 시스템 초기화 실패');
        console.log('💡 새로운 모듈들(main_loader, data_matcher, stats_calculator)이 올바르게 로드되었는지 확인하세요.');
    }
}, 200);

console.log('✅ 데이터 로더 시스템 로딩 완료 (레거시 호환성)');
"""