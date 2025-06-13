# html_reporter/scripts/drawer/events.py
"""
드로어 이벤트 처리 및 초기화
"""

def get_drawer_event_scripts():
    """드로어 이벤트 처리 관련 스크립트"""
    return """
// ─────────── DOM 로딩 완료 후 초기화 ───────────
document.addEventListener('DOMContentLoaded', function() {
    console.log('🎯 드로어 이벤트 리스너 등록 중...');
    
    initializeDrawerEventListeners();
    loadSearchHistory();
    
    console.log('✅ 드로어 이벤트 리스너 등록 완료');
});

function initializeDrawerEventListeners() {
    // 드로어 닫기 버튼
    const closeBtn = document.getElementById('drawer-close');
    if (closeBtn) {
        closeBtn.addEventListener('click', closeInquiryDrawer);
        console.log('📌 드로어 닫기 버튼 이벤트 등록');
    }
    
    // 오버레이 클릭으로 닫기
    const overlay = document.getElementById('drawer-overlay');
    if (overlay) {
        overlay.addEventListener('click', closeInquiryDrawer);
        console.log('📌 오버레이 클릭 이벤트 등록');
    }
    
    // 뒤로가기 버튼
    const backBtn = document.getElementById('back-to-list');
    if (backBtn) {
        backBtn.addEventListener('click', showInquiryList);
        console.log('📌 뒤로가기 버튼 이벤트 등록');
    }
    
    // 정렬 및 필터 변경
    const sortSelect = document.getElementById('drawer-sort');
    if (sortSelect) {
        sortSelect.addEventListener('change', handleSortChange);
        console.log('📌 정렬 셀렉트 이벤트 등록');
    }
    
    const statusSelect = document.getElementById('drawer-status-filter');
    if (statusSelect) {
        statusSelect.addEventListener('change', handleStatusFilterChange);
        console.log('📌 상태 필터 셀렉트 이벤트 등록');
    }
    
    // 검색 입력
    const searchInput = document.getElementById('drawer-search-input');
    if (searchInput) {
        // 검색어 입력 (디바운스 적용)
        const debouncedSearch = debounce(handleSearchInput, 300);
        searchInput.addEventListener('input', debouncedSearch);
        
        // 키보드 단축키
        searchInput.addEventListener('keydown', handleSearchKeyDown);
        
        console.log('📌 검색 입력 이벤트 등록 (디바운스 300ms)');
    }
    
    // 검색어 지우기 버튼
    const searchClearBtn = document.getElementById('search-clear');
    if (searchClearBtn) {
        searchClearBtn.addEventListener('click', clearSearchInput);
        console.log('📌 검색어 지우기 버튼 이벤트 등록');
    }
    
    // 키보드 단축키 (전역)
    registerGlobalKeyboardShortcuts();
}

// ─────────── 전역 키보드 단축키 ───────────
function registerGlobalKeyboardShortcuts() {
    document.addEventListener('keydown', function(e) {
        // ESC 키 처리
        if (e.key === 'Escape') {
            const drawer = document.getElementById('inquiry-drawer');
            if (drawer && drawer.classList.contains('open')) {
                const detailView = document.getElementById('inquiry-detail-view');
                if (detailView && detailView.classList.contains('active')) {
                    // 상세보기에서 목록으로
                    showInquiryList();
                } else {
                    // 드로어 닫기
                    closeInquiryDrawer();
                }
                e.preventDefault();
            }
        }
        
        // Ctrl/Cmd + K: 검색창 포커스
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
            const drawer = document.getElementById('inquiry-drawer');
            if (drawer && drawer.classList.contains('open')) {
                const searchInput = document.getElementById('drawer-search-input');
                if (searchInput) {
                    searchInput.focus();
                    searchInput.select();
                    e.preventDefault();
                }
            }
        }
        
        // Ctrl/Cmd + Enter: 첫 번째 문의 상세보기
        if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
            const drawer = document.getElementById('inquiry-drawer');
            if (drawer && drawer.classList.contains('open')) {
                const firstInquiry = document.querySelector('.inquiry-item');
                if (firstInquiry) {
                    const inquiryId = firstInquiry.dataset.inquiryId;
                    if (inquiryId) {
                        viewInquiryDetail(inquiryId);
                        e.preventDefault();
                    }
                }
            }
        }
    });
    
    console.log('📌 전역 키보드 단축키 등록 완료');
    console.log('   - ESC: 드로어 닫기 / 상세보기 → 목록');
    console.log('   - Ctrl/Cmd + K: 검색창 포커스');
    console.log('   - Ctrl/Cmd + Enter: 첫 번째 문의 상세보기');
}

// ─────────── 창 크기 변경 대응 ───────────
window.addEventListener('resize', function() {
    // 모바일에서 드로어가 열려있을 때 화면 회전 대응
    const drawer = document.getElementById('inquiry-drawer');
    if (drawer && drawer.classList.contains('open')) {
        // 드로어 레이아웃 재조정 (필요시)
        console.log('📱 화면 크기 변경 감지 - 드로어 레이아웃 확인');
    }
});

// ─────────── 드로어 상태 변경 이벤트 ───────────
function onDrawerStateChange(isOpen) {
    console.log(`🔄 드로어 상태 변경: ${isOpen ? '열림' : '닫힘'}`);
    
    // 드로어 열림/닫힘에 따른 추가 처리
    if (isOpen) {
        // 드로어가 열렸을 때
        document.body.classList.add('drawer-open');
        
        // 검색창 포커스 (지연 실행)
        setTimeout(() => {
            const searchInput = document.getElementById('drawer-search-input');
            if (searchInput) {
                searchInput.focus();
            }
        }, 300);
        
    } else {
        // 드로어가 닫혔을 때
        document.body.classList.remove('drawer-open');
        
        // 검색 상태 초기화
        const searchInput = document.getElementById('drawer-search-input');
        if (searchInput) {
            searchInput.value = '';
        }
        
        const searchClearBtn = document.getElementById('search-clear');
        if (searchClearBtn) {
            searchClearBtn.classList.add('hidden');
        }
    }
    
    // 커스텀 이벤트 발송 (다른 컴포넌트에서 수신 가능)
    const event = new CustomEvent('drawerStateChanged', {
        detail: { isOpen: isOpen }
    });
    document.dispatchEvent(event);
}

// ─────────── 에러 처리 ───────────
window.addEventListener('error', function(e) {
    // 드로어 관련 스크립트 에러 처리
    if (e.filename && e.filename.includes('drawer')) {
        console.error('❌ 드로어 스크립트 에러:', e.error);
        
        // 에러 발생시 드로어 상태 안전하게 초기화
        try {
            closeInquiryDrawer();
        } catch (resetError) {
            console.error('❌ 드로어 초기화 중 에러:', resetError);
        }
    }
});

// ─────────── 디버깅 정보 ───────────
function printDrawerDebugInfo() {
    console.log('🔍 드로어 디버깅 정보:');
    console.log(`  - 현재 카테고리: ${currentCategory}`);
    console.log(`  - 전체 문의: ${currentInquiryData.length}건`);
    console.log(`  - 필터링된 문의: ${filteredInquiryData.length}건`);
    console.log(`  - 현재 상세보기: ${currentInquiryDetail ? currentInquiryDetail.inquiry_id : '없음'}`);
    console.log(`  - 검색 기록: ${searchHistory.length}개`);
    
    const drawer = document.getElementById('inquiry-drawer');
    console.log(`  - 드로어 상태: ${drawer ? (drawer.classList.contains('open') ? '열림' : '닫힘') : '없음'}`);
}

// 전역 함수로 등록 (디버깅용)
window.printDrawerDebugInfo = printDrawerDebugInfo;

// ─────────── 초기화 완료 ───────────
console.log('✅ 드로어 이벤트 시스템 로딩 완료');
console.log('📋 사용 가능한 디버깅 함수:');
console.log('  - printDrawerDebugInfo(): 현재 상태 출력');
"""