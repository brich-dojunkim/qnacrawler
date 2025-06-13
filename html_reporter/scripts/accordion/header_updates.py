"""
헤더 업데이트 기능 (정렬 기준에 따른 동적 표시) - 비율 계산 버그 수정
"""

def get_header_update_scripts():
    """헤더 업데이트 스크립트 - 비율 계산 로직 수정"""
    return """
// 헤더 업데이트 함수 (정렬 기준에 따른 동적 표시) - 비율 계산 수정
function updateAccordionHeaders(metric, isTeamView) {
    console.log(`🔄 헤더 업데이트: ${metric} (${isTeamView ? '팀별' : '여정별'})`);
    
    try {
        const itemSelector = isTeamView ? '.team-accordion-item' : '.journey-accordion-item';
        const countSelector = isTeamView ? '.team-count' : '.journey-count';
        const progressSelector = isTeamView ? '.team-progress-fill' : '.journey-progress-fill';
        const percentageSelector = isTeamView ? '.team-percentage' : '.journey-percentage';
        
        const items = document.querySelectorAll(itemSelector);
        
        // 최대값 찾기 (프로그레스바 계산용)
        let maxValue = 0;
        items.forEach(item => {
            const value = getMetricValueV2(item, metric);
            if (value > maxValue) {
                maxValue = value;
            }
        });
        
        // 각 아이템의 헤더 업데이트
        items.forEach(item => {
            const value = getMetricValueV2(item, metric);
            
            // 카운트 텍스트 업데이트 - 모든 정렬에서 건수로 통일
            const countElement = item.querySelector(countSelector);
            if (countElement) {
                const originalInquiries = parseInt(item.dataset.totalInquiries) || 0;
                countElement.textContent = `(${originalInquiries.toLocaleString()}건)`;
            }
            
            // 프로그레스바 업데이트 - 메트릭별 다른 계산 방식 적용
            const progressElement = item.querySelector(progressSelector);
            const percentageElement = item.querySelector(percentageSelector);
            
            if (progressElement && maxValue > 0) {
                let progressWidth = 0;
                let displayPercentage = '';
                
                switch(metric) {
                    case 'total':
                        // 문의량: 최대값 대비 비율로 프로그레스바 계산
                        progressWidth = (value / maxValue) * 100;
                        // 표시는 원래 비율(전체 대비) 유지
                        const originalTotalInquiries = parseInt(item.dataset.totalInquiries) || 0;
                        const totalSum = Array.from(items).reduce((sum, i) => sum + (parseInt(i.dataset.totalInquiries) || 0), 0);
                        displayPercentage = totalSum > 0 ? Math.round((originalTotalInquiries / totalSum) * 100) + '%' : '0%';
                        break;
                        
                    case 'urgent':
                        // 긴급률: 최대 긴급률 기준으로 프로그레스바
                        progressWidth = maxValue > 0 ? (value / maxValue) * 100 : 0;
                        displayPercentage = `${value}%`;
                        break;
                        
                    case 'completed':
                        // 완료율: 최대 완료율 기준으로 프로그레스바
                        progressWidth = maxValue > 0 ? (value / maxValue) * 100 : 0;
                        displayPercentage = `${value}%`;
                        break;
                        
                    default:
                        progressWidth = (value / maxValue) * 100;
                        displayPercentage = Math.round((value / maxValue) * 100) + '%';
                }
                
                progressElement.style.width = `${progressWidth}%`;
                
                if (percentageElement) {
                    percentageElement.textContent = displayPercentage;
                }
            }
        });
        
        console.log(`✅ 헤더 업데이트 완료: ${items.length}개 아이템`);
        
    } catch (error) {
        console.error('❌ 헤더 업데이트 오류:', error);
    }
}
"""