# html_reporter/styles/system/base.py (대시보드 헤더 스타일)
"""기본 시스템 스타일 - 통합 대시보드 헤더"""

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

/* === 타이트한 대시보드 헤더 === */
.dashboard-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 20px 30px;
    position: relative;
}

.dashboard-title {
    font-size: 1.4rem;
    font-weight: 700;
    margin-bottom: 12px;
    text-shadow: 0 2px 4px rgba(0,0,0,0.2);
    text-align: center;
}

.dashboard-stats {
    display: flex;
    flex-direction: column;
    gap: 6px;
    text-align: center;
}

.stats-line {
    font-size: 1.1rem;
    font-weight: 500;
    color: rgba(255, 255, 255, 0.95);
}

.stats-line strong {
    font-weight: 700;
    color: white;
}

.insights-line {
    font-size: 0.95rem;
    font-weight: 500;
    color: rgba(255, 255, 255, 0.9);
}

.insights-line strong {
    font-weight: 700;
    color: white;
}

.date-line {
    font-size: 0.85rem;
    color: rgba(255, 255, 255, 0.8);
    margin-top: 4px;
}

/* === 메인 콘텐츠 (패딩 줄임) === */
.main-content {
    padding: 0;
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

/* === 반응형 타이트 대시보드 === */
@media (max-width: 768px) {
    body {
        padding: 10px;
    }
    
    .container {
        border-radius: 16px;
    }
    
    .dashboard-header {
        padding: 16px 20px;
    }
    
    .dashboard-title {
        font-size: 1.2rem;
    }
    
    .stats-line {
        font-size: 1rem;
    }
    
    .insights-line {
        font-size: 0.9rem;
    }
    
    .date-line {
        font-size: 0.8rem;
    }
}

@media (max-width: 480px) {
    .dashboard-title {
        font-size: 1.1rem;
    }
    
    .stats-line {
        font-size: 0.95rem;
        line-height: 1.4;
    }
    
    .insights-line {
        font-size: 0.85rem;
        line-height: 1.4;
    }
    
    .date-line {
        font-size: 0.75rem;
    }
}
"""