# html_reporter/templates/drawer.py
"""
사이드 드로어 템플릿 - 문의 상세보기용
"""

def get_drawer_template():
    """사이드 드로어 메인 템플릿"""
    return """
    <!-- 사이드 드로어 -->
    <div id="inquiry-drawer" class="inquiry-drawer">
        <div class="drawer-overlay" id="drawer-overlay"></div>
        <div class="drawer-panel">
            <div class="drawer-header">
                <div class="drawer-title-section">
                    <h3 id="drawer-category-name" class="drawer-category-name">카테고리명</h3>
                    <span id="drawer-inquiry-count" class="drawer-inquiry-count">0건</span>
                </div>
                <div class="drawer-controls">
                    <select id="drawer-sort" class="drawer-select">
                        <option value="latest">최신순</option>
                        <option value="oldest">오래된순</option>
                        <option value="urgent">긴급순</option>
                        <option value="status">답변상태순</option>
                    </select>
                    <select id="drawer-status-filter" class="drawer-select">
                        <option value="all">전체</option>
                        <option value="unanswered">미답변</option>
                        <option value="answered">답변완료</option>
                    </select>
                    <button id="drawer-close" class="drawer-close-btn" title="닫기">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <line x1="18" y1="6" x2="6" y2="18"></line>
                            <line x1="6" y1="6" x2="18" y2="18"></line>
                        </svg>
                    </button>
                </div>
            </div>
            
            <div class="drawer-search">
                <div class="search-input-wrapper">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="search-icon">
                        <circle cx="11" cy="11" r="8"></circle>
                        <path d="m21 21-4.35-4.35"></path>
                    </svg>
                    <input type="text" id="drawer-search-input" placeholder="문의 내용 검색..." class="drawer-search-input">
                    <button id="search-clear" class="search-clear-btn hidden" title="검색어 지우기">✕</button>
                </div>
            </div>
            
            <div class="drawer-content">
                <!-- 문의 목록 뷰 -->
                <div id="inquiry-list-view" class="inquiry-list-view">
                    <div id="inquiry-list" class="inquiry-list">
                        <!-- 문의 목록이 동적으로 생성됨 -->
                    </div>
                    <div id="inquiry-list-empty" class="inquiry-list-empty hidden">
                        <div class="empty-state">
                            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1">
                                <path d="M9 11H5a2 2 0 0 0-2 2v7a2 2 0 0 0 2 2h7a2 2 0 0 0 2-2v-4"></path>
                                <circle cx="16" cy="5" r="3"></circle>
                            </svg>
                            <h4>문의가 없습니다</h4>
                            <p>해당 조건에 맞는 문의를 찾을 수 없습니다.</p>
                        </div>
                    </div>
                    <div id="inquiry-list-loading" class="inquiry-list-loading hidden">
                        <div class="loading-spinner"></div>
                        <p>문의를 불러오는 중...</p>
                    </div>
                </div>
                
                <!-- 문의 상세보기 뷰 -->
                <div id="inquiry-detail-view" class="inquiry-detail-view hidden">
                    <div class="detail-header">
                        <button id="back-to-list" class="back-btn">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <polyline points="15,18 9,12 15,6"></polyline>
                            </svg>
                            목록으로
                        </button>
                        <div class="detail-inquiry-info">
                            <span id="detail-inquiry-id" class="detail-inquiry-id">#123456</span>
                            <span id="detail-inquiry-status" class="detail-inquiry-status">미답변</span>
                        </div>
                    </div>
                    <div id="inquiry-detail-content" class="inquiry-detail-content">
                        <!-- 상세 내용이 여기에 표시됨 -->
                    </div>
                </div>
            </div>
        </div>
    </div>
    """

def get_inquiry_item_template():
    """개별 문의 아이템 템플릿"""
    return """
    <div class="inquiry-item" data-inquiry-id="{inquiry_id}" data-status="{answer_status}" data-urgent="{is_urgent}">
        <div class="inquiry-item-header">
            <div class="inquiry-id-section">
                <span class="inquiry-id">#{inquiry_id}</span>
                <div class="inquiry-badges">
                    {urgent_badge}
                    <span class="status-badge status-{status_class}">{answer_status}</span>
                </div>
            </div>
            <div class="inquiry-meta">
                <span class="inquiry-date">{registration_date}</span>
                <span class="inquiry-seller">{seller}</span>
            </div>
        </div>
        <div class="inquiry-preview">
            <p class="inquiry-preview-text">{question_preview}</p>
        </div>
        <div class="inquiry-item-footer">
            <div class="order-info">
                {order_info}
            </div>
            <button class="view-detail-btn" onclick="viewInquiryDetail('{inquiry_id}')">
                상세보기
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <polyline points="9,18 15,12 9,6"></polyline>
                </svg>
            </button>
        </div>
    </div>
    """

def get_inquiry_detail_template():
    """문의 상세보기 템플릿"""
    return """
    <div class="inquiry-detail-full">
        <div class="inquiry-header-info">
            <div class="inquiry-main-info">
                <h4 class="inquiry-title">문의 #{inquiry_id}</h4>
                <div class="inquiry-meta-row">
                    <span class="meta-item">
                        <strong>작성자:</strong> {author_name}
                    </span>
                    <span class="meta-item">
                        <strong>등록일:</strong> {registration_date}
                    </span>
                    <span class="meta-item">
                        <strong>상태:</strong> 
                        <span class="status-badge status-{status_class}">{answer_status}</span>
                    </span>
                </div>
            </div>
            
            <div class="inquiry-order-info">
                {order_info_detail}
            </div>
            
            <div class="inquiry-contact-info">
                <div class="contact-item">
                    <strong>이메일:</strong> {email}
                </div>
                <div class="contact-item">
                    <strong>연락처:</strong> {phone}
                </div>
            </div>
        </div>
        
        <div class="inquiry-content-section">
            <h5 class="section-title">📝 문의 내용</h5>
            <div class="inquiry-content">
                <pre class="inquiry-text">{question_content}</pre>
            </div>
        </div>
        
        <div class="answers-section">
            <h5 class="section-title">💬 답변 ({answer_count}개)</h5>
            <div class="answers-list">
                {answers_html}
            </div>
        </div>
    </div>
    """

def get_answer_item_template():
    """답변 아이템 템플릿"""
    return """
    <div class="answer-item">
        <div class="answer-header">
            <div class="answer-author">
                <strong>{author_name}</strong>
                <span class="answer-dept">{author_department}</span>
            </div>
            <div class="answer-date">{answer_date}</div>
        </div>
        <div class="answer-content">
            <pre class="answer-text">{content}</pre>
        </div>
    </div>
    """