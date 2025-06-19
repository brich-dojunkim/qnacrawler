# html_reporter/templates/overview.py
"""개요 템플릿 - 단일 페이지, 완료율 칼럼 포함, 문의 모달 지원 - 하드코딩 제거"""

def get_overview_template():
    """단일 페이지 템플릿 - 완료율 칼럼이 추가된 뷰 + 문의 모달 (import 방식)"""
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
        
        <!-- 🚨 중요: 하드코딩 제거 - inquiry_modal_template으로 대체 -->
        {inquiry_modal_template}
        
        <!-- 드로어 영역 (있다면) -->
        {drawer_html}
    </div>
    """