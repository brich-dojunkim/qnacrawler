# html_reporter/styles/overview.py
"""개요 탭 전용 스타일"""

def get_overview_styles():
    return """
/* === 메인 통계 그리드 === */
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
    display: flex;
    align-items: center;
    gap: 20px;
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

.stat-card-small.urgent::before {
    background: linear-gradient(90deg, #ef4444, #dc2626);
}

.stat-card-small.completed::before {
    background: linear-gradient(90deg, #10b981, #059669);
}

.stat-card-small.pending::before {
    background: linear-gradient(90deg, #f59e0b, #d97706);
}

.stat-number-medium {
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 5px;
}

.stat-card-small.urgent .stat-number-medium {
    color: #dc2626;
}

.stat-card-small.completed .stat-number-medium {
    color: #059669;
}

.stat-card-small.pending .stat-number-medium {
    color: #d97706;
}

.stat-label-medium {
    font-size: 0.9rem;
    color: #64748b;
    font-weight: 500;
    margin-bottom: 10px;
}

/* === 프로그레스 바 === */
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

.progress-fill-small.urgent {
    background: linear-gradient(90deg, #ef4444, #dc2626);
}

.progress-fill-small.completed {
    background: linear-gradient(90deg, #10b981, #059669);
}

.progress-fill-small.pending {
    background: linear-gradient(90deg, #f59e0b, #d97706);
}

.progress-text {
    font-size: 0.75rem;
    font-weight: 600;
    color: #64748b;
    min-width: 35px;
}

/* === 분포 그리드 === */
.distribution-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 30px;
}

.distribution-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 24px;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04);
    position: relative;
    overflow: hidden;
}

.distribution-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, #667eea, #764ba2);
}

.distribution-card-title {
    font-size: 1.1rem;
    font-weight: 700;
    margin-bottom: 20px;
    color: #374151;
    display: flex;
    align-items: center;
    gap: 8px;
}

/* === 순위 아이템 === */
.simple-rank-item {
    display: flex;
    align-items: center;
    padding: 16px 20px;
    margin-bottom: 12px;
    background: linear-gradient(135deg, #f8fafc, #f1f5f9);
    border-radius: 12px;
    border: 1px solid #e2e8f0;
    transition: all 0.3s ease;
}

.simple-rank-item:hover {
    background: linear-gradient(135deg, #e0f2fe, #e3f2fd);
    transform: translateY(-2px);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
}

.simple-rank-number {
    min-width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    color: white;
    background: linear-gradient(135deg, #667eea, #764ba2);
    border-radius: 50%;
    font-size: 1rem;
    margin-right: 20px;
}

.simple-rank-content {
    flex: 1;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.simple-rank-name {
    font-size: 1rem;
    font-weight: 600;
    color: #374151;
}

.simple-rank-details {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 2px;
}

.simple-rank-count {
    font-size: 1.1rem;
    font-weight: 700;
    color: #667eea;
}

.simple-rank-percentage {
    font-size: 0.85rem;
    color: #64748b;
    font-weight: 500;
}

.rank-summary {
    margin-top: 16px;
    padding-top: 16px;
    border-top: 1px solid #e2e8f0;
    text-align: center;
    font-size: 0.85rem;
    color: #64748b;
    font-weight: 500;
}
"""