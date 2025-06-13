"""
이벤트 처리 및 초기화
"""

def get_event_scripts():
    """이벤트 처리 스크립트"""
    return """
// 뷰 변경시 호출
window.onViewChange = function() {
    if (window.resetAccordionSort) {
        window.resetAccordionSort();
    }
};

// 로딩 완료
console.log('✅ 아코디언 정렬 시스템 v2.1 로딩 완료');

// 디버깅 정보
setTimeout(() => {
    console.log('🔍 시스템 상태:');
    console.log(`  - 정렬 버튼: ${document.querySelectorAll('.accordion-sort-btn').length}개`);
    console.log(`  - 팀 아이템: ${document.querySelectorAll('.team-accordion-item').length}개`);
    console.log(`  - 여정 아이템: ${document.querySelectorAll('.journey-accordion-item').length}개`);
    console.log('  - sortAccordions:', typeof window.sortAccordions);
    console.log('  - resetAccordionSort:', typeof window.resetAccordionSort);
    console.log('  - updateAccordionHeaders:', typeof updateAccordionHeaders);
}, 500);
"""