# html_reporter/scripts/drawer.py
"""
사이드 드로어 JavaScript 기능
"""

def get_drawer_scripts():
    """사이드 드로어 스크립트"""
    return """
// ═══════════════════════════════════════════════════════════
// 사이드 드로어 시스템 v1.0
// ═══════════════════════════════════════════════════════════

console.log('🚀 사이드 드로어 시스템 로딩 중...');

// 전역 변수
let currentInquiryData = [];
let filteredInquiryData = [];
let currentCategory = null;
let currentInquiryDetail = null;

// ─────────── 드로어 열기/닫기 ───────────
function openInquiryDrawer(categoryName, inquiryData) {
    console.log(`📂 드로어 열기: ${categoryName} (${inquiryData.length}건)`);
    
    currentCategory = categoryName;
    currentInquiryData = inquiryData;
    filteredInquiryData = [...inquiryData];
    
    // 드로어 UI 업데이트
    updateDrawerHeader();
    renderInquiryList();
    
    // 드로어 열기 애니메이션
    const drawer = document.getElementById('inquiry-drawer');
    const mainSection = document.querySelector('.detailed-analysis-section');
    
    drawer.classList.add('open');
    mainSection.classList.add('drawer-open');
    
    // 검색 입력 초기화
    const searchInput = document.getElementById('drawer-search-input');
    if (searchInput) {
        searchInput.value = '';
    }
    
    // 목록 뷰로 초기화
    showInquiryList();
}

function closeInquiryDrawer() {
    console.log('❌ 드로어 닫기');
    
    const drawer = document.getElementById('inquiry-drawer');
    const mainSection = document.querySelector('.detailed-analysis-section');
    
    drawer.classList.remove('open');
    mainSection.classList.remove('drawer-open');
    
    // 상태 초기화
    currentCategory = null;
    currentInquiryData = [];
    filteredInquiryData = [];
    currentInquiryDetail = null;
    
    // 뷰 초기화
    showInquiryList();
}

// ─────────── 헤더 업데이트 ───────────
function updateDrawerHeader() {
    const categoryNameEl = document.getElementById('drawer-category-name');
    const inquiryCountEl = document.getElementById('drawer-inquiry-count');
    
    if (categoryNameEl) {
        categoryNameEl.textContent = currentCategory || '카테고리';
    }
    
    if (inquiryCountEl) {
        inquiryCountEl.textContent = `${filteredInquiryData.length}건`;
    }
}

// ─────────── 문의 목록 렌더링 ───────────
function renderInquiryList() {
    const listContainer = document.getElementById('inquiry-list');
    const emptyState = document.getElementById('inquiry-list-empty');
    
    if (!listContainer) return;
    
    if (filteredInquiryData.length === 0) {
        listContainer.innerHTML = '';
        if (emptyState) emptyState.classList.remove('hidden');
        return;
    }
    
    if (emptyState) emptyState.classList.add('hidden');
    
    const listHTML = filteredInquiryData.map(inquiry => {
        return generateInquiryItemHTML(inquiry);
    }).join('');
    
    listContainer.innerHTML = listHTML;
    
    console.log(`✅ 문의 목록 렌더링 완료: ${filteredInquiryData.length}건`);
}

// ─────────── 문의 아이템 HTML 생성 ───────────
function generateInquiryItemHTML(inquiry) {
    const urgentBadge = inquiry.is_urgent ? '<span class="urgent-badge">긴급</span>' : '';
    const statusClass = inquiry.answer_status === '답변완료' ? 'answered' : 'unanswered';
    
    // 주문 정보 생성
    let orderInfo = '';
    if (inquiry.product_order_number) {
        orderInfo = `주문: ${inquiry.product_order_number}`;
    }
    if (inquiry.breach_order_number) {
        orderInfo += orderInfo ? ` | 브리치: ${inquiry.breach_order_number}` : `브리치: ${inquiry.breach_order_number}`;
    }
    
    // 날짜 포맷팅
    const date = new Date(inquiry.registration_date);
    const formattedDate = date.toLocaleDateString('ko-KR') + ' ' + date.toLocaleTimeString('ko-KR', {hour: '2-digit', minute: '2-digit'});
    
    return `
        <div class="inquiry-item" data-inquiry-id="${inquiry.inquiry_id}" data-status="${inquiry.answer_status}" data-urgent="${inquiry.is_urgent}">
            <div class="inquiry-item-header">
                <div class="inquiry-id-section">
                    <span class="inquiry-id">#${inquiry.inquiry_id}</span>
                    <div class="inquiry-badges">
                        ${urgentBadge}
                        <span class="status-badge status-${statusClass}">${inquiry.answer_status}</span>
                    </div>
                </div>
                <div class="inquiry-meta">
                    <span class="inquiry-date">${formattedDate}</span>
                    <span class="inquiry-seller">${inquiry.seller}</span>
                </div>
            </div>
            <div class="inquiry-preview">
                <p class="inquiry-preview-text">${inquiry.question_preview}</p>
            </div>
            <div class="inquiry-item-footer">
                <div class="order-info">
                    ${orderInfo}
                </div>
                <button class="view-detail-btn" onclick="viewInquiryDetail('${inquiry.inquiry_id}')">
                    상세보기
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <polyline points="9,18 15,12 9,6"></polyline>
                    </svg>
                </button>
            </div>
        </div>
    `;
}

// ─────────── 문의 상세보기 ───────────
function viewInquiryDetail(inquiryId) {
    console.log(`📋 상세보기: ${inquiryId}`);
    
    const inquiry = currentInquiryData.find(item => item.inquiry_id === inquiryId);
    if (!inquiry) {
        console.error('문의를 찾을 수 없습니다:', inquiryId);
        return;
    }
    
    currentInquiryDetail = inquiry;
    renderInquiryDetail(inquiry);
    showInquiryDetail();
}

function renderInquiryDetail(inquiry) {
    const detailContainer = document.getElementById('inquiry-detail-content');
    const inquiryIdEl = document.getElementById('detail-inquiry-id');
    const inquiryStatusEl = document.getElementById('detail-inquiry-status');
    
    if (!detailContainer) return;
    
    // 헤더 정보 업데이트
    if (inquiryIdEl) {
        inquiryIdEl.textContent = `#${inquiry.inquiry_id}`;
    }
    
    if (inquiryStatusEl) {
        inquiryStatusEl.textContent = inquiry.answer_status;
        inquiryStatusEl.className = `detail-inquiry-status status-badge status-${inquiry.answer_status === '답변완료' ? 'answered' : 'unanswered'}`;
    }
    
    // 상세 내용 생성
    const detailHTML = generateInquiryDetailHTML(inquiry);
    detailContainer.innerHTML = detailHTML;
}

function generateInquiryDetailHTML(inquiry) {
    const statusClass = inquiry.answer_status === '답변완료' ? 'answered' : 'unanswered';
    const urgentBadge = inquiry.is_urgent ? '<span class="urgent-badge">긴급</span>' : '';
    
    // 주문 정보 상세
    let orderInfoDetail = '';
    if (inquiry.product_order_number || inquiry.breach_order_number) {
        orderInfoDetail = `
            <div class="inquiry-order-info">
                ${inquiry.product_order_number ? `<div class="contact-item"><strong>상품 주문번호:</strong> ${inquiry.product_order_number}</div>` : ''}
                ${inquiry.breach_order_number ? `<div class="contact-item"><strong>브리치 주문번호:</strong> ${inquiry.breach_order_number}</div>` : ''}
            </div>
        `;
    }
    
    // 답변 목록 생성
    const answersHTML = inquiry.answers && inquiry.answers.length > 0 
        ? inquiry.answers.map(answer => generateAnswerHTML(answer)).join('')
        : '<div class="empty-state"><p>아직 답변이 없습니다.</p></div>';
    
    // 날짜 포맷팅
    const regDate = new Date(inquiry.registration_date);
    const formattedRegDate = regDate.toLocaleDateString('ko-KR') + ' ' + regDate.toLocaleTimeString('ko-KR');
    
    return `
        <div class="inquiry-detail-full">
            <div class="inquiry-header-info">
                <div class="inquiry-main-info">
                    <h4 class="inquiry-title">문의 #${inquiry.inquiry_id} ${urgentBadge}</h4>
                    <div class="inquiry-meta-row">
                        <span class="meta-item">
                            <strong>작성자:</strong> ${inquiry.author_info?.author || '정보없음'}
                        </span>
                        <span class="meta-item">
                            <strong>등록일:</strong> ${formattedRegDate}
                        </span>
                        <span class="meta-item">
                            <strong>상태:</strong> 
                            <span class="status-badge status-${statusClass}">${inquiry.answer_status}</span>
                        </span>
                    </div>
                </div>
                
                ${orderInfoDetail}
                
                <div class="inquiry-contact-info">
                    <div class="contact-item">
                        <strong>이메일:</strong> ${inquiry.author_info?.email || '정보없음'}
                    </div>
                    <div class="contact-item">
                        <strong>연락처:</strong> ${inquiry.author_info?.phone || '정보없음'}
                    </div>
                </div>
            </div>
            
            <div class="inquiry-content-section">
                <h5 class="section-title">📝 문의 내용</h5>
                <div class="inquiry-content">
                    <pre class="inquiry-text">${inquiry.question_content}</pre>
                </div>
            </div>
            
            <div class="answers-section">
                <h5 class="section-title">💬 답변 (${inquiry.answers?.length || 0}개)</h5>
                <div class="answers-list">
                    ${answersHTML}
                </div>
            </div>
        </div>
    `;
}

function generateAnswerHTML(answer) {
    const answerDate = new Date(answer.answer_date);
    const formattedAnswerDate = answerDate.toLocaleDateString('ko-KR') + ' ' + answerDate.toLocaleTimeString('ko-KR');
    
    return `
        <div class="answer-item">
            <div class="answer-header">
                <div class="answer-author">
                    <strong>${answer.author_name}</strong>
                    <span class="answer-dept">${answer.author_department}</span>
                </div>
                <div class="answer-date">${formattedAnswerDate}</div>
            </div>
            <div class="answer-content">
                <pre class="answer-text">${answer.content}</pre>
            </div>
        </div>
    `;
}

// ─────────── 뷰 전환 ───────────
function showInquiryList() {
    const listView = document.getElementById('inquiry-list-view');
    const detailView = document.getElementById('inquiry-detail-view');
    
    if (listView) listView.classList.remove('detail-mode');
    if (detailView) detailView.classList.remove('active');
}

function showInquiryDetail() {
    const listView = document.getElementById('inquiry-list-view');
    const detailView = document.getElementById('inquiry-detail-view');
    
    if (listView) listView.classList.add('detail-mode');
    if (detailView) detailView.classList.add('active');
}

// ─────────── 필터링 및 정렬 ───────────
function applyDrawerFilters() {
    let filtered = [...currentInquiryData];
    
    // 상태 필터
    const statusFilter = document.getElementById('drawer-status-filter')?.value;
    if (statusFilter && statusFilter !== 'all') {
        if (statusFilter === 'answered') {
            filtered = filtered.filter(item => item.answer_status === '답변완료');
        } else if (statusFilter === 'unanswered') {
            filtered = filtered.filter(item => item.answer_status === '미답변');
        }
    }
    
    // 검색어 필터
    const searchTerm = document.getElementById('drawer-search-input')?.value?.toLowerCase();
    if (searchTerm) {
        filtered = filtered.filter(item => 
            item.question_content.toLowerCase().includes(searchTerm) ||
            item.question_preview.toLowerCase().includes(searchTerm) ||
            item.seller.toLowerCase().includes(searchTerm)
        );
    }
    
    // 정렬
    const sortOption = document.getElementById('drawer-sort')?.value;
    if (sortOption) {
        switch(sortOption) {
            case 'latest':
                filtered.sort((a, b) => new Date(b.registration_date) - new Date(a.registration_date));
                break;
            case 'oldest':
                filtered.sort((a, b) => new Date(a.registration_date) - new Date(b.registration_date));
                break;
            case 'urgent':
                filtered.sort((a, b) => {
                    if (a.is_urgent === b.is_urgent) {
                        return new Date(b.registration_date) - new Date(a.registration_date);
                    }
                    return b.is_urgent - a.is_urgent;
                });
                break;
            case 'status':
                filtered.sort((a, b) => {
                    if (a.answer_status === b.answer_status) {
                        return new Date(b.registration_date) - new Date(a.registration_date);
                    }
                    return a.answer_status === '미답변' ? -1 : 1;
                });
                break;
        }
    }
    
    filteredInquiryData = filtered;
    updateDrawerHeader();
    renderInquiryList();
    
    console.log(`🔍 필터 적용 완료: ${filtered.length}건`);
}

// ─────────── 이벤트 리스너 ───────────
document.addEventListener('DOMContentLoaded', function() {
    console.log('🎯 드로어 이벤트 리스너 등록 중...');
    
    // 드로어 닫기 버튼
    const closeBtn = document.getElementById('drawer-close');
    if (closeBtn) {
        closeBtn.addEventListener('click', closeInquiryDrawer);
    }
    
    // 오버레이 클릭으로 닫기
    const overlay = document.getElementById('drawer-overlay');
    if (overlay) {
        overlay.addEventListener('click', closeInquiryDrawer);
    }
    
    // 뒤로가기 버튼
    const backBtn = document.getElementById('back-to-list');
    if (backBtn) {
        backBtn.addEventListener('click', showInquiryList);
    }
    
    // 정렬 및 필터 변경
    const sortSelect = document.getElementById('drawer-sort');
    if (sortSelect) {
        sortSelect.addEventListener('change', applyDrawerFilters);
    }
    
    const statusSelect = document.getElementById('drawer-status-filter');
    if (statusSelect) {
        statusSelect.addEventListener('change', applyDrawerFilters);
    }
    
    // 검색 입력
    const searchInput = document.getElementById('drawer-search-input');
    if (searchInput) {
        searchInput.addEventListener('input', debounce(applyDrawerFilters, 300));
        
        // 검색어 지우기 버튼 표시/숨김
        searchInput.addEventListener('input', function() {
            const clearBtn = document.getElementById('search-clear');
            if (clearBtn) {
                if (this.value) {
                    clearBtn.classList.remove('hidden');
                } else {
                    clearBtn.classList.add('hidden');
                }
            }
        });
    }
    
    // 검색어 지우기 버튼
    const searchClearBtn = document.getElementById('search-clear');
    if (searchClearBtn) {
        searchClearBtn.addEventListener('click', function() {
            const searchInput = document.getElementById('drawer-search-input');
            if (searchInput) {
                searchInput.value = '';
                this.classList.add('hidden');
                applyDrawerFilters();
            }
        });
    }
    
    // ESC 키로 드로어 닫기
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            const drawer = document.getElementById('inquiry-drawer');
            if (drawer && drawer.classList.contains('open')) {
                const detailView = document.getElementById('inquiry-detail-view');
                if (detailView && detailView.classList.contains('active')) {
                    // 상세보기에서 목록으로
                    showInquiryList();
                } else {
                    // 드로어 닫기
                    closeInquiryDrawer();
                }
            }
        }
    });
    
    console.log('✅ 드로어 이벤트 리스너 등록 완료');
});

// ─────────── 유틸리티 함수 ───────────
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// ─────────── 외부 연동 함수 (기존 카테고리 버튼과 연결) ───────────
window.openCategoryDrawer = function(categoryName, subCategoryName) {
    console.log(`🎯 카테고리 드로어 열기 요청: ${categoryName} > ${subCategoryName}`);
    
    // 실제 데이터는 window.rawInquiryData에서 가져온다고 가정
    if (!window.rawInquiryData) {
        console.error('❌ 원본 문의 데이터를 찾을 수 없습니다.');
        alert('문의 데이터를 불러올 수 없습니다.');
        return;
    }
    
    console.log(`📊 전체 데이터 수: ${window.rawInquiryData.length}건`);
    
    // 해당 카테고리의 문의들만 필터링 (수정된 부분)
    const categoryInquiries = window.rawInquiryData.filter(inquiry => {
        // 다양한 필드명 패턴 지원
        let inquiryCategory = null;
        
        // 1. category.sub_category (중첩 구조)
        if (inquiry.category && inquiry.category.sub_category) {
            inquiryCategory = inquiry.category.sub_category;
        }
        // 2. sub_category (평면 구조)
        else if (inquiry.sub_category) {
            inquiryCategory = inquiry.sub_category;
        }
        // 3. category (문자열)
        else if (typeof inquiry.category === 'string') {
            inquiryCategory = inquiry.category;
        }
        
        // 디버깅용 로그 (첫 5개만)
        if (window.rawInquiryData.indexOf(inquiry) < 5) {
            console.log(`🔍 문의 ${inquiry.inquiry_id}: 카테고리 = "${inquiryCategory}", 찾는 카테고리 = "${subCategoryName}"`);
        }
        
        return inquiryCategory === subCategoryName;
    });
    
    console.log(`🔍 필터링 결과: ${categoryInquiries.length}건 (전체 ${window.rawInquiryData.length}건 중)`);
    
    if (categoryInquiries.length === 0) {
        // 디버깅 정보 제공
        console.log('❌ 필터링 결과가 0건입니다. 디버깅 정보:');
        console.log(`   찾는 카테고리: "${subCategoryName}"`);
        
        // 실제 존재하는 카테고리들 확인
        const existingCategories = new Set();
        window.rawInquiryData.slice(0, 10).forEach(inquiry => {
            if (inquiry.category && inquiry.category.sub_category) {
                existingCategories.add(inquiry.category.sub_category);
            } else if (inquiry.sub_category) {
                existingCategories.add(inquiry.sub_category);
            } else if (typeof inquiry.category === 'string') {
                existingCategories.add(inquiry.category);
            }
        });
        
        console.log('   실제 존재하는 카테고리들 (샘플 10개):', Array.from(existingCategories));
        
        alert(`'${subCategoryName}' 카테고리에 해당하는 문의가 없습니다.\n\n디버깅 정보:\n- 전체 문의: ${window.rawInquiryData.length}건\n- 필터링 결과: 0건\n\n콘솔을 확인해주세요.`);
        return;
    }
    
    openInquiryDrawer(subCategoryName, categoryInquiries);
};

console.log('✅ 사이드 드로어 시스템 로딩 완료');
"""