"""
아코디언 정렬 기능
"""

def get_sorting_scripts():
    """정렬 관련 스크립트"""
    return """
// ─────────── 정렬 기능 (헤더 업데이트 포함) ───────────
console.log('🎯 정렬 시스템 v2.1 로딩 중...');

// 전역 정렬 상태
window.accordionSortState = {
    metric: null,
    order: null
};

// 메인 정렬 함수
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
        console.log(`📊 뷰 타입: ${isTeamView ? '팀별' : '여정별'}`);
        
        // 정렬 순서 결정
        let order = 'desc';
        if (window.accordionSortState.metric === metric) {
            order = window.accordionSortState.order === 'desc' ? 'asc' : 'desc';
        }
        
        window.accordionSortState = { metric, order };
        console.log(`📋 정렬 설정: ${metric} ${order}`);
        
        // 버튼 상태 업데이트
        updateSortButtonsV2(metric, order);
        
        // 헤더 정보 업데이트 (정렬 전)
        updateAccordionHeaders(metric, isTeamView);
        
        // 실제 정렬 실행
        if (isTeamView) {
            sortItemsV2('.teams-accordion-container', '.team-accordion-item', metric, order);
        } else {
            sortItemsV2('.journey-accordion-container', '.journey-accordion-item', metric, order);
        }
        
        console.log(`✅ 정렬 완료: ${metric} ${order}`);
        
    } catch (error) {
        console.error('❌ 정렬 오류:', error);
    }
};

// 버튼 상태 업데이트
function updateSortButtonsV2(activeMetric, order) {
    console.log(`🎨 버튼 업데이트 v2: ${activeMetric} ${order}`);
    
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
    console.log(`🔄 아이템 정렬 v2: ${containerSelector} ${metric} ${order}`);
    
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
            const aValue = getMetricValueV2(a, metric);
            const bValue = getMetricValueV2(b, metric);
            
            return order === 'asc' ? aValue - bValue : bValue - aValue;
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

// 정렬 초기화
window.resetAccordionSort = function() {
    console.log('🔄 정렬 초기화');
    
    try {
        window.accordionSortState = { metric: null, order: null };
        
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
        
        // 헤더를 기본 상태(총 문의)로 복원
        const activeView = document.querySelector('.analysis-view.active');
        if (activeView) {
            const isTeamView = activeView.id.includes('teams');
            updateAccordionHeaders('total', isTeamView);
        }
        
        // 원래 순서로 복원
        const activeView2 = document.querySelector('.analysis-view.active');
        if (!activeView2) return;
        
        const isTeamView = activeView2.id.includes('teams');
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
        
        console.log('✅ 정렬 초기화 완료');
        
    } catch (error) {
        console.error('❌ 정렬 초기화 오류:', error);
    }
};
"""