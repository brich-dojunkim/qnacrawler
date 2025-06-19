# html_reporter/scripts/inquiry_modal/filters.py
"""
문의 모달 필터링 및 검색 스크립트 - 아코디언 스타일 적용
"""

def get_filters_scripts():
    """아코디언 스타일이 적용된 필터링 및 검색 관련 스크립트"""
    return """
// ─────────── 아코디언 스타일 필터링 시스템 ───────────
console.log('🔍 아코디언 스타일 필터링 시스템 로딩 중...');

// 필터 상태 관리
let filterState = {
    search: '',
    urgency: 'all',      // 'all', 'urgent', 'normal'
    status: 'all',       // 'all', 'completed', 'pending'
    sort: 'latest'       // 'latest' | 'length_desc'
};

// 검색 디바운스 타이머
let searchDebounceTimer = null;
window.currentSearchTerm = '';

// ─────────── 이벤트 리스너 설정 ───────────
document.addEventListener('DOMContentLoaded', function() {
    setupAccordionStyleFilterEventListeners();
});

function setupAccordionStyleFilterEventListeners() {
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

    // 외부 클릭 시 드롭다운 닫기
    document.addEventListener('click', function(e) {
        if (!e.target.closest('.filter-dropdown-wrapper')) {
            closeUrgencyDropdown();
            closeStatusDropdown();
        }
    });
}

// ─────────── 검색 입력 처리 (디바운스) ───────────
function handleSearchInput(searchTerm) {
    // 이전 타이머 취소
    if (searchDebounceTimer) {
        clearTimeout(searchDebounceTimer);
    }

    // 검색어 상태 업데이트
    window.currentSearchTerm = searchTerm.trim();
    filterState.search = window.currentSearchTerm;

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
    filterState.search = '';
    applyAllFiltersAndRender();
};

// ─────────── 긴급/일반 필터 드롭다운 ───────────
window.toggleUrgencyFilter = function() {
    closeStatusDropdown();
    const dropdown = document.getElementById('urgency-dropdown');
    if (dropdown) {
        dropdown.classList.toggle('hidden');
    }
};

window.selectUrgencyFilter = function(value) {
    filterState.urgency = value;
    updateUrgencyButtonState();
    console.log(`🚨 긴급도 필터: ${filterState.urgency}`);
    applyAllFiltersAndRender();
    closeUrgencyDropdown();
};

function closeUrgencyDropdown() {
    const dropdown = document.getElementById('urgency-dropdown');
    if (dropdown) dropdown.classList.add('hidden');
}

function updateUrgencyButtonState() {
    const toggleBtn = document.getElementById('urgency-toggle');
    if (toggleBtn) {
        // 기존 클래스 제거
        toggleBtn.classList.remove('active', 'urgent-active', 'normal-active');

        switch(filterState.urgency) {
            case 'urgent':
                toggleBtn.classList.add('active', 'urgent-active');
                break;
            case 'normal':
                toggleBtn.classList.add('active', 'normal-active');
                break;
            case 'all':
            default:
                // 기본 상태 (필터 없음)
                break;
        }
    }
}

// ─────────── 답변완료/미답변 필터 드롭다운 ───────────
window.toggleStatusFilter = function() {
    closeUrgencyDropdown();
    const dropdown = document.getElementById('status-dropdown');
    if (dropdown) {
        dropdown.classList.toggle('hidden');
    }
};

window.selectStatusFilter = function(value) {
    filterState.status = value;
    updateStatusButtonState();
    console.log(`✅ 상태 필터: ${filterState.status}`);
    applyAllFiltersAndRender();
    closeStatusDropdown();
};

function closeStatusDropdown() {
    const dropdown = document.getElementById('status-dropdown');
    if (dropdown) dropdown.classList.add('hidden');
}

function updateStatusButtonState() {
    const toggleBtn = document.getElementById('status-toggle');
    if (toggleBtn) {
        // 기존 클래스 제거
        toggleBtn.classList.remove('active', 'completed-active', 'pending-active');

        switch(filterState.status) {
            case 'completed':
                toggleBtn.classList.add('active', 'completed-active');
                break;
            case 'pending':
                toggleBtn.classList.add('active', 'pending-active');
                break;
            case 'all':
            default:
                // 기본 상태 (필터 없음)
                break;
        }
    }
}

// ─────────── 정렬 설정 (아코디언 스타일) ───────────
window.setSortOrder = function(sortType) {
    const previousSort = filterState.sort;
    filterState.sort = sortType;

    // 모든 정렬 버튼 비활성화
    document.querySelectorAll('.accordion-filter-sort').forEach(btn => {
        btn.classList.remove('active');
        const direction = btn.querySelector('.sort-direction');
        if (direction) {
            direction.textContent = '▼';
            direction.classList.remove('asc');
        }
    });

    // 선택된 정렬 버튼 활성화
    const sortBtn = document.getElementById(`sort-${sortType}`);
    if (sortBtn) {
        sortBtn.classList.add('active');

        // 정렬 방향 표시 (같은 정렬을 다시 클릭하면 방향 변경)
        const direction = sortBtn.querySelector('.sort-direction');
        if (direction) {
            if (previousSort === sortType) {
                // 같은 정렬을 다시 클릭한 경우 방향 토글
                const isAsc = direction.classList.contains('asc');
                direction.classList.toggle('asc', !isAsc);
                direction.textContent = isAsc ? '▼' : '▲';
                filterState.sort = isAsc ? sortType : sortType + '_asc';
            } else {
                // 다른 정렬로 변경한 경우 기본 내림차순
                direction.classList.remove('asc');
                direction.textContent = '▼';
            }
        }
    }

    console.log(`📊 정렬 변경: ${filterState.sort}`);

    // 첫 페이지로 이동
    window.inquiryModalState.currentPage = 1;
    applyAllFiltersAndRender();
};

// ─────────── 새로고침 및 필터 초기화 ───────────
window.refreshAndResetFilters = function() {
    console.log('🔄 필터 초기화 및 새로고침 시작');

    // 필터 상태 초기화
    filterState = {
        search: '',
        urgency: 'all',
        status: 'all',
        sort: 'latest'
    };

    // UI 초기화
    resetFilterUI();

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

    // 데이터 새로고침
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

// ─────────── UI 초기화 ───────────
function resetFilterUI() {
    // 검색 입력 초기화
    const searchInput = document.getElementById('inquiry-search');
    if (searchInput) {
        searchInput.value = '';
    }

    const clearBtn = document.getElementById('clear-search');
    if (clearBtn) {
        clearBtn.style.display = 'none';
    }

    // 토글 버튼 및 드롭다운 초기화
    filterState.urgency = 'all';
    filterState.status = 'all';
    updateUrgencyButtonState();
    updateStatusButtonState();
    const urgencySelect = document.getElementById('urgency-filter-select');
    if (urgencySelect) urgencySelect.value = 'all';
    const statusSelect = document.getElementById('status-filter-select');
    if (statusSelect) statusSelect.value = 'all';
    closeUrgencyDropdown();
    closeStatusDropdown();

    // 정렬 버튼 초기화
    document.querySelectorAll('.accordion-filter-sort').forEach(btn => {
        btn.classList.remove('active');
        const direction = btn.querySelector('.sort-direction');
        if (direction) {
            direction.textContent = '▼';
            direction.classList.remove('asc');
        }
    });

    const latestSortBtn = document.getElementById('sort-latest');
    if (latestSortBtn) {
        latestSortBtn.classList.add('active');
    }

    console.log('✅ 필터 UI 초기화 완료');
}

// ─────────── 아코디언 스타일 필터 적용 및 렌더링 ───────────
window.applyAllFiltersAndRender = function() {
    console.log('🎯 아코디언 스타일 필터 적용 및 렌더링 시작');

    try {
        // 🔧 원본 데이터가 있는지 확인
        if (!window.inquiryModalState.allInquiries || window.inquiryModalState.allInquiries.length === 0) {
            console.warn('⚠️ 원본 데이터가 없습니다.');
            showEmptyState();
            return;
        }

        // 필터링 실행
        const filteredInquiries = applyAccordionStyleFilters(window.inquiryModalState.allInquiries, filterState);
        console.log(`📊 필터링 결과: ${filteredInquiries.length}건 (원본: ${window.inquiryModalState.allInquiries.length}건)`);

        // 정렬 적용
        const sortedInquiries = applySorting(filteredInquiries, filterState.sort);

        // 상태 업데이트
        window.inquiryModalState.filteredInquiries = sortedInquiries;
        window.inquiryModalState.filteredItems = sortedInquiries.length;

        // 페이지네이션 적용 및 렌더링
        updatePaginationAndRender();

        console.log('✅ 아코디언 스타일 필터 적용 및 렌더링 완료');

    } catch (error) {
        console.error('❌ 필터 적용 오류:', error);
        hideInquiryLoading();
        showEmptyState();
    }
};

// ─────────── 아코디언 스타일 필터링 로직 ───────────
function applyAccordionStyleFilters(inquiries, filters) {
    if (!inquiries || inquiries.length === 0) return [];

    let filtered = [...inquiries];
    console.log(`🔄 필터링 시작: ${filtered.length}건`);

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

    // 긴급도 필터
    if (filters.urgency !== 'all') {
        console.log(`🚨 긴급도 필터: ${filters.urgency}`);
        if (filters.urgency === 'urgent') {
            filtered = filtered.filter(inquiry =>
                inquiry.is_urgent === true ||
                inquiry.is_urgent === 'true' ||
                inquiry.is_urgent === 1
            );
        } else if (filters.urgency === 'normal') {
            filtered = filtered.filter(inquiry =>
                !inquiry.is_urgent ||
                inquiry.is_urgent === false ||
                inquiry.is_urgent === 'false' ||
                inquiry.is_urgent === 0
            );
        }
        console.log(`🎯 긴급도 필터 결과: ${filtered.length}건`);
    }

    // 상태 필터
    if (filters.status !== 'all') {
        console.log(`📋 상태 필터: ${filters.status}`);
        if (filters.status === 'completed') {
            filtered = filtered.filter(inquiry =>
                inquiry.answer_status === '답변완료' ||
                (inquiry.answers && inquiry.answers.length > 0)
            );
        } else if (filters.status === 'pending') {
            filtered = filtered.filter(inquiry =>
                inquiry.answer_status !== '답변완료' &&
                (!inquiry.answers || inquiry.answers.length === 0)
            );
        }
        console.log(`🎯 상태 필터 결과: ${filtered.length}건`);
    }

    console.log(`✅ 최종 필터링 결과: ${filtered.length}건`);
    return filtered;
}

// ─────────── 레거시 호환성 함수 (기존 함수명 유지) ───────────
window.clearAllInquiryFilters = function() {
    console.log('🧹 레거시 호환성: clearAllInquiryFilters 호출됨');
    refreshAndResetFilters();
};

// ─────────── 필터 디버깅 함수 ───────────
window.debugAccordionFilters = function() {
    console.log('🔍 아코디언 스타일 필터 디버깅 정보:');

    console.log('현재 필터 상태:', filterState);
    console.log('전체 문의:', window.inquiryModalState.allInquiries?.length || 0);
    console.log('필터링된 문의:', window.inquiryModalState.filteredInquiries?.length || 0);

    if (window.inquiryModalState.allInquiries && window.inquiryModalState.allInquiries.length > 0) {
        console.log('📊 긴급도 분포:', {
            urgent: window.inquiryModalState.allInquiries.filter(inq => inq.is_urgent).length,
            normal: window.inquiryModalState.allInquiries.filter(inq => !inq.is_urgent).length
        });

        console.log('📊 상태 분포:', {
            completed: window.inquiryModalState.allInquiries.filter(inq =>
                inq.answer_status === '답변완료' || (inq.answers && inq.answers.length > 0)
            ).length,
            pending: window.inquiryModalState.allInquiries.filter(inq =>
                inq.answer_status !== '답변완료' && (!inq.answers || inq.answers.length === 0)
            ).length
        });
    }
};

// ─────────── 레거시 호환성 함수들 ───────────
window.debugFilters = function() {
    console.log('🔍 레거시 호환성: debugFilters 호출됨');
    debugAccordionFilters();
};

console.log('✅ 아코디언 스타일 필터링 시스템 로딩 완료');
"""
