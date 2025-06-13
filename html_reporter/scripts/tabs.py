# html_reporter/scripts/tabs.py - 수정된 버전

def get_tab_scripts() -> str:
    return """
function toggleAnalysisView(){
    const view=document.querySelector('input[name="analysis-view"]:checked').value;
    
    // 모든 분석 뷰 숨기기
    document.querySelectorAll('.analysis-view').forEach(v=>{
        v.style.display='none'; 
        v.classList.remove('active');
    });
    
    // 컨트롤 버튼 전환
    const accordionControls = document.querySelector('.accordion-controls');
    const tableControls = document.querySelector('.table-controls');
    
    if (view === 'categories') {
        // 카테고리 테이블 뷰 활성화
        const target = document.getElementById('categories-table-view');
        if (target) {
            target.style.display = 'block';
            target.classList.add('active');
        }
        
        // 컨트롤 전환
        if (accordionControls) accordionControls.classList.add('hidden');
        if (tableControls) tableControls.classList.add('active');
        
        // 테이블 초기화
        setTimeout(() => {
            if (typeof initCategoryTable === 'function') {
                initCategoryTable();
            }
        }, 100);
        
    } else {
        // 아코디언 뷰 활성화 (teams 또는 journey)
        const target = document.getElementById(`${view}-accordion-view`);
        if (target) {
            target.style.display = 'block';
            target.classList.add('active');
        }
        
        // 컨트롤 전환
        if (accordionControls) accordionControls.classList.remove('hidden');
        if (tableControls) tableControls.classList.remove('active');
        
        // === 여정순서 버튼 표시/숨김 처리 ===
        const journeyOrderBtn = document.querySelector('.accordion-sort-btn.journey-only');
        if (journeyOrderBtn) {
            if (view === 'journey') {
                // 여정별 분석일 때만 여정순서 버튼 표시
                journeyOrderBtn.style.display = 'flex';
                console.log('여정순서 버튼 표시됨');
            } else {
                // 팀별 분석일 때는 여정순서 버튼 숨김
                journeyOrderBtn.style.display = 'none';
                console.log('여정순서 버튼 숨겨짐');
            }
        }
        
        // 아코디언 정렬 초기화 (뷰 전환시)
        if (typeof resetAccordionSort === 'function') {
            resetAccordionSort();
        }
        
        // 뷰 변경 이벤트 호출 (accordion.js에서 사용)
        if (typeof onViewChange === 'function') {
            onViewChange();
        }
    }
    
    console.log(`분석 뷰 전환: ${view}`);
}
"""