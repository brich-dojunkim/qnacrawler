# html_reporter/scripts/inquiry_modal/data_loader.py
"""
문의 데이터 로딩 및 카테고리 매칭 스크립트 - 안전한 필터링 로직 + 로딩 상태 관리
"""

def get_data_loader_scripts():
    """데이터 로딩 관련 스크립트 - 안전한 타입 체크 추가 + 로딩 상태 관리"""
    return """
// ─────────── 데이터 로딩 및 매칭 (로딩 상태 관리 개선) ───────────
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
        
        // 🔧 중요: 필터링 및 렌더링 (로딩은 여기서 숨겨짐)
        applyAllFiltersAndRender();
        
        console.log('✅ 카테고리 데이터 로딩 완료');
        
    } catch (error) {
        console.error('❌ 카테고리 문의 로딩 오류:', error);
        hideInquiryLoading();
        showEmptyState();
    }
};

// ─────────── 안전한 카테고리별 문의 필터링 ───────────
function filterInquiriesByCategory(categoryName) {
    console.log(`🔍 카테고리 필터링 시작: "${categoryName}"`);
    
    const matchedInquiries = window.rawInquiryData.filter(inquiry => {
        if (!inquiry) return false;
        
        // 안전한 필드 추출 함수
        function safeGetField(obj, path) {
            try {
                const keys = path.split('.');
                let value = obj;
                for (const key of keys) {
                    if (value && typeof value === 'object' && key in value) {
                        value = value[key];
                    } else {
                        return null;
                    }
                }
                // 문자열이 아닌 경우 문자열로 변환
                return value && typeof value === 'string' ? value : (value ? String(value) : null);
            } catch (e) {
                return null;
            }
        }
        
        // 다양한 매칭 방식 시도 - 안전한 필드 추출
        const matchFields = [
            safeGetField(inquiry, 'sub_category'),
            safeGetField(inquiry, 'category'),
            safeGetField(inquiry, 'main_category'),
            safeGetField(inquiry, 'category_name'),
            safeGetField(inquiry, 'category.sub_category'),
            safeGetField(inquiry, 'category.category'),
            safeGetField(inquiry, 'category.full_text')
        ].filter(field => field !== null); // null 값 제거
        
        // 정확한 매칭 먼저 시도
        const exactMatch = matchFields.some(field => {
            if (!field) return false;
            try {
                return field.trim().toLowerCase() === categoryName.trim().toLowerCase();
            } catch (e) {
                console.warn('정확한 매칭 중 오류:', e, 'field:', field);
                return false;
            }
        });
        
        if (exactMatch) return true;
        
        // 부분 매칭 시도 (카테고리명이 필드에 포함되거나 반대의 경우)
        const partialMatch = matchFields.some(field => {
            if (!field) return false;
            try {
                const fieldLower = field.trim().toLowerCase();
                const categoryLower = categoryName.trim().toLowerCase();
                return fieldLower.includes(categoryLower) || categoryLower.includes(fieldLower);
            } catch (e) {
                console.warn('부분 매칭 중 오류:', e, 'field:', field);
                return false;
            }
        });
        
        return partialMatch;
    });
    
    console.log(`✅ 매칭 결과: ${matchedInquiries.length}건`);
    
    // 매칭된 문의의 샘플 로그 (처음 3개)
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

// ─────────── 통계 계산 ───────────
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
        
        // 완료된 문의 카운트
        if (inquiry.answer_status === '답변완료' || 
            (inquiry.answers && inquiry.answers.length > 0)) {
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

// ─────────── 팀 필터 옵션 업데이트 ───────────
function updateTeamFilterOptions(inquiries) {
    const teamFilter = document.getElementById('team-filter');
    if (!teamFilter) return;
    
    // 고유한 팀 목록 추출
    const teams = new Set();
    inquiries.forEach(inquiry => {
        const team = inquiry.assigned_team || inquiry.category?.assigned_team;
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

// ─────────── 데이터 변환 유틸리티 ───────────
function ensureInquiryDataIntegrity(inquiry) {
    // 기본값 설정 및 데이터 타입 보정
    return {
        inquiry_id: inquiry.inquiry_id || 'unknown',
        question_content: inquiry.question_content || '',
        sub_category: inquiry.sub_category || inquiry.category?.sub_category || '기타',
        assigned_team: inquiry.assigned_team || inquiry.category?.assigned_team || '미분류',
        registration_date: inquiry.registration_date || new Date().toISOString(),
        is_urgent: Boolean(inquiry.is_urgent),
        answer_status: inquiry.answer_status || '답변대기',
        answers: Array.isArray(inquiry.answers) ? inquiry.answers : [],
        author_info: inquiry.author_info || {},
        content_length: inquiry.question_content ? inquiry.question_content.length : 0
    };
}

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