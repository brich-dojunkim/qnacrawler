# html_reporter/styles/components/accordion/sub_table.py
"""
세부카테고리 테이블 스타일
"""

def get_sub_table_container_styles():
    """세부카테고리 테이블 컨테이너 및 제목"""
    return """
/* === 세부카테고리 테이블 스타일 === */
.sub-categories-table {
    margin-top: 16px;
    background: white;
    border-radius: 12px;
    border: 1px solid #e2e8f0;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}

.sub-categories-title {
    font-size: 1rem;
    font-weight: 700;
    color: #374151;
    padding: 16px 20px;
    margin: 0;
    background: linear-gradient(135deg, #f8fafc, #e2e8f0);
    border-bottom: 1px solid #e2e8f0;
    display: flex;
    align-items: center;
    gap: 8px;
}

.sub-categories-table-container {
    background: white;
}
"""

def get_sub_table_header_styles():
    """세부카테고리 테이블 헤더"""
    return """
.sub-categories-table-header {
    display: grid;
    grid-template-columns: 2fr 1fr 1.2fr 0.8fr 0.8fr 0.6fr;
    gap: 0;
    padding: 12px 0;
    background: linear-gradient(135deg, #f1f5f9, #e2e8f0);
    border-bottom: 1px solid #e2e8f0;
}

.sub-cat-column {
    padding: 0 12px;
    font-weight: 700;
    font-size: 0.9rem;
    color: #374151;
    display: flex;
    align-items: center;
    border-right: 1px solid #e2e8f0;
    min-height: 32px;
}

.sub-cat-column:last-child {
    border-right: none;
    justify-content: center;
}
"""

def get_sub_table_body_styles():
    """세부카테고리 테이블 바디 및 로우"""
    return """
.sub-categories-table-body {
    max-height: 400px;
    overflow-y: auto;
}

.sub-category-row {
    display: grid;
    grid-template-columns: 2fr 1fr 1.2fr 0.8fr 0.8fr 0.6fr;
    gap: 0;
    padding: 10px 0;
    border-bottom: 1px solid #f3f4f6;
    transition: background 0.2s ease;
    cursor: pointer;
}

.sub-category-row:hover {
    background: #f8fafc;
}

.sub-category-row:last-child {
    border-bottom: none;
}

.sub-cat-cell {
    padding: 0 12px;
    display: flex;
    align-items: center;
    font-size: 0.85rem;
    border-right: 1px solid #f8fafc;
    min-height: 36px;
}

.sub-cat-cell:last-child {
    border-right: none;
    justify-content: center;
}
"""

def get_sub_table_content_styles():
    """세부카테고리 테이블 내용 스타일"""
    return """
.sub-cat-cell .category-name {
    font-weight: 600;
    color: #374151;
    line-height: 1.3;
}

.sub-cat-cell .team-badge,
.sub-cat-cell .journey-badge {
    padding: 3px 8px;
    border-radius: 10px;
    font-size: 0.7rem;
    font-weight: 600;
    display: inline-block;
}

.sub-cat-cell .team-badge {
    background: #fef3c7;
    color: #92400e;
}

.sub-cat-cell .journey-badge {
    background: #d1fae5;
    color: #065f46;
}

.sub-cat-cell .metric-value {
    font-weight: 600;
    color: #667eea;
}

.sub-cat-cell .urgent-rate {
    font-weight: 600;
}

.sub-cat-cell .urgent-rate.high {
    color: #dc2626;
}

.sub-cat-cell .urgent-rate.medium {
    color: #d97706;
}

.sub-cat-cell .urgent-rate.low {
    color: #059669;
}
"""

def get_sub_table_action_styles():
    """세부카테고리 테이블 액션 버튼 및 요약"""
    return """
.sub-cat-action-btn {
    background: #667eea;
    color: white;
    border: none;
    border-radius: 6px;
    padding: 6px;
    cursor: pointer;
    transition: all 0.2s ease;
    display: flex;
    align-items: center;
    justify-content: center;
    min-width: 28px;
    height: 28px;
}

.sub-cat-action-btn:hover {
    background: #5b67d8;
    transform: scale(1.05);
}

.sub-cat-action-btn svg {
    width: 10px;
    height: 10px;
    stroke-width: 2.5;
}

.sub-category-summary {
    padding: 12px 20px;
    background: linear-gradient(135deg, #f8fafc, #f1f5f9);
    text-align: center;
    font-size: 0.85rem;
    color: #64748b;
    font-weight: 500;
    border-top: 1px solid #e2e8f0;
}

/* === 세부카테고리 테이블 스크롤바 === */
.sub-categories-table-body::-webkit-scrollbar {
    width: 6px;
}

.sub-categories-table-body::-webkit-scrollbar-track {
    background: #f1f5f9;
}

.sub-categories-table-body::-webkit-scrollbar-thumb {
    background: #cbd5e1;
    border-radius: 3px;
}

.sub-categories-table-body::-webkit-scrollbar-thumb:hover {
    background: #94a3b8;
}
"""