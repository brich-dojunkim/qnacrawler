# html_reporter/scripts/inquiry_modal/data_loader.py (수정된 버전)
"""
문의 데이터 로딩 및 카테고리 매칭 스크립트 - 실제 JSON 구조에 맞게 수정
"""

def get_data_loader_scripts():
    """데이터 로딩 관련 스크립트 - 실제 JSON 구조에 맞게 수정"""
    return """
// ─────────── 데이터 로딩 및 매칭 (실제 JSON 구조 반영) ───────────
console.log('📊 데이터 로더 시스템 로딩 중...');

// 카테고리별 문의 로딩 메인 함수
window.loadCategoryInquiries = function(categoryName) {
    console.log(`📋 카테고리 문의 로딩: ${categoryName}`);
    
    try {
        // 원본 데이터 확인
        if (!window.rawInquiryData || !Array.isArray(window.rawInquiryData)) {
            console.error('❌ 원본 문의 데이터가 없습니다.');
            hideInquiryLoading();
            showEmptyState();
            return;
        }
        
        console.log(`📦 전체 원본 데이터: ${window.rawInquiryData.length}건`);
        
        // 카테고리에 해당하는 문의들 필터링
        const categoryInquiries = filterInquiriesByCategory(categoryName);
        console.log(`🎯 ${categoryName} 매칭 문의: ${categoryInquiries.length}건`);
        
        if (categoryInquiries.length === 0) {
            console.log('📭 해당 카테고리의 문의가 없습니다.');
            hideInquiryLoading();
            showEmptyState();
            updateInquiryStats(0, 0, 0, 0);
            return;
        }
        
        // 상태 업데이트
        window.inquiryModalState.allInquiries = categoryInquiries;
        window.inquiryModalState.totalItems = categoryInquiries.length;
        
        // 통계 계산 및 업데이트
        const stats = calculateInquiryStats(categoryInquiries);
        updateInquiryStats(stats.total, stats.urgent, stats.completed, stats.avgLength);
        
        // 팀 필터 옵션 업데이트
        updateTeamFilterOptions(categoryInquiries);
        
        // 필터링 및 렌더링
        applyAllFiltersAndRender();
        
        console.log('✅ 카테고리 데이터 로딩 완료');
        
    } catch (error) {
        console.error('❌ 카테고리 문의 로딩 오류:', error);
        hideInquiryLoading();
        showEmptyState();
    }
};

// ─────────── 실제 JSON 구조에 맞춘 카테고리별 문의 필터링 ───────────
function filterInquiriesByCategory(categoryName) {
    console.log(`🔍 카테고리 필터링 시작: "${categoryName}"`);
    
    const matchedInquiries = window.rawInquiryData.filter(inquiry => {
        if (!inquiry) return false;
        
        try {
            // 실제 JSON 구조에 맞춘 필드 추출
            const subCategory = inquiry.category?.sub_category || inquiry.sub_category;
            const fullText = inquiry.category?.full_text || '';
            
            if (!subCategory) return false;
            
            const categoryLower = categoryName.trim().toLowerCase();
            const subCategoryLower = subCategory.trim().toLowerCase();
            const fullTextLower = fullText.trim().toLowerCase();
            
            // 정확한 매칭 또는 부분 매칭
            return subCategoryLower === categoryLower || 
                   subCategoryLower.includes(categoryLower) || 
                   categoryLower.includes(subCategoryLower) ||
                   fullTextLower.includes(categoryLower);
                   
        } catch (e) {
            console.warn('필터링 중 오류:', e, 'inquiry:', inquiry);
            return false;
        }
    });
    
    console.log(`✅ 매칭 결과: ${matchedInquiries.length}건`);
    
    // 매칭된 문의의 샘플 로그
    if (matchedInquiries.length > 0) {
        console.log('📝 매칭된 문의 샘플:');
        matchedInquiries.slice(0, 3).forEach((inquiry, index) => {
            const id = inquiry.inquiry_id || 'N/A';
            const subCat = inquiry.category?.sub_category || inquiry.sub_category || 'N/A';
            const content = (inquiry.question_content || '').substring(0, 50) + '...';
            console.log(`  ${index + 1}. ID: ${id}, 카테고리: ${subCat}, 내용: ${content}`);
        });
    }
    
    return matchedInquiries;
}

// ─────────── 실제 JSON 구조에 맞춘 통계 계산 ───────────
function calculateInquiryStats(inquiries) {
    if (!inquiries || inquiries.length === 0) {
        return { total: 0, urgent: 0, completed: 0, avgLength: 0 };
    }
    
    const total = inquiries.length;
    let urgent = 0;
    let completed = 0;
    let totalLength = 0;
    
    inquiries.forEach(inquiry => {
        // 긴급 문의 카운트
        if (inquiry.is_urgent === true || inquiry.is_urgent === 'true' || inquiry.is_urgent === 1) {
            urgent++;
        }
        
        // 완료된 문의 카운트 - 실제 JSON 구조에 맞춤
        if (inquiry.answer_status === '답변완료' || 
            (inquiry.answers && Array.isArray(inquiry.answers) && inquiry.answers.length > 0)) {
            completed++;
        }
        
        // 문의 내용 길이
        const contentLength = inquiry.question_content ? inquiry.question_content.length : 0;
        totalLength += contentLength;
    });
    
    const avgLength = total > 0 ? Math.round(totalLength / total) : 0;
    
    console.log(`📊 통계 계산 완료: 총 ${total}건, 긴급 ${urgent}건, 완료 ${completed}건, 평균 ${avgLength}자`);
    
    return { total, urgent, completed, avgLength };
}

// ─────────── 실제 JSON 구조에 맞춘 팀 필터 옵션 업데이트 ───────────
function updateTeamFilterOptions(inquiries) {
    const teamFilter = document.getElementById('team-filter');
    if (!teamFilter) return;
    
    // 고유한 팀 목록 추출 - 실제 JSON 구조에 맞춤
    const teams = new Set();
    inquiries.forEach(inquiry => {
        const team = inquiry.category?.assigned_team || inquiry.assigned_team;
        if (team && typeof team === 'string' && team.trim()) {
            teams.add(team.trim());
        }
    });
    
    // 팀 필터 옵션 생성
    const sortedTeams = Array.from(teams).sort();
    let optionsHtml = '<option value="">👥 모든 팀</option>';
    
    sortedTeams.forEach(team => {
        optionsHtml += `<option value="${team}">${team}</option>`;
    });
    
    teamFilter.innerHTML = optionsHtml;
    
    console.log(`👥 팀 필터 업데이트: ${sortedTeams.length}개 팀`);
}

// ─────────── 검색어 하이라이팅 ───────────
window.highlightSearchTerm = function(text, searchTerm) {
    if (!searchTerm || !text) return text;
    
    try {
        const regex = new RegExp(`(${searchTerm.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&')})`, 'gi');
        return text.replace(regex, '<mark class="search-highlight">$1</mark>');
    } catch (error) {
        console.warn('검색어 하이라이팅 오류:', error);
        return text;
    }
};

// ─────────── 디버깅 함수 ───────────
window.debugInquiryData = function() {
    console.log('🔍 문의 데이터 디버깅 정보:');
    console.log('전체 원본 데이터:', window.rawInquiryData?.length || 0);
    console.log('현재 카테고리:', window.inquiryModalState.currentCategory);
    console.log('필터링된 문의:', window.inquiryModalState.allInquiries?.length || 0);
    console.log('현재 페이지 문의:', window.inquiryModalState.currentPageInquiries?.length || 0);
    
    if (window.rawInquiryData && window.rawInquiryData.length > 0) {
        console.log('첫 번째 원본 데이터 샘플:', window.rawInquiryData[0]);
    }
    
    if (window.inquiryModalState.allInquiries && window.inquiryModalState.allInquiries.length > 0) {
        console.log('첫 번째 필터링된 데이터 샘플:', window.inquiryModalState.allInquiries[0]);
    }
};

console.log('✅ 데이터 로더 시스템 로딩 완료');
"""