"""
카테고리 테이블 상태 관리
"""

def get_state_scripts():
    """상태 관리 관련 스크립트"""
    return """
// ─────────── 테이블 필터 상태 ───────────
let tableFilters = {
    team: '',
    journey: '',
    sort: '',
    sortOrder: ''
};

// ─────────── 필터 적용 메인 함수 (카테고리 검색 제거) ───────────
function applyTableFilters() {
    const rows = Array.from(document.querySelectorAll('.category-table-row'));
    let visibleCount = 0;

    // 필터링
    rows.forEach(row => {
        let show = true;

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

// ─────────── 상태 업데이트 (카테고리 검색 제거) ───────────
function updateTableFilterStatus(visible, total) {
    const statusElement = document.getElementById('table-filter-status');
    const countElement = document.getElementById('visible-categories-count');
    const clearBtn = document.querySelector('.clear-table-filters');
    
    if (countElement) {
        countElement.textContent = visible;
    }
    
    let statusText = '';
    let filterDescription = '';
    
    // 적용된 필터들 수집 (카테고리 검색 제외)
    const activeFilters = [];
    if (tableFilters.team) {
        activeFilters.push(`팀: ${tableFilters.team}`);
    }
    if (tableFilters.journey) {
        activeFilters.push(`여정: ${tableFilters.journey}`);
    }
    
    if (activeFilters.length > 0) {
        filterDescription = activeFilters.join(' | ');
        statusText = `📂 <strong>필터 적용</strong>: ${filterDescription} (${total}개 중 ${visible}개 표시)`;
        if (clearBtn) clearBtn.style.display = 'inline';
    } else {
        statusText = `📂 <strong>전체 카테고리</strong> 표시 중 (${visible}개)`;
        if (clearBtn) clearBtn.style.display = 'none';
    }
    
    if (statusElement) {
        statusElement.innerHTML = statusText + (clearBtn && clearBtn.style.display === 'inline' ? clearBtn.outerHTML : '');
    }
}

// ─────────── 기타 테이블 기능 ───────────
function exportTableData() {
    console.log('테이블 데이터 내보내기 실행');
    const visibleRows = document.querySelectorAll('.category-table-row:not(.hidden)');
    console.log(`내보낼 데이터: ${visibleRows.length}개 카테고리`);
    alert('필터된 카테고리 데이터를 CSV로 내보냅니다.');
}
"""