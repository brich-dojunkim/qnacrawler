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
    
    <!-- 팀별/여정별 토글 분석 -->
    <div class="analysis-toggle-section">
        <div class="section-header-with-toggle">
            <h2>📋 상세 분석</h2>
            <div class="analysis-toggle-controls">
                <input type="radio" id="view-teams" name="analysis-view" value="teams" checked>
                <label for="view-teams" class="toggle-btn">👥 팀별 보기</label>
                
                <input type="radio" id="view-journey" name="analysis-view" value="journey">
                <label for="view-journey" class="toggle-btn">🎯 여정별 보기</label>
            </div>
        </div>
        
        <!-- 팀별 아코디언 뷰 -->
        <div id="teams-accordion-view" class="analysis-view active">
            <div class="teams-accordion-container">
                {team_accordion_items}
            </div>
        </div>
        
        <!-- 여정별 아코디언 뷰 -->
        <div id="journey-accordion-view" class="analysis-view" style="display: none;">
            <div class="journey-accordion-container">
                {journey_accordion_items}
            </div>
        </div>
    </div>
</div>"""