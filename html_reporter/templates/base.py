# html_reporter/templates/base.py
"""공통 베이스 템플릿들 - 단순화된 디자인"""

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
        
        <!-- 탭 네비게이션 -->
        <div class="tab-navigation">
            <div class="tab-nav">
                <button class="tab-btn active" onclick="switchTab('overview')">분석 개요</button>
                <button class="tab-btn" onclick="switchTab('teams')">팀별 분석</button>
                <button class="tab-btn" onclick="switchTab('journey')">유저 여정</button>
                <button class="tab-btn" onclick="switchTab('categories')">세부 카테고리</button>
            </div>
        </div>
        
        <div class="main-content">
            {content}
        </div>
        {footer}
    </div>
    {scripts}
</body>
</html>"""

def get_header_template():
    return """<div class="header">
    <h1>카테고리 기반 VoC 분석</h1>
    <p>고객 문의 데이터의 카테고리별 분석 및 인사이트 도출</p>
    <p>분석 기준일: {analysis_date}</p>
</div>"""

def get_footer_template():
    return """<div class="footer">
    <p>카테고리 기반 VoC 분석 보고서</p>
    <p>생성일시: {generated_at} | Pretendard 폰트 적용</p>
</div>"""