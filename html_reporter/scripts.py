# html_reporter/scripts.py
"""JavaScript 코드 모음 - 단순화된 기능"""

def get_main_scripts():
    return """
// 모달 열기 함수
function openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
    }
}

// 모달 닫기 함수
function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.remove('active');
        document.body.style.overflow = 'auto';
    }
}

// 카테고리 필터링 함수
function filterCategories(type) {
    // 활성 버튼 업데이트
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    
    event.target.classList.add('active');
    
    const container = document.getElementById('categories-container');
    if (!container) return;
    
    const cards = Array.from(container.children);
    
    // 정렬 함수
    let sortFunction;
    switch(type) {
        case 'team':
            sortFunction = (a, b) => {
                const teamA = a.getAttribute('data-team') || '';
                const teamB = b.getAttribute('data-team') || '';
                return teamA.localeCompare(teamB);
            };
            break;
        case 'journey':
            const journeyOrder = ['계정·입점', '상품·콘텐츠', '주문·배송', '반품·취소', '정산', '기타'];
            sortFunction = (a, b) => {
                const journeyA = a.getAttribute('data-journey') || '';
                const journeyB = b.getAttribute('data-journey') || '';
                const indexA = journeyOrder.indexOf(journeyA);
                const indexB = journeyOrder.indexOf(journeyB);
                
                const finalIndexA = indexA === -1 ? journeyOrder.length : indexA;
                const finalIndexB = indexB === -1 ? journeyOrder.length : indexB;
                
                return finalIndexA - finalIndexB;
            };
            break;
        default: // 'all'
            sortFunction = (a, b) => {
                const countA = parseInt(a.getAttribute('data-count')) || 0;
                const countB = parseInt(b.getAttribute('data-count')) || 0;
                return countB - countA; // 내림차순
            };
    }
    
    // 정렬 및 재배치
    cards.sort(sortFunction);
    cards.forEach(card => {
        container.appendChild(card);
    });
}

// 탭 전환 함수
function switchTab(tabName) {
    // 모든 탭 컨텐츠 숨기기
    document.querySelectorAll('.tab-content').forEach(tab => {
        tab.classList.remove('active');
    });
    
    // 모든 탭 버튼 비활성화
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    
    // 선택된 탭 활성화
    document.getElementById(tabName).classList.add('active');
    event.target.classList.add('active');
}

// ESC 키로 모달 닫기
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        const activeModal = document.querySelector('.modal-overlay.active');
        if (activeModal) {
            const modalId = activeModal.id;
            closeModal(modalId);
        }
    }
});

// 모달 외부 클릭으로 닫기
document.addEventListener('click', function(event) {
    if (event.target.classList.contains('modal-overlay')) {
        const modalId = event.target.id;
        closeModal(modalId);
    }
});

// DOMContentLoaded 이벤트
document.addEventListener('DOMContentLoaded', function() {
    console.log('VoC 리포터 로드 완료');
    
    // 첫 번째 탭 활성화 확인
    const firstTab = document.querySelector('.tab-content');
    const firstBtn = document.querySelector('.tab-btn');
    
    if (firstTab && firstBtn) {
        firstTab.classList.add('active');
        firstBtn.classList.add('active');
    }
});
"""