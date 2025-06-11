# html_reporter/scripts/category_table.py (새 파일)
"""카테고리 테이블 필터링 및 정렬 스크립트"""

def get_category_table_scripts():
    return """
// ═══════════════════════════════════════════════════════════
// 카테고리 테이블 필터링 및 정렬 스크립트
// ═══════════════════════════════════════════════════════════

let tableFilters = {
    category: '',
    team: '',
    journey: '',
    sort: '',
    sortOrder: ''
};

// ─────────── 필터링 함수들 ───────────
function filterByCategory(value) {
    tableFilters.category = value.toLowerCase();
    applyTableFilters();
}

function filterByTeam(value) {
    tableFilters.team = value;
    applyTableFilters();
}

function filterByJourney(value) {
    tableFilters.journey = value;
    applyTableFilters();
}

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
    document.querySelectorAll('.sort-button').forEach(btn => {
        btn.classList.remove('active', 'asc', 'desc');
    });
    
    // 활성 버튼 스타일 적용
    activeBtn.classList.add('active', tableFilters.sortOrder);
}

// ─────────── 필터 적용 메인 함수 ───────────
function applyTableFilters() {
    const rows = Array.from(document.querySelectorAll('.category-table-row'));
    let visibleCount = 0;

    // 필터링
    rows.forEach(row => {
        let show = true;

        // 카테고리명 검색
        if (tableFilters.category) {
            const categoryName = row.dataset.category || '';
            if (!categoryName.includes(tableFilters.category)) {
                show = false;
            }
        }

        // 팀 필터
        if (tableFilters.team) {
            const team = row.dataset.team;
            if (team !== tableFilters.team) {
                show = false;
            }
        }

        // 여정 필터
        if (tableFilters.journey) {
            const journey = row.dataset.journey;
            if (journey !== tableFilters.journey) {
                show = false;
            }
        }

        if (show) {
            row.classList.remove('hidden');
            visibleCount++;
        } else {
            row.classList.add('hidden');
        }
    });

    // 정렬
    if (tableFilters.sort) {
        sortTableRows(rows);
    }

    updateTableFilterStatus(visibleCount, rows.length);
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

// ─────────── 상태 업데이트 ───────────
function updateTableFilterStatus(visible, total) {
    const statusElement = document.getElementById('table-filter-status');
    const countElement = document.getElementById('visible-categories-count');
    const clearBtn = document.querySelector('.clear-table-filters');
    
    if (countElement) {
        countElement.textContent = visible;
    }
    
    let statusText = '';
    
    if (tableFilters.category || tableFilters.team || tableFilters.journey) {
        statusText = `📂 <strong>필터 적용됨</strong> (${total}개 중 ${visible}개 표시)`;
        if (clearBtn) clearBtn.style.display = 'inline';
    } else {
        statusText = `📂 <strong>전체 카테고리</strong> 표시 중 (${visible}개)`;
        if (clearBtn) clearBtn.style.display = 'none';
    }
    
    if (statusElement) {
        statusElement.innerHTML = statusText + (clearBtn && clearBtn.style.display === 'inline' ? clearBtn.outerHTML : '');
    }
}

// ─────────── 필터 초기화 ───────────
function clearAllTableFilters() {
    tableFilters = { category: '', team: '', journey: '', sort: '', sortOrder: '' };
    
    // 모든 입력 초기화
    const categoryInput = document.querySelector('.filter-input');
    if (categoryInput) categoryInput.value = '';
    
    document.querySelectorAll('.filter-dropdown').forEach(select => {
        select.selectedIndex = 0;
    });
    
    document.querySelectorAll('.sort-button').forEach(btn => {
        btn.classList.remove('active', 'asc', 'desc');
    });
    
    applyTableFilters();
}

function resetTableFilters() {
    clearAllTableFilters();
}

// ─────────── 기타 테이블 기능 ───────────
function exportTableData() {
    console.log('테이블 데이터 내보내기 실행');
    const visibleRows = document.querySelectorAll('.category-table-row:not(.hidden)');
    console.log(`내보낼 데이터: ${visibleRows.length}개 카테고리`);
    alert('필터된 카테고리 데이터를 CSV로 내보냅니다.');
}

function toggleSelectAll() {
    const btn = document.getElementById('select-all-text');
    if (!btn) return;
    
    if (btn.textContent === '☐') {
        btn.textContent = '☑';
        console.log('전체 카테고리 선택');
    } else {
        btn.textContent = '☐';
        console.log('전체 카테고리 선택 해제');
    }
}

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
"""