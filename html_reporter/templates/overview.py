# html_reporter/templates/overview.py (개선된 버전)
"""분석 개요 탭 템플릿들 - 대시보드 스타일 개선"""

def get_overview_template():
    return """<!-- 분석 개요 탭 -->
<div id="overview" class="tab-content active">
    <!-- 실시간 현황 -->
    <div class="main-stats-grid">
        <div class="stat-card-large">
            <div class="stat-info">
                <div class="stat-number-large">{total_inquiries:,}</div>
                <div class="stat-label-large">총 문의</div>
            </div>
        </div>
        <div class="stat-card-small urgent">
            <div class="stat-number-medium">{urgent_count}</div>
            <div class="stat-label-medium">긴급 문의</div>
            <div class="stat-progress">
                <div class="progress-bar-small">
                    <div class="progress-fill-small urgent" style="width: {urgent_rate}%"></div>
                </div>
                <span class="progress-text">{urgent_rate}%</span>
            </div>
        </div>
        <div class="stat-card-small completed">
            <div class="stat-number-medium">{answered_count}</div>
            <div class="stat-label-medium">답변 완료</div>
            <div class="stat-progress">
                <div class="progress-bar-small">
                    <div class="progress-fill-small completed" style="width: {answer_rate}%"></div>
                </div>
                <span class="progress-text">{answer_rate}%</span>
            </div>
        </div>
        <div class="stat-card-small pending">
            <div class="stat-number-medium">{pending_count}</div>
            <div class="stat-label-medium">답변 대기</div>
            <div class="stat-progress">
                <div class="progress-bar-small">
                    <div class="progress-fill-small pending" style="width: {pending_rate}%"></div>
                </div>
                <span class="progress-text">{pending_rate}%</span>
            </div>
        </div>
    </div>
    
    <!-- 상세 분포 -->
    <div class="distribution-grid">
        {rank_tables}
    </div>
</div>"""