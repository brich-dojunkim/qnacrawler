# html_reporter/templates/inquiry_modal/inquiry_card.py (JavaScript 함수 포함)
"""
개별 문의 카드 템플릿 - JavaScript에서 사용할 함수 포함
"""

def get_inquiry_card_template():
    """개별 문의 카드 템플릿 - JavaScript에서 동적 생성용"""
    return """
    function createInquiryCard(inquiry) {
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
            <div class="inquiry-card" data-inquiry-id="\${inquiry.inquiry_id || 'unknown'}">
                <div class="inquiry-card-header">
                    <div class="inquiry-meta">
                        <span class="urgency-badge \${urgencyClass}">
                            <span class="urgency-icon">\${urgencyIcon}</span>
                            \${urgencyText}
                        </span>
                        <span class="team-badge">\${inquiry.assigned_team || '미분류'}</span>
                        <span class="category-badge">\${inquiry.sub_category || '기타'}</span>
                        <span class="date-badge">\${formattedDate}</span>
                    </div>
                    <div class="inquiry-actions">
                        <span class="status-badge \${statusClass}">
                            <span class="status-icon">\${statusIcon}</span>
                            \${statusText}
                        </span>
                    </div>
                </div>
                
                <div class="inquiry-card-body">
                    <div class="inquiry-content">
                        <div class="content-preview">\${highlightedPreview}</div>
                        \${content.length > 200 ? `
                            <button class="show-full-content" onclick="toggleFullContent(this)">
                                <span class="expand-text">전체 보기</span>
                                <span class="collapse-text" style="display: none;">접기</span>
                                <svg class="expand-icon" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <polyline points="6 9 12 15 18 9"></polyline>
                                </svg>
                            </button>
                            <div class="full-content" style="display: none;">
                                \${highlightSearchTerm(content, window.currentSearchTerm || '')}
                            </div>
                        ` : ''}
                    </div>
                    
                    \${hasAnswer ? `
                        <div class="answer-section">
                            <div class="answer-header">
                                <span class="answer-label">💬 답변</span>
                                <span class="answer-meta">\${inquiry.answers[0].answerer_info?.name || '담당자'} | \${new Date(inquiry.answers[0].answer_date).toLocaleDateString('ko-KR')}</span>
                            </div>
                            <div class="answer-preview">\${answerPreview}</div>
                            \${inquiry.answers[0].answer_content && inquiry.answers[0].answer_content.length > 100 ? `
                                <button class="show-full-answer" onclick="toggleFullAnswer(this)">
                                    <span class="expand-text">답변 전체 보기</span>
                                    <span class="collapse-text" style="display: none;">답변 접기</span>
                                </button>
                                <div class="full-answer" style="display: none;">
                                    \${inquiry.answers[0].answer_content}
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
                            ID: \${inquiry.inquiry_id || 'N/A'}
                        </span>
                        <span class="stat-item">
                            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                                <polyline points="14 2 14 8 20 8"></polyline>
                                <line x1="16" y1="13" x2="8" y2="13"></line>
                                <line x1="16" y1="17" x2="8" y2="17"></line>
                                <polyline points="10 9 9 9 8 9"></polyline>
                            </svg>
                            \${content.length}자
                        </span>
                        \${inquiry.answers && inquiry.answers.length > 0 ? `
                            <span class="stat-item">
                                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
                                </svg>
                                답변 \${inquiry.answers.length}개
                            </span>
                        ` : ''}
                    </div>
                    
                    <div class="inquiry-actions-footer">
                        \${hasAnswer ? `
                            <button class="action-btn secondary" onclick="showInquiryAnswers('\${inquiry.inquiry_id}')">
                                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
                                </svg>
                                전체 답변
                            </button>
                        ` : ''}
                        <button class="action-btn primary" onclick="showInquiryDetail('\${inquiry.inquiry_id}')">
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
    }
    """

def get_inquiry_list_template():
    """문의 목록 컨테이너 템플릿"""
    return """
    <!-- 문의 목록은 JavaScript에서 동적으로 생성됩니다 -->
    <div id="inquiry-list" class="inquiry-list">
        <!-- createInquiryCard() 함수로 생성된 카드들이 여기에 추가됩니다 -->
    </div>
    """

def get_loading_template():
    """로딩 스피너 템플릿"""
    return """
    <div class="inquiry-loading">
        <div class="loading-spinner"></div>
        <span>문의 목록을 불러오는 중...</span>
    </div>
    """

def get_empty_state_template():
    """빈 상태 템플릿"""
    return """
    <div class="no-inquiries">
        <div class="no-inquiries-icon">📭</div>
        <div class="no-inquiries-text">조건에 맞는 문의가 없습니다.</div>
        <button class="clear-filters-btn" onclick="clearAllInquiryFilters()">필터 초기화</button>
    </div>
    """