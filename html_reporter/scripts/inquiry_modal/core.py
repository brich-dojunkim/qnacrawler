# html_reporter/scripts/inquiry_modal/core.py (수정된 버전 - 안전한 DOM 조작)
"""
문의 상세보기 모달 핵심 기능 스크립트 - 안전한 DOM 조작 + 카드 생성 함수 포함 + 로딩 상태 관리
"""

def get_core_scripts():
    """모달 핵심 기능 + 안전한 DOM 조작 스크립트 + 로딩 상태 관리"""
    return """
// ─────────── 문의 모달 핵심 기능 (안전한 DOM 조작 + 로딩 관리) ───────────
console.log('📋 문의 모달 핵심 기능 로딩 중...');

// 전역 상태 관리
window.inquiryModalState = {
    isOpen: false,
    currentCategory: null,
    currentCategoryType: null,
    currentPage: 1,
    itemsPerPage: 20,
    totalItems: 0,
    filteredItems: 0,
    currentFilters: {
        search: '',
        team: '',
        urgency: '',
        status: '',
        sort: 'latest'
    },
    allInquiries: [],
    filteredInquiries: [],
    currentPageInquiries: []
};

// ─────────── 로딩 상태 표시 (개선된 버전) ───────────
function showInquiryLoading() {
    console.log('🔄 로딩 상태 표시');
    
    const listContainer = document.getElementById('inquiry-list-container');
    if (listContainer) {
        // 기존 내용 모두 숨기기
        const inquiryList = document.getElementById('inquiry-list');
        const emptyState = document.getElementById('no-inquiries');
        
        if (inquiryList) inquiryList.style.display = 'none';
        if (emptyState) emptyState.style.display = 'none';
        
        // 로딩 요소 확인 및 표시
        let loadingElement = document.getElementById('inquiry-loading');
        if (!loadingElement) {
            // 로딩 요소가 없으면 생성
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
    
    // 통계 초기화
    updateInquiryStats(0, 0, 0, 0);
    
    // 페이지네이션 숨김
    const paginationControls = document.getElementById('pagination-controls');
    if (paginationControls) {
        paginationControls.style.display = 'none';
    }
}

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
        
        // inquiry-list div 생성
        listElement = document.createElement('div');
        listElement.id = 'inquiry-list';
        listElement.className = 'inquiry-list';
        
        // 기존 내용 앞에 삽입
        container.insertBefore(listElement, container.firstChild);
        console.log('✅ inquiry-list 요소를 동적으로 생성했습니다.');
    }
    
    return listElement;
}

// ─────────── DOM 구조 디버깅 함수 ───────────
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
    
    // 자동으로 inquiry-list 생성
    if (!list) {
        ensureInquiryListElement();
    }
}

// ─────────── 모달 열기 메인 함수 (로딩 관리 개선) ───────────
window.openInquiryModal = function(categoryType, categoryName) {
    console.log(`🎯 문의 모달 열기: ${categoryType} - ${categoryName}`);
    
    try {
        // 상태 초기화
        window.inquiryModalState.currentCategory = categoryName;
        window.inquiryModalState.currentCategoryType = categoryType;
        window.inquiryModalState.currentPage = 1;
        
        // 모달 표시
        const modal = document.getElementById('inquiry-detail-modal');
        if (modal) {
            modal.classList.add('active');
            document.body.style.overflow = 'hidden';
            window.inquiryModalState.isOpen = true;
            
            // 모달 제목 업데이트
            updateModalTitle(categoryType, categoryName);
            
            // DOM 구조 확인 및 안전한 요소 생성
            setTimeout(() => {
                debugInquiryModalDOM();
            }, 100);
            
            // 🔧 중요: 로딩 상태 먼저 표시
            showInquiryLoading();
            
            // 데이터 로딩 (충분한 시간 여유 후)
            setTimeout(() => {
                if (typeof loadCategoryInquiries === 'function') {
                    loadCategoryInquiries(categoryName);
                } else {
                    console.error('❌ loadCategoryInquiries 함수를 찾을 수 없습니다.');
                    hideInquiryLoading();
                    showEmptyState();
                }
            }, 300);
            
        } else {
            console.error('❌ 문의 모달 요소를 찾을 수 없습니다.');
        }
        
    } catch (error) {
        console.error('❌ 문의 모달 열기 오류:', error);
        hideInquiryLoading();
        alert('문의 목록을 불러오는 중 오류가 발생했습니다.');
    }
};

// ─────────── 모달 닫기 ───────────
window.closeInquiryModal = function() {
    console.log('🔒 문의 모달 닫기');
    
    try {
        const modal = document.getElementById('inquiry-detail-modal');
        if (modal) {
            modal.classList.remove('active');
            document.body.style.overflow = 'auto';
            window.inquiryModalState.isOpen = false;
            
            // 상태 초기화
            resetModalState();
        }
        
    } catch (error) {
        console.error('❌ 문의 모달 닫기 오류:', error);
    }
};

// ─────────── 모달 상태 초기화 ───────────
function resetModalState() {
    window.inquiryModalState = {
        isOpen: false,
        currentCategory: null,
        currentCategoryType: null,
        currentPage: 1,
        itemsPerPage: 20,
        totalItems: 0,
        filteredItems: 0,
        currentFilters: {
            search: '',
            team: '',
            urgency: '',
            status: '',
            sort: 'latest'
        },
        allInquiries: [],
        filteredInquiries: [],
        currentPageInquiries: []
    };
    
    // UI 초기화
    const searchInput = document.getElementById('inquiry-search');
    if (searchInput) searchInput.value = '';
    
    const filters = ['team-filter', 'urgency-filter', 'status-filter'];
    filters.forEach(filterId => {
        const filter = document.getElementById(filterId);
        if (filter) filter.selectedIndex = 0;
    });
    
    const sortFilter = document.getElementById('sort-filter');
    if (sortFilter) sortFilter.value = 'latest';
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

// ─────────── 새로고침 함수 ───────────
window.refreshInquiryModal = function() {
    console.log('🔄 문의 모달 새로고침');
    
    if (window.inquiryModalState.currentCategory) {
        showInquiryLoading();
        setTimeout(() => {
            if (typeof loadCategoryInquiries === 'function') {
                loadCategoryInquiries(window.inquiryModalState.currentCategory);
            }
        }, 300);
    }
};

// ─────────── ESC 키로 모달 닫기 ───────────
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape' && window.inquiryModalState.isOpen) {
        closeInquiryModal();
    }
});

// ─────────── 모달 외부 클릭으로 닫기 ───────────
document.addEventListener('click', function(event) {
    if (event.target.classList.contains('inquiry-modal-overlay') && window.inquiryModalState.isOpen) {
        closeInquiryModal();
    }
});

// ─────────── 문의 상세보기 함수 ───────────
window.showInquiryDetail = function(inquiryId) {
    console.log(`🔍 문의 상세보기: ${inquiryId}`);
    
    // 상세 문의 정보를 별도 모달이나 확장 영역에서 표시
    // 현재는 콘솔 로그만 출력
    const inquiry = window.inquiryModalState.allInquiries.find(inq => inq.inquiry_id === inquiryId);
    if (inquiry) {
        alert(`문의 ID: ${inquiryId}\\n내용: ${inquiry.question_content?.substring(0, 200)}...`);
    }
};

// ─────────── 답변 보기 함수 ───────────
window.showInquiryAnswers = function(inquiryId) {
    console.log(`💬 답변 보기: ${inquiryId}`);
    
    const inquiry = window.inquiryModalState.allInquiries.find(inq => inq.inquiry_id === inquiryId);
    if (inquiry && inquiry.answers && inquiry.answers.length > 0) {
        let answersText = `문의 ID: ${inquiryId}\\n\\n`;
        inquiry.answers.forEach((answer, index) => {
            answersText += `답변 ${index + 1}:\\n${answer.answer_content}\\n\\n`;
        });
        alert(answersText);
    } else {
        alert('답변이 없습니다.');
    }
};

// ─────────── 전체 내용 토글 ───────────
window.toggleFullContent = function(button) {
    const card = button.closest('.inquiry-card');
    const preview = card.querySelector('.content-preview');
    const fullContent = card.querySelector('.full-content');
    const expandText = button.querySelector('.expand-text');
    const collapseText = button.querySelector('.collapse-text');
    const expandIcon = button.querySelector('.expand-icon');
    
    if (fullContent.style.display === 'none') {
        // 전체 내용 보기
        preview.style.display = 'none';
        fullContent.style.display = 'block';
        expandText.style.display = 'none';
        collapseText.style.display = 'inline';
        expandIcon.style.transform = 'rotate(180deg)';
    } else {
        // 미리보기로 돌아가기
        preview.style.display = 'block';
        fullContent.style.display = 'none';
        expandText.style.display = 'inline';
        collapseText.style.display = 'none';
        expandIcon.style.transform = 'rotate(0deg)';
    }
};

// ─────────── 전체 답변 토글 ───────────
window.toggleFullAnswer = function(button) {
    const answerSection = button.closest('.answer-section');
    const preview = answerSection.querySelector('.answer-preview');
    const fullAnswer = answerSection.querySelector('.full-answer');
    const expandText = button.querySelector('.expand-text');
    const collapseText = button.querySelector('.collapse-text');
    
    if (fullAnswer.style.display === 'none') {
        // 전체 답변 보기
        preview.style.display = 'none';
        fullAnswer.style.display = 'block';
        expandText.style.display = 'none';
        collapseText.style.display = 'inline';
    } else {
        // 미리보기로 돌아가기
        preview.style.display = 'block';
        fullAnswer.style.display = 'none';
        expandText.style.display = 'inline';
        collapseText.style.display = 'none';
    }
};

console.log('✅ 문의 모달 핵심 기능 로딩 완료');

// ─────────── 문의 카드 생성 함수 (안전한 버전) ───────────
window.createInquiryCard = function(inquiry) {
    const urgencyIcon = inquiry.is_urgent ? '🚨' : '📋';
    const urgencyClass = inquiry.is_urgent ? 'urgent' : 'normal';
    const urgencyText = inquiry.is_urgent ? '긴급' : '일반';
    
    const statusIcon = inquiry.answer_status === '답변완료' ? '✅' : 
                      inquiry.answer_status === '진행중' ? '🔄' : '⏳';
    const statusClass = inquiry.answer_status === '답변완료' ? 'completed' : 
                       inquiry.answer_status === '진행중' ? 'in-progress' : 'pending';
    const statusText = inquiry.answer_status || '답변대기';
    
    // 날짜 포맷팅
    const date = new Date(inquiry.registration_date);
    const formattedDate = date.toLocaleDateString('ko-KR') + ' ' + 
                         date.toLocaleTimeString('ko-KR', {hour: '2-digit', minute: '2-digit'});
    
    // 문의 내용 미리보기 (200자 제한)
    const content = inquiry.question_content || '';
    const preview = content.length > 200 ? content.substring(0, 200) + '...' : content;
    
    // 검색어 하이라이팅
    const highlightedPreview = highlightSearchTerm(preview, window.currentSearchTerm || '');
    
    // 답변 내용 확인
    const hasAnswer = inquiry.answers && inquiry.answers.length > 0;
    const answerPreview = hasAnswer ? 
        (inquiry.answers[0].answer_content || '').substring(0, 100) + 
        (inquiry.answers[0].answer_content && inquiry.answers[0].answer_content.length > 100 ? '...' : '') 
        : '';
    
    return `
        <div class="inquiry-card" data-inquiry-id="${inquiry.inquiry_id || 'unknown'}">
            <div class="inquiry-card-header">
                <div class="inquiry-meta">
                    <span class="urgency-badge ${urgencyClass}">
                        <span class="urgency-icon">${urgencyIcon}</span>
                        ${urgencyText}
                    </span>
                    <span class="team-badge">${inquiry.assigned_team || '미분류'}</span>
                    <span class="category-badge">${inquiry.sub_category || '기타'}</span>
                    <span class="date-badge">${formattedDate}</span>
                </div>
                <div class="inquiry-actions">
                    <span class="status-badge ${statusClass}">
                        <span class="status-icon">${statusIcon}</span>
                        ${statusText}
                    </span>
                </div>
            </div>
            
            <div class="inquiry-card-body">
                <div class="inquiry-content">
                    <div class="content-preview">${highlightedPreview}</div>
                    ${content.length > 200 ? `
                        <button class="show-full-content" onclick="toggleFullContent(this)">
                            <span class="expand-text">전체 보기</span>
                            <span class="collapse-text" style="display: none;">접기</span>
                            <svg class="expand-icon" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <polyline points="6 9 12 15 18 9"></polyline>
                            </svg>
                        </button>
                        <div class="full-content" style="display: none;">
                            ${highlightSearchTerm(content, window.currentSearchTerm || '')}
                        </div>
                    ` : ''}
                </div>
                
                ${hasAnswer ? `
                    <div class="answer-section">
                        <div class="answer-header">
                            <span class="answer-label">💬 답변</span>
                            <span class="answer-meta">${inquiry.answers[0].answerer_info?.name || '담당자'} | ${new Date(inquiry.answers[0].answer_date).toLocaleDateString('ko-KR')}</span>
                        </div>
                        <div class="answer-preview">${answerPreview}</div>
                        ${inquiry.answers[0].answer_content && inquiry.answers[0].answer_content.length > 100 ? `
                            <button class="show-full-answer" onclick="toggleFullAnswer(this)">
                                <span class="expand-text">답변 전체 보기</span>
                                <span class="collapse-text" style="display: none;">답변 접기</span>
                            </button>
                            <div class="full-answer" style="display: none;">
                                ${inquiry.answers[0].answer_content}
                            </div>
                        ` : ''}
                    </div>
                ` : ''}
            </div>
            
            <div class="inquiry-card-footer">
                <div class="inquiry-stats">
                    <span class="stat-item">
                        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                            <polyline points="14 2 14 8 20 8"></polyline>
                        </svg>
                        ID: ${inquiry.inquiry_id || 'N/A'}
                    </span>
                    <span class="stat-item">
                        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                            <polyline points="14 2 14 8 20 8"></polyline>
                            <line x1="16" y1="13" x2="8" y2="13"></line>
                            <line x1="16" y1="17" x2="8" y2="17"></line>
                            <polyline points="10 9 9 9 8 9"></polyline>
                        </svg>
                        ${content.length}자
                    </span>
                    ${inquiry.answers && inquiry.answers.length > 0 ? `
                        <span class="stat-item">
                            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
                            </svg>
                            답변 ${inquiry.answers.length}개
                        </span>
                    ` : ''}
                </div>
                
                <div class="inquiry-actions-footer">
                    ${hasAnswer ? `
                        <button class="action-btn secondary" onclick="showInquiryAnswers('${inquiry.inquiry_id}')">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
                            </svg>
                            전체 답변
                        </button>
                    ` : ''}
                    <button class="action-btn primary" onclick="showInquiryDetail('${inquiry.inquiry_id}')">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <circle cx="11" cy="11" r="8"></circle>
                            <path d="m21 21-4.35-4.35"></path>
                        </svg>
                        상세보기
                    </button>
                </div>
            </div>
        </div>
    `;
};

console.log('✅ 문의 모달 핵심 기능 + 카드 생성 함수 로딩 완료');
"""