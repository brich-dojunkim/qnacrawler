# html_reporter/scripts/bootstrap.py (탭 제거된 초기화)
"""DOMContentLoaded 초기화 - 탭 제거된 버전"""

def get_bootstrap_scripts() -> str:
    return """
document.addEventListener('DOMContentLoaded',()=>{
    console.log('VoC 리포터 로드 완료');

    // 카테고리 필터 초기화
    if(document.getElementById('categories-table-view')){
        setTimeout(()=>{ populateTeamOptions(); initCategoryFilters(); applyFilters(); },100);
    }

    // 상세 분석 섹션 초기화
    if(document.querySelector('.detailed-analysis-section')){
        console.log('상세 분석 섹션 초기화');
        
        // 분석 뷰 토글 이벤트 리스너 추가
        document.querySelectorAll('input[name="analysis-view"]')
            .forEach(r=>r.addEventListener('change', toggleAnalysisView));
        
        console.log('분석 뷰 토글 이벤트 리스너 등록 완료');
    }
});
"""