# html_reporter/styles/components/accordion/responsive.py
"""
아코디언 컴포넌트 반응형 스타일 - 정렬 버튼 포함
"""

def get_tablet_responsive_styles():
    """태블릿 반응형 스타일 (768px 이하)"""
    return """
/* === 반응형 - 태블릿 === */
@media (max-width: 768px) {
    .controls-bar {
        padding-left: 20px;
        padding-right: 20px;
        flex-direction: column;
        gap: 12px;
        align-items: stretch;
    }
    
    .view-toggle-group {
        justify-content: center;
    }
    
    .bulk-controls {
        justify-content: center;
        flex-wrap: wrap;
        gap: 12px;
    }
    
    .accordion-controls {
        flex-direction: column;
        gap: 12px;
        align-items: center;
    }
    
    .accordion-sort-controls {
        border-right: none;
        border-bottom: 1px solid #e2e8f0;
        padding-bottom: 8px;
        margin-right: 0;
        margin-bottom: 8px;
        justify-content: center;
    }
    
    .bulk-actions {
        justify-content: center;
    }
    
    .accordion-content-area {
        padding-left: 20px;
        padding-right: 20px;
    }
    
    .team-accordion-header,
    .journey-accordion-header {
        flex-direction: column;
        gap: 12px;
        padding: 16px 20px;
    }
    
    .team-summary-info,
    .journey-summary-info {
        align-self: stretch;
        justify-content: space-between;
        min-width: auto;
    }
    
    .team-progress-container,
    .journey-progress-container {
        align-self: stretch;
        margin: 0;
    }
    
    .team-metrics-grid,
    .journey-metrics-grid {
        grid-template-columns: 1fr;
        gap: 12px;
    }
    
    .team-detail-box,
    .journey-detail-box {
        padding: 16px;
    }
}
"""

def get_mobile_responsive_styles():
    """모바일 반응형 스타일 (480px 이하)"""
    return """
@media (max-width: 480px) {
    .controls-bar {
        padding: 12px 20px;
    }
    
    .view-toggle-label {
        font-size: 0.85rem;
    }
    
    .toggle-btn {
        padding: 6px 12px;
        font-size: 0.85rem;
    }
    
    .bulk-control-btn {
        padding: 5px 10px;
        font-size: 0.75rem;
    }
    
    /* 정렬 버튼 모바일 반응형 */
    .accordion-sort-btn {
        padding: 5px 8px;
        font-size: 0.7rem;
        gap: 2px;
    }
    
    .sort-direction {
        font-size: 0.5rem;
    }
    
    .accordion-sort-controls {
        gap: 4px;
    }
    
    .team-accordion-header,
    .journey-accordion-header {
        padding: 12px 16px;
    }
    
    .team-name,
    .journey-name {
        font-size: 1rem;
    }
    
    .team-count,
    .journey-count {
        font-size: 0.85rem;
    }
}
"""

def get_sub_table_responsive_styles():
    """세부카테고리 테이블 반응형 스타일"""
    return """
/* === 세부카테고리 테이블 모바일 반응형 === */
@media (max-width: 768px) {
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

/* === 추가 반응형 - 매우 작은 화면 === */
@media (max-width: 320px) {
    .accordion-sort-controls {
        flex-direction: column;
        gap: 4px;
        width: 100%;
    }
    
    .accordion-sort-btn {
        width: 100%;
        justify-content: center;
        padding: 6px 8px;
    }
    
    .bulk-actions {
        flex-direction: column;
        width: 100%;
        gap: 4px;
    }
    
    .bulk-control-btn {
        width: 100%;
        text-align: center;
    }
}
"""