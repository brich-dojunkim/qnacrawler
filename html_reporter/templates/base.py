# html_reporter/templates/base.py
"""공통 베이스 템플릿들"""

def get_base_template():
    return """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>카테고리 기반 VoC 분석 보고서</title>
    <link href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" rel="stylesheet">
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
    return """<div class="header">
    <h1>카테고리 기반 VoC 분석</h1>
    <p>고객 문의 데이터의 카테고리별 분석 결과</p>
    <p>{analysis_date}</p>
</div>"""

def get_footer_template():
    return """<div class="footer">
    <p>카테고리 기반 VoC 분석 보고서</p>
    <p>생성일시: {generated_at} | Pretendard 폰트 적용</p>
</div>"""