"""
카테고리 테이블 정렬 시스템
"""

def get_sorting_scripts():
    """정렬 관련 스크립트"""
    return """
// ─────────── 정렬 함수들 ───────────
function sortByInquiries() {
    const btn = document.getElementById('inquiries-sort');
    if (tableFilters.sort === 'inquiries') {
        tableFilters.sortOrder = tableFilters.sortOrder === 'asc' ? 'desc' : 'asc';
    } else {
        tableFilters.sort = 'inquiries';
        tableFilters.sortOrder = 'desc';
    }
    
    updateSortButtons(btn);
    applyTableFilters();
}

function sortByUrgent() {
    const btn = document.getElementById('urgent-sort');
    if (tableFilters.sort === 'urgent') {
        tableFilters.sortOrder = tableFilters.sortOrder === 'asc' ? 'desc' : 'asc';
    } else {
        tableFilters.sort = 'urgent';
        tableFilters.sortOrder = 'desc';
    }
    
    updateSortButtons(btn);
    applyTableFilters();
}

function updateSortButtons(activeBtn) {
    // 모든 정렬 버튼 초기화
    document.querySelectorAll('.sort-icon-btn').forEach(btn => {
        btn.classList.remove('active', 'asc', 'desc');
    });
    
    // 활성 버튼 스타일 적용
    activeBtn.classList.add('active', tableFilters.sortOrder);
}

// ─────────── 정렬 실행 ───────────
function sortTableRows(rows) {
    const visibleRows = rows.filter(row => !row.classList.contains('hidden'));
    const container = document.querySelector('.category-table-body');

    visibleRows.sort((a, b) => {
        let aVal, bVal;
        
        if (tableFilters.sort === 'inquiries') {
            aVal = parseInt(a.dataset.inquiries || '0');
            bVal = parseInt(b.dataset.inquiries || '0');
        } else if (tableFilters.sort === 'urgent') {
            aVal = parseFloat(a.dataset.urgent || '0');
            bVal = parseFloat(b.dataset.urgent || '0');
        }

        if (tableFilters.sortOrder === 'asc') {
            return aVal - bVal;
        } else {
            return bVal - aVal;
        }
    });

    // DOM 재배치
    visibleRows.forEach(row => container.appendChild(row));
}
"""