# html_reporter/styles/components/cards.py
"""모든 카드 컴포넌트 스타일 - 헤더 배지 레이아웃 개선 (완전 수정버전)"""

def get_card_styles():
    return """
/* === 기본 엔터티 카드 === */
.entity-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 24px;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.entity-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, #667eea, #764ba2);
    transform: scaleX(0);
    transition: transform 0.3s ease;
}

.entity-card:hover::before {
    transform: scaleX(1);
}

.entity-card:hover {
    border-color: #c7d2fe;
}

/* === 엔터티 카드 헤더 개선 === */
.entity-card-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 20px;
    padding-bottom: 16px;
    border-bottom: 1px solid #f1f5f9;
}

.entity-card-title {
    font-size: 1.25rem;
    font-weight: 600;
    margin: 0;
    color: #1e293b;
    flex: 1;
    padding-right: 16px; /* 제목과 배지 사이 간격 */
}

.entity-card-badge {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    padding: 6px 16px;
    border-radius: 20px;
    font-size: 0.875rem;
    font-weight: 600;
    box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}

/* === 메트릭 리스트 === */
.metrics-list {
    list-style: none;
    padding: 0;
    margin: 16px 0;
}

.metrics-list li {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 16px;
    margin-bottom: 8px;
    background: linear-gradient(135deg, #f8fafc, #f1f5f9);
    border-radius: 10px;
    border: 1px solid #e2e8f0;
    transition: background 0.2s ease;
}

.metrics-list li:hover {
    background: linear-gradient(135deg, #e0f2fe, #e3f2fd);
}

.metrics-list li:last-child {
    margin-bottom: 0;
}

.metric-name {
    font-size: 0.9rem;
    color: #475569;
    font-weight: 500;
}

.metric-number {
    font-size: 1.1rem;
    font-weight: 700;
    color: #667eea;
}

/* === 문의 카드 (모달용) === */
.inquiry-card {
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 16px;
    margin-bottom: 16px;
    background: linear-gradient(135deg, #f8fafc, #f1f5f9);
    transition: background 0.3s ease;
    border-left: 4px solid #667eea;
}

.inquiry-card:hover {
    background: linear-gradient(135deg, #e0f2fe, #e3f2fd);
}

.inquiry-card:last-child {
    margin-bottom: 0;
}

/* === 문의 카드 헤더 === */
.inquiry-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 12px;
    font-size: 0.9rem;
    color: #64748b;
    font-weight: 500;
}

/* === 문의 카드 내용 === */
.inquiry-content {
    color: #374151;
    line-height: 1.6;
    font-size: 0.95rem;
}
"""