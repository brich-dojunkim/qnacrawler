# html_reporter/templates/overview.py (컨트롤 바 모듈화 적용)
"""개요 템플릿 - 단일 페이지, 완료율 칼럼 포함, 문의 모달 지원 - 컨트롤 바 모듈화"""

def get_overview_template():
    """단일 페이지 템플릿 - 컨트롤 바 모듈화 적용"""
    return """
    <div class="main-content-wrapper">
        <div class="detailed-analysis-section">
            {controls_bar_template}
            
            <div class="accordion-content-area">
                <!-- 팀별 아코디언 뷰 (기본 활성화) -->
                <div id="teams-accordion-view" class="analysis-view active">
                    <div class="teams-accordion-container">
                        {team_accordion_items}
                    </div>
                </div>
                
                <!-- 여정별 아코디언 뷰 -->
                <div id="journey-accordion-view" class="analysis-view">
                    <div class="journey-accordion-container">
                        {journey_accordion_items}
                    </div>
                </div>
                
                <!-- 카테고리 테이블 뷰 (완료율 칼럼 추가) -->
                <div id="categories-table-view" class="analysis-view">
                    {complete_category_table_template}
                </div>
            </div>
        </div>
        
        <!-- 문의 모달 템플릿 (모듈화됨) -->
        {inquiry_modal_template}
    </div>
    """