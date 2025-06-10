# html_reporter/templates/journey.py
"""유저 여정 탭 템플릿 – 제목 제거 + 가로 한 줄(5등분) 레이아웃"""

# ────────────────────────── 섹션(탭) 레벨 ──────────────────────────
def get_journey_section_template():
    """
    여정(stage) 카드들을 담는 섹션 전체 HTML을 반환합니다.
    {journey_cards} 자리표시자에 개별 카드 HTML을 연결해 넣어 주세요.
    """
    return """<!-- 유저 여정 탭 -->
<div id="journey" class="tab-content">
    <div class="grid grid-5">
        {journey_cards}
    </div>
</div>"""


# ────────────────────────── 카드(여정) 레벨 ──────────────────────────
def get_journey_card_template():
    """
    개별 여정(stage) 정보를 렌더링하는 카드 HTML 템플릿.
    빌더에서 .format(**data) 로 값을 채워 넣어 사용합니다.
    """
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
