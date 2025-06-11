"""
카테고리 세그먼트 필터 & 정렬 스크립트
"""

def get_filter_scripts() -> str:
    return """
// ─────────── 필터 초기화 ───────────
function initCategoryFilters() {
    const seg = document.getElementById('segment-select');
    if (seg) seg.addEventListener('change', applyFilters);
    document.querySelectorAll('input[name="sort-type"]')
        .forEach(r => r.addEventListener('change', applyFilters));
}

// ─────────── 필터 적용 ───────────
function applyFilters() {
    const segVal  = document.getElementById('segment-select').value;
    const sortVal = document.querySelector('input[name="sort-type"]:checked').value;
    const cont    = document.getElementById('categories-container');
    if (!cont) return;

    const all  = Array.from(cont.children);
    let visible= [];

    // ① 세그먼트 필터
    if (segVal === 'all') {
        visible = all;
        updateSegmentInfo('전체 카테고리', all.length);
    } else if (segVal.startsWith('team-')) {
        const team = segVal.replace('team-','');
        visible = all.filter(c => c.dataset.team === team);
        updateSegmentInfo(`${team} 팀`, visible.length);
    } else if (segVal.startsWith('journey-')) {
        const jny = segVal.replace('journey-','');
        visible = all.filter(c => c.dataset.journey === jny);
        updateSegmentInfo(`${jny} 여정`, visible.length);
    }

    // ② 정렬
    visible.sort((a,b) => applySortLogic(a,b,sortVal));

    // ③ DOM 반영
    all.forEach(c => { c.style.display = visible.includes(c) ? 'block':'none'; });
    visible.forEach(c => cont.appendChild(c));

    updateFilterFeedback(segVal, sortVal, visible.length);
}

function applySortLogic(a,b,type){
    switch(type){
        case 'volume': return (b.dataset.count|0) - (a.dataset.count|0);
        case 'urgent': return parseFloat(b.dataset.urgentRate||0) - parseFloat(a.dataset.urgentRate||0);
        case 'answer': return parseFloat(a.dataset.answerRate||0) - parseFloat(b.dataset.answerRate||0);
        default:       return 0;
    }
}

// ─────────── 보조 UI 업데이트 ───────────
function updateSegmentInfo(segText, count){
    const t = document.getElementById('current-segment-text');
    const n = document.getElementById('visible-count');
    if (t) t.textContent = segText;
    if (n) n.textContent = count;
}

function updateFilterFeedback(segVal, sortVal, count){
    const box=document.getElementById('categories-container');
    if(!box) return;

    box.classList.remove('filter-all','filter-team','filter-journey',
                         'filter-volume','filter-urgent','filter-answer');

    if(segVal==='all')          box.classList.add('filter-all');
    else if(segVal.startsWith('team-'))    box.classList.add('filter-team');
    else if(segVal.startsWith('journey-')) box.classList.add('filter-journey');

    box.classList.add(`filter-${sortVal}`);
    console.log(`필터 피드백: ${segVal} + ${sortVal} → ${count}개`);
}

// ─────────── 드롭다운 옵션 동적 생성 ───────────
function populateTeamOptions() {
    const sel = document.getElementById('segment-select');
    const cont= document.getElementById('categories-container');
    if (!sel || !cont) return;

    const optgrp = sel.querySelector('optgroup[label="팀별"]');
    optgrp.querySelectorAll('option').forEach(o=>o.remove());

    const teams = new Set([...cont.children].map(c=>c.dataset.team).filter(t=>t && t!=='기타'));
    [...teams].sort().forEach(t=>{
        const o=document.createElement('option');
        o.value=`team-${t}`; o.textContent=t; optgrp.appendChild(o);
    });
}
"""
