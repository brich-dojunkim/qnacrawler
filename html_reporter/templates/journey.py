# html_reporter/templates/journey.py
"""유저 여정 탭 템플릿들"""

def get_journey_section_template():
    return """<!-- 유저 여정 탭 -->
<div id="journey" class="tab-content">
    <div class="major-section">
        <div class="major-section-header">
            <h2>유저 여정별 문의 내용 분석</h2>
        </div>
        <div class="major-section-content">
            <div class="grid grid-4">
                {journey_cards}
            </div>
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
        <li><span class="metric-name">답변률</span><span class="metric-number">{answer_rate}%</span></li>
        <li><span class="metric-name">평균길이</span><span class="metric-number">{avg_content_length}</span></li>
    </ul>
    {sub_categories}
</div>"""