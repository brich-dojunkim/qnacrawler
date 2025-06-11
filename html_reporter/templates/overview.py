# html_reporter/templates/overview.py (아이디어 2 적용)
"""분석 개요 탭 템플릿들 - 팀별 아코디언 통합 버전"""

def get_overview_template():
    return """<!-- 통합 분석 개요 탭 -->
<div id="overview" class="tab-content active">
    <!-- 전체 현황 -->
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
    
    <!-- 유저 여정별 분포 (기존 유지) -->
    <div class="distribution-grid">
        {journey_rank_table}
    </div>
    
    <!-- 팀별 아코디언 분석 -->
    <div class="teams-accordion-section">
        <h2 style="margin-bottom: 20px;">👥 팀별 분석</h2>
        <div class="teams-accordion-container">
            {team_accordion_items}
        </div>
    </div>
</div>"""