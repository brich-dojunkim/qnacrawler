# html_reporter/scripts/drawer/rendering.py
"""
드로어 렌더링 및 상세보기 기능
"""

def get_drawer_rendering_scripts():
    """드로어 렌더링 관련 스크립트"""
    return """
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

console.log('✅ 드로어 렌더링 기능 로딩 완료');
"""