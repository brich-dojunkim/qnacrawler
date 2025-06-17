# html_reporter/scripts/inquiry_modal/pagination.py (수정된 버전 - 안전한 DOM 조작)
"""
문의 모달 페이지네이션 스크립트 - 안전한 DOM 조작 + 로딩 상태 관리
"""

def get_pagination_scripts():
    """페이지네이션 관련 스크립트 - 안전한 DOM 조작 + 로딩 상태 관리"""
    return """
// ─────────── 페이지네이션 시스템 (안전한 DOM 조작 + 로딩 관리) ───────────
console.log('📄 페이지네이션 시스템 로딩 중...');

// ─────────── 로딩 상태 관리 함수들 ───────────
function showInquiryLoading() {
    console.log('🔄 로딩 상태 표시');
    
    // 기존 콘텐츠 숨기기
    const listContainer = document.getElementById('inquiry-list');
    if (listContainer) {
        listContainer.style.display = 'none';
    }
    
    const emptyState = document.getElementById('no-inquiries');
    if (emptyState) {
        emptyState.style.display = 'none';
    }
    
    // 로딩 표시
    const loadingElement = document.getElementById('inquiry-loading');
    if (loadingElement) {
        loadingElement.style.display = 'flex';
    } else {
        // 로딩 요소가 없으면 동적 생성
        const container = document.getElementById('inquiry-list-container');
        if (container) {
            const loadingHtml = `
                <div id="inquiry-loading" class="inquiry-loading" style="display: flex;">
                    <div class="loading-spinner"></div>
                    <span>문의 목록을 불러오는 중...</span>
                </div>
            `;
            container.insertAdjacentHTML('afterbegin', loadingHtml);
        }
    }
}

function hideInquiryLoading() {
    console.log('✅ 로딩 상태 숨김');
    
    const loadingElement = document.getElementById('inquiry-loading');
    if (loadingElement) {
        loadingElement.style.display = 'none';
    }
    
    // 리스트 컨테이너 다시 표시
    const listContainer = document.getElementById('inquiry-list');
    if (listContainer) {
        listContainer.style.display = 'flex';
    }
}

// ─────────── 페이지네이션 적용 및 렌더링 ───────────
window.updatePaginationAndRender = function() {
    console.log('📄 페이지네이션 업데이트 시작');
    
    try {
        const filteredInquiries = window.inquiryModalState.filteredInquiries || [];
        const currentPage = window.inquiryModalState.currentPage;
        const itemsPerPage = window.inquiryModalState.itemsPerPage;
        
        // 총 페이지 수 계산
        const totalPages = Math.ceil(filteredInquiries.length / itemsPerPage);
        
        // 현재 페이지가 유효 범위를 벗어나면 조정
        if (currentPage > totalPages && totalPages > 0) {
            window.inquiryModalState.currentPage = totalPages;
        } else if (currentPage < 1) {
            window.inquiryModalState.currentPage = 1;
        }
        
        // 현재 페이지 문의들 추출
        const startIndex = (window.inquiryModalState.currentPage - 1) * itemsPerPage;
        const endIndex = Math.min(startIndex + itemsPerPage, filteredInquiries.length);
        const currentPageInquiries = filteredInquiries.slice(startIndex, endIndex);
        
        // 상태 업데이트
        window.inquiryModalState.currentPageInquiries = currentPageInquiries;
        
        console.log(`📊 페이지네이션: ${window.inquiryModalState.currentPage}/${totalPages} 페이지, ${currentPageInquiries.length}개 표시`);
        
        // 문의 목록 렌더링 (안전한 버전)
        renderInquiryListSafe(currentPageInquiries);
        
        // 페이지네이션 컨트롤 업데이트
        updatePaginationControls(window.inquiryModalState.currentPage, totalPages, filteredInquiries.length);
        
        // 페이지네이션 정보 업데이트
        updatePaginationInfo(startIndex, endIndex, filteredInquiries.length);
        
    } catch (error) {
        console.error('❌ 페이지네이션 업데이트 오류:', error);
        hideInquiryLoading();
        showEmptyState();
    }
};

// ─────────── 문의 목록 렌더링 (로딩 상태 관리 개선) ───────────
function renderInquiryListSafe(inquiries) {
    // 🔧 중요: 먼저 로딩 상태 숨기기
    hideInquiryLoading();
    
    // inquiry-list 요소 확인 및 생성
    let listContainer = document.getElementById('inquiry-list');
    
    if (!listContainer) {
        console.log('⚠️ inquiry-list 요소가 없어서 생성합니다.');
        
        const parentContainer = document.getElementById('inquiry-list-container');
        if (!parentContainer) {
            console.error('❌ inquiry-list-container도 찾을 수 없습니다!');
            return;
        }
        
        // inquiry-list div 생성
        listContainer = document.createElement('div');
        listContainer.id = 'inquiry-list';
        listContainer.className = 'inquiry-list';
        
        // 기존 내용 앞에 삽입
        parentContainer.insertBefore(listContainer, parentContainer.firstChild);
        console.log('✅ inquiry-list 요소를 동적으로 생성했습니다.');
    }
    
    if (!inquiries || inquiries.length === 0) {
        showEmptyState();
        return;
    }
    
    console.log(`🎨 문의 목록 렌더링: ${inquiries.length}개`);
    
    // 문의 카드들 생성
    let cardsHtml = '';
    inquiries.forEach(inquiry => {
        try {
            // createInquiryCard 함수 존재 확인
            if (typeof window.createInquiryCard === 'function') {
                cardsHtml += window.createInquiryCard(inquiry);
            } else {
                console.error('❌ createInquiryCard 함수를 찾을 수 없습니다.');
                cardsHtml += createSimpleInquiryCard(inquiry);
            }
        } catch (error) {
            console.error('문의 카드 생성 오류:', error, inquiry);
            cardsHtml += createErrorCard(inquiry);
        }
    });
    
    // DOM 업데이트
    listContainer.innerHTML = cardsHtml;
    
    // 스크롤을 맨 위로 이동
    const modalBody = document.querySelector('.inquiry-modal-body');
    if (modalBody) {
        modalBody.scrollTop = 0;
    }
    
    console.log('✅ 문의 목록 렌더링 완료');
}

// ─────────── 간단한 문의 카드 생성 (fallback) ───────────
function createSimpleInquiryCard(inquiry) {
    return `
        <div class="inquiry-card" data-inquiry-id="${inquiry.inquiry_id || 'unknown'}">
            <div class="inquiry-card-header">
                <strong>${inquiry.inquiry_id || 'ID 없음'}</strong>
                <span class="urgency-badge ${inquiry.is_urgent ? 'urgent' : 'normal'}">
                    ${inquiry.is_urgent ? '🚨 긴급' : '📋 일반'}
                </span>
            </div>
            <div class="inquiry-card-body">
                <div class="inquiry-content">
                    ${(inquiry.question_content || '내용 없음').substring(0, 200)}...
                </div>
            </div>
            <div class="inquiry-card-footer">
                <small>팀: ${inquiry.assigned_team || '미분류'} | 카테고리: ${inquiry.sub_category || '기타'}</small>
            </div>
        </div>
    `;
}

// ─────────── 오류 카드 생성 ───────────
function createErrorCard(inquiry) {
    return `
        <div class="inquiry-card error-card">
            <div class="inquiry-card-body">
                <div style="color: #dc2626; text-align: center; padding: 20px;">
                    ❌ 문의 카드 생성 오류<br>
                    ID: ${inquiry?.inquiry_id || '알 수 없음'}
                </div>
            </div>
        </div>
    `;
}

// ─────────── 빈 상태 표시 (로딩 상태 관리 개선) ───────────
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

// ─────────── 페이지네이션 컨트롤 업데이트 ───────────
function updatePaginationControls(currentPage, totalPages, totalItems) {
    const paginationControls = document.getElementById('pagination-controls');
    if (!paginationControls) return;
    
    // 페이지네이션이 필요 없으면 숨김
    if (totalPages <= 1) {
        paginationControls.style.display = 'none';
        return;
    }
    
    paginationControls.style.display = 'flex';
    
    // 이전/다음 버튼 상태 업데이트
    const prevBtn = document.getElementById('prev-page');
    const nextBtn = document.getElementById('next-page');
    
    if (prevBtn) {
        prevBtn.disabled = currentPage <= 1;
    }
    
    if (nextBtn) {
        nextBtn.disabled = currentPage >= totalPages;
    }
    
    // 페이지 번호 버튼들 생성
    updatePageNumbers(currentPage, totalPages);
}

// ─────────── 페이지 번호 버튼들 업데이트 ───────────
function updatePageNumbers(currentPage, totalPages) {
    const pageNumbersContainer = document.getElementById('page-numbers');
    if (!pageNumbersContainer) return;
    
    let numbersHtml = '';
    
    // 표시할 페이지 번호 범위 계산
    const maxVisiblePages = 7;
    let startPage = Math.max(1, currentPage - Math.floor(maxVisiblePages / 2));
    let endPage = Math.min(totalPages, startPage + maxVisiblePages - 1);
    
    // 끝 페이지가 조정되었으면 시작 페이지도 조정
    if (endPage - startPage < maxVisiblePages - 1) {
        startPage = Math.max(1, endPage - maxVisiblePages + 1);
    }
    
    // 첫 페이지 (1이 범위에 없을 때)
    if (startPage > 1) {
        numbersHtml += createPageButton(1, currentPage === 1);
        if (startPage > 2) {
            numbersHtml += '<span class="page-ellipsis">...</span>';
        }
    }
    
    // 중간 페이지들
    for (let i = startPage; i <= endPage; i++) {
        numbersHtml += createPageButton(i, currentPage === i);
    }
    
    // 마지막 페이지 (totalPages가 범위에 없을 때)
    if (endPage < totalPages) {
        if (endPage < totalPages - 1) {
            numbersHtml += '<span class="page-ellipsis">...</span>';
        }
        numbersHtml += createPageButton(totalPages, currentPage === totalPages);
    }
    
    pageNumbersContainer.innerHTML = numbersHtml;
}

// ─────────── 페이지 버튼 생성 ───────────
function createPageButton(pageNumber, isActive) {
    const activeClass = isActive ? 'active' : '';
    return `
        <button class="page-number-btn ${activeClass}" 
                onclick="goToPage(${pageNumber})" 
                ${isActive ? 'disabled' : ''}>
            ${pageNumber}
        </button>
    `;
}

// ─────────── 페이지네이션 정보 업데이트 ───────────
function updatePaginationInfo(startIndex, endIndex, totalItems) {
    const paginationText = document.getElementById('pagination-text');
    if (paginationText && totalItems > 0) {
        paginationText.textContent = `${totalItems.toLocaleString()}개 문의 중 ${(startIndex + 1).toLocaleString()}-${endIndex.toLocaleString()}개 표시`;
    } else if (paginationText) {
        paginationText.textContent = '0개 문의';
    }
}

// ─────────── 페이지 이동 함수들 ───────────
window.goToPage = function(pageNumber) {
    console.log(`📄 페이지 이동: ${pageNumber}`);
    
    const totalPages = Math.ceil(window.inquiryModalState.filteredItems / window.inquiryModalState.itemsPerPage);
    
    if (pageNumber >= 1 && pageNumber <= totalPages) {
        window.inquiryModalState.currentPage = pageNumber;
        updatePaginationAndRender();
    }
};

window.goToPreviousPage = function() {
    if (window.inquiryModalState.currentPage > 1) {
        goToPage(window.inquiryModalState.currentPage - 1);
    }
};

window.goToNextPage = function() {
    const totalPages = Math.ceil(window.inquiryModalState.filteredItems / window.inquiryModalState.itemsPerPage);
    if (window.inquiryModalState.currentPage < totalPages) {
        goToPage(window.inquiryModalState.currentPage + 1);
    }
};

// ─────────── 페이지당 항목 수 변경 ───────────
window.changeItemsPerPage = function() {
    const select = document.getElementById('items-per-page');
    if (select) {
        const newItemsPerPage = parseInt(select.value);
        console.log(`📄 페이지당 항목 수 변경: ${newItemsPerPage}`);
        
        window.inquiryModalState.itemsPerPage = newItemsPerPage;
        window.inquiryModalState.currentPage = 1; // 첫 페이지로 이동
        
        updatePaginationAndRender();
    }
};

// ─────────── 키보드 네비게이션 ───────────
document.addEventListener('keydown', function(event) {
    if (!window.inquiryModalState.isOpen) return;
    
    const totalPages = Math.ceil(window.inquiryModalState.filteredItems / window.inquiryModalState.itemsPerPage);
    
    switch(event.key) {
        case 'ArrowLeft':
            if (event.ctrlKey && window.inquiryModalState.currentPage > 1) {
                event.preventDefault();
                goToPreviousPage();
            }
            break;
        case 'ArrowRight':
            if (event.ctrlKey && window.inquiryModalState.currentPage < totalPages) {
                event.preventDefault();
                goToNextPage();
            }
            break;
        case 'Home':
            if (event.ctrlKey) {
                event.preventDefault();
                goToPage(1);
            }
            break;
        case 'End':
            if (event.ctrlKey && totalPages > 0) {
                event.preventDefault();
                goToPage(totalPages);
            }
            break;
    }
});

// ─────────── 페이지네이션 디버깅 ───────────
window.debugPagination = function() {
    console.log('🔍 페이지네이션 디버깅 정보:');
    console.log('현재 페이지:', window.inquiryModalState.currentPage);
    console.log('페이지당 항목 수:', window.inquiryModalState.itemsPerPage);
    console.log('전체 항목 수:', window.inquiryModalState.filteredItems);
    console.log('현재 페이지 항목 수:', window.inquiryModalState.currentPageInquiries?.length || 0);
    
    const totalPages = Math.ceil(window.inquiryModalState.filteredItems / window.inquiryModalState.itemsPerPage);
    console.log('총 페이지 수:', totalPages);
    
    // DOM 요소 확인
    console.log('inquiry-list 요소:', document.getElementById('inquiry-list') ? '✅ 존재' : '❌ 없음');
    console.log('inquiry-list-container 요소:', document.getElementById('inquiry-list-container') ? '✅ 존재' : '❌ 없음');
};

console.log('✅ 페이지네이션 시스템 로딩 완료 (로딩 상태 관리 개선)');
"""