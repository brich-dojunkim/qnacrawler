# html_reporter/templates/base.py (통합 대시보드 헤더)
"""공통 베이스 템플릿들 - 통합 대시보드 헤더"""

def get_base_template():
    return """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>카테고리 기반 VoC 분석 보고서</title>
    <link href="https://fonts.googleapis.com/css2?family=Pretendard:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>{styles}</style>
</head>
<body>
    <div class="container">
        {header}

        <div class="main-content">
            {content}
        </div>

        {footer}
    </div>
    {scripts}
</body>
</html>"""

def get_header_template():
    return """<div class="dashboard-header">
    <div class="dashboard-title">📊 VoC 분석 대시보드</div>
    
    <div class="dashboard-stats">
        <div class="stats-line">
            총 <strong>{total_inquiries:,}건</strong> | 긴급 <strong>{urgent_count}건</strong>({urgent_rate}%) | 완료율 <strong>{answer_rate}%</strong>
        </div>
        <div class="insights-line">
            주요단계: <strong>{main_journey}</strong> | 최다팀: <strong>{top_team}</strong>
        </div>
        <div class="date-line">📅 {analysis_date} 기준</div>
    </div>
</div>"""

def get_footer_template():
    return """<div class="footer">
    <p>카테고리 기반 VoC 분석 보고서</p>
    <p>생성일시: {generated_at} | Pretendard 폰트 적용</p>
</div>"""