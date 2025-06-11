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
    document.querySelectorAll('.analysis-view').forEach(v=>{
        v.style.display='none'; v.classList.remove('active');
    });
    const target=document.getElementById(`${view}-accordion-view`);
    if(target){ target.style.display='block'; target.classList.add('active'); }
    
    console.log(`분석 뷰 전환: ${view}`);
}
"""