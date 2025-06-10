# html_reporter/templates/category.py
"""세부 카테고리 탭 템플릿들 - 헤더 배지 레이아웃 개선 (완전 수정버전)"""

def get_category_section_template():
    return """<!-- 세부 카테고리 탭 -->
<div id="categories" class="tab-content">
    <div class="filter-buttons">
        <button class="filter-btn active" onclick="filterCategories('all')">전체</button>
        <button class="filter-btn" onclick="filterCategories('team')">팀별</button>
        <button class="filter-btn" onclick="filterCategories('journey')">유저여정별</button>
    </div>
    <div class="grid grid-3" id="categories-container">
        {category_cards}
    </div>
</div>"""


def get_category_card_template():
    """수정된 카테고리 카드 템플릿 - 제목과 배지들을 가로 일렬로 배치"""
    return """<div class="entity-card" data-team="{main_team}" data-journey="{main_journey}" data-count="{total_inquiries}">
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