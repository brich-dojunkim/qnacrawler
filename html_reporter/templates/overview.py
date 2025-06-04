# html_reporter/templates/overview.py
"""분석 개요 탭 템플릿들"""

def get_overview_template():
    return """<!-- 분석 개요 탭 -->
<div id="overview" class="tab-content active">
    <div class="major-section">
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
                        <div class="data-stat-name">총 문의</div>
                        <div class="data-stat-number">{total_inquiries:,}</div>
                    </div>
                    <div class="data-stat">
                        <div class="data-stat-name">긴급 문의</div>
                        <div class="data-stat-number">{urgent_count}</div>
                    </div>
                    <div class="data-stat">
                        <div class="data-stat-name">답변 완료</div>
                        <div class="data-stat-number">{answered_count}</div>
                    </div>
                    <div class="data-stat">
                        <div class="data-stat-name">답변 대기</div>
                        <div class="data-stat-number">{pending_count}</div>
                    </div>
                </div>
            </div>
            <div class="grid grid-2">
                {rank_tables}
            </div>
        </div>
    </div>
</div>"""