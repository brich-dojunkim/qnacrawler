# html_reporter/styles/system/base.py
"""기본 시스템 스타일 - 리셋, 폰트, 전역 설정"""

def get_base_styles():
    return """
/* === 기본 리셋 === */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* === 전역 기본 스타일 === */
body {
    font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    color: #333;
    line-height: 1.6;
    padding: 20px;
}

/* === 메인 컨테이너 === */
.container {
    max-width: 1400px;
    margin: 0 auto;
    background: white;
    border-radius: 20px;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
    overflow: hidden;
}

/* === 헤더 === */
.header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 40px 30px;
    text-align: center;
    position: relative;
}

.header h1 {
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 15px;
    text-shadow: 0 4px 8px rgba(0,0,0,0.2);
}

.header p {
    font-size: 1.1rem;
    margin-bottom: 10px;
    opacity: 0.95;
}

.header .analysis-date {
    font-size: 1rem;
    margin-top: 15px;
    padding: 8px 16px;
    background: rgba(255, 255, 255, 0.15);
    border-radius: 20px;
    display: inline-block;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.2);
}

/* === 메인 콘텐츠 === */
.main-content {
    padding: 40px 30px;
}

/* === 푸터 === */
.footer {
    text-align: center;
    padding: 30px;
    background: linear-gradient(135deg, #f8fafc, #e2e8f0);
    border-top: 1px solid #e2e8f0;
    color: #64748b;
    font-size: 0.9rem;
    font-weight: 500;
}
"""