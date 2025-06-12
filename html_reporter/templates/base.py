# html_reporter/templates/base.py (깔끔한 헤더 버전)
"""공통 베이스 템플릿들 - 기존 디자인 유지하면서 헤더만 구분"""

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
    <div class="header-title">📊 VoC 분석 대시보드</div>
    
    <div class="header-metrics">
        <div class="metric-card total">
            <div class="metric-icon">📋</div>
            <div class="metric-content">
                <div class="metric-label">총 문의</div>
                <div class="metric-value">{total_inquiries:,}건</div>
            </div>
        </div>
        
        <div class="metric-card urgent">
            <div class="metric-icon">🚨</div>
            <div class="metric-content">
                <div class="metric-label">긴급률</div>
                <div class="metric-value">{urgent_rate}% ({urgent_count}건)</div>
            </div>
        </div>
        
        <div class="metric-card completed">
            <div class="metric-icon">✅</div>
            <div class="metric-content">
                <div class="metric-label">완료율</div>
                <div class="metric-value">{answer_rate}%</div>
            </div>
        </div>
        
        <div class="metric-card status">
            <div class="metric-icon">📊</div>
            <div class="metric-content">
                <div class="metric-label">주요 현황</div>
                <div class="metric-value">{main_journey} · {top_team}</div>
            </div>
        </div>
    </div>
    
    <div class="header-date">📅 {analysis_date} 기준</div>
</div>"""

def get_footer_template():
    return """<div class="footer">
    <p>카테고리 기반 VoC 분석 보고서</p>
    <p>생성일시: {generated_at} | Pretendard 폰트 적용</p>
</div>"""