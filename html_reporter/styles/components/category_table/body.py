# html_reporter/styles/components/category_table/body.py
"""
카테고리 테이블 본문 스타일 - 아코디언과 동일한 여백
"""

def get_table_container_styles():
    """테이블 컨테이너 스타일 - 중복 여백 방지"""
    return """
/* === 카테고리 테이블 뷰 (중복 여백 방지) === */
.category-table-container {
    background: white;
    padding: 0; /* 패딩 제거 - accordion-content-area가 이미 패딩 제공 */
}

.category-table {
    background: white;
    border-radius: 0 0 8px 8px;
    overflow: hidden;
    border: 1px solid #e2e8f0;
    border-top: none;
    margin: 0; /* 마진도 0 - accordion-content-area 패딩 사용 */
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}
"""

def get_table_body_styles():
    """테이블 본문 스타일 (메인 테이블과 아코디언 내부 테이블 공통)"""
    return """
/* === 공통 테이블 로우 스타일 (완료율 칼럼 추가) === */
.category-table-row,
.sub-category-row {
    display: grid;
    grid-template-columns: 2fr 1fr 1.2fr 0.8fr 0.8fr 0.8fr 0.6fr;
    gap: 0;
    padding: 12px 0;
    border-bottom: 1px solid #e5e7eb;
    transition: background 0.2s ease;
    cursor: pointer;
}

.category-table-row > div,
.sub-cat-cell {
    padding: 0 12px;
    display: flex;
    align-items: center;
    border-right: 1px solid #f3f4f6;
    font-size: 0.9rem;
}

.category-table-row > div:last-child,
.sub-cat-cell:last-child {
    border-right: none;
    justify-content: center;
}

.category-table-row:hover,
.sub-category-row:hover {
    background: #f8fafc;
}

.category-table-row:last-child,
.sub-category-row:last-child {
    border-bottom: none;
}

.category-table-row.hidden,
.sub-category-row.hidden {
    display: none;
}

/* === 공통 셀 내용 스타일 === */
.category-name {
    font-weight: 600;
    color: #374151;
    line-height: 1.3;
}

.team-badge, .journey-badge {
    padding: 4px 8px;
    border-radius: 12px;
    font-size: 0.75rem;
    font-weight: 600;
    display: inline-block;
}

.team-badge {
    background: #fef3c7;
    color: #92400e;
}

.journey-badge {
    background: #d1fae5;
    color: #065f46;
}

.metric-value {
    font-weight: 600;
    color: #667eea;
}

.urgent-rate {
    font-weight: 600;
}

.urgent-rate.high {
    color: #dc2626;
}

.urgent-rate.medium {
    color: #d97706;
}

.urgent-rate.low {
    color: #059669;
}

/* === 완료율 스타일 === */
.complete-rate {
    font-weight: 600;
}

.complete-rate.high {
    color: #059669;
}

.complete-rate.medium {
    color: #d97706;
}

.complete-rate.low {
    color: #dc2626;
}

/* === 공통 액션 버튼 === */
.action-btn,
.sub-cat-action-btn {
    background: #667eea;
    color: white;
    border: none;
    border-radius: 6px;
    padding: 8px;
    cursor: pointer;
    transition: all 0.2s ease;
    display: flex;
    align-items: center;
    justify-content: center;
    min-width: 32px;
    height: 32px;
}

.action-btn:hover,
.sub-cat-action-btn:hover {
    background: #5b67d8;
    transform: scale(1.05);
}
"""

def get_accordion_table_styles():
    """아코디언 내부 세부카테고리 테이블 스타일 (메인 테이블과 통일)"""
    return """
/* === 세부카테고리 테이블 (완료율 칼럼 추가) === */
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

.sub-categories-table-header {
    display: grid;
    grid-template-columns: 2fr 1fr 1.2fr 0.8fr 0.8fr 0.8fr 0.6fr;
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

.sub-categories-table-body {
    max-height: 400px;
    overflow-y: auto;
}

.sub-category-row {
    display: grid;
    grid-template-columns: 2fr 1fr 1.2fr 0.8fr 0.8fr 0.8fr 0.6fr;
    gap: 0;
    padding: 10px 0;
    border-bottom: 1px solid #f3f4f6;
    transition: background 0.2s ease;
    cursor: pointer;
}

.sub-cat-cell {
    padding: 0 12px;
    display: flex;
    align-items: center;
    font-size: 0.85rem;
    border-right: 1px solid #f8fafc;
    min-height: 36px;
}

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

/* === 카테고리 테이블 반응형 === */
@media (max-width: 768px) {
    .table-filter-header, 
    .category-table-row,
    .sub-categories-table-header,
    .sub-category-row {
        grid-template-columns: 1fr;
        gap: 8px;
    }
    
    .filter-column,
    .sub-cat-column {
        margin-bottom: 8px;
        border-right: none;
        border-bottom: 1px solid #e2e8f0;
        padding-bottom: 8px;
        justify-content: flex-start;
    }
    
    .filter-column:last-child,
    .sub-cat-column:last-child {
        border-bottom: none;
        justify-content: center;
    }
    
    .dropdown-menu {
        position: static;
        box-shadow: none;
        border: 1px solid #d1d5db;
        margin-top: 4px;
        width: 100%;
    }
    
    /* 모바일에서도 중복 여백 방지 */
    .category-table-container {
        padding: 0; /* 패딩 제거 - accordion-content-area가 패딩 제공 */
    }
    
    .table-filter-status {
        padding: 8px 15px;
    }
    
    .category-table-row > div,
    .sub-cat-cell {
        border-right: none;
        border-bottom: 1px solid #f3f4f6;
        padding: 8px 12px;
        justify-content: flex-start;
    }
    
    .category-table-row > div:last-child,
    .sub-cat-cell:last-child {
        border-bottom: none;
        justify-content: center;
    }
    
    .new-modal-content {
        width: 95%;
        margin: 20px;
    }
    
    .new-modal-header {
        padding: 16px 20px;
    }
    
    .new-modal-body {
        padding: 20px;
    }
    
    /* === 세부카테고리 테이블 모바일 반응형 === */
    .sub-categories-table-header,
    .sub-category-row {
        grid-template-columns: 1fr;
        gap: 8px;
    }
    
    .sub-cat-column,
    .sub-cat-cell {
        border-right: none;
        border-bottom: 1px solid #f3f4f6;
        padding: 8px 12px;
        justify-content: flex-start;
    }
    
    .sub-cat-column:last-child,
    .sub-cat-cell:last-child {
        border-bottom: none;
        justify-content: center;
    }
    
    .sub-categories-table-body {
        max-height: 300px;
    }
    
    .sub-categories-title {
        font-size: 0.9rem;
        padding: 12px 16px;
    }
    
    .sub-cat-column,
    .sub-cat-cell {
        font-size: 0.8rem;
        padding: 6px 12px;
    }
}

@media (max-width: 480px) {
    .table-filter-header, 
    .category-table-row,
    .sub-categories-table-header,
    .sub-category-row {
        padding: 10px 15px;
    }
    
    .filter-icon-btn, .sort-icon-btn {
        min-width: 14px;
        height: 14px;
    }
    
    .filter-icon-btn svg, .sort-icon-btn svg {
        width: 8px;
        height: 8px;
    }
    
    .action-btn svg,
    .sub-cat-action-btn svg {
        width: 10px;
        height: 10px;
    }
}
"""