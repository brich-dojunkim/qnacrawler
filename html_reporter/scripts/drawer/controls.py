# html_reporter/scripts/drawer/controls.py
"""
드로어 헤더 업데이트 및 컨트롤 기능
"""

def get_drawer_control_scripts():
    """드로어 컨트롤 관련 스크립트"""
    return """
// ─────────── 헤더 업데이트 ───────────
function updateDrawerHeader() {
    const categoryNameEl = document.getElementById('drawer-category-name');
    const inquiryCountEl = document.getElementById('drawer-inquiry-count');
    
    if (categoryNameEl) {
        categoryNameEl.textContent = currentCategory || '카테고리';
    }
    
    if (inquiryCountEl) {
        inquiryCountEl.textContent = `${filteredInquiryData.length}건`;
    }
}

// ─────────── 필터링 및 정렬 ───────────
function applyDrawerFilters() {
    let filtered = [...currentInquiryData];
    
    // 상태 필터
    const statusFilter = document.getElementById('drawer-status-filter')?.value;
    if (statusFilter && statusFilter !== 'all') {
        if (statusFilter === 'answered') {
            filtered = filtered.filter(item => item.answer_status === '답변완료');
        } else if (statusFilter === 'unanswered') {
            filtered = filtered.filter(item => item.answer_status === '미답변');
        }
    }
    
    // 검색어 필터
    const searchTerm = document.getElementById('drawer-search-input')?.value?.toLowerCase();
    if (searchTerm) {
        filtered = filtered.filter(item => 
            item.question_content.toLowerCase().includes(searchTerm) ||
            item.question_preview.toLowerCase().includes(searchTerm) ||
            item.seller.toLowerCase().includes(searchTerm)
        );
    }
    
    // 정렬
    const sortOption = document.getElementById('drawer-sort')?.value;
    if (sortOption) {
        switch(sortOption) {
            case 'latest':
                filtered.sort((a, b) => new Date(b.registration_date) - new Date(a.registration_date));
                break;
            case 'oldest':
                filtered.sort((a, b) => new Date(a.registration_date) - new Date(b.registration_date));
                break;
            case 'urgent':
                filtered.sort((a, b) => {
                    if (a.is_urgent === b.is_urgent) {
                        return new Date(b.registration_date) - new Date(a.registration_date);
                    }
                    return b.is_urgent - a.is_urgent;
                });
                break;
            case 'status':
                filtered.sort((a, b) => {
                    if (a.answer_status === b.answer_status) {
                        return new Date(b.registration_date) - new Date(a.registration_date);
                    }
                    return a.answer_status === '미답변' ? -1 : 1;
                });
                break;
        }
    }
    
    filteredInquiryData = filtered;
    updateDrawerHeader();
    renderInquiryList();
    
    console.log(`🔍 필터 적용 완료: ${filtered.length}건`);
}

// ─────────── 유틸리티 함수 ───────────
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

console.log('✅ 드로어 컨트롤 기능 로딩 완료');
"""