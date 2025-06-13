"""
벌크 제어 기능 (전체 펼치기/접기)
"""

def get_bulk_control_scripts():
    """벌크 제어 스크립트"""
    return """
// ─────────── 전체 펼치기/접기 ───────────
function expandAllTeamAccordions() {
    console.log('팀별 전체 펼치기 실행');
    document.querySelectorAll('.team-accordion-item')
        .forEach(item => {
            const content = item.querySelector('.team-accordion-content');
            if (content && !item.classList.contains('expanded')) {
                const id = content.id.replace('content-','');
                toggleTeamAccordion(id);
            }
        });
}

function collapseAllTeamAccordions() {
    console.log('팀별 전체 접기 실행');
    document.querySelectorAll('.team-accordion-item')
        .forEach(item => {
            const content = item.querySelector('.team-accordion-content');
            if (content && item.classList.contains('expanded')) {
                const id = content.id.replace('content-','');
                toggleTeamAccordion(id);
            }
        });
}

function expandAllJourneyAccordions() {
    console.log('여정별 전체 펼치기 실행');
    document.querySelectorAll('.journey-accordion-item')
        .forEach(item => {
            const content = item.querySelector('.journey-accordion-content');
            if (content && !item.classList.contains('expanded')) {
                const id = content.id.replace('journey-content-','');
                toggleJourneyAccordion(id);
            }
        });
}

function collapseAllJourneyAccordions() {
    console.log('여정별 전체 접기 실행');
    document.querySelectorAll('.journey-accordion-item')
        .forEach(item => {
            const content = item.querySelector('.journey-accordion-content');
            if (content && item.classList.contains('expanded')) {
                const id = content.id.replace('journey-content-','');
                toggleJourneyAccordion(id);
            }
        });
}

// ─────────── 통합 전체 제어 ───────────
function expandAllAccordions() {
    const activeView = document.querySelector('.analysis-view.active');
    if (!activeView) return;
    
    const viewType = activeView.id.includes('teams') ? 'team' : 'journey';
    
    if (viewType === 'team') {
        expandAllTeamAccordions();
    } else {
        expandAllJourneyAccordions();
    }
}

function collapseAllAccordions() {
    const activeView = document.querySelector('.analysis-view.active');
    if (!activeView) return;
    
    const viewType = activeView.id.includes('teams') ? 'team' : 'journey';
    
    if (viewType === 'team') {
        collapseAllTeamAccordions();
    } else {
        collapseAllJourneyAccordions();
    }
}
"""