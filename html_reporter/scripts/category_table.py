# html_reporter/scripts/category_table.py (카테고리 검색 기능 제거)
"""카테고리 테이블 필터링 및 정렬 스크립트 - 카테고리 검색 기능 제거"""

def get_category_table_scripts():
    return """
// ═══════════════════════════════════════════════════════════
// 카테고리 테이블 필터링 및 정렬 스크립트 - 카테고리 검색 기능 제거
// ═══════════════════════════════════════════════════════════

let tableFilters = {
    team: '',
    journey: '',
    sort: '',
    sortOrder: ''
};

// ─────────── 새 모달 시스템 ───────────
function openCategoryModal(button) {
    const row = button.closest('.category-table-row');
    const categoryName = row.dataset.categoryName;
    const team = row.dataset.team;
    const journey = row.dataset.journey;
    const inquiries = row.dataset.inquiries;
    const urgentRate = row.dataset.urgent;
    
    console.log(`카테고리 모달 열기: ${categoryName}`);
    
    // 모달 HTML 생성
    const modalContent = `
        <div style="margin-bottom: 20px; padding: 16px; background: linear-gradient(135deg, #f8fafc, #e2e8f0); border-radius: 8px;">
            <h4 style="margin: 0 0 12px 0; color: #374151;">📊 ${categoryName} 상세 정보</h4>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 12px;">
                <div style="text-align: center;">
                    <div style="font-size: 1.5rem; font-weight: bold; color: #667eea;">${inquiries}</div>
                    <div style="font-size: 0.85rem; color: #6b7280;">총 문의</div>
                </div>
                <div style="text-align: center;">
                    <div style="font-size: 1.5rem; font-weight: bold; color: #ef4444;">${urgentRate}%</div>
                    <div style="font-size: 0.85rem; color: #6b7280;">긴급률</div>
                </div>
                <div style="text-align: center;">
                    <div style="font-size: 1rem; font-weight: bold; color: #f59e0b;">${team}</div>
                    <div style="font-size: 0.85rem; color: #6b7280;">담당팀</div>
                </div>
                <div style="text-align: center;">
                    <div style="font-size: 1rem; font-weight: bold; color: #10b981;">${journey}</div>
                    <div style="font-size: 0.85rem; color: #6b7280;">유저여정</div>
                </div>
            </div>
        </div>
        
        <div style="background: #f8fafc; padding: 16px; border-radius: 8px;">
            <h5 style="margin: 0 0 12px 0; color: #374151;">📝 문의 샘플</h5>
            <div style="background: white; padding: 12px; border-radius: 6px; border-left: 4px solid #667eea;">
                <div style="font-size: 0.9rem; color: #6b7280; margin-bottom: 8px;">
                    <strong>샘플 문의 내용:</strong>
                </div>
                <div style="color: #374151; line-height: 1.5;">
                    이 카테고리에 해당하는 실제 고객 문의 내용이 여기에 표시됩니다. 
                    현재는 샘플 데이터로 표시되고 있으며, 실제 구현 시에는 해당 카테고리의 
                    대표적인 문의 사례들이 표시될 예정입니다.
                </div>
                <div style="margin-top: 8px; font-size: 0.8rem; color: #9ca3af;">
                    등록일: 2024-01-15 | 상태: 답변완료
                </div>
            </div>
            <div style="background: white; padding: 12px; border-radius: 6px; border-left: 4px solid #f59e0b; margin-top: 8px;">
                <div style="font-size: 0.9rem; color: #6b7280; margin-bottom: 8px;">
                    <strong>긴급 문의 샘플:</strong>
                </div>
                <div style="color: #374151; line-height: 1.5;">
                    긴급하게 처리가 필요한 문의 사례입니다. 
                    이런 유형의 문의들이 전체 문의 중 ${urgentRate}%를 차지하고 있습니다.
                </div>
                <div style="margin-top: 8px; font-size: 0.8rem; color: #ef4444;">
                    등록일: 2024-01-16 | 상태: 처리중 | 🚨 긴급
                </div>
            </div>
        </div>
    `;
    
    createNewModal(`category-modal-${categoryName.replace(/[^a-zA-Z0-9]/g, '')}`, 
                   `📂 ${categoryName} 상세 보기`, 
                   modalContent);
}

function createNewModal(modalId, title, content) {
    // 기존 모달이 있다면 제거
    const existingModal = document.getElementById(modalId);
    if (existingModal) {
        existingModal.remove();
    }
    
    // 새 모달 생성
    const modal = document.createElement('div');
    modal.id = modalId;
    modal.className = 'new-modal-overlay';
    modal.innerHTML = `
        <div class="new-modal-content">
            <div class="new-modal-header">
                <h3 class="new-modal-title">${title}</h3>
                <button class="new-modal-close" onclick="closeNewModal('${modalId}')">&times;</button>
            </div>
            <div class="new-modal-body">
                ${content}
            </div>
        </div>
    `;
    
    // body에 추가
    document.body.appendChild(modal);
    
    // 모달 표시
    setTimeout(() => {
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
    }, 10);
}

function closeNewModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.remove('active');
        document.body.style.overflow = 'auto';
        setTimeout(() => {
            modal.remove();
        }, 300);
    }
}

// ─────────── 드롭다운 토글 함수들 (카테고리 검색 제거) ───────────
function toggleTeamFilter() {
    const btn = event.target.closest('.filter-icon-btn');
    const dropdown = document.getElementById('team-dropdown');
    
    // 다른 활성 드롭다운들 닫기
    closeOtherDropdowns('team');
    
    if (dropdown.classList.contains('hidden')) {
        dropdown.classList.remove('hidden');
        btn.classList.add('active');
    } else {
        dropdown.classList.add('hidden');
        btn.classList.remove('active');
        // 드롭다운을 닫을 때 필터 초기화
        const select = document.getElementById('team-filter-dropdown');
        if (select.value) {
            select.selectedIndex = 0;
            filterByTeam('');
        }
    }
}

function toggleJourneyFilter() {
    const btn = event.target.closest('.filter-icon-btn');
    const dropdown = document.getElementById('journey-dropdown');
    
    // 다른 활성 드롭다운들 닫기
    closeOtherDropdowns('journey');
    
    if (dropdown.classList.contains('hidden')) {
        dropdown.classList.remove('hidden');
        btn.classList.add('active');
    } else {
        dropdown.classList.add('hidden');
        btn.classList.remove('active');
        // 드롭다운을 닫을 때 필터 초기화
        const select = document.getElementById('journey-filter-dropdown');
        if (select.value) {
            select.selectedIndex = 0;
            filterByJourney('');
        }
    }
}

function closeOtherDropdowns(except) {
    const dropdowns = [
        { id: 'team-dropdown', btn: '[onclick="toggleTeamFilter()"]', reset: () => {
            document.getElementById('team-filter-dropdown').selectedIndex = 0;
            filterByTeam('');
        }},
        { id: 'journey-dropdown', btn: '[onclick="toggleJourneyFilter()"]', reset: () => {
            document.getElementById('journey-filter-dropdown').selectedIndex = 0;
            filterByJourney('');
        }}
    ];
    
    dropdowns.forEach(item => {
        const dropdownType = item.id.split('-')[0];
        if (dropdownType !== except) {
            const dropdown = document.getElementById(item.id);
            const btn = document.querySelector(item.btn);
            if (dropdown && !dropdown.classList.contains('hidden')) {
                dropdown.classList.add('hidden');
                if (btn) btn.classList.remove('active');
                item.reset();
            }
        }
    });
}

// ─────────── 필터링 함수들 (카테고리 검색 제거) ───────────
function filterByTeam(value) {
    tableFilters.team = value;
    applyTableFilters();
    
    // 필터 선택 즉시 드롭다운 닫기
    const dropdown = document.getElementById('team-dropdown');
    const btn = document.querySelector('[onclick="toggleTeamFilter()"]');
    if (dropdown) dropdown.classList.add('hidden');
    if (btn) btn.classList.remove('active');
}

function filterByJourney(value) {
    tableFilters.journey = value;
    applyTableFilters();
    
    // 필터 선택 즉시 드롭다운 닫기
    const dropdown = document.getElementById('journey-dropdown');
    const btn = document.querySelector('[onclick="toggleJourneyFilter()"]');
    if (dropdown) dropdown.classList.add('hidden');
    if (btn) btn.classList.remove('active');
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
    document.querySelectorAll('.sort-icon-btn').forEach(btn => {
        btn.classList.remove('active', 'asc', 'desc');
    });
    
    // 활성 버튼 스타일 적용
    activeBtn.classList.add('active', tableFilters.sortOrder);
}

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

// ─────────── 필터 초기화 (카테고리 검색 제거) ───────────
function clearAllTableFilters() {
    tableFilters = { team: '', journey: '', sort: '', sortOrder: '' };
    
    // 팀/여정 필터만 초기화
    document.querySelectorAll('.dropdown-filter-select').forEach(select => {
        select.selectedIndex = 0;
    });
    
    document.querySelectorAll('.dropdown-menu').forEach(dropdown => {
        dropdown.classList.add('hidden');
    });
    
    document.querySelectorAll('.filter-icon-btn, .sort-icon-btn').forEach(btn => {
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
"""