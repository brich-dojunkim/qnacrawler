# html_reporter/templates/overview.py (개선된 디자인 적용)
"""분석 개요 탭 템플릿들 - 개선된 상세 분석 섹션"""

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
    
    <!-- 개선된 상세 분석 섹션 -->
    <div class="detailed-analysis-section">
        <!-- 섹션 헤더 -->
        <div class="section-header">
            <h2 class="section-title">상세 분석</h2>
        </div>

        <!-- 통합 컨트롤 바 -->
        <div class="controls-bar">
            <div class="view-toggle-group">
                <span class="view-toggle-label">보기 방식:</span>
                <div class="view-toggle-controls">
                    <input type="radio" id="view-teams" name="analysis-view" value="teams" checked>
                    <label for="view-teams" class="toggle-btn">👥 팀별 보기</label>
                    
                    <input type="radio" id="view-journey" name="analysis-view" value="journey">
                    <label for="view-journey" class="toggle-btn">🎯 여정별 보기</label>
                </div>
            </div>
            
            <div class="bulk-controls">
                <button class="bulk-control-btn" onclick="expandAllAccordions()">전체 펼치기</button>
                <button class="bulk-control-btn" onclick="collapseAllAccordions()">전체 접기</button>
            </div>
        </div>

        <!-- 아코디언 컨텐츠 영역 -->
        <div class="accordion-content-area">
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
    </div>
</div>"""