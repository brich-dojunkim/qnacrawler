# html_reporter/scripts/inquiry_modal/dom_utils.py
"""
문의 모달 DOM 조작 유틸리티
"""

def get_dom_utils_scripts():
    """DOM 조작 유틸리티 스크립트"""
    return """
// ─────────── DOM 유틸리티 시스템 ───────────
console.log('🔧 DOM 유틸리티 시스템 로딩 중...');

// ─────────── DOM 요소 확인 및 안전한 생성 ───────────
function ensureInquiryListElement() {
    let listElement = document.getElementById('inquiry-list');
    
    if (!listElement) {
        console.log('⚠️ inquiry-list 요소가 없어서 생성합니다.');
        
        const container = document.getElementById('inquiry-list-container');
        if (!container) {
            console.error('❌ inquiry-list-container도 찾을 수 없습니다!');
            return null;
        }
        
        listElement = document.createElement('div');
        listElement.id = 'inquiry-list';
        listElement.className = 'inquiry-list';
        
        container.insertBefore(listElement, container.firstChild);
        console.log('✅ inquiry-list 요소를 동적으로 생성했습니다.');
    }
    
    return listElement;
}

function ensureElement(id, className = '', tagName = 'div') {
    let element = document.getElementById(id);
    
    if (!element) {
        element = document.createElement(tagName);
        element.id = id;
        if (className) element.className = className;
        
        // 부모 컨테이너 찾기
        const container = document.getElementById('inquiry-list-container');
        if (container) {
            container.appendChild(element);
        }
    }
    
    return element;
}

// ─────────── 요소 표시/숨김 유틸리티 ───────────
function showElement(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        element.style.display = 'flex';
    }
}

function hideElement(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        element.style.display = 'none';
    }
}

function toggleElement(elementId, forceShow = null) {
    const element = document.getElementById(elementId);
    if (element) {
        if (forceShow === true) {
            element.style.display = 'flex';
        } else if (forceShow === false) {
            element.style.display = 'none';
        } else {
            element.style.display = element.style.display === 'none' ? 'flex' : 'none';
        }
    }
}

// ─────────── 모달 제목 업데이트 ───────────
function updateModalTitle(categoryType, categoryName) {
    const titleElement = document.getElementById('inquiry-modal-title');
    if (titleElement) {
        const typeText = categoryType === 'category' ? '카테고리' : '세부카테고리';
        titleElement.innerHTML = `📂 ${categoryName} 문의 목록`;
        titleElement.setAttribute('title', `${typeText}: ${categoryName}`);
    }
}

// ─────────── 통계 업데이트 ───────────
function updateInquiryStats(total, urgent, completed, avgLength) {
    const elements = {
        'total-inquiries-count': total,
        'urgent-inquiries-count': urgent,
        'completed-inquiries-count': completed,
        'avg-length': avgLength
    };
    
    Object.entries(elements).forEach(([id, value]) => {
        const element = document.getElementById(id);
        if (element) {
            element.textContent = typeof value === 'number' ? value.toLocaleString() : value;
        }
    });
}

// ─────────── 로딩 상태 관리 ───────────
function showInquiryLoading() {
    console.log('🔄 로딩 상태 표시');
    
    const listContainer = document.getElementById('inquiry-list-container');
    if (listContainer) {
        const inquiryList = document.getElementById('inquiry-list');
        const emptyState = document.getElementById('no-inquiries');
        
        if (inquiryList) inquiryList.style.display = 'none';
        if (emptyState) emptyState.style.display = 'none';
        
        let loadingElement = document.getElementById('inquiry-loading');
        if (!loadingElement) {
            const loadingHtml = `
                <div id="inquiry-loading" class="inquiry-loading">
                    <div class="loading-spinner"></div>
                    <span>문의 목록을 불러오는 중...</span>
                </div>
            `;
            listContainer.insertAdjacentHTML('afterbegin', loadingHtml);
            loadingElement = document.getElementById('inquiry-loading');
        }
        
        loadingElement.style.display = 'flex';
        console.log('✅ 로딩 상태 표시 완료');
    }
    
    updateInquiryStats(0, 0, 0, 0);
    
    const paginationControls = document.getElementById('pagination-controls');
    if (paginationControls) {
        paginationControls.style.display = 'none';
    }
}

function hideInquiryLoading() {
    console.log('✅ 로딩 상태 숨김');
    
    const loadingElement = document.getElementById('inquiry-loading');
    if (loadingElement) {
        loadingElement.style.display = 'none';
    }
    
    const listContainer = document.getElementById('inquiry-list');
    if (listContainer) {
        listContainer.style.display = 'flex';
    }
}

function showEmptyState() {
    console.log('📭 빈 상태 표시');
    
    // 로딩 상태 먼저 숨기기
    hideInquiryLoading();
    
    // 리스트 숨기기
    const listContainer = document.getElementById('inquiry-list');
    if (listContainer) {
        listContainer.style.display = 'none';
    }
    
    // 빈 상태 표시
    const emptyState = document.getElementById('no-inquiries');
    if (emptyState) {
        emptyState.style.display = 'flex';
    } else {
        // 빈 상태 요소가 없으면 동적 생성
        const container = document.getElementById('inquiry-list-container');
        if (container) {
            const emptyHtml = `
                <div id="no-inquiries" class="no-inquiries" style="display: flex;">
                    <div class="no-inquiries-icon">📭</div>
                    <div class="no-inquiries-text">조건에 맞는 문의가 없습니다.</div>
                    <button class="clear-filters-btn" onclick="clearAllInquiryFilters()">필터 초기화</button>
                </div>
            `;
            container.insertAdjacentHTML('beforeend', emptyHtml);
        }
    }
}

// ─────────── DOM 구조 디버깅 ───────────
function debugInquiryModalDOM() {
    console.log('🔍 문의 모달 DOM 구조 확인:');
    
    const modal = document.getElementById('inquiry-detail-modal');
    console.log('Modal:', modal ? '✅ 존재' : '❌ 없음');
    
    const container = document.getElementById('inquiry-list-container');
    console.log('Container:', container ? '✅ 존재' : '❌ 없음');
    
    const list = document.getElementById('inquiry-list');
    console.log('List:', list ? '✅ 존재' : '❌ 없음');
    
    if (container && !list) {
        console.log('📋 Container 내부 HTML:');
        console.log(container.innerHTML.substring(0, 300) + '...');
    }
    
    if (!list) {
        ensureInquiryListElement();
    }
}

// ─────────── 스크롤 관리 ───────────
function scrollToTop() {
    const modalBody = document.querySelector('.inquiry-modal-body');
    if (modalBody) {
        modalBody.scrollTop = 0;
    }
}

function scrollToElement(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        element.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
}

// ─────────── 클래스 관리 유틸리티 ───────────
function addClass(elementId, className) {
    const element = document.getElementById(elementId);
    if (element && element.classList) {
        element.classList.add(className);
    }
}

function removeClass(elementId, className) {
    const element = document.getElementById(elementId);
    if (element && element.classList) {
        element.classList.remove(className);
    }
}

function toggleClass(elementId, className) {
    const element = document.getElementById(elementId);
    if (element && element.classList) {
        element.classList.toggle(className);
    }
}

console.log('✅ DOM 유틸리티 시스템 로딩 완료');
"""