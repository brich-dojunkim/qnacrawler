# html_reporter/templates/overview.py (수정된 버전 - inquiry-list 요소 확실히 포함)
"""개요 템플릿 - 단일 페이지, 완료율 칼럼 포함, 문의 모달 지원 - inquiry-list 요소 확실히 포함"""

def get_overview_template():
    """단일 페이지 템플릿 - 완료율 칼럼이 추가된 뷰 + 문의 모달 (inquiry-list 확실히 포함)"""
    return """
    <div class="main-content-wrapper">
        <div class="detailed-analysis-section">
            <div class="controls-bar">
                <div class="view-toggle-group">
                    <div class="view-toggle-controls">
                        <input type="radio" name="analysis-view" value="teams" id="teams-view" checked>
                        <label for="teams-view" class="toggle-btn">팀별 분석</label>
                        
                        <input type="radio" name="analysis-view" value="journey" id="journey-view">
                        <label for="journey-view" class="toggle-btn">여정별 분석</label>
                        
                        <input type="radio" name="analysis-view" value="categories" id="categories-view">
                        <label for="categories-view" class="toggle-btn">카테고리 테이블</label>
                    </div>
                </div>
                
                <div class="bulk-controls">
                    <div class="accordion-controls">
                        <div class="accordion-sort-controls">
                            <button class="accordion-sort-btn" data-sort="total" onclick="sortAccordions('total')" title="문의율 기준 정렬">
                                문의율
                                <span class="sort-direction">▼</span>
                            </button>
                            <button class="accordion-sort-btn" data-sort="urgent" onclick="sortAccordions('urgent')" title="긴급률 기준 정렬">
                                긴급률
                                <span class="sort-direction">▼</span>
                            </button>
                            <button class="accordion-sort-btn" data-sort="completed" onclick="sortAccordions('completed')" title="완료율 기준 정렬">
                                완료율
                                <span class="sort-direction">▼</span>
                            </button>
                            <button class="accordion-sort-btn journey-only" data-sort="journey" onclick="sortAccordions('journey')" title="여정 순서 기준 정렬">
                                여정순서
                                <span class="sort-direction">▼</span>
                            </button>
                        </div>
                        <div class="bulk-actions">
                            <button class="bulk-control-btn" onclick="expandAllAccordions()">전체 펼치기</button>
                            <button class="bulk-control-btn" onclick="collapseAllAccordions()">전체 접기</button>
                        </div>
                    </div>
                    
                    <div class="table-controls">
                        <button class="bulk-control-btn" onclick="exportTableData()">내보내기</button>
                        <button class="bulk-control-btn" onclick="resetTableFilters()">필터 초기화</button>
                    </div>
                </div>
            </div>
            
            <div class="accordion-content-area">
                <!-- 팀별 아코디언 뷰 (기본 활성화) -->
                <div id="teams-accordion-view" class="analysis-view active">
                    <div class="teams-accordion-container">
                        {team_accordion_items}
                    </div>
                </div>
                
                <!-- 여정별 아코디언 뷰 -->
                <div id="journey-accordion-view" class="analysis-view">
                    <div class="journey-accordion-container">
                        {journey_accordion_items}
                    </div>
                </div>
                
                <!-- 카테고리 테이블 뷰 (완료율 칼럼 추가) -->
                <div id="categories-table-view" class="analysis-view">
                    <div class="category-table-container">
                        <div id="table-filter-status" class="table-filter-status">
                            전체 카테고리 표시 중 (<span id="visible-categories-count">0</span>개)
                            <button class="clear-table-filters" onclick="clearAllTableFilters()" style="display: none;">모든 필터 제거</button>
                        </div>
                        
                        <div class="category-table">
                            <div class="table-filter-header">
                                <div class="filter-column">
                                    <div class="column-header">
                                        <span class="column-label">카테고리명</span>
                                    </div>
                                </div>
                                
                                <div class="filter-column">
                                    <div class="column-header">
                                        <span class="column-label">담당팀</span>
                                        <div class="filter-dropdown-wrapper">
                                            <button class="filter-icon-btn" onclick="toggleTeamFilter()" title="팀 필터">
                                                <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3">
                                                    <polygon points="22,3 2,3 10,12.46 10,19 14,21 14,12.46"></polygon>
                                                </svg>
                                            </button>
                                            <div id="team-dropdown" class="dropdown-menu hidden">
                                                <select id="team-filter-dropdown" class="dropdown-filter-select" onchange="filterByTeam(this.value)">
                                                    <option value="">전체 팀</option>
                                                    {team_filter_options}
                                                </select>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                
                                <div class="filter-column">
                                    <div class="column-header">
                                        <span class="column-label">유저여정</span>
                                        <div class="filter-dropdown-wrapper">
                                            <button class="filter-icon-btn" onclick="toggleJourneyFilter()" title="여정 필터">
                                                <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3">
                                                    <polygon points="22,3 2,3 10,12.46 10,19 14,21 14,12.46"></polygon>
                                                </svg>
                                            </button>
                                            <div id="journey-dropdown" class="dropdown-menu hidden">
                                                <select id="journey-filter-dropdown" class="dropdown-filter-select" onchange="filterByJourney(this.value)">
                                                    <option value="">전체 여정</option>
                                                    <option value="계정·입점">계정·입점</option>
                                                    <option value="상품·콘텐츠">상품·콘텐츠</option>
                                                    <option value="주문·배송">주문·배송</option>
                                                    <option value="반품·취소">반품·취소</option>
                                                    <option value="정산">정산</option>
                                                    <option value="기타">기타</option>
                                                </select>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                
                                <div class="filter-column">
                                    <div class="column-header">
                                        <span class="column-label">문의율</span>
                                        <button id="inquiries-sort" class="sort-icon-btn" onclick="sortByInquiries()" title="문의율 정렬">
                                            <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3">
                                                <path d="m7 15 5 5 5-5"></path>
                                                <path d="m7 9 5-5 5 5"></path>
                                            </svg>
                                        </button>
                                    </div>
                                </div>
                                
                                <div class="filter-column">
                                    <div class="column-header">
                                        <span class="column-label">긴급률</span>
                                        <button id="urgent-sort" class="sort-icon-btn" onclick="sortByUrgent()" title="긴급률 정렬">
                                            <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3">
                                                <path d="m7 15 5 5 5-5"></path>
                                                <path d="m7 9 5-5 5 5"></path>
                                            </svg>
                                        </button>
                                    </div>
                                </div>
                                
                                <div class="filter-column">
                                    <div class="column-header">
                                        <span class="column-label">완료율</span>
                                        <button id="complete-sort" class="sort-icon-btn" onclick="sortByComplete()" title="완료율 정렬">
                                            <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3">
                                                <path d="m7 15 5 5 5-5"></path>
                                                <path d="m7 9 5-5 5 5"></path>
                                            </svg>
                                        </button>
                                    </div>
                                </div>
                                
                                <div class="filter-column">
                                    <div class="column-header">
                                        <span class="column-label">상세보기</span>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="category-table-body">
                                {category_table_rows}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- 🔧 수정된 문의 상세보기 모달 - inquiry-list div 확실히 포함! -->
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
                
                <!-- 🚨 핵심 수정: 문의 목록 영역 - inquiry-list div 확실히 포함! -->
                <div class="inquiry-modal-body">
                    <div id="inquiry-list-container" class="inquiry-list-container">
                        <!-- ✅ 가장 중요한 부분: inquiry-list div가 반드시 있어야 함! -->
                        <div id="inquiry-list" class="inquiry-list">
                            <!-- 📝 JavaScript의 createInquiryCard() 함수로 생성된 카드들이 여기에 추가됩니다 -->
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
        
        <!-- 드로어 영역 (있다면) -->
        {drawer_html}
    </div>
    """