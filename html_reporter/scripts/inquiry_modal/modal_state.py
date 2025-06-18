# html_reporter/scripts/inquiry_modal/modal_state.py
"""
문의 모달 상태 관리 전용 모듈
"""

def get_modal_state_scripts():
    """모달 상태 관리 스크립트"""
    return """
// ─────────── 모달 상태 관리 시스템 ───────────
console.log('🗂 모달 상태 관리 시스템 로딩 중...');

// 전역 상태 관리
window.inquiryModalState = {
    isOpen: false,
    currentCategory: null,
    currentCategoryType: null,
    currentPage: 1,
    itemsPerPage: 20,
    totalItems: 0,
    filteredItems: 0,
    currentFilters: {
        search: '',
        team: '',
        urgency: '',
        status: '',
        sort: 'latest'
    },
    allInquiries: [],
    filteredInquiries: [],
    currentPageInquiries: []
};

// ─────────── 상태 초기화 ───────────
function resetModalState() {
    window.inquiryModalState = {
        isOpen: false,
        currentCategory: null,
        currentCategoryType: null,
        currentPage: 1,
        itemsPerPage: 20,
        totalItems: 0,
        filteredItems: 0,
        currentFilters: {
            search: '',
            team: '',
            urgency: '',
            status: '',
            sort: 'latest'
        },
        allInquiries: [],
        filteredInquiries: [],
        currentPageInquiries: []
    };
    
    const searchInput = document.getElementById('inquiry-search');
    if (searchInput) searchInput.value = '';
    
    const filters = ['team-filter', 'urgency-filter', 'status-filter'];
    filters.forEach(filterId => {
        const filter = document.getElementById(filterId);
        if (filter) filter.selectedIndex = 0;
    });
    
    const sortFilter = document.getElementById('sort-filter');
    if (sortFilter) sortFilter.value = 'latest';
}

// ─────────── 상태 업데이트 함수들 ───────────
function updateModalState(updates) {
    Object.assign(window.inquiryModalState, updates);
}

function updateFilters(filterUpdates) {
    Object.assign(window.inquiryModalState.currentFilters, filterUpdates);
}

function setCurrentCategory(categoryType, categoryName) {
    window.inquiryModalState.currentCategory = categoryName;
    window.inquiryModalState.currentCategoryType = categoryType;
}

function setInquiryData(allInquiries, filteredInquiries = null) {
    window.inquiryModalState.allInquiries = allInquiries;
    window.inquiryModalState.filteredInquiries = filteredInquiries || allInquiries;
    window.inquiryModalState.totalItems = allInquiries.length;
    window.inquiryModalState.filteredItems = window.inquiryModalState.filteredInquiries.length;
}

function setCurrentPage(page) {
    window.inquiryModalState.currentPage = page;
}

function setItemsPerPage(items) {
    window.inquiryModalState.itemsPerPage = items;
}

function getCurrentState() {
    return window.inquiryModalState;
}

// ─────────── 상태 검증 함수들 ───────────
function validateModalState() {
    const state = window.inquiryModalState;
    const errors = [];
    
    if (!Array.isArray(state.allInquiries)) {
        errors.push('allInquiries가 배열이 아닙니다');
    }
    
    if (!Array.isArray(state.filteredInquiries)) {
        errors.push('filteredInquiries가 배열이 아닙니다');
    }
    
    if (state.currentPage < 1) {
        errors.push('currentPage가 1보다 작습니다');
    }
    
    if (state.itemsPerPage < 1) {
        errors.push('itemsPerPage가 1보다 작습니다');
    }
    
    return errors;
}

function debugModalState() {
    console.log('🔍 모달 상태 디버깅:', {
        isOpen: window.inquiryModalState.isOpen,
        currentCategory: window.inquiryModalState.currentCategory,
        currentCategoryType: window.inquiryModalState.currentCategoryType,
        currentPage: window.inquiryModalState.currentPage,
        itemsPerPage: window.inquiryModalState.itemsPerPage,
        totalItems: window.inquiryModalState.totalItems,
        filteredItems: window.inquiryModalState.filteredItems,
        allInquiriesLength: window.inquiryModalState.allInquiries?.length || 0,
        filteredInquiriesLength: window.inquiryModalState.filteredInquiries?.length || 0,
        currentPageInquiriesLength: window.inquiryModalState.currentPageInquiries?.length || 0,
        filters: window.inquiryModalState.currentFilters
    });
}

console.log('✅ 모달 상태 관리 시스템 로딩 완료');
"""