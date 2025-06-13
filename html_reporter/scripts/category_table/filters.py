"""
카테고리 테이블 필터링 시스템
"""

def get_filter_scripts():
    """필터링 관련 스크립트"""
    return """
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
"""