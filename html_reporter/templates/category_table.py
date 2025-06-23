# html_reporter/templates/category_table.py (테이블 필터 헤더 통합)
"""카테고리 테이블 전체 템플릿 - 로우, 필터 헤더, 상태 표시 등 모든 테이블 관련 기능"""

def get_category_table_row_template():
    """개별 카테고리 테이블 로우 템플릿 - 문의율 칼럼 포함 + 문의 모달 연결"""
    return """<div class="category-table-row" 
             data-team="{main_team}" 
             data-journey="{main_journey}" 
             data-inquiries="{total_inquiries}" 
             data-urgent="{urgent_rate}"
             data-complete="{answer_rate}"
             data-category="{name_lower}"
             data-category-name="{name}">
    <div class="category-name">{name}</div>
    <div><span class="team-badge">{main_team}</span></div>
    <div><span class="journey-badge">{main_journey}</span></div>
    <div class="metric-value">{inquiry_rate}%</div>
    <div class="urgent-rate {urgent_level}">{urgent_rate}%</div>
    <div class="complete-rate {complete_level}">{answer_rate}%</div>
    <div>
        <button class="action-btn" onclick="openInquiryModal('category', '{name}')" title="상세 문의 보기">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                <circle cx="11" cy="11" r="8"></circle>
                <path d="m21 21-4.35-4.35"></path>
            </svg>
        </button>
    </div>
</div>"""

def get_table_filter_header_template():
    """테이블 필터 헤더 템플릿 - 칼럼명, 필터, 정렬 버튼 포함"""
    return """<div class="table-filter-header">
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
</div>"""

def get_table_filter_status_template():
    """테이블 필터 상태 표시 템플릿"""
    return """<div id="table-filter-status" class="table-filter-status">
    전체 카테고리 표시 중 (<span id="visible-categories-count">0</span>개)
    <button class="clear-table-filters" onclick="clearAllTableFilters()" style="display: none;">모든 필터 제거</button>
</div>"""

def get_complete_category_table_template():
    """완전한 카테고리 테이블 템플릿 - 상태 표시 + 필터 헤더 + 테이블 바디"""
    return """<div class="category-table-container">
    {table_filter_status}
    
    <div class="category-table">
        {table_filter_header}
        
        <div class="category-table-body">
            {category_table_rows}
        </div>
    </div>
</div>"""

def get_team_filter_options(teams):
    """팀 필터 옵션 생성"""
    options = []
    for team in sorted(teams):
        if team != '기타':
            options.append(f'<option value="{team}">{team}</option>')
    return '\n                                                '.join(options)

def get_journey_filter_options():
    """여정 필터 옵션 생성 - 고정된 여정 목록"""
    journeys = [
        "계정·입점", "상품·콘텐츠", "주문·배송", 
        "반품·취소", "정산", "기타"
    ]
    options = []
    for journey in journeys:
        options.append(f'<option value="{journey}">{journey}</option>')
    return '\n                        '.join(options)