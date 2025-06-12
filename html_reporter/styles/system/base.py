# html_reporter/styles/system/base.py (깔끔한 헤더 스타일)
"""기본 시스템 스타일 - 기존 디자인 유지하면서 헤더만 구분된 배경색"""

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

/* === 푸터와 어울리는 헤더 === */
.dashboard-header {
    background: #f8fafc;
    color: #374151;
    padding: 24px 30px;
    border-bottom: 1px solid #e2e8f0;
}

.header-title {
    font-size: 1.5rem;
    font-weight: 600;
    text-align: center;
    margin-bottom: 20px;
}

.header-metrics {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    margin-bottom: 16px;
}

.metric-card {
    background: white;
    border: 2px solid #e2e8f0;
    border-radius: 12px;
    padding: 16px;
    display: flex;
    align-items: center;
    gap: 12px;
    transition: all 0.3s ease;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

/* === 각 카드별 다른 테두리 색상 === */
.metric-card.total {
    border-color: #667eea;
}

.metric-card.urgent {
    border-color: #ef4444;
}

.metric-card.completed {
    border-color: #10b981;
}

.metric-card.status {
    border-color: #f59e0b;
}

.metric-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.metric-card.total:hover {
    border-color: #5b67d8;
    background: #f8faff;
}

.metric-card.urgent:hover {
    border-color: #dc2626;
    background: #fef2f2;
}

.metric-card.completed:hover {
    border-color: #059669;
    background: #f0fdf4;
}

.metric-card.status:hover {
    border-color: #d97706;
    background: #fffbeb;
}

.metric-icon {
    font-size: 1.5rem;
    opacity: 0.9;
    flex-shrink: 0;
}

.metric-content {
    flex: 1;
    min-width: 0;
}

.metric-label {
    font-size: 0.8rem;
    font-weight: 500;
    color: #6b7280;
    margin-bottom: 2px;
}

.metric-value {
    font-size: 1rem;
    font-weight: 600;
    color: #374151;
    line-height: 1.2;
}

.header-date {
    text-align: center;
    font-size: 0.8rem;
    color: #6b7280;
    font-weight: 500;
}

/* === 메인 콘텐츠 === */
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

/* === 반응형 - 태블릿 === */
@media (max-width: 768px) {
    body {
        padding: 10px;
    }
    
    .container {
        border-radius: 16px;
    }
    
    .dashboard-header {
        padding: 20px;
    }
    
    .header-title {
        font-size: 1.3rem;
        margin-bottom: 16px;
    }
    
    .header-metrics {
        grid-template-columns: repeat(2, 1fr);
        gap: 12px;
        margin-bottom: 12px;
    }
    
    .metric-card {
        padding: 12px;
        gap: 10px;
    }
    
    .metric-icon {
        font-size: 1.3rem;
    }
    
    .metric-value {
        font-size: 0.9rem;
    }
    
    .metric-label {
        font-size: 0.75rem;
    }
}

/* === 반응형 - 모바일 === */
@media (max-width: 480px) {
    .dashboard-header {
        padding: 16px;
    }
    
    .header-title {
        font-size: 1.2rem;
        margin-bottom: 12px;
    }
    
    .header-metrics {
        grid-template-columns: 1fr;
        gap: 10px;
        margin-bottom: 10px;
    }
    
    .metric-card {
        padding: 12px 16px;
        gap: 12px;
    }
    
    .metric-icon {
        font-size: 1.4rem;
    }
    
    .metric-value {
        font-size: 0.85rem;
    }
    
    .header-date {
        font-size: 0.75rem;
    }
}
"""