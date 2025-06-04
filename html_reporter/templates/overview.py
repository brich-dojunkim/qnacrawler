# html_reporter/templates/overview.py
"""분석 개요 탭 템플릿들 - 개선된 디자인"""

def get_overview_template():
    return """<!-- 분석 개요 탭 -->
<div id="overview" class="tab-content active">
    <div class="major-section">
        <div class="major-section-header">
            <h2>분석 개요</h2>
        </div>
        <div class="major-section-content">
            <!-- 상단: 통계 + 상태 -->
            <div class="overview-top-section">
                <div class="stats-overview">
                    <div class="main-stats-grid">
                        <div class="stat-card-large">
                            <div class="stat-icon">📋</div>
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
                </div>
            </div>
            
            <!-- 중앙: 인사이트 카드 -->
            <div class="insights-section">
                <div class="insight-card">
                    <h3 class="insight-title">주요 발견사항</h3>
                    <div class="insight-items">
                        {insights_content}
                    </div>
                </div>
            </div>
            
            <!-- 하단: 순위표 -->
            <div class="rankings-section">
                <div class="grid grid-2">
                    {rank_tables}
                </div>
            </div>
        </div>
    </div>
</div>"""
