# html_reporter/templates/inquiry_modal/layout.py
"""
문의 상세보기 모달 기본 레이아웃 템플릿 - inquiry-list 요소 추가
"""

def get_inquiry_modal_layout():
    """문의 모달 전체 레이아웃 템플릿 - 누락된 inquiry-list 추가"""
    return """
    <!-- 문의 상세보기 모달 -->
    <div id="inquiry-detail-modal" class="inquiry-modal-overlay">
        <div class="inquiry-modal-content">
            <!-- 모달 헤더 -->
            <div class="inquiry-modal-header">
                <div class="inquiry-modal-title-section">
                    <h3 id="inquiry-modal-title" class="inquiry-modal-title">
                        📂 카테고리 문의 목록
                    </h3>
                    <div id="inquiry-modal-stats" class="inquiry-modal-stats">
                        <span class="stat-item">
                            <span class="stat-icon">📊</span>
                            <span class="stat-label">총 문의:</span>
                            <span id="total-inquiries-count" class="stat-value">0</span>
                        </span>
                        <span class="stat-item">
                            <span class="stat-icon">🚨</span>
                            <span class="stat-label">긴급:</span>
                            <span id="urgent-inquiries-count" class="stat-value">0</span>
                        </span>
                        <span class="stat-item">
                            <span class="stat-icon">✅</span>
                            <span class="stat-label">완료:</span>
                            <span id="completed-inquiries-count" class="stat-value">0</span>
                        </span>
                        <span class="stat-item">
                            <span class="stat-icon">📏</span>
                            <span class="stat-label">평균길이:</span>
                            <span id="avg-length" class="stat-value">0</span>자
                        </span>
                    </div>
                </div>
                <button class="inquiry-modal-close" onclick="closeInquiryModal()">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <line x1="18" y1="6" x2="6" y2="18"></line>
                        <line x1="6" y1="6" x2="18" y2="18"></line>
                    </svg>
                </button>
            </div>
            
            <!-- 필터 바 -->
            <div class="inquiry-modal-filters">
                <div class="filter-group">
                    <div class="search-wrapper">
                        <svg class="search-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <circle cx="11" cy="11" r="8"></circle>
                            <path d="m21 21-4.35-4.35"></path>
                        </svg>
                        <input type="text" id="inquiry-search" placeholder="문의 내용 검색..." class="search-input">
                        <button id="clear-search" class="clear-search-btn" style="display: none;" onclick="clearInquirySearch()">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <line x1="18" y1="6" x2="6" y2="18"></line>
                                <line x1="6" y1="6" x2="18" y2="18"></line>
                            </svg>
                        </button>
                    </div>
                </div>
                
                <div class="filter-group">
                    <select id="team-filter" class="filter-select">
                        <option value="">👥 모든 팀</option>
                    </select>
                </div>
                
                <div class="filter-group">
                    <select id="urgency-filter" class="filter-select">
                        <option value="">🚨 모든 긴급도</option>
                        <option value="urgent">긴급</option>
                        <option value="normal">일반</option>
                    </select>
                </div>
                
                <div class="filter-group">
                    <select id="status-filter" class="filter-select">
                        <option value="">📋 모든 상태</option>
                        <option value="answered">답변완료</option>
                        <option value="pending">답변대기</option>
                        <option value="in_progress">진행중</option>
                    </select>
                </div>
                
                <div class="filter-group">
                    <select id="sort-filter" class="filter-select">
                        <option value="latest">📅 최신순</option>
                        <option value="urgent">🚨 긴급순</option>
                        <option value="length_desc">📏 긴 문의순</option>
                        <option value="length_asc">📏 짧은 문의순</option>
                        <option value="team">👥 팀별순</option>
                    </select>
                </div>
                
                <div class="filter-actions">
                    <button id="refresh-inquiries" class="filter-action-btn" onclick="refreshInquiryModal()" title="새로고침">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <polyline points="23 4 23 10 17 10"></polyline>
                            <polyline points="1 20 1 14 7 14"></polyline>
                            <path d="M20.49 9A9 9 0 0 0 5.64 5.64L1 10m22 4l-4.64 4.36A9 9 0 0 1 3.51 15"></path>
                        </svg>
                    </button>
                    <button id="clear-filters" class="filter-action-btn" onclick="clearAllInquiryFilters()" title="필터 초기화">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <line x1="18" y1="6" x2="6" y2="18"></line>
                            <line x1="6" y1="6" x2="18" y2="18"></line>
                        </svg>
                    </button>
                </div>
            </div>
            
            <!-- 문의 목록 영역 -->
            <div class="inquiry-modal-body">
                <div id="inquiry-list-container" class="inquiry-list-container">
                    <!-- 📌 중요: inquiry-list div 추가! -->
                    <div id="inquiry-list" class="inquiry-list">
                        <!-- 문의 카드들이 여기에 동적으로 추가됩니다 -->
                    </div>
                    
                    <!-- 로딩 상태 -->
                    <div id="inquiry-loading" class="inquiry-loading" style="display: none;">
                        <div class="loading-spinner"></div>
                        <span>문의 목록을 불러오는 중...</span>
                    </div>
                    
                    <!-- 빈 상태 -->
                    <div id="no-inquiries" class="no-inquiries" style="display: none;">
                        <div class="no-inquiries-icon">📭</div>
                        <div class="no-inquiries-text">조건에 맞는 문의가 없습니다.</div>
                        <button class="clear-filters-btn" onclick="clearAllInquiryFilters()">필터 초기화</button>
                    </div>
                </div>
            </div>
            
            <!-- 페이지네이션 푸터 -->
            <div class="inquiry-modal-footer">
                <div class="pagination-info">
                    <span id="pagination-text">0개 문의 중 0-0개 표시</span>
                </div>
                <div id="pagination-controls" class="pagination-controls">
                    <button id="prev-page" class="pagination-btn" onclick="goToPreviousPage()" disabled>
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <polyline points="15 18 9 12 15 6"></polyline>
                        </svg>
                        이전
                    </button>
                    <div id="page-numbers" class="page-numbers">
                        <!-- 페이지 번호들이 여기에 동적으로 추가됩니다 -->
                    </div>
                    <button id="next-page" class="pagination-btn" onclick="goToNextPage()" disabled>
                        다음
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <polyline points="9 18 15 12 9 6"></polyline>
                        </svg>
                    </button>
                </div>
                <div class="results-per-page">
                    <select id="items-per-page" class="items-per-page-select" onchange="changeItemsPerPage()">
                        <option value="10">10개씩</option>
                        <option value="20" selected>20개씩</option>
                        <option value="50">50개씩</option>
                        <option value="100">100개씩</option>
                    </select>
                </div>
            </div>
        </div>
    </div>
    """