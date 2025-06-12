"""
팀별·여정별 아코디언 및 전체 제어 스크립트 - 최종 완성 버전
"""

def get_accordion_scripts() -> str:
    return """
console.log('🚀 아코디언 스크립트 로딩 시작 - v2.0');

// ─────────── 팀별 아코디언 ───────────
function toggleTeamAccordion(teamId) {
    const content = document.getElementById(`content-${teamId}`);
    const item    = content.closest('.team-accordion-item');

    if (content.style.display === 'none' || !content.style.display) {
        openAccordion(content, item);
    } else {
        closeAccordion(content, item);
    }
}

// ─────────── 여정별 아코디언 ───────────
function toggleJourneyAccordion(journeyId) {
    const content = document.getElementById(`journey-content-${journeyId}`);
    const item    = content.closest('.journey-accordion-item');

    if (content.style.display === 'none' || !content.style.display) {
        openAccordion(content, item);
    } else {
        closeAccordion(content, item);
    }
}

// ─────────── 공통 열기/닫기 로직 ───────────
function openAccordion(content, item) {
    content.style.display   = 'block';
    content.style.height    = '0px';
    content.style.overflow  = 'hidden';
    content.style.transition= 'height 0.3s ease';
    item.classList.add('expanded');

    const h = content.scrollHeight;
    requestAnimationFrame(() => { content.style.height = h + 'px'; });

    setTimeout(() => {
        content.style.height = 'auto';
        content.style.overflow = 'visible';
    }, 300);
}

function closeAccordion(content, item) {
    content.style.height    = content.scrollHeight + 'px';
    content.style.overflow  = 'hidden';
    content.style.transition= 'height 0.3s ease';

    requestAnimationFrame(() => { content.style.height = '0px'; });

    setTimeout(() => {
        content.style.display   = 'none';
        content.style.height    = '';
        content.style.overflow  = '';
        content.style.transition= '';
        item.classList.remove('expanded');
    }, 300);
}

// ─────────── 전체 펼치기/접기 ───────────
function expandAllTeamAccordions() {
    console.log('팀별 전체 펼치기 실행');
    document.querySelectorAll('.team-accordion-item')
        .forEach(item => {
            const content = item.querySelector('.team-accordion-content');
            if (content && !item.classList.contains('expanded')) {
                const id = content.id.replace('content-','');
                toggleTeamAccordion(id);
            }
        });
}

function collapseAllTeamAccordions() {
    console.log('팀별 전체 접기 실행');
    document.querySelectorAll('.team-accordion-item')
        .forEach(item => {
            const content = item.querySelector('.team-accordion-content');
            if (content && item.classList.contains('expanded')) {
                const id = content.id.replace('content-','');
                toggleTeamAccordion(id);
            }
        });
}

function expandAllJourneyAccordions() {
    console.log('여정별 전체 펼치기 실행');
    document.querySelectorAll('.journey-accordion-item')
        .forEach(item => {
            const content = item.querySelector('.journey-accordion-content');
            if (content && !item.classList.contains('expanded')) {
                const id = content.id.replace('journey-content-','');
                toggleJourneyAccordion(id);
            }
        });
}

function collapseAllJourneyAccordions() {
    console.log('여정별 전체 접기 실행');
    document.querySelectorAll('.journey-accordion-item')
        .forEach(item => {
            const content = item.querySelector('.journey-accordion-content');
            if (content && item.classList.contains('expanded')) {
                const id = content.id.replace('journey-content-','');
                toggleJourneyAccordion(id);
            }
        });
}

// ─────────── 통합 전체 제어 ───────────
function expandAllAccordions() {
    const activeView = document.querySelector('.analysis-view.active');
    if (!activeView) return;
    
    const viewType = activeView.id.includes('teams') ? 'team' : 'journey';
    
    if (viewType === 'team') {
        expandAllTeamAccordions();
    } else {
        expandAllJourneyAccordions();
    }
}

function collapseAllAccordions() {
    const activeView = document.querySelector('.analysis-view.active');
    if (!activeView) return;
    
    const viewType = activeView.id.includes('teams') ? 'team' : 'journey';
    
    if (viewType === 'team') {
        collapseAllTeamAccordions();
    } else {
        collapseAllJourneyAccordions();
    }
}

// ─────────── 정렬 기능 (완전 새 버전) ───────────
console.log('🎯 정렬 시스템 v2.0 로딩 중...');

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

// 버튼 상태 업데이트 (완전 새 버전)
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

// 아이템 정렬 (완전 새 버전)
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

// 메트릭 값 추출 (완전 새 버전)
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
        
        // 원래 순서로 복원
        const activeView = document.querySelector('.analysis-view.active');
        if (!activeView) return;
        
        const isTeamView = activeView.id.includes('teams');
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

// 뷰 변경시 호출
window.onViewChange = function() {
    if (window.resetAccordionSort) {
        window.resetAccordionSort();
    }
};

// 로딩 완료
console.log('✅ 아코디언 정렬 시스템 v2.0 로딩 완료');

// 디버깅 정보
setTimeout(() => {
    console.log('🔍 시스템 상태:');
    console.log(`  - 정렬 버튼: ${document.querySelectorAll('.accordion-sort-btn').length}개`);
    console.log(`  - 팀 아이템: ${document.querySelectorAll('.team-accordion-item').length}개`);
    console.log(`  - 여정 아이템: ${document.querySelectorAll('.journey-accordion-item').length}개`);
    console.log('  - sortAccordions:', typeof window.sortAccordions);
    console.log('  - resetAccordionSort:', typeof window.resetAccordionSort);
}, 500);
"""