# html_reporter/scripts/bootstrap.py - 수정된 버전

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
        
        // === 초기 여정순서 버튼 상태 설정 ===
        const initialView = document.querySelector('input[name="analysis-view"]:checked');
        const journeyOrderBtn = document.querySelector('.accordion-sort-btn.journey-only');
        
        if (journeyOrderBtn && initialView) {
            const viewValue = initialView.value;
            if (viewValue === 'journey') {
                journeyOrderBtn.style.display = 'flex';
                console.log('초기 로딩: 여정순서 버튼 표시 (여정별 뷰)');
            } else {
                journeyOrderBtn.style.display = 'none';
                console.log('초기 로딩: 여정순서 버튼 숨김 (팀별 뷰)');
            }
        }
        
        console.log('분석 뷰 토글 이벤트 리스너 등록 완료');
    }
});
"""