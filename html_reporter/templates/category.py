# html_reporter/templates/category.py
"""세부 카테고리 탭 템플릿들 - 세그먼트 선택 + 정렬 기준 방식"""

def get_category_section_template():
    return """<!-- 세부 카테고리 탭 -->
<div id="categories" class="tab-content">
    <div class="filter-controls">
        <!-- 세그먼트 선택 드롭다운 -->
        <div class="filter-group">
            <label class="filter-label">보기 범위</label>
            <div class="segment-selector">
                <select id="segment-select" class="segment-dropdown">
                    <option value="all">전체 카테고리</option>
                    <optgroup label="팀별">
                        {team_options}
                    </optgroup>
                    <optgroup label="유저 여정별">
                        <option value="journey-계정·입점">계정·입점</option>
                        <option value="journey-상품·콘텐츠">상품·콘텐츠</option>
                        <option value="journey-주문·배송">주문·배송</option>
                        <option value="journey-반품·취소">반품·취소</option>
                        <option value="journey-정산">정산</option>
                        <option value="journey-기타">기타</option>
                    </optgroup>
                </select>
            </div>
        </div>
        
        <!-- 정렬 기준 세그먼트 -->
        <div class="filter-group">
            <label class="filter-label">정렬 기준</label>
            <div class="segment-control" id="sortSegment">
                <input type="radio" id="sort-volume" name="sort-type" value="volume" checked>
                <label for="sort-volume" class="segment-item">문의량별</label>
                
                <input type="radio" id="sort-urgent" name="sort-type" value="urgent">
                <label for="sort-urgent" class="segment-item">긴급도별</label>
                
                <input type="radio" id="sort-answer" name="sort-type" value="answer">
                <label for="sort-answer" class="segment-item">답변률별</label>
            </div>
        </div>
    </div>
    
    <!-- 현재 선택된 세그먼트 표시 -->
    <div class="current-segment-info">
        <span class="segment-indicator">
            📂 <span id="current-segment-text">전체 카테고리</span>
            (<span id="visible-count">0</span>개 표시)
        </span>
    </div>
    
    <div class="grid grid-3" id="categories-container">
        {category_cards}
    </div>
</div>"""


def get_category_card_template():
    """카테고리 카드 템플릿 - 제목과 배지들을 가로 일렬로 배치"""
    return """<div class="entity-card" data-team="{main_team}" data-journey="{main_journey}" data-count="{total_inquiries}" data-urgent-rate="{urgent_rate}" data-answer-rate="{answer_rate}">
    <div class="entity-card-header">
        <h3 class="entity-card-title" style="font-size: 1rem; line-height: 1.4;">{name}</h3>
        <div class="header-badges">
            <span class="journey-badge">{main_journey}</span>
            <div class="team-badges">
                {team_badges}
            </div>
        </div>
    </div>
    <ul class="metrics-list">
        <li><span class="metric-name">총 문의</span><span class="metric-number">{total_inquiries}</span></li>
        <li><span class="metric-name">긴급</span><span class="metric-number">{urgent_count}</span></li>
        <li><span class="metric-name">긴급률</span><span class="metric-number">{urgent_rate}%</span></li>
        <li><span class="metric-name">평균길이</span><span class="metric-number">{avg_content_length}</span></li>
    </ul>
    <button class="modal-trigger" onclick="openModal('{modal_id}')">
        문의 내용 보기 ({total_inquiries}건)
    </button>
</div>"""


def get_modal_template():
    return """<div class="modal-overlay" id="{modal_id}" onclick="closeModal('{modal_id}')">
    <div class="modal-content" onclick="event.stopPropagation()">
        <div class="modal-header">
            <h3 class="modal-title">{title}</h3>
            <button class="modal-close" onclick="closeModal('{modal_id}')">&times;</button>
        </div>
        <div class="modal-body">
            {content}
        </div>
    </div>
</div>"""