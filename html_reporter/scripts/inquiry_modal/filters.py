# html_reporter/scripts/inquiry_modal/filters.py
"""
문의 모달 필터링 및 검색 스크립트
"""

def get_filters_scripts():
    """필터링 및 검색 관련 스크립트"""
    return """
// ─────────── 필터링 및 검색 시스템 ───────────
console.log('🔍 필터링 시스템 로딩 중...');

// 검색 디바운스 타이머
let searchDebounceTimer = null;
window.currentSearchTerm = '';

// ─────────── 검색 이벤트 리스너 설정 ───────────
document.addEventListener('DOMContentLoaded', function() {
    setupFilterEventListeners();
});

function setupFilterEventListeners() {
    // 검색 입력 이벤트
    const searchInput = document.getElementById('inquiry-search');
    if (searchInput) {
        searchInput.addEventListener('input', function(e) {
            handleSearchInput(e.target.value);
        });
        
        searchInput.addEventListener('keydown', function(e) {
            if (e.key === 'Enter') {
                e.preventDefault();
                applyAllFiltersAndRender();
            }
        });
    }
    
    // 필터 드롭다운 이벤트
    const filterIds = ['team-filter', 'urgency-filter', 'status-filter', 'sort-filter'];
    filterIds.forEach(filterId => {
        const filter = document.getElementById(filterId);
        if (filter) {
            filter.addEventListener('change', function() {
                applyAllFiltersAndRender();
            });
        }
    });
    
    // 페이지당 항목 수 변경
    const itemsPerPageSelect = document.getElementById('items-per-page');
    if (itemsPerPageSelect) {
        itemsPerPageSelect.addEventListener('change', function() {
            changeItemsPerPage();
        });
    }
}

// ─────────── 검색 입력 처리 (디바운스) ───────────
function handleSearchInput(searchTerm) {
    // 이전 타이머 취소
    if (searchDebounceTimer) {
        clearTimeout(searchDebounceTimer);
    }
    
    // 검색어 상태 업데이트
    window.currentSearchTerm = searchTerm.trim();
    
    // Clear 버튼 표시/숨김
    const clearBtn = document.getElementById('clear-search');
    if (clearBtn) {
        clearBtn.style.display = searchTerm.length > 0 ? 'block' : 'none';
    }
    
    // 500ms 후 실제 검색 실행
    searchDebounceTimer = setTimeout(() => {
        console.log(`🔍 검색 실행: "${window.currentSearchTerm}"`);
        applyAllFiltersAndRender();
    }, 500);
}

// ─────────── 검색어 초기화 ───────────
window.clearInquirySearch = function() {
    const searchInput = document.getElementById('inquiry-search');
    const clearBtn = document.getElementById('clear-search');
    
    if (searchInput) {
        searchInput.value = '';
        searchInput.focus();
    }
    
    if (clearBtn) {
        clearBtn.style.display = 'none';
    }
    
    window.currentSearchTerm = '';
    applyAllFiltersAndRender();
};

// ─────────── 모든 필터 초기화 ───────────
window.clearAllInquiryFilters = function() {
    console.log('🧹 모든 필터 초기화');
    
    // 검색어 초기화
    const searchInput = document.getElementById('inquiry-search');
    if (searchInput) {
        searchInput.value = '';
    }
    
    const clearBtn = document.getElementById('clear-search');
    if (clearBtn) {
        clearBtn.style.display = 'none';
    }
    
    // 필터 드롭다운 초기화
    const filterSelects = ['team-filter', 'urgency-filter', 'status-filter'];
    filterSelects.forEach(selectId => {
        const select = document.getElementById(selectId);
        if (select) {
            select.selectedIndex = 0;
        }
    });
    
    // 정렬은 최신순으로 리셋
    const sortFilter = document.getElementById('sort-filter');
    if (sortFilter) {
        sortFilter.value = 'latest';
    }
    
    // 상태 초기화
    window.currentSearchTerm = '';
    window.inquiryModalState.currentPage = 1;
    window.inquiryModalState.currentFilters = {
        search: '',
        team: '',
        urgency: '',
        status: '',
        sort: 'latest'
    };
    
    // 필터 적용
    applyAllFiltersAndRender();
};

// ─────────── 모든 필터 적용 및 렌더링 ───────────
window.applyAllFiltersAndRender = function() {
    console.log('🎯 모든 필터 적용 및 렌더링 시작');
    
    try {
        // 현재 필터 값들 가져오기
        const filters = getCurrentFilterValues();
        
        // 상태 업데이트
        window.inquiryModalState.currentFilters = filters;
        
        // 필터링 실행
        const filteredInquiries = applyFilters(window.inquiryModalState.allInquiries, filters);
        console.log(`📊 필터링 결과: ${filteredInquiries.length}건`);
        
        // 정렬 적용
        const sortedInquiries = applySorting(filteredInquiries, filters.sort);
        
        // 상태 업데이트
        window.inquiryModalState.filteredInquiries = sortedInquiries;
        window.inquiryModalState.filteredItems = sortedInquiries.length;
        
        // 페이지네이션 적용 및 렌더링
        updatePaginationAndRender();
        
    } catch (error) {
        console.error('❌ 필터 적용 오류:', error);
        showEmptyState();
    }
};

// ─────────── 현재 필터 값들 가져오기 ───────────
function getCurrentFilterValues() {
    return {
        search: window.currentSearchTerm || '',
        team: document.getElementById('team-filter')?.value || '',
        urgency: document.getElementById('urgency-filter')?.value || '',
        status: document.getElementById('status-filter')?.value || '',
        sort: document.getElementById('sort-filter')?.value || 'latest'
    };
}

// ─────────── 필터링 로직 ───────────
function applyFilters(inquiries, filters) {
    if (!inquiries || inquiries.length === 0) return [];
    
    let filtered = [...inquiries];
    
    // 검색어 필터
    if (filters.search) {
        console.log(`🔍 검색어 필터: "${filters.search}"`);
        const searchTerm = filters.search.toLowerCase();
        filtered = filtered.filter(inquiry => {
            const content = (inquiry.question_content || '').toLowerCase();
            const category = (inquiry.sub_category || '').toLowerCase();
            const team = (inquiry.assigned_team || '').toLowerCase();
            const id = (inquiry.inquiry_id || '').toString().toLowerCase();
            
            return content.includes(searchTerm) || 
                   category.includes(searchTerm) || 
                   team.includes(searchTerm) || 
                   id.includes(searchTerm);
        });
        console.log(`🎯 검색 결과: ${filtered.length}건`);
    }
    
    // 팀 필터
    if (filters.team) {
        console.log(`👥 팀 필터: "${filters.team}"`);
        filtered = filtered.filter(inquiry => inquiry.assigned_team === filters.team);
        console.log(`🎯 팀 필터 결과: ${filtered.length}건`);
    }
    
    // 긴급도 필터
    if (filters.urgency) {
        console.log(`🚨 긴급도 필터: "${filters.urgency}"`);
        if (filters.urgency === 'urgent') {
            filtered = filtered.filter(inquiry => inquiry.is_urgent === true || inquiry.is_urgent === 'true' || inquiry.is_urgent === 1);
        } else if (filters.urgency === 'normal') {
            filtered = filtered.filter(inquiry => !inquiry.is_urgent || inquiry.is_urgent === false || inquiry.is_urgent === 'false' || inquiry.is_urgent === 0);
        }
        console.log(`🎯 긴급도 필터 결과: ${filtered.length}건`);
    }
    
    // 상태 필터
    if (filters.status) {
        console.log(`📋 상태 필터: "${filters.status}"`);
        if (filters.status === 'answered') {
            filtered = filtered.filter(inquiry => 
                inquiry.answer_status === '답변완료' || 
                (inquiry.answers && inquiry.answers.length > 0)
            );
        } else if (filters.status === 'pending') {
            filtered = filtered.filter(inquiry => 
                !inquiry.answer_status || 
                inquiry.answer_status === '답변대기' || 
                inquiry.answer_status === '대기중' ||
                (!inquiry.answers || inquiry.answers.length === 0)
            );
        } else if (filters.status === 'in_progress') {
            filtered = filtered.filter(inquiry => 
                inquiry.answer_status === '진행중' || 
                inquiry.answer_status === '처리중'
            );
        }
        console.log(`🎯 상태 필터 결과: ${filtered.length}건`);
    }
    
    return filtered;
}

console.log('✅ 필터링 시스템 로딩 완료');
"""