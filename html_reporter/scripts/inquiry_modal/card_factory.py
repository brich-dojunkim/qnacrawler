# html_reporter/scripts/inquiry_modal/card_factory.py
"""
문의 카드 생성 팩토리 모듈 - 답변 관련 요소 제거
"""

def get_card_factory_scripts():
    """카드 생성 팩토리 스크립트 - 답변 관련 요소 제거"""
    return """
// ─────────── 문의 카드 생성 팩토리 ───────────
console.log('🏭 문의 카드 생성 팩토리 로딩 중...');

// ─────────── 메인 카드 생성 함수 ───────────
window.createInquiryCard = function(inquiry) {
    console.log('🎨 문의 카드 생성:', inquiry);
    
    try {
        const cardData = extractCardData(inquiry);
        return generateCardHTML(cardData);
    } catch (error) {
        console.error('❌ 카드 생성 오류:', error, inquiry);
        return createErrorCard(inquiry);
    }
};

// ─────────── 카드 데이터 추출 ───────────
function extractCardData(inquiry) {
    // 긴급도 정보
    const urgencyIcon = inquiry.is_urgent ? '🚨' : '📋';
    const urgencyClass = inquiry.is_urgent ? 'urgent' : 'normal';
    const urgencyText = inquiry.is_urgent ? '긴급' : '일반';
    
    // 상태 정보
    const statusIcon = inquiry.answer_status === '답변완료' ? '✅' : 
                      inquiry.answer_status === '진행중' ? '🔄' : '⏳';
    const statusClass = inquiry.answer_status === '답변완료' ? 'completed' : 
                       inquiry.answer_status === '진행중' ? 'in-progress' : 'pending';
    const statusText = inquiry.answer_status || '답변대기';
    
    // 날짜 포맷팅
    const date = new Date(inquiry.registration_date);
    const formattedDate = date.toLocaleDateString('ko-KR') + ' ' + 
                         date.toLocaleTimeString('ko-KR', {hour: '2-digit', minute: '2-digit'});
    
    // 문의 내용 처리
    const content = inquiry.question_content || '';
    const preview = content.length > 200 ? content.substring(0, 200) + '...' : content;
    const highlightedPreview = highlightSearchTerm(preview, window.currentSearchTerm || '');
    
    // 🚨 중요: 팀/카테고리 정보 제거 - 이제 모달 헤더에 표시
    
    // 판매자와 작성자 정보
    const sellerName = inquiry.seller || '판매자';
    const authorFull = inquiry.author_info?.author || '';
    const authorName = authorFull.includes('(') 
        ? authorFull.split('(')[0].trim() 
        : authorFull || '작성자';
    const authorEmail = inquiry.author_info?.email || '';
    const authorPhone = inquiry.author_info?.phone || '';

    // 답변 정보
    const hasAnswer = inquiry.answers && inquiry.answers.length > 0;
    let answerPreview = '';
    let answerAuthor = '담당자';
    let answerDate = '';
    let answerContent = '';
    
    if (hasAnswer) {
        const firstAnswer = inquiry.answers[0];
        answerContent = firstAnswer.content || '';
        answerPreview = answerContent.length > 100 ? 
            answerContent.substring(0, 100) + '...' : answerContent;
        
        answerAuthor = firstAnswer.author_name || '담당자';
        answerDate = firstAnswer.answer_date || '';

        if (answerDate) {
            answerDate = new Date(answerDate).toLocaleDateString('ko-KR');
        }
    }
    
    return {
        id: inquiry.inquiry_id || 'unknown',
        urgencyIcon, urgencyClass, urgencyText,
        statusIcon, statusClass, statusText,
        sellerName, authorName, authorEmail, authorPhone,
        formattedDate, content, preview, highlightedPreview,
        hasAnswer, answerPreview, answerAuthor, answerDate, answerContent
    };
}

// ─────────── 카드 HTML 생성 ───────────
function generateCardHTML(data) {
    return `
        <div class="inquiry-card" data-inquiry-id="${data.id}">
            ${generateCardHeader(data)}
            ${generateCardBody(data)}
            ${generateCardFooter(data)}
        </div>
    `;
}

// ─────────── 카드 헤더 생성 (팀/카테고리 배지 제거) ───────────
function generateCardHeader(data) {
    return `
        <div class="inquiry-card-header">
            <div class="inquiry-meta">
                <span class="urgency-badge ${data.urgencyClass}">
                    <span class="urgency-icon">${data.urgencyIcon}</span>
                    ${data.urgencyText}
                </span>
                <span class="seller-badge">🏢${data.sellerName}</span>
                <span class="author-badge" onclick="showAuthorInfo('${data.authorEmail}', '${data.authorPhone}', '${data.authorName}')" 
                    title="클릭하여 연락처 보기" style="cursor: pointer;">✍️${data.authorName}</span>
                <span class="date-badge">${data.formattedDate}</span>
            </div>
            <div class="inquiry-actions">
                <span class="status-badge ${data.statusClass}">
                    <span class="status-icon">${data.statusIcon}</span>
                    ${data.statusText}
                </span>
            </div>
        </div>
    `;
}

// ─────────── 카드 본문 생성 ───────────
function generateCardBody(data) {
    return `
        <div class="inquiry-card-body">
            <div class="inquiry-content">
                <div class="content-preview">${data.highlightedPreview}</div>
                ${data.content.length > 200 ? generateExpandButton(data) : ''}
            </div>
            ${data.hasAnswer ? generateAnswerSection(data) : ''}
        </div>
    `;
}

// ─────────── 확장 버튼 생성 ───────────
function generateExpandButton(data) {
    return `
        <button class="show-full-content" onclick="toggleFullContent(this)">
            <span class="expand-text">전체 보기</span>
            <span class="collapse-text" style="display: none;">접기</span>
            <svg class="expand-icon" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
        </button>
        <div class="full-content" style="display: none;">
            ${highlightSearchTerm(data.content, window.currentSearchTerm || '')}
        </div>
    `;
}

// ─────────── 답변 섹션 생성 ───────────
function generateAnswerSection(data) {
    return `
        <div class="answer-section">
            <div class="answer-header">
                <span class="answer-label">💬 답변</span>
                <span class="answer-meta">${data.answerAuthor}${data.answerDate ? ' | ' + data.answerDate : ''}</span>
            </div>
            <div class="answer-preview">${data.answerPreview}</div>
            ${data.answerPreview.length > 100 ? generateAnswerExpandButton(data) : ''}
        </div>
    `;
}

// ─────────── 답변 확장 버튼 생성 ───────────
function generateAnswerExpandButton(data) {
    return `
        <button class="show-full-answer" onclick="toggleFullAnswer(this)">
            <span class="expand-text">답변 전체 보기</span>
            <span class="collapse-text" style="display: none;">답변 접기</span>
        </button>
        <div class="full-answer" style="display: none;">
            ${data.answerContent || ''}
        </div>
    `;
}

// ─────────── 카드 푸터 생성 (답변 관련 요소 제거) ───────────
function generateCardFooter(data) {
    return `
        <div class="inquiry-card-footer">
            <div class="inquiry-stats">
                <span class="stat-item">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                        <polyline points="14 2 14 8 20 8"></polyline>
                    </svg>
                    ID: ${data.id}
                </span>
                <span class="stat-item">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                        <polyline points="14 2 14 8 20 8"></polyline>
                        <line x1="16" y1="13" x2="8" y2="13"></line>
                        <line x1="16" y1="17" x2="8" y2="17"></line>
                        <polyline points="10 9 9 9 8 9"></polyline>
                    </svg>
                    ${data.content.length}자
                </span>
            </div>
        </div>
    `;
}

// ─────────── 간단한 카드 생성 (fallback) ───────────
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

// ─────────── 검색어 하이라이팅 ───────────
window.highlightSearchTerm = function(text, searchTerm) {
    if (!searchTerm || !text) return text;
    
    try {
        const regex = new RegExp(`(${searchTerm.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&')})`, 'gi');
        return text.replace(regex, '<mark class="search-highlight">$1</mark>');
    } catch (error) {
        console.warn('⚠️ 검색어 하이라이팅 오류:', error);
        return text;
    }
};

console.log('✅ 문의 카드 생성 팩토리 로딩 완료');
"""