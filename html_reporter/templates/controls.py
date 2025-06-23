# html_reporter/templates/controls.py
"""컨트롤 바 템플릿 - 뷰 토글, 정렬, 벌크 액션 등 모든 컨트롤 요소들"""

def get_controls_bar_template():
    """전체 컨트롤 바 템플릿 - overview.py에서 사용"""
    return """<div class="controls-bar">
    <div class="view-toggle-group">
        <div class="view-toggle-controls">
            <input type="radio" name="analysis-view" value="teams" id="teams-view" checked>
            <label for="teams-view" class="toggle-btn">팀별 분석</label>
            
            <input type="radio" name="analysis-view" value="journey" id="journey-view">
            <label for="journey-view" class="toggle-btn">여정별 분석</label>
            
            <input type="radio" name="analysis-view" value="categories" id="categories-view">
            <label for="categories-view" class="toggle-btn">카테고리 테이블</label>
        </div>
    </div>
    
    <div class="bulk-controls">
        <div class="accordion-controls">
            <div class="accordion-sort-controls">
                <button class="accordion-sort-btn" data-sort="total" onclick="sortAccordions('total')" title="문의율 기준 정렬">
                    문의율
                    <span class="sort-direction">▼</span>
                </button>
                <button class="accordion-sort-btn" data-sort="urgent" onclick="sortAccordions('urgent')" title="긴급률 기준 정렬">
                    긴급률
                    <span class="sort-direction">▼</span>
                </button>
                <button class="accordion-sort-btn" data-sort="completed" onclick="sortAccordions('completed')" title="완료율 기준 정렬">
                    완료율
                    <span class="sort-direction">▼</span>
                </button>
                <button class="accordion-sort-btn journey-only" data-sort="journey" onclick="sortAccordions('journey')" title="여정 순서 기준 정렬">
                    여정순서
                    <span class="sort-direction">▼</span>
                </button>
            </div>
            <div class="bulk-actions">
                <button class="bulk-control-btn" onclick="expandAllAccordions()">전체 펼치기</button>
                <button class="bulk-control-btn" onclick="collapseAllAccordions()">전체 접기</button>
            </div>
        </div>
        
        <div class="table-controls">
            <button class="bulk-control-btn" onclick="exportTableData()">내보내기</button>
            <button class="bulk-control-btn" onclick="resetTableFilters()">필터 초기화</button>
        </div>
    </div>
</div>"""

def get_view_toggle_controls():
    """뷰 토글 컨트롤만 별도로 필요한 경우"""
    return """<div class="view-toggle-controls">
    <input type="radio" name="analysis-view" value="teams" id="teams-view" checked>
    <label for="teams-view" class="toggle-btn">팀별 분석</label>
    
    <input type="radio" name="analysis-view" value="journey" id="journey-view">
    <label for="journey-view" class="toggle-btn">여정별 분석</label>
    
    <input type="radio" name="analysis-view" value="categories" id="categories-view">
    <label for="categories-view" class="toggle-btn">카테고리 테이블</label>
</div>"""

def get_accordion_sort_controls():
    """아코디언 정렬 컨트롤만 별도로 필요한 경우"""
    return """<div class="accordion-sort-controls">
    <button class="accordion-sort-btn" data-sort="total" onclick="sortAccordions('total')" title="문의율 기준 정렬">
        문의율
        <span class="sort-direction">▼</span>
    </button>
    <button class="accordion-sort-btn" data-sort="urgent" onclick="sortAccordions('urgent')" title="긴급률 기준 정렬">
        긴급률
        <span class="sort-direction">▼</span>
    </button>
    <button class="accordion-sort-btn" data-sort="completed" onclick="sortAccordions('completed')" title="완료율 기준 정렬">
        완료율
        <span class="sort-direction">▼</span>
    </button>
    <button class="accordion-sort-btn journey-only" data-sort="journey" onclick="sortAccordions('journey')" title="여정 순서 기준 정렬">
        여정순서
        <span class="sort-direction">▼</span>
    </button>
</div>"""

def get_bulk_actions():
    """벌크 액션 버튼들만 별도로 필요한 경우"""
    return """<div class="bulk-actions">
    <button class="bulk-control-btn" onclick="expandAllAccordions()">전체 펼치기</button>
    <button class="bulk-control-btn" onclick="collapseAllAccordions()">전체 접기</button>
</div>"""

def get_table_controls():
    """테이블 컨트롤만 별도로 필요한 경우"""
    return """<div class="table-controls">
    <button class="bulk-control-btn" onclick="exportTableData()">내보내기</button>
    <button class="bulk-control-btn" onclick="resetTableFilters()">필터 초기화</button>
</div>"""