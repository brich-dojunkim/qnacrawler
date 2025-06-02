# html_reporter/templates.py
"""HTML 템플릿 모음"""

def get_base_template():
    return """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>카테고리 기반 VoC 분석 보고서</title>
    <link href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" rel="stylesheet">
    <style>{styles}</style>
</head>
<body>
    <div class="container">
        {header}
        <div class="main-content">
            {content}
        </div>
        {footer}
    </div>
    {scripts}
</body>
</html>"""

def get_header_template():
    return """<div class="header">
    <h1>카테고리 기반 VoC 분석</h1>
    <p>고객 문의 데이터의 카테고리별 분석 결과</p>
    <p>{analysis_date}</p>
</div>"""

def get_overview_template():
    return """<div class="major-section">
    <div class="major-section-header">
        <h2>분석 개요</h2>
    </div>
    <div class="major-section-content">
        <div class="data-overview">
            <div class="data-overview-header">
                <h3 class="entity-card-title">데이터 현황</h3>
                <span class="entity-card-badge">{total_inquiries:,}건</span>
            </div>
            <div class="data-stats">
                <div class="data-stat">
                    <div class="data-stat-name">총문의</div>
                    <div class="data-stat-number">{total_inquiries:,}</div>
                </div>
                <div class="data-stat">
                    <div class="data-stat-name">긴급문의</div>
                    <div class="data-stat-number">{urgent_count}</div>
                </div>
            </div>
        </div>
        <div class="grid grid-2">
            {rank_tables}
        </div>
    </div>
</div>"""

def get_team_section_template():
    return """<div class="major-section">
    <div class="major-section-header">
        <h2>팀별 문의 내용 분석</h2>
    </div>
    <div class="major-section-content">
        <div class="grid grid-4">
            {team_cards}
        </div>
    </div>
</div>"""

def get_team_card_template():
    return """<div class="entity-card">
    <div class="entity-card-header">
        <h3 class="entity-card-title">{name}</h3>
        <span class="entity-card-badge">{total_inquiries}건</span>
    </div>
    <ul class="metrics-list">
        <li><span class="metric-name">총 문의</span><span class="metric-number">{total_inquiries}</span></li>
        <li><span class="metric-name">긴급</span><span class="metric-number">{urgent_count}</span></li>
        <li><span class="metric-name">답변완료</span><span class="metric-number">{answered_count}</span></li>
        <li><span class="metric-name">평균길이</span><span class="metric-number">{avg_content_length}</span></li>
    </ul>
    {sub_categories}
</div>"""

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

def get_journey_section_template():
    return """<div class="major-section">
    <div class="major-section-header">
        <h2>유저 여정별 문의 내용 분석</h2>
    </div>
    <div class="major-section-content">
        <div class="grid grid-5">
            {journey_cards}
        </div>
    </div>
</div>"""

def get_journey_card_template():
    return """<div class="entity-card">
    <div class="entity-card-header">
        <h3 class="entity-card-title">{name}</h3>
        <span class="entity-card-badge">{total_inquiries}건</span>
    </div>
    <ul class="metrics-list">
        <li><span class="metric-name">총 문의</span><span class="metric-number">{total_inquiries}</span></li>
        <li><span class="metric-name">긴급</span><span class="metric-number">{urgent_count}</span></li>
        <li><span class="metric-name">답변완료</span><span class="metric-number">{answered_count}</span></li>
        <li><span class="metric-name">평균길이</span><span class="metric-number">{avg_content_length}</span></li>
    </ul>
    {sub_categories}
</div>"""

def get_footer_template():
    return """<div class="footer">
    <p>카테고리 기반 VoC 분석 보고서</p>
    <p>생성일시: {generated_at} | Pretendard 폰트 적용</p>
</div>"""