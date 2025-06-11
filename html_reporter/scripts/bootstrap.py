"""
DOMContentLoaded 초기화 – 옵션 생성‧필터‧아코디언 제어 버튼 세팅
"""

def get_bootstrap_scripts() -> str:
    return """
document.addEventListener('DOMContentLoaded',()=>{
    console.log('VoC 리포터 로드 완료');

    // 첫 탭 활성화
    const firstTab=document.querySelector('.tab-content');
    const firstBtn=document.querySelector('.tab-btn');
    if(firstTab&&firstBtn){ firstTab.classList.add('active'); firstBtn.classList.add('active'); }

    // 카테고리 필터
    if(document.getElementById('categories')){
        setTimeout(()=>{ populateTeamOptions(); initCategoryFilters(); applyFilters(); },100);
    }

    // 분석 뷰 토글 & 제어 버튼
    if(document.querySelector('.analysis-toggle-section')){
        document.querySelectorAll('input[name="analysis-view"]')
            .forEach(r=>r.addEventListener('change', toggleAnalysisView));

        // 제어 버튼 삽입
        ['teams','journey'].forEach(type=>{
            const v=document.getElementById(`${type}-accordion-view`);
            if(!v) return;
            const wrap=document.createElement('div');
            wrap.className=`accordion-controls ${type}-controls`;
            wrap.style.cssText='margin-bottom:16px;text-align:right;gap:8px;display:flex;justify-content:flex-end;';
            wrap.innerHTML = type==='teams'
                ? `<button onclick="expandAllTeamAccordions()">팀별 전체 펼치기</button>
                   <button onclick="collapseAllTeamAccordions()">팀별 전체 접기</button>`
                : `<button onclick="expandAllJourneyAccordions()">여정별 전체 펼치기</button>
                   <button onclick="collapseAllJourneyAccordions()">여정별 전체 접기</button>`;
            v.insertBefore(wrap, v.firstChild);
        });
    }
});
"""
