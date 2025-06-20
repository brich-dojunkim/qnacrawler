# html_reporter/templates/inquiry_modal/layout.py
"""
문의 상세보기 모달 기본 레이아웃 템플릿 - 3-Way 탭 스위치
"""

def get_inquiry_modal_layout():
    """문의 모달 전체 레이아웃 템플릿 - 3-Way 탭 스위치"""
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

            <!-- 3-Way 탭 스위치 필터 바 -->
            <div class="inquiry-modal-filters">
                <!-- 검색 영역 -->
                <div class="filter-group search-group">
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

                <!-- 긴급도 3-Way 탭 -->
                <div class="filter-group">
                    <div class="bordered-tab-group urgency-tabs">
                        <button class="bordered-tab-btn active all" data-value="all" onclick="selectUrgencyTab('all')">전체</button>
                        <button class="bordered-tab-btn urgent" data-value="urgent" onclick="selectUrgencyTab('urgent')">긴급</button>
                        <button class="bordered-tab-btn normal" data-value="normal" onclick="selectUrgencyTab('normal')">일반</button>
                    </div>
                </div>

                <!-- 상태 3-Way 탭 -->
                <div class="filter-group">
                    <div class="bordered-tab-group status-tabs">
                        <button class="bordered-tab-btn active all" data-value="all" onclick="selectStatusTab('all')">전체</button>
                        <button class="bordered-tab-btn completed" data-value="completed" onclick="selectStatusTab('completed')">완료</button>
                        <button class="bordered-tab-btn pending" data-value="pending" onclick="selectStatusTab('pending')">미답변</button>
                    </div>
                </div>

                <!-- 정렬 버튼들 -->
                <div class="filter-group sort-group">
                    <button id="sort-latest" class="accordion-filter-sort active" onclick="setSortOrder('latest')">
                        <span class="sort-text">최신순</span>
                        <span class="sort-direction">▼</span>
                    </button>
                    <button id="sort-length_desc" class="accordion-filter-sort" onclick="setSortOrder('length_desc')">
                        <span class="sort-text">문의길이순</span>
                        <span class="sort-direction">▼</span>
                    </button>
                </div>

                <!-- 새로고침 버튼 -->
                <div class="filter-actions">
                    <button id="refresh-inquiries" class="filter-action-btn" onclick="refreshAndResetFilters()" title="필터 초기화 및 새로고침">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <polyline points="23 4 23 10 17 10"></polyline>
                            <polyline points="1 20 1 14 7 14"></polyline>
                            <path d="M20.49 9A9 9 0 0 0 5.64 5.64L1 10m22 4l-4.64 4.36A9 9 0 0 1 3.51 15"></path>
                        </svg>
                    </button>
                </div>
            </div>

            <!-- 문의 목록 영역 -->
            <div class="inquiry-modal-body">
                <div id="inquiry-list-container" class="inquiry-list-container">
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
                        <button class="clear-filters-btn" onclick="refreshAndResetFilters()">필터 초기화</button>
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