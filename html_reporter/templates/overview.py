# html_reporter/templates/overview.py (최종 수정 - 새 모달 + 개선된 아이콘)
"""분석 개요 탭 템플릿들 - 새 모달 시스템 + 개선된 아이콘 위치"""

def get_overview_template():
    return """<!-- 통합 분석 개요 탭 -->
<div id="overview" class="tab-content active">
    <!-- 전체 현황 -->
    <div class="main-stats-grid">
        <div class="stat-card-large">
            <div class="stat-info">
                <div class="stat-number-large">{total_inquiries:,}</div>
                <div class="stat-label-large">총 문의</div>
            </div>
        </div>
        <div class="stat-card-small urgent">
            <div class="stat-number-medium">{urgent_count}</div>
            <div class="stat-label-medium">긴급 문의</div>
            <div class="stat-progress">
                <div class="progress-bar-small">
                    <div class="progress-fill-small urgent" style="width: {urgent_rate}%"></div>
                </div>
                <span class="progress-text">{urgent_rate}%</span>
            </div>
        </div>
        <div class="stat-card-small completed">
            <div class="stat-number-medium">{answered_count}</div>
            <div class="stat-label-medium">답변 완료</div>
            <div class="stat-progress">
                <div class="progress-bar-small">
                    <div class="progress-fill-small completed" style="width: {answer_rate}%"></div>
                </div>
                <span class="progress-text">{answer_rate}%</span>
            </div>
        </div>
        <div class="stat-card-small pending">
            <div class="stat-number-medium">{pending_count}</div>
            <div class="stat-label-medium">답변 대기</div>
            <div class="stat-progress">
                <div class="progress-bar-small">
                    <div class="progress-fill-small pending" style="width: {pending_rate}%"></div>
                </div>
                <span class="progress-text">{pending_rate}%</span>
            </div>
        </div>
    </div>
    
    <!-- 상세 분석 섹션 -->
    <div class="detailed-analysis-section">
        <!-- 섹션 헤더 -->
        <div class="section-header">
            <h2 class="section-title">상세 분석</h2>
        </div>

        <!-- 통합 컨트롤 바 -->
        <div class="controls-bar">
            <div class="view-toggle-group">
                <span class="view-toggle-label">보기 방식:</span>
                <div class="view-toggle-controls">
                    <input type="radio" id="view-teams" name="analysis-view" value="teams" checked>
                    <label for="view-teams" class="toggle-btn">👥 팀별 보기</label>
                    
                    <input type="radio" id="view-journey" name="analysis-view" value="journey">
                    <label for="view-journey" class="toggle-btn">🎯 여정별 보기</label>
                    
                    <input type="radio" id="view-categories" name="analysis-view" value="categories">
                    <label for="view-categories" class="toggle-btn">📂 카테고리별 보기</label>
                </div>
            </div>
            
            <!-- 아코디언 컨트롤 (팀별/여정별일 때) -->
            <div class="bulk-controls accordion-controls">
                <button class="bulk-control-btn" onclick="expandAllAccordions()">전체 펼치기</button>
                <button class="bulk-control-btn" onclick="collapseAllAccordions()">전체 접기</button>
            </div>
            
            <!-- 테이블 컨트롤 (카테고리별일 때) -->
            <div class="bulk-controls table-controls" style="display: none;">
                <button class="bulk-control-btn" onclick="resetTableFilters()">🔄 필터 초기화</button>
                <button class="bulk-control-btn" onclick="exportTableData()">📥 내보내기</button>
            </div>
        </div>

        <!-- 아코디언 컨텐츠 영역 -->
        <div class="accordion-content-area">
            <!-- 팀별 아코디언 뷰 -->
            <div id="teams-accordion-view" class="analysis-view active">
                <div class="teams-accordion-container">
                    {team_accordion_items}
                </div>
            </div>
            
            <!-- 여정별 아코디언 뷰 -->
            <div id="journey-accordion-view" class="analysis-view" style="display: none;">
                <div class="journey-accordion-container">
                    {journey_accordion_items}
                </div>
            </div>
            
            <!-- 카테고리별 테이블 뷰 -->
            <div id="categories-table-view" class="analysis-view" style="display: none;">
                <!-- 필터 상태 표시 -->
                <div class="table-filter-status" id="table-filter-status">
                    📂 <strong>전체 카테고리</strong> 표시 중 (<span id="visible-categories-count">0</span>개)
                    <button class="clear-table-filters" onclick="clearAllTableFilters()" style="display: none;">모든 필터 지우기</button>
                </div>
                
                <!-- 테이블 컨테이너 -->
                <div class="category-table-container">
                    <div class="category-table">
                        <!-- 텍스트 옆 아이콘 + 드롭다운 헤더 -->
                        <div class="table-filter-header">
                            <div class="filter-column">
                                <div class="column-header">
                                    <span class="column-label">카테고리명</span>
                                    <div class="filter-dropdown-wrapper">
                                        <button class="filter-icon-btn" onclick="toggleSearchFilter()" title="카테고리 검색">
                                            <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3">
                                                <circle cx="11" cy="11" r="8"></circle>
                                                <path d="m21 21-4.35-4.35"></path>
                                            </svg>
                                        </button>
                                        <div class="dropdown-menu hidden" id="search-dropdown">
                                            <input type="text" class="dropdown-filter-input" id="category-search-input" 
                                                   placeholder="카테고리 검색..." oninput="filterByCategory(this.value)">
                                        </div>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="filter-column">
                                <div class="column-header">
                                    <span class="column-label">담당팀</span>
                                    <div class="filter-dropdown-wrapper">
                                        <button class="filter-icon-btn" onclick="toggleTeamFilter()" title="팀 필터">
                                            <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3">
                                                <path d="M6 9l6 6 6-6"></path>
                                            </svg>
                                        </button>
                                        <div class="dropdown-menu hidden" id="team-dropdown">
                                            <select class="dropdown-filter-select" id="team-filter-dropdown" onchange="filterByTeam(this.value)">
                                                <option value="">모든 팀</option>
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
                                                <path d="M6 9l6 6 6-6"></path>
                                            </svg>
                                        </button>
                                        <div class="dropdown-menu hidden" id="journey-dropdown">
                                            <select class="dropdown-filter-select" id="journey-filter-dropdown" onchange="filterByJourney(this.value)">
                                                <option value="">모든 여정</option>
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
                                    <span class="column-label">문의수</span>
                                    <button class="sort-icon-btn" onclick="sortByInquiries()" id="inquiries-sort" title="문의수 정렬">
                                        <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3">
                                            <path d="M7 13l5 5 5-5"></path>
                                        </svg>
                                    </button>
                                </div>
                            </div>
                            
                            <div class="filter-column">
                                <div class="column-header">
                                    <span class="column-label">긴급률</span>
                                    <button class="sort-icon-btn" onclick="sortByUrgent()" id="urgent-sort" title="긴급률 정렬">
                                        <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3">
                                            <path d="M7 13l5 5 5-5"></path>
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

                        <!-- 카테고리 데이터 로우들 -->
                        <div class="category-table-body" id="category-table-body">
                            {category_table_rows}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>"""