# html_reporter/scripts/bootstrap.py (개선된 초기화)
"""DOMContentLoaded 초기화 - 개선된 상세 분석 섹션 지원"""

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

    // 개선된 분석 뷰 토글 & 컨트롤
    if(document.querySelector('.detailed-analysis-section')){
        console.log('개선된 상세 분석 섹션 초기화');
        
        // 분석 뷰 토글 이벤트 리스너 추가
        document.querySelectorAll('input[name="analysis-view"]')
            .forEach(r=>r.addEventListener('change', toggleAnalysisView));
        
        // 기존 제어 버튼들 제거 (이제 통합 컨트롤 바에 있음)
        // 더 이상 개별 버튼을 동적으로 추가하지 않음
        console.log('통합 컨트롤 바 사용으로 개별 버튼 생성 생략');
    }
    
    // 레거시 분석 토글 섹션 지원 (하위 호환성)
    else if(document.querySelector('.analysis-toggle-section')){
        console.log('레거시 분석 토글 섹션 초기화');
        
        document.querySelectorAll('input[name="analysis-view"]')
            .forEach(r=>r.addEventListener('change', toggleAnalysisView));

        // 레거시 제어 버튼 삽입
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