# html_reporter/templates/team.py
"""팀별 분석 탭 템플릿들 (제목 제거 + 3 + 4 레이아웃)"""

def get_team_section_template():
    return """<!-- 팀별 분석 탭 -->
<div id="teams" class="tab-content">
    <div class="teams-layout">
        {team_cards}
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
        <li><span class="metric-name">답변률</span><span class="metric-number">{answer_rate}%</span></li>
        <li><span class="metric-name">평균길이</span><span class="metric-number">{avg_content_length}</span></li>
    </ul>
    {sub_categories}
</div>"""
