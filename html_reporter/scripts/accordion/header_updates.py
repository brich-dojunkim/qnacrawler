"""
헤더 업데이트 기능 (정렬 기준에 따른 동적 표시)
"""

def get_header_update_scripts():
    """헤더 업데이트 스크립트"""
    return """
// 헤더 업데이트 함수 (정렬 기준에 따른 동적 표시)
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
            
            // 카운트 텍스트 업데이트
            const countElement = item.querySelector(countSelector);
            if (countElement) {
                let displayText = '';
                switch(metric) {
                    case 'total':
                        displayText = `(${value.toLocaleString()}건)`;
                        break;
                    case 'urgent':
                        displayText = `(${value}%)`;
                        break;
                    case 'completed':
                        displayText = `(${value}%)`;
                        break;
                    default:
                        displayText = `(${value.toLocaleString()}건)`;
                }
                countElement.textContent = displayText;
            }
            
            // 프로그레스바 업데이트
            const progressElement = item.querySelector(progressSelector);
            if (progressElement && maxValue > 0) {
                const percentage = (value / maxValue) * 100;
                progressElement.style.width = `${percentage}%`;
            }
            
            // 퍼센티지 텍스트 업데이트
            const percentageElement = item.querySelector(percentageSelector);
            if (percentageElement && maxValue > 0) {
                const percentage = Math.round((value / maxValue) * 100);
                let displayText = '';
                switch(metric) {
                    case 'total':
                        displayText = `${percentage}%`;
                        break;
                    case 'urgent':
                        displayText = `${value}%`;
                        break;
                    case 'completed':
                        displayText = `${value}%`;
                        break;
                    default:
                        displayText = `${percentage}%`;
                }
                percentageElement.textContent = displayText;
            }
        });
        
        console.log(`✅ 헤더 업데이트 완료: ${items.length}개 아이템`);
        
    } catch (error) {
        console.error('❌ 헤더 업데이트 오류:', error);
    }
}
"""