# html_reporter/scripts/inquiry_modal/sorting.py
"""
문의 모달 정렬 기능 스크립트
"""

def get_sorting_scripts():
    """정렬 관련 스크립트"""
    return """
// ─────────── 정렬 시스템 ───────────
console.log('📊 정렬 시스템 로딩 중...');

// ─────────── 정렬 적용 메인 함수 ───────────
window.applySorting = function(inquiries, sortType) {
    if (!inquiries || inquiries.length === 0) return [];
    
    console.log(`🔄 정렬 적용: ${sortType}, ${inquiries.length}건`);
    
    const sorted = [...inquiries];
    
    switch (sortType) {
        case 'latest':
            return sortByLatest(sorted);
        case 'urgent':
            return sortByUrgency(sorted);
        case 'length_desc':
            return sortByLengthDesc(sorted);
        case 'length_asc':
            return sortByLengthAsc(sorted);
        case 'team':
            return sortByTeam(sorted);
        default:
            console.warn(`⚠️ 알 수 없는 정렬 타입: ${sortType}, 최신순으로 정렬합니다.`);
            return sortByLatest(sorted);
    }
};

// ─────────── 최신순 정렬 ───────────
function sortByLatest(inquiries) {
    return inquiries.sort((a, b) => {
        const dateA = new Date(a.registration_date || 0);
        const dateB = new Date(b.registration_date || 0);
        return dateB - dateA; // 최신 순 (내림차순)
    });
}

// ─────────── 긴급순 정렬 ───────────
function sortByUrgency(inquiries) {
    return inquiries.sort((a, b) => {
        // 긴급도 우선 정렬
        const urgentA = Boolean(a.is_urgent);
        const urgentB = Boolean(b.is_urgent);
        
        if (urgentA && !urgentB) return -1;
        if (!urgentA && urgentB) return 1;
        
        // 긴급도가 같으면 최신순
        const dateA = new Date(a.registration_date || 0);
        const dateB = new Date(b.registration_date || 0);
        return dateB - dateA;
    });
}

// ─────────── 문의 길이순 정렬 (긴 순서) ───────────
function sortByLengthDesc(inquiries) {
    return inquiries.sort((a, b) => {
        const lengthA = (a.question_content || '').length;
        const lengthB = (b.question_content || '').length;
        
        if (lengthA === lengthB) {
            // 길이가 같으면 최신순
            const dateA = new Date(a.registration_date || 0);
            const dateB = new Date(b.registration_date || 0);
            return dateB - dateA;
        }
        
        return lengthB - lengthA; // 긴 순서 (내림차순)
    });
}

// ─────────── 문의 길이순 정렬 (짧은 순서) ───────────
function sortByLengthAsc(inquiries) {
    return inquiries.sort((a, b) => {
        const lengthA = (a.question_content || '').length;
        const lengthB = (b.question_content || '').length;
        
        if (lengthA === lengthB) {
            // 길이가 같으면 최신순
            const dateA = new Date(a.registration_date || 0);
            const dateB = new Date(b.registration_date || 0);
            return dateB - dateA;
        }
        
        return lengthA - lengthB; // 짧은 순서 (오름차순)
    });
}

// ─────────── 팀별 정렬 ───────────
function sortByTeam(inquiries) {
    return inquiries.sort((a, b) => {
        const teamA = (a.assigned_team || '미분류').toLowerCase();
        const teamB = (b.assigned_team || '미분류').toLowerCase();
        
        if (teamA === teamB) {
            // 팀이 같으면 최신순
            const dateA = new Date(a.registration_date || 0);
            const dateB = new Date(b.registration_date || 0);
            return dateB - dateA;
        }
        
        return teamA.localeCompare(teamB); // 알파벳 순
    });
}

// ─────────── 정렬 상태 표시 업데이트 ───────────
function updateSortingStatus(sortType, itemCount) {
    const sortNames = {
        'latest': '최신순',
        'urgent': '긴급순',
        'length_desc': '긴 문의순',
        'length_asc': '짧은 문의순',
        'team': '팀별순'
    };
    
    const sortName = sortNames[sortType] || '기본순';
    console.log(`📊 정렬 완료: ${sortName}, ${itemCount}건`);
}

// ─────────── 정렬 변경 이벤트 핸들러 ───────────
window.changeSortOrder = function(newSortType) {
    console.log(`🔄 정렬 변경: ${newSortType}`);
    
    const sortFilter = document.getElementById('sort-filter');
    if (sortFilter) {
        sortFilter.value = newSortType;
    }
    
    // 첫 페이지로 이동
    window.inquiryModalState.currentPage = 1;
    
    // 필터 및 정렬 다시 적용
    applyAllFiltersAndRender();
};

// ─────────── 정렬 성능 측정 ───────────
function measureSortPerformance(inquiries, sortType, sortFunction) {
    const startTime = performance.now();
    const result = sortFunction(inquiries);
    const endTime = performance.now();
    
    const duration = Math.round((endTime - startTime) * 100) / 100;
    console.log(`⏱️ 정렬 성능: ${sortType} - ${inquiries.length}건 처리에 ${duration}ms 소요`);
    
    return result;
}

// ─────────── 정렬 안정성 검증 ───────────
function validateSortStability(originalArray, sortedArray) {
    if (originalArray.length !== sortedArray.length) {
        console.error('❌ 정렬 중 데이터 손실 발생!');
        return false;
    }
    
    // 각 항목이 모두 존재하는지 확인
    const originalIds = new Set(originalArray.map(item => item.inquiry_id));
    const sortedIds = new Set(sortedArray.map(item => item.inquiry_id));
    
    if (originalIds.size !== sortedIds.size) {
        console.error('❌ 정렬 중 중복 데이터 발생!');
        return false;
    }
    
    for (let id of originalIds) {
        if (!sortedIds.has(id)) {
            console.error(`❌ 정렬 중 데이터 누락: ${id}`);
            return false;
        }
    }
    
    console.log('✅ 정렬 안정성 검증 완료');
    return true;
}

// ─────────── 정렬 디버깅 함수 ───────────
window.debugSorting = function() {
    console.log('🔍 정렬 디버깅 정보:');
    console.log('현재 정렬 타입:', window.inquiryModalState.currentFilters.sort);
    console.log('필터링된 문의 수:', window.inquiryModalState.filteredInquiries?.length || 0);
    
    if (window.inquiryModalState.filteredInquiries && window.inquiryModalState.filteredInquiries.length > 0) {
        const first5 = window.inquiryModalState.filteredInquiries.slice(0, 5);
        console.log('상위 5개 문의 정렬 상태:');
        first5.forEach((inquiry, index) => {
            const date = new Date(inquiry.registration_date).toLocaleDateString('ko-KR');
            const urgent = inquiry.is_urgent ? '🚨' : '📋';
            const length = (inquiry.question_content || '').length;
            console.log(`  ${index + 1}. ${urgent} ${inquiry.assigned_team} | ${date} | ${length}자 | ID: ${inquiry.inquiry_id}`);
        });
    }
};

console.log('✅ 정렬 시스템 로딩 완료');
"""