# html_reporter/templates/category_table.py (새 파일)
"""카테고리 테이블 로우 템플릿"""

def get_category_table_row_template():
    """개별 카테고리 테이블 로우 템플릿"""
    return """<div class="category-table-row" 
             data-team="{main_team}" 
             data-journey="{main_journey}" 
             data-inquiries="{total_inquiries}" 
             data-urgent="{urgent_rate}"
             data-category="{name_lower}">
    <div class="category-name">{name}</div>
    <div><span class="team-badge">{main_team}</span></div>
    <div><span class="journey-badge">{main_journey}</span></div>
    <div class="metric-value">{total_inquiries}건</div>
    <div class="urgent-rate {urgent_level}">{urgent_rate}%</div>
    <div><button class="action-btn" onclick="openModal('{modal_id}')">👁️</button></div>
</div>"""

def get_team_filter_options(teams):
    """팀 필터 옵션 생성"""
    options = []
    for team in sorted(teams):
        if team != '기타':
            options.append(f'<option value="{team}">{team}</option>')
    return '\n                                    '.join(options)