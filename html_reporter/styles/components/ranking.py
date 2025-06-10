# html_reporter/styles/components/ranking.py
"""순위 및 랭킹 컴포넌트"""

def get_ranking_styles():
    return """
/* === 분포 그리드 레이아웃 === */
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

/* === 순위 아이템 컴포넌트 === */
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