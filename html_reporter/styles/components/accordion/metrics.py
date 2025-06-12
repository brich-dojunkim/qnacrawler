# html_reporter/styles/components/accordion/metrics.py
"""
아코디언 내부 메트릭 카드 스타일
헤더 메트릭과 일치하는 보더 색상 시스템
"""

def get_metrics_grid_styles():
    """메트릭 그리드 레이아웃"""
    return """
.team-metrics-grid,
.journey-metrics-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 16px;
    margin-bottom: 24px;
}
"""

def get_metric_item_base_styles():
    """메트릭 아이템 기본 스타일"""
    return """
/* === 헤더 메트릭과 일치하는 보더 색상 적용 === */
.metric-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 16px;
    background: white;
    border-radius: 8px;
    transition: all 0.3s ease;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.metric-item:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.metric-label {
    font-size: 0.9rem;
    color: #475569;
    font-weight: 500;
}

.metric-value {
    font-size: 1.1rem;
    font-weight: 700;
    color: #667eea;
}
"""

def get_metric_item_border_styles():
    """헤더 메트릭과 동일한 보더 색상 스타일"""
    return """
/* 헤더 메트릭 카드와 동일한 보더 색상 */
.metric-item.total {
    border: 2px solid #667eea;
}

.metric-item.urgent {
    border: 2px solid #ef4444;
}

.metric-item.completed {
    border: 2px solid #10b981;
}

.metric-item.status {
    border: 2px solid #f59e0b;
}

/* 호버 효과도 헤더와 동일하게 */
.metric-item.total:hover {
    border-color: #5b67d8;
    background: #f8faff;
}

.metric-item.urgent:hover {
    border-color: #dc2626;
    background: #fef2f2;
}

.metric-item.completed:hover {
    border-color: #059669;
    background: #f0fdf4;
}

.metric-item.status:hover {
    border-color: #d97706;
    background: #fffbeb;
}
"""