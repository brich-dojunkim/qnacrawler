# html_reporter/scripts/inquiry_modal/main_loader.py
"""
문의 데이터 메인 로더
"""

def get_main_loader_scripts():
    """메인 데이터 로더 스크립트"""
    return """
// ─────────── 메인 데이터 로더 시스템 ───────────
console.log('📁 메인 데이터 로더 시스템 로딩 중...');

// ─────────── 카테고리별 문의 로딩 메인 함수 ───────────
window.loadCategoryInquiries = function(categoryName) {
    console.log(`📋 카테고리 문의 로딩: "${categoryName}"`);
    
    try {
        // 데이터 유효성 검증
        if (!validateRawData()) {
            handleDataError();
            return;
        }
        
        console.log(`📦 전체 원본 데이터: ${window.rawInquiryData.length}건`);
        
        // 카테고리별 필터링
        const categoryInquiries = filterInquiriesByCategory(categoryName);
        console.log(`🎯 "${categoryName}" 매칭 문의: ${categoryInquiries.length}건`);
        
        if (categoryInquiries.length === 0) {
            handleEmptyResult();
            return;
        }
        
        // 데이터 처리 및 UI 업데이트
        processLoadedData(categoryInquiries);
        
        console.log('✅ 카테고리 데이터 로딩 완료');
        
    } catch (error) {
        handleLoadingError(error);
    }
};

// ─────────── 원본 데이터 유효성 검증 ───────────
function validateRawData() {
    if (!window.rawInquiryData) {
        console.error('❌ 원본 문의 데이터가 없습니다.');
        console.log('🔍 window.rawInquiryData 상태:', typeof window.rawInquiryData, window.rawInquiryData);
        return false;
    }
    
    if (!Array.isArray(window.rawInquiryData)) {
        console.error('❌ 원본 데이터가 배열이 아닙니다.');
        return false;
    }
    
    if (window.rawInquiryData.length === 0) {
        console.error('❌ 원본 데이터가 비어있습니다.');
        return false;
    }
    
    return true;
}

// ─────────── 로드된 데이터 처리 ───────────
function processLoadedData(categoryInquiries) {
    // 상태 업데이트
    setInquiryData(categoryInquiries);
    
    // 통계 계산
    const stats = calculateInquiryStats(categoryInquiries);
    updateInquiryStats(stats.total, stats.urgent, stats.completed, stats.avgLength);
    
    // 팀 필터 옵션 업데이트
    updateTeamFilterOptions(categoryInquiries);
    
    // 필터링 및 렌더링
    applyAllFiltersAndRender();
}

// ─────────── 에러 처리 함수들 ───────────
function handleDataError() {
    console.error('❌ 데이터 검증 실패');
    hideInquiryLoading();
    showEmptyState();
    updateInquiryStats(0, 0, 0, 0);
}

function handleEmptyResult() {
    console.log('📭 해당 카테고리의 문의가 없습니다.');
    hideInquiryLoading();
    showEmptyState();
    updateInquiryStats(0, 0, 0, 0);
}

function handleLoadingError(error) {
    console.error('❌ 카테고리 문의 로딩 오류:', error);
    console.log('❌ 오류 스택:', error.stack);
    hideInquiryLoading();
    showEmptyState();
    alert('문의 데이터를 불러오는 중 오류가 발생했습니다.');
}

// ─────────── 데이터 변환 유틸리티 ───────────
function normalizeInquiryData(rawData) {
    if (!Array.isArray(rawData)) {
        console.warn('⚠️ 원본 데이터가 배열이 아닙니다. 변환을 시도합니다.');
        
        if (typeof rawData === 'object' && rawData.data) {
            return rawData.data;
        } else if (typeof rawData === 'object') {
            return [rawData];
        }
        
        return [];
    }
    
    return rawData;
}

function validateInquiryStructure(inquiry) {
    const requiredFields = ['inquiry_id', 'question_content'];
    const missingFields = requiredFields.filter(field => !inquiry[field]);
    
    if (missingFields.length > 0) {
        console.warn(`⚠️ 문의 ${inquiry.inquiry_id || 'Unknown'} 필수 필드 누락:`, missingFields);
        return false;
    }
    
    return true;
}

// ─────────── 데이터 사전 처리 ───────────
function preprocessInquiryData(inquiries) {
    return inquiries.filter(inquiry => {
        if (!inquiry) return false;
        
        // 구조 검증
        if (!validateInquiryStructure(inquiry)) {
            return false;
        }
        
        // 기본값 설정
        inquiry.is_urgent = inquiry.is_urgent || false;
        inquiry.answer_status = inquiry.answer_status || '답변대기';
        inquiry.question_content = inquiry.question_content || '';
        
        return true;
    });
}

// ─────────── 캐시 관리 ───────────
const inquiryDataCache = new Map();

function getCachedInquiries(categoryName) {
    return inquiryDataCache.get(categoryName);
}

function setCachedInquiries(categoryName, inquiries) {
    inquiryDataCache.set(categoryName, {
        data: inquiries,
        timestamp: Date.now()
    });
}

function clearInquiryCache() {
    inquiryDataCache.clear();
    console.log('🧹 문의 데이터 캐시 정리 완료');
}

// ─────────── 로딩 상태 관리 ───────────
function setLoadingState(isLoading) {
    if (isLoading) {
        showInquiryLoading();
    } else {
        hideInquiryLoading();
    }
}

function setErrorState(message = '데이터를 불러올 수 없습니다.') {
    hideInquiryLoading();
    showEmptyState();
    console.error('❌ 오류 상태:', message);
}

// ─────────── 데이터 로딩 성능 측정 ───────────
function measureLoadingPerformance(categoryName, loadFunction) {
    const startTime = performance.now();
    
    const result = loadFunction(categoryName);
    
    const endTime = performance.now();
    const duration = Math.round((endTime - startTime) * 100) / 100;
    
    console.log(`⏱️ "${categoryName}" 로딩 성능: ${duration}ms`);
    
    return result;
}

// ─────────── 강화된 디버깅 함수 ───────────
window.debugDataLoading = function() {
    console.log('🔍 데이터 로딩 디버깅 정보:');
    
    const state = getCurrentState();
    
    console.log(`📦 전체 원본 데이터: ${window.rawInquiryData?.length || 0}건`);
    console.log(`🎯 현재 카테고리: ${state.currentCategory}`);
    console.log(`📊 필터링된 문의: ${state.allInquiries?.length || 0}건`);
    console.log(`📄 현재 페이지 문의: ${state.currentPageInquiries?.length || 0}건`);
    
    if (window.rawInquiryData && window.rawInquiryData.length > 0) {
        console.log('📋 첫 번째 원본 데이터 구조:');
        const firstData = window.rawInquiryData[0];
        console.log('  - inquiry_id:', firstData.inquiry_id);
        console.log('  - is_urgent:', firstData.is_urgent);
        console.log('  - answer_status:', firstData.answer_status);
        console.log('  - category 객체:', firstData.category);
        console.log('  - 직접 assigned_team:', firstData.assigned_team);
        console.log('  - 직접 sub_category:', firstData.sub_category);
        console.log('  - answers 배열:', firstData.answers?.length || 0, '개');
        console.log('  - question_content 길이:', firstData.question_content?.length || 0, '자');
    }
    
    if (state.allInquiries && state.allInquiries.length > 0) {
        console.log('📊 필터링된 첫 번째 데이터:');
        const firstFiltered = state.allInquiries[0];
        console.log('  - inquiry_id:', firstFiltered.inquiry_id);
        console.log('  - 매칭된 카테고리:', firstFiltered.category?.sub_category || firstFiltered.sub_category);
        console.log('  - 팀:', firstFiltered.category?.assigned_team || firstFiltered.assigned_team);
    }
    
    // 카테고리별 분포 확인
    if (window.rawInquiryData && window.rawInquiryData.length > 0) {
        const categoryCount = {};
        window.rawInquiryData.forEach(inquiry => {
            const category = inquiry.category?.sub_category || inquiry.sub_category || '알 수 없음';
            categoryCount[category] = (categoryCount[category] || 0) + 1;
        });
        
        console.log('📊 전체 카테고리 분포 (상위 10개):');
        Object.entries(categoryCount)
            .sort((a, b) => b[1] - a[1])
            .slice(0, 10)
            .forEach(([category, count]) => {
                console.log(`  - ${category}: ${count}건`);
            });
    }
    
    // 캐시 상태 확인
    console.log('💾 캐시 상태:', {
        cacheSize: inquiryDataCache.size,
        cachedCategories: Array.from(inquiryDataCache.keys())
    });
};

// 자동으로 디버깅 정보 출력 (개발용)
setTimeout(() => {
    if (window.rawInquiryData) {
        console.log('🚀 데이터 로더 자동 디버깅:');
        window.debugDataLoading();
    }
}, 1000);

console.log('✅ 메인 데이터 로더 시스템 로딩 완료');
"""