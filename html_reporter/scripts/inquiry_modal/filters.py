# html_reporter/scripts/inquiry_modal/filters.py
"""
문의 모달 필터링 및 검색 스크립트 - 3-Way 탭 스위치 - 화살표 애니메이션 문제 해결
"""

def get_filters_scripts():
    """3-Way 탭 스위치가 적용된 필터링 및 검색 관련 스크립트 - 화살표 애니메이션 문제 해결"""
    return """
// ─────────── 3-Way 탭 스위치 필터링 시스템 ───────────
console.log('🔍 3-Way 탭 스위치 필터링 시스템 로딩 중...');

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
    setupTabSwitchEventListeners();
});

function setupTabSwitchEventListeners() {
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

// ─────────── 긴급도 탭 선택 ───────────
window.selectUrgencyTab = function(value) {
    console.log(`🚨 긴급도 탭 선택: ${value}`);
    
    // 이전 활성화된 탭 제거
    document.querySelectorAll('.urgency-tabs .bordered-tab-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    
    // 새로운 탭 활성화
    const selectedTab = document.querySelector(`.urgency-tabs .bordered-tab-btn[data-value="${value}"]`);
    if (selectedTab) {
        selectedTab.classList.add('active');
    }
    
    // 필터 상태 업데이트
    filterState.urgency = value;
    
    // 필터 적용
    applyAllFiltersAndRender();
};

// ─────────── 상태 탭 선택 ───────────
window.selectStatusTab = function(value) {
    console.log(`✅ 상태 탭 선택: ${value}`);
    
    // 이전 활성화된 탭 제거
    document.querySelectorAll('.status-tabs .bordered-tab-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    
    // 새로운 탭 활성화
    const selectedTab = document.querySelector(`.status-tabs .bordered-tab-btn[data-value="${value}"]`);
    if (selectedTab) {
        selectedTab.classList.add('active');
    }
    
    // 필터 상태 업데이트
    filterState.status = value;
    
    // 필터 적용
    applyAllFiltersAndRender();
};

// ─────────── 정렬 설정 (화살표 애니메이션 문제 해결) ───────────
window.setSortOrder = function(sortType) {
    console.log(`📊 정렬 버튼 클릭: ${sortType}`);
    
    const currentSortBtn = document.getElementById(`sort-${sortType}`);
    if (!currentSortBtn) {
        console.error(`❌ 정렬 버튼을 찾을 수 없습니다: sort-${sortType}`);
        return;
    }
    
    const direction = currentSortBtn.querySelector('.sort-direction');
    if (!direction) {
        console.error(`❌ 정렬 방향 요소를 찾을 수 없습니다`);
        return;
    }
    
    // 🔧 핵심 수정: CSS transform 충돌 방지
    direction.style.transform = 'none !important';
    direction.style.transition = 'none';
    
    const isCurrentlyActive = currentSortBtn.classList.contains('active');
    
    if (isCurrentlyActive) {
        // 같은 버튼 재클릭 - 방향만 토글
        const isCurrentlyAsc = direction.classList.contains('asc');
        
        if (isCurrentlyAsc) {
            // 오름차순 → 내림차순
            direction.classList.remove('asc');
            direction.textContent = '▼';
            filterState.sort = sortType;
            console.log(`${sortType}: 오름차순 → 내림차순, 화살표: ▼`);
        } else {
            // 내림차순 → 오름차순  
            direction.classList.add('asc');
            direction.textContent = '▲';
            filterState.sort = sortType + '_asc';
            console.log(`${sortType}: 내림차순 → 오름차순, 화살표: ▲`);
        }
    } else {
        // 다른 버튼 클릭 - 모든 버튼 초기화
        document.querySelectorAll('.accordion-filter-sort').forEach(btn => {
            btn.classList.remove('active');
            const btnDirection = btn.querySelector('.sort-direction');
            if (btnDirection) {
                btnDirection.textContent = '▼';
                btnDirection.classList.remove('asc');
                // 🔧 추가: transform 스타일 제거
                btnDirection.style.transform = 'none !important';
                btnDirection.style.transition = 'none';
            }
        });
        
        // 클릭된 버튼만 활성화
        currentSortBtn.classList.add('active');
        direction.classList.remove('asc');
        direction.textContent = '▼';
        filterState.sort = sortType;
        console.log(`${sortType}: 새 버튼 - 내림차순으로 시작, 화살표: ▼`);
    }
    
    // 🔧 추가: 변경 후 다시 한번 확인
    setTimeout(() => {
        console.log(`🔍 변경 후 확인: ${direction.textContent}, asc클래스: ${direction.classList.contains('asc')}`);
        
        // transform이 다시 적용되었다면 강제 제거
        if (direction.style.transform && direction.style.transform !== 'none') {
            direction.style.transform = 'none !important';
            console.log('⚠️ Transform 스타일이 다시 적용되어 제거했습니다');
        }
    }, 100);

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

    // 긴급도 탭 초기화 (전체 선택)
    document.querySelectorAll('.urgency-tabs .bordered-tab-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    const urgencyAllTab = document.querySelector('.urgency-tabs .bordered-tab-btn[data-value="all"]');
    if (urgencyAllTab) {
        urgencyAllTab.classList.add('active');
    }

    // 상태 탭 초기화 (전체 선택)
    document.querySelectorAll('.status-tabs .bordered-tab-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    const statusAllTab = document.querySelector('.status-tabs .bordered-tab-btn[data-value="all"]');
    if (statusAllTab) {
        statusAllTab.classList.add('active');
    }

    // 정렬 버튼 초기화
    document.querySelectorAll('.accordion-filter-sort').forEach(btn => {
        btn.classList.remove('active');
        const direction = btn.querySelector('.sort-direction');
        if (direction) {
            direction.textContent = '▼';
            direction.classList.remove('asc');
            // 🔧 추가: transform 스타일 제거
            direction.style.transform = 'none !important';
            direction.style.transition = 'none';
        }
    });

    const latestSortBtn = document.getElementById('sort-latest');
    if (latestSortBtn) {
        latestSortBtn.classList.add('active');
    }

    console.log('✅ 필터 UI 초기화 완료');
}

// ─────────── 3-Way 탭 스위치 필터 적용 및 렌더링 ───────────
window.applyAllFiltersAndRender = function() {
    console.log('🎯 3-Way 탭 스위치 필터 적용 및 렌더링 시작');

    try {
        // 원본 데이터가 있는지 확인
        if (!window.inquiryModalState.allInquiries || window.inquiryModalState.allInquiries.length === 0) {
            console.warn('⚠️ 원본 데이터가 없습니다.');
            showEmptyState();
            return;
        }

        // 필터링 실행
        const filteredInquiries = applyTabSwitchFilters(window.inquiryModalState.allInquiries, filterState);
        console.log(`📊 필터링 결과: ${filteredInquiries.length}건 (원본: ${window.inquiryModalState.allInquiries.length}건)`);

        // 정렬 적용
        const sortedInquiries = applySorting(filteredInquiries, filterState.sort);

        // 상태 업데이트
        window.inquiryModalState.filteredInquiries = sortedInquiries;
        window.inquiryModalState.filteredItems = sortedInquiries.length;

        // 페이지네이션 적용 및 렌더링
        updatePaginationAndRender();

        console.log('✅ 3-Way 탭 스위치 필터 적용 및 렌더링 완료');

    } catch (error) {
        console.error('❌ 필터 적용 오류:', error);
        hideInquiryLoading();
        showEmptyState();
    }
};

// ─────────── 3-Way 탭 스위치 필터링 로직 ───────────
function applyTabSwitchFilters(inquiries, filters) {
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
window.debugTabSwitchFilters = function() {
    console.log('🔍 3-Way 탭 스위치 필터 디버깅 정보:');

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

    // 현재 활성화된 탭 상태 확인
    const activeUrgencyTab = document.querySelector('.urgency-tabs .bordered-tab-btn.active');
    const activeStatusTab = document.querySelector('.status-tabs .bordered-tab-btn.active');
    
    console.log('📊 UI 상태:', {
        activeUrgencyTab: activeUrgencyTab?.dataset?.value || 'none',
        activeStatusTab: activeStatusTab?.dataset?.value || 'none'
    });
};

// ─────────── 레거시 호환성 함수들 ───────────
window.debugFilters = function() {
    console.log('🔍 레거시 호환성: debugFilters 호출됨');
    debugTabSwitchFilters();
};

// ─────────── 탭 상태 동기화 함수 ───────────
function syncTabStates() {
    // 긴급도 탭 동기화
    document.querySelectorAll('.urgency-tabs .bordered-tab-btn').forEach(btn => {
        btn.classList.remove('active');
        if (btn.dataset.value === filterState.urgency) {
            btn.classList.add('active');
        }
    });

    // 상태 탭 동기화
    document.querySelectorAll('.status-tabs .bordered-tab-btn').forEach(btn => {
        btn.classList.remove('active');
        if (btn.dataset.value === filterState.status) {
            btn.classList.add('active');
        }
    });
}

// ─────────── 화살표 애니메이션 문제 해결 초기화 ───────────
function fixArrowAnimationIssues() {
    console.log('🔧 화살표 애니메이션 문제 해결 중...');
    
    // 모든 .sort-direction 요소에서 transform 관련 스타일 제거
    document.querySelectorAll('.sort-direction').forEach(arrow => {
        arrow.style.transform = 'none !important';
        arrow.style.transition = 'none !important';
        
        // CSS 클래스 기반 transform도 제거
        arrow.classList.remove('asc', 'desc');
        
        // 기본 화살표로 설정
        if (!arrow.textContent || arrow.textContent.trim() === '') {
            arrow.textContent = '▼';
        }
    });
    
    // CSS 스타일 동적 추가로 강제 덮어쓰기
    const style = document.createElement('style');
    style.id = 'arrow-fix-styles';
    style.textContent = `
        /* 화살표 애니메이션 문제 해결 */
        .sort-direction {
            transform: none !important;
            transition: none !important;
        }
        
        .sort-direction.asc {
            transform: none !important;
        }
        
        .sort-direction.desc {
            transform: none !important;
        }
        
        /* 호버 효과에서도 transform 제거 */
        .accordion-filter-sort:hover .sort-direction {
            transform: none !important;
        }
        
        .accordion-filter-sort.active .sort-direction {
            transform: none !important;
        }
    `;
    
    // 기존 스타일이 있으면 제거하고 새로 추가
    const existingStyle = document.getElementById('arrow-fix-styles');
    if (existingStyle) {
        existingStyle.remove();
    }
    document.head.appendChild(style);
    
    console.log('✅ 화살표 애니메이션 문제 해결 완료');
}

// ─────────── 초기화 시 탭 상태 설정 및 화살표 문제 해결 ───────────
setTimeout(() => {
    // 기존 탭 상태 동기화
    syncTabStates();
    
    // 🔧 새로 추가: 화살표 문제 해결
    fixArrowAnimationIssues();
    
    console.log('🎯 3-Way 탭 스위치 초기 상태 설정 완료');
}, 100);

console.log('✅ 3-Way 탭 스위치 필터링 시스템 로딩 완료');
"""