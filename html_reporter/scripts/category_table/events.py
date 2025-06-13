"""
카테고리 테이블 이벤트 처리 및 초기화
"""

def get_event_scripts():
    """이벤트 처리 관련 스크립트"""
    return """
// ─────────── 외부 클릭으로 드롭다운 닫기 ───────────
document.addEventListener('click', function(event) {
    // 드롭다운 관련 요소가 아닌 곳을 클릭했을 때 모든 드롭다운 닫기
    if (!event.target.closest('.filter-dropdown-wrapper')) {
        closeOtherDropdowns('none');
    }
});

// ─────────── ESC 키로 모달 닫기 ───────────
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        const activeModal = document.querySelector('.new-modal-overlay.active');
        if (activeModal) {
            closeNewModal(activeModal.id);
        }
    }
});

// ─────────── 초기화 ───────────
function initCategoryTable() {
    console.log('카테고리 테이블 초기화');
    
    // 초기 필터 상태 설정
    const allRows = document.querySelectorAll('.category-table-row');
    updateTableFilterStatus(allRows.length, allRows.length);
    
    // 초기 정렬 (문의량 내림차순)
    if (allRows.length > 0) {
        tableFilters.sort = 'inquiries';
        tableFilters.sortOrder = 'desc';
        
        const inquiriesBtn = document.getElementById('inquiries-sort');
        if (inquiriesBtn) {
            updateSortButtons(inquiriesBtn);
            sortTableRows(Array.from(allRows));
        }
    }
}

console.log('✅ 카테고리 테이블 시스템 로딩 완료');
"""