"""
아코디언 정렬 기능 - 여정순서 정렬 + 여정 설명 박스 표시/숨김 포함
"""

def get_sorting_scripts():
    """정렬 관련 스크립트 - 여정 설명 박스 표시/숨김 포함"""
    return """
// ─────────── 정렬 기능 (헤더 업데이트 포함) + 여정순서 + 여정 설명 ───────────
console.log('🎯 정렬 시스템 v2.4 로딩 중 (여정 설명 박스 포함)...');

// 여정 시간 순서 정의
const JOURNEY_TIME_ORDER = [
    '계정·입점',
    '상품·콘텐츠', 
    '주문·배송',
    '반품·취소',
    '정산',
    '기타'
];

// 전역 정렬 상태
window.accordionSortState = {
    metric: null,
    order: null
};

// 여정 설명 박스 표시/숨김 함수
function toggleJourneyDescriptions(show) {
    console.log(`${show ? '표시' : '숨김'}: 여정 설명 박스`);
    
    try {
        const descriptionBoxes = document.querySelectorAll('.journey-description-box');
        
        descriptionBoxes.forEach(box => {
            if (show) {
                box.style.display = 'block';
            } else {
                box.style.display = 'none';
            }
        });
        
        console.log(`✅ 여정 설명 박스 ${show ? '표시' : '숨김'} 완료`);
        
    } catch (error) {
        console.error('❌ 여정 설명 박스 토글 오류:', error);
    }
}

// 메인 정렬 함수 (여정 설명 박스 토글 추가)
window.sortAccordions = function(metric) {
    console.log(`🚀 정렬 시작: ${metric}`);
    
    try {
        // 현재 뷰 확인
        const activeView = document.querySelector('.analysis-view.active');
        if (!activeView) {
            console.log('❌ 활성 뷰 없음');
            return;
        }
        
        const isTeamView = activeView.id.includes('teams');
        const isJourneyView = activeView.id.includes('journey');
        console.log(`📊 뷰 타입: ${isTeamView ? '팀별' : isJourneyView ? '여정별' : '카테고리'}`);
        
        // 여정순서 정렬은 여정별 분석에서만 가능
        if (metric === 'journey' && !isJourneyView) {
            console.log('❌ 여정순서 정렬은 여정별 분석에서만 가능');
            alert('여정순서 정렬은 여정별 분석에서만 사용할 수 있습니다.');
            return;
        }
        
        // === 여정 설명 박스 표시/숨김 처리 ===
        if (isJourneyView) {
            if (metric === 'journey') {
                // 여정순서 정렬시 설명 박스 표시
                toggleJourneyDescriptions(true);
            } else {
                // 다른 정렬시 설명 박스 숨김
                toggleJourneyDescriptions(false);
            }
        }
        
        // 정렬 순서 결정
        let order = 'desc';
        if (metric === 'journey') {
            // 여정순서는 항상 시간순(asc) - 토글 없음
            order = 'asc';
            window.accordionSortState = { metric: 'journey', order: 'asc' };
        } else if (window.accordionSortState.metric === metric) {
            order = window.accordionSortState.order === 'desc' ? 'asc' : 'desc';
            window.accordionSortState = { metric, order };
        } else {
            window.accordionSortState = { metric, order };
        }
        
        console.log(`📋 정렬 설정: ${metric} ${order}`);
        
        // 버튼 상태 업데이트
        updateSortButtonsV2(metric, order);
        
        // 헤더 정보 업데이트 (여정순서가 아닐 때만)
        if (metric !== 'journey') {
            updateAccordionHeaders(metric, isTeamView);
        }
        
        // 실제 정렬 실행
        if (isTeamView) {
            sortItemsV2('.teams-accordion-container', '.team-accordion-item', metric, order);
        } else if (isJourneyView) {
            sortItemsV2('.journey-accordion-container', '.journey-accordion-item', metric, order);
        }
        
        console.log(`✅ 정렬 완료: ${metric} ${order}`);
        
    } catch (error) {
        console.error('❌ 정렬 오류:', error);
    }
};

// 버튼 상태 업데이트
function updateSortButtonsV2(activeMetric, order) {
    console.log(`🎨 버튼 업데이트 v2.4: ${activeMetric} ${order}`);
    
    try {
        // 모든 버튼 초기화
        const buttons = document.querySelectorAll('.accordion-sort-btn');
        buttons.forEach(btn => {
            if (btn && btn.classList) {
                btn.classList.remove('active');
                
                const icon = btn.querySelector('.sort-direction');
                if (icon && icon.classList) {
                    icon.classList.remove('asc', 'desc');
                }
            }
        });
        
        // 활성 버튼 설정
        const activeBtn = document.querySelector(`[data-sort="${activeMetric}"]`);
        if (activeBtn && activeBtn.classList) {
            activeBtn.classList.add('active');
            
            const icon = activeBtn.querySelector('.sort-direction');
            if (icon && icon.classList) {
                icon.classList.add(order);
                console.log(`✅ 아이콘 ${order} 클래스 추가`);
            } else {
                console.log(`⚠️ 아이콘을 찾을 수 없음`);
            }
        }
        
        console.log(`✅ 버튼 업데이트 완료`);
        
    } catch (error) {
        console.error('❌ 버튼 업데이트 오류:', error);
    }
}

// 아이템 정렬
function sortItemsV2(containerSelector, itemSelector, metric, order) {
    console.log(`🔄 아이템 정렬 v2.4: ${containerSelector} ${metric} ${order}`);
    
    try {
        const container = document.querySelector(containerSelector);
        if (!container) {
            console.log(`❌ 컨테이너 없음: ${containerSelector}`);
            return;
        }
        
        const items = Array.from(container.querySelectorAll(itemSelector));
        console.log(`📦 정렬 대상: ${items.length}개`);
        
        if (items.length === 0) return;
        
        // 정렬 실행
        items.sort((a, b) => {
            if (metric === 'journey') {
                // 여정순서 정렬
                return sortByJourneyOrder(a, b);
            } else {
                // 기존 메트릭 정렬
                const aValue = getMetricValueV2(a, metric);
                const bValue = getMetricValueV2(b, metric);
                
                return order === 'asc' ? aValue - bValue : bValue - aValue;
            }
        });
        
        // DOM 재배치
        items.forEach((item, index) => {
            setTimeout(() => {
                container.appendChild(item);
            }, index * 30);
        });
        
        console.log(`✅ 정렬 완료: ${items.length}개 아이템`);
        
    } catch (error) {
        console.error('❌ 아이템 정렬 오류:', error);
    }
}

// 여정 순서별 정렬 함수
function sortByJourneyOrder(a, b) {
    try {
        // 여정별 아이템에서 여정명 추출
        const aJourneyName = a.querySelector('.journey-name')?.textContent?.trim() || '';
        const bJourneyName = b.querySelector('.journey-name')?.textContent?.trim() || '';
        
        const aIndex = JOURNEY_TIME_ORDER.indexOf(aJourneyName);
        const bIndex = JOURNEY_TIME_ORDER.indexOf(bJourneyName);
        
        // 정의된 순서대로 정렬
        const aOrder = aIndex !== -1 ? aIndex : JOURNEY_TIME_ORDER.length;
        const bOrder = bIndex !== -1 ? bIndex : JOURNEY_TIME_ORDER.length;
        
        if (aOrder === bOrder) {
            // 같은 여정이거나 둘 다 정의되지 않은 경우, 문의량으로 2차 정렬
            const aInquiries = getMetricValueV2(a, 'total');
            const bInquiries = getMetricValueV2(b, 'total');
            return bInquiries - aInquiries; // 문의량 내림차순
        }
        
        return aOrder - bOrder; // 여정 순서대로
        
    } catch (error) {
        console.error('❌ 여정 순서 정렬 오류:', error);
        return 0;
    }
}

// 메트릭 값 추출
function getMetricValueV2(element, metric) {
    if (!element || !element.dataset) return 0;
    
    switch(metric) {
        case 'total':
            return parseInt(element.dataset.totalInquiries) || 0;
        case 'urgent':
            return parseFloat(element.dataset.urgentRate) || 0;
        case 'completed':
            return parseFloat(element.dataset.answerRate) || 0;
        default:
            return 0;
    }
}

// 정렬 초기화 (여정 설명 박스 숨김 + 원래 비율 복원)
window.resetAccordionSort = function() {
    console.log('🔄 정렬 초기화');
    
    try {
        window.accordionSortState = { metric: null, order: null };
        
        // 여정 설명 박스 숨김
        const activeView = document.querySelector('.analysis-view.active');
        if (activeView && activeView.id.includes('journey')) {
            toggleJourneyDescriptions(false);
        }
        
        // 모든 버튼 비활성화
        document.querySelectorAll('.accordion-sort-btn').forEach(btn => {
            if (btn && btn.classList) {
                btn.classList.remove('active');
                
                const icon = btn.querySelector('.sort-direction');
                if (icon && icon.classList) {
                    icon.classList.remove('asc', 'desc');
                }
            }
        });
        
        // 헤더를 원래 상태로 복원 (비율 포함)
        const activeView2 = document.querySelector('.analysis-view.active');
        if (activeView2) {
            const isTeamView = activeView2.id.includes('teams');
            const itemSelector = isTeamView ? '.team-accordion-item' : '.journey-accordion-item';
            const countSelector = isTeamView ? '.team-count' : '.journey-count';
            const progressSelector = isTeamView ? '.team-progress-fill' : '.journey-progress-fill';
            const percentageSelector = isTeamView ? '.team-percentage' : '.journey-percentage';
            
            const items = document.querySelectorAll(itemSelector);
            
            // 전체 문의 수 계산 (원래 비율 복원용)
            const totalInquiries = Array.from(items).reduce((sum, item) => {
                return sum + (parseInt(item.dataset.totalInquiries) || 0);
            }, 0);
            
            // 각 아이템을 원래 상태로 복원
            items.forEach(item => {
                const originalInquiries = parseInt(item.dataset.totalInquiries) || 0;
                const originalPercentage = totalInquiries > 0 ? Math.round((originalInquiries / totalInquiries) * 100) : 0;
                
                // 카운트 텍스트 복원
                const countElement = item.querySelector(countSelector);
                if (countElement) {
                    countElement.textContent = `(${originalInquiries.toLocaleString()}건)`;
                }
                
                // 프로그레스바와 비율 복원
                const progressElement = item.querySelector(progressSelector);
                const percentageElement = item.querySelector(percentageSelector);
                
                if (progressElement && percentageElement) {
                    // 최대값 기준 프로그레스바 계산
                    const maxInquiries = Math.max(...Array.from(items).map(i => parseInt(i.dataset.totalInquiries) || 0));
                    const progressWidth = maxInquiries > 0 ? (originalInquiries / maxInquiries) * 100 : 0;
                    
                    progressElement.style.width = `${progressWidth}%`;
                    percentageElement.textContent = `${originalPercentage}%`;
                }
            });
        }
        
        // 원래 순서로 복원
        const activeView3 = document.querySelector('.analysis-view.active');
        if (!activeView3) return;
        
        const isTeamView = activeView3.id.includes('teams');
        const isJourneyView = activeView3.id.includes('journey');
        const containerSelector = isTeamView ? '.teams-accordion-container' : '.journey-accordion-container';
        const itemSelector = isTeamView ? '.team-accordion-item' : '.journey-accordion-item';
        
        const container = document.querySelector(containerSelector);
        if (container) {
            const items = Array.from(container.querySelectorAll(itemSelector));
            items.sort((a, b) => {
                const aOrder = parseInt(a.dataset.originalOrder) || 0;
                const bOrder = parseInt(b.dataset.originalOrder) || 0;
                return aOrder - bOrder;
            });
            
            items.forEach(item => container.appendChild(item));
        }
        
        console.log('✅ 정렬 초기화 완료 (원래 비율 복원됨)');
        
    } catch (error) {
        console.error('❌ 정렬 초기화 오류:', error);
    }
};
"""