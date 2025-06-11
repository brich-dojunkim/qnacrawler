# html_reporter/scripts.py
"""JavaScript 코드 모음 - 세그먼트 선택 + 정렬 기준 방식"""

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

// 개선된 카테고리 필터링 함수
function initCategoryFilters() {
    // 세그먼트 선택 드롭다운 이벤트
    const segmentSelect = document.getElementById('segment-select');
    if (segmentSelect) {
        segmentSelect.addEventListener('change', applyFilters);
    }
    
    // 정렬 기준 라디오 버튼 이벤트
    document.querySelectorAll('input[name="sort-type"]').forEach(radio => {
        radio.addEventListener('change', applyFilters);
    });
}

function applyFilters() {
    const segmentValue = document.getElementById('segment-select').value;
    const sortType = document.querySelector('input[name="sort-type"]:checked').value;
    
    console.log(`필터 적용: 세그먼트=${segmentValue}, 정렬=${sortType}`);
    
    const container = document.getElementById('categories-container');
    if (!container) return;
    
    const allCards = Array.from(container.children);
    
    // 1단계: 세그먼트에 따른 필터링
    let visibleCards = [];
    
    if (segmentValue === 'all') {
        visibleCards = allCards;
        updateSegmentInfo('전체 카테고리', allCards.length);
    } else if (segmentValue.startsWith('team-')) {
        const targetTeam = segmentValue.replace('team-', '');
        visibleCards = allCards.filter(card => card.getAttribute('data-team') === targetTeam);
        updateSegmentInfo(`${targetTeam} 팀`, visibleCards.length);
    } else if (segmentValue.startsWith('journey-')) {
        const targetJourney = segmentValue.replace('journey-', '');
        visibleCards = allCards.filter(card => card.getAttribute('data-journey') === targetJourney);
        updateSegmentInfo(`${targetJourney} 여정`, visibleCards.length);
    }
    
    // 2단계: 보이는 카드들만 정렬
    visibleCards.sort((a, b) => applySortLogic(a, b, sortType));
    
    // 3단계: DOM 업데이트 (숨기기/보이기 + 재배치)
    allCards.forEach(card => {
        if (visibleCards.includes(card)) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
    
    // 정렬된 순서대로 재배치
    visibleCards.forEach(card => {
        container.appendChild(card);
    });
    
    // 시각적 피드백 업데이트
    updateFilterFeedback(segmentValue, sortType, visibleCards.length);
}

function applySortLogic(a, b, sortType) {
    switch(sortType) {
        case 'volume':
            const countA = parseInt(a.getAttribute('data-count')) || 0;
            const countB = parseInt(b.getAttribute('data-count')) || 0;
            return countB - countA; // 내림차순 (많은 순)
            
        case 'urgent':
            const urgentA = parseFloat(a.getAttribute('data-urgent-rate')) || 0;
            const urgentB = parseFloat(b.getAttribute('data-urgent-rate')) || 0;
            return urgentB - urgentA; // 내림차순 (높은 순)
            
        case 'answer':
            const answerA = parseFloat(a.getAttribute('data-answer-rate')) || 0;
            const answerB = parseFloat(b.getAttribute('data-answer-rate')) || 0;
            return answerA - answerB; // 오름차순 (낮은 순, 문제있는 것 우선)
            
        default:
            return 0;
    }
}

function updateSegmentInfo(segmentText, visibleCount) {
    const segmentTextElement = document.getElementById('current-segment-text');
    const visibleCountElement = document.getElementById('visible-count');
    
    if (segmentTextElement) {
        segmentTextElement.textContent = segmentText;
    }
    
    if (visibleCountElement) {
        visibleCountElement.textContent = visibleCount;
    }
}

function updateFilterFeedback(segmentValue, sortType, visibleCount) {
    const container = document.getElementById('categories-container');
    
    // 기존 피드백 클래스 제거
    container.classList.remove('filter-all', 'filter-team', 'filter-journey', 'filter-volume', 'filter-urgent', 'filter-answer');
    
    // 새로운 피드백 클래스 추가
    if (segmentValue === 'all') {
        container.classList.add('filter-all');
    } else if (segmentValue.startsWith('team-')) {
        container.classList.add('filter-team');
    } else if (segmentValue.startsWith('journey-')) {
        container.classList.add('filter-journey');
    }
    
    container.classList.add(`filter-${sortType}`);
    
    console.log(`필터 피드백 업데이트: ${segmentValue} + ${sortType} (${visibleCount}개 표시)`);
}

// 팀 옵션 동적 생성 함수
function populateTeamOptions() {
    const segmentSelect = document.getElementById('segment-select');
    const container = document.getElementById('categories-container');
    
    if (!segmentSelect || !container) return;
    
    // 기존 팀 옵션 제거
    const existingTeamOptions = segmentSelect.querySelectorAll('optgroup[label="팀별"] option');
    existingTeamOptions.forEach(option => option.remove());
    
    // 모든 카드에서 팀 정보 수집
    const teams = new Set();
    const cards = container.children;
    
    for (let card of cards) {
        const team = card.getAttribute('data-team');
        if (team && team !== '기타') {
            teams.add(team);
        }
    }
    
    // 팀 옵션 추가
    const teamOptgroup = segmentSelect.querySelector('optgroup[label="팀별"]');
    const sortedTeams = Array.from(teams).sort();
    
    sortedTeams.forEach(team => {
        const option = document.createElement('option');
        option.value = `team-${team}`;
        option.textContent = team;
        teamOptgroup.appendChild(option);
    });
    
    console.log(`팀 옵션 ${sortedTeams.length}개 생성 완료:`, sortedTeams);
}

// 기존 호환성 함수
function filterCategories(type) {
    console.log('기존 filterCategories 호출됨:', type);
    // 새로운 방식으로 변환
    if (type === 'team') {
        // 첫 번째 팀 선택
        const firstTeamOption = document.querySelector('optgroup[label="팀별"] option');
        if (firstTeamOption) {
            document.getElementById('segment-select').value = firstTeamOption.value;
        }
    } else if (type === 'journey') {
        // 첫 번째 여정 선택
        document.getElementById('segment-select').value = 'journey-계정·입점';
    }
    
    applyFilters();
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
    
    // 개선된 카테고리 필터 초기화
    if (document.getElementById('categories')) {
        console.log('개선된 카테고리 필터 초기화');
        
        // 팀 옵션 동적 생성
        setTimeout(() => {
            populateTeamOptions();
            initCategoryFilters();
            applyFilters(); // 초기 필터 적용
        }, 100);
    }
});
"""