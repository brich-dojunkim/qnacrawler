"""
팀별·여정별 아코디언 및 전체 제어 스크립트
"""

def get_accordion_scripts() -> str:
    return """
// ─────────── 팀별 아코디언 ───────────
function toggleTeamAccordion(teamId) {
    const content = document.getElementById(`content-${teamId}`);
    const item    = content.closest('.team-accordion-item');

    if (content.style.display === 'none' || !content.style.display) {
        openAccordion(content, item);
    } else {
        closeAccordion(content, item);
    }
}

// ─────────── 여정별 아코디언 ───────────
function toggleJourneyAccordion(journeyId) {
    const content = document.getElementById(`journey-content-${journeyId}`);
    const item    = content.closest('.journey-accordion-item');

    if (content.style.display === 'none' || !content.style.display) {
        openAccordion(content, item);
    } else {
        closeAccordion(content, item);
    }
}

// ─────────── 공통 열기/닫기 로직 ───────────
function openAccordion(content, item) {
    content.style.display   = 'block';
    content.style.height    = '0px';
    content.style.overflow  = 'hidden';
    content.style.transition= 'height 0.3s ease';
    item.classList.add('expanded');

    const h = content.scrollHeight;
    requestAnimationFrame(() => { content.style.height = h + 'px'; });

    setTimeout(() => {
        content.style.height = 'auto';
        content.style.overflow = 'visible';
    }, 300);
}

function closeAccordion(content, item) {
    content.style.height    = content.scrollHeight + 'px';
    content.style.overflow  = 'hidden';
    content.style.transition= 'height 0.3s ease';

    requestAnimationFrame(() => { content.style.height = '0px'; });

    setTimeout(() => {
        content.style.display   = 'none';
        content.style.height    = '';
        content.style.overflow  = '';
        content.style.transition= '';
        item.classList.remove('expanded');
    }, 300);
}

// ─────────── 전체 펼치기/접기 (개선된 버전) ───────────
function expandAllTeamAccordions() {
    console.log('팀별 전체 펼치기 실행');
    document.querySelectorAll('.team-accordion-item')
        .forEach(item => {
            const content = item.querySelector('.team-accordion-content');
            if (content && !item.classList.contains('expanded')) {
                const id = content.id.replace('content-','');
                console.log(`팀 펼치기: ${id}`);
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
                console.log(`팀 접기: ${id}`);
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
                console.log(`여정 펼치기: ${id}`);
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
                console.log(`여정 접기: ${id}`);
                toggleJourneyAccordion(id);
            }
        });
}

// ─────────── 통합 전체 제어 (새로 추가) ───────────
function expandAllAccordions() {
    console.log('통합 전체 펼치기 실행');
    const activeView = document.querySelector('.analysis-view.active');
    if (!activeView) {
        console.log('활성 뷰를 찾을 수 없음');
        return;
    }
    
    const viewType = activeView.id.includes('teams') ? 'team' : 'journey';
    console.log(`현재 뷰 타입: ${viewType}`);
    
    if (viewType === 'team') {
        expandAllTeamAccordions();
    } else {
        expandAllJourneyAccordions();
    }
}

function collapseAllAccordions() {
    console.log('통합 전체 접기 실행');
    const activeView = document.querySelector('.analysis-view.active');
    if (!activeView) {
        console.log('활성 뷰를 찾을 수 없음');
        return;
    }
    
    const viewType = activeView.id.includes('teams') ? 'team' : 'journey';
    console.log(`현재 뷰 타입: ${viewType}`);
    
    if (viewType === 'team') {
        collapseAllTeamAccordions();
    } else {
        collapseAllJourneyAccordions();
    }
}
"""