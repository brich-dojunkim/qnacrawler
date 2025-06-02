# html_reporter/templates/category.py
"""📂 세부 카테고리 탭 템플릿들"""

def get_category_section_template():
    return """<div class="major-section">
    <div class="major-section-header">
        <h2>세부 카테고리별 문의 내용</h2>
    </div>
    <div class="major-section-content">
        <div class="filter-buttons">
            <button class="filter-btn active" onclick="filterCategories('all')">전체</button>
            <button class="filter-btn" onclick="filterCategories('team')">팀별</button>
            <button class="filter-btn" onclick="filterCategories('journey')">유저여정별</button>
        </div>
        <div class="grid grid-3" id="categories-container">
            {category_cards}
        </div>
    </div>
</div>"""

def get_category_card_template():
    return """<div class="entity-card" data-team="{main_team}" data-journey="{main_journey}" data-count="{total_inquiries}">
    <div class="entity-card-header">
        <h3 class="entity-card-title" style="font-size: 1rem; line-height: 1.4;">{name}</h3>
        <span class="entity-card-badge">{total_inquiries}건</span>
    </div>
    <ul class="metrics-list">
        <li><span class="metric-name">총 문의</span><span class="metric-number">{total_inquiries}</span></li>
        <li><span class="metric-name">긴급</span><span class="metric-number">{urgent_count}</span></li>
        <li><span class="metric-name">평균길이</span><span class="metric-number">{avg_content_length}</span></li>
    </ul>
    <div style="margin: 1rem 0;">
        <h4 class="small-subsection-title">담당팀</h4>
        <div class="team-badges">
            {team_badges}
        </div>
        <h4 class="small-subsection-title">유저 여정</h4>
        <div style="margin: 0.5rem 0;">
            <span class="journey-badge">{main_journey}</span>
        </div>
    </div>
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