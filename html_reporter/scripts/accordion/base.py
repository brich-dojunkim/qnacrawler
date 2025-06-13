"""
기본 아코디언 토글 기능
"""

def get_accordion_base_scripts():
    """기본 아코디언 열기/닫기 스크립트"""
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
"""