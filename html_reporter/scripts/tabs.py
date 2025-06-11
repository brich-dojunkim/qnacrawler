# html_reporter/scripts/tabs.py (개선된 기능 추가)
"""탭 전환 & 분석 뷰 토글 - 개선된 컨트롤 기능"""

def get_tab_scripts() -> str:
    return """
function switchTab(name){
    document.querySelectorAll('.tab-content').forEach(t=>t.classList.remove('active'));
    document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));
    document.getElementById(name).classList.add('active');
    event.target.classList.add('active');
}

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
    }
    
    console.log(`분석 뷰 전환: ${view}`);
}
"""