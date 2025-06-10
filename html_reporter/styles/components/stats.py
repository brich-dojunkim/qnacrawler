# html_reporter/styles/components/stats.py
"""통계 카드 및 프로그레스 컴포넌트"""

def get_stats_styles():
    return """
/* === 메인 통계 그리드 레이아웃 === */
.main-stats-grid {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr 1fr;
    gap: 20px;
    margin-bottom: 40px;
}

/* === 대형 통계 카드 === */
.stat-card-large {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    padding: 30px;
    border-radius: 16px;
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
}

.stat-number-large {
    font-size: 3rem;
    font-weight: 700;
    line-height: 1;
    margin-bottom: 5px;
}

.stat-label-large {
    font-size: 1.1rem;
    opacity: 0.9;
    font-weight: 500;
}

/* === 소형 통계 카드 === */
.stat-card-small {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
    position: relative;
    overflow: hidden;
}

.stat-card-small::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
}

.stat-card-small.urgent::before { background: linear-gradient(90deg, #ef4444, #dc2626); }
.stat-card-small.completed::before { background: linear-gradient(90deg, #10b981, #059669); }
.stat-card-small.pending::before { background: linear-gradient(90deg, #f59e0b, #d97706); }

.stat-number-medium {
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 5px;
}

.stat-card-small.urgent .stat-number-medium { color: #dc2626; }
.stat-card-small.completed .stat-number-medium { color: #059669; }
.stat-card-small.pending .stat-number-medium { color: #d97706; }

.stat-label-medium {
    font-size: 0.9rem;
    color: #64748b;
    font-weight: 500;
    margin-bottom: 10px;
}

/* === 프로그레스 바 컴포넌트 === */
.stat-progress {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-top: 10px;
}

.progress-bar-small {
    flex: 1;
    height: 6px;
    background: #f1f5f9;
    border-radius: 3px;
    overflow: hidden;
}

.progress-fill-small {
    height: 100%;
    border-radius: 3px;
    transition: width 0.3s ease;
}

.progress-fill-small.urgent { background: linear-gradient(90deg, #ef4444, #dc2626); }
.progress-fill-small.completed { background: linear-gradient(90deg, #10b981, #059669); }
.progress-fill-small.pending { background: linear-gradient(90deg, #f59e0b, #d97706); }

.progress-text {
    font-size: 0.75rem;
    font-weight: 600;
    color: #64748b;
    min-width: 35px;
}
"""