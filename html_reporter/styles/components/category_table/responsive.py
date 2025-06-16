"""
카테고리 테이블 반응형 스타일 - 아코디언과 동일한 여백
"""

def get_responsive_styles():
    """반응형 스타일 - 아코디언과 동일한 여백"""
    return """
/* === 반응형 === */
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
    
    .category-table-container {
        padding: 0; /* 중복 여백 방지 - accordion-content-area가 패딩 제공 */
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