# html_reporter/scripts.py
"""JavaScript 코드 모음"""

def get_main_scripts():
    return """
function openModal(modalId) {
    document.getElementById(modalId).classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeModal(modalId) {
    document.getElementById(modalId).classList.remove('active');
    document.body.style.overflow = 'auto';
}

function filterCategories(type) {
    // 활성 버튼 업데이트
    document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');
    
    const container = document.getElementById('categories-container');
    const cards = Array.from(container.children);
    
    // 정렬 함수
    let sortFunction;
    switch(type) {
        case 'team':
            sortFunction = (a, b) => {
                const teamA = a.getAttribute('data-team');
                const teamB = b.getAttribute('data-team');
                return teamA.localeCompare(teamB);
            };
            break;
        case 'journey':
            const journeyOrder = ['계정·입점', '상품·콘텐츠', '주문·배송', '반품·취소', '정산', '기타'];
            sortFunction = (a, b) => {
                const journeyA = a.getAttribute('data-journey');
                const journeyB = b.getAttribute('data-journey');
                const indexA = journeyOrder.indexOf(journeyA);
                const indexB = journeyOrder.indexOf(journeyB);
                
                const finalIndexA = indexA === -1 ? journeyOrder.length : indexA;
                const finalIndexB = indexB === -1 ? journeyOrder.length : indexB;
                
                return finalIndexA - finalIndexB;
            };
            break;
        default: // 'all'
            sortFunction = (a, b) => {
                const countA = parseInt(a.getAttribute('data-count'));
                const countB = parseInt(b.getAttribute('data-count'));
                return countB - countA; // 내림차순
            };
    }
    
    // 정렬 및 재배치
    cards.sort(sortFunction);
    cards.forEach(card => container.appendChild(card));
}

// ESC 키로 모달 닫기
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        const activeModal = document.querySelector('.modal-overlay.active');
        if (activeModal) {
            activeModal.classList.remove('active');
            document.body.style.overflow = 'auto';
        }
    }
});

document.addEventListener('DOMContentLoaded', function() {
    console.log('VoC 리포터 로드 완료');
});
"""
