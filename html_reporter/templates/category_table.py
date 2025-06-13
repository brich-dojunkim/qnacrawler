# html_reporter/templates/category_table.py (완료율 칼럼 추가된 버전)
"""카테고리 테이블 로우 템플릿 - 완료율 칼럼 포함"""

def get_category_table_row_template():
    """개별 카테고리 테이블 로우 템플릿 - 완료율 칼럼 포함"""
    return """<div class="category-table-row" 
             data-team="{main_team}" 
             data-journey="{main_journey}" 
             data-inquiries="{total_inquiries}" 
             data-urgent="{urgent_rate}"
             data-complete="{answer_rate}"
             data-category="{name_lower}"
             data-category-name="{name}">
    <div class="category-name">{name}</div>
    <div><span class="team-badge">{main_team}</span></div>
    <div><span class="journey-badge">{main_journey}</span></div>
    <div class="metric-value">{total_inquiries}건</div>
    <div class="urgent-rate {urgent_level}">{urgent_rate}%</div>
    <div class="complete-rate {complete_level}">{answer_rate}%</div>
    <div>
        <button class="action-btn" onclick="openCategoryModal(this)" title="상세 문의 보기">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                <circle cx="11" cy="11" r="8"></circle>
                <path d="m21 21-4.35-4.35"></path>
            </svg>
        </button>
    </div>
</div>"""

def get_team_filter_options(teams):
    """팀 필터 옵션 생성"""
    options = []
    for team in sorted(teams):
        if team != '기타':
            options.append(f'<option value="{team}">{team}</option>')
    return '\n                                                '.join(options)