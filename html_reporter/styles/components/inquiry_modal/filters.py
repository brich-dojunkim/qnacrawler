# html_reporter/styles/components/inquiry_modal/filters.py
"""
문의 상세보기 모달 필터 바 스타일 - 개선된 토글 및 정렬 버튼
"""

def get_filters_styles():
    """개선된 필터 바 스타일 - 토글 및 정렬 버튼"""
    return """
/* === 개선된 필터 바 === */
.inquiry-modal-filters {
    background: white;
    border-bottom: 1px solid #e5e7eb;
    padding: 16px 20px;
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    align-items: center;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.filter-group {
    display: flex;
    align-items: center;
    gap: 8px;
}

/* === 검색 영역 === */
.search-group {
    flex: 1;
    min-width: 250px;
    max-width: 350px;
}

.search-wrapper {
    position: relative;
    width: 100%;
}

.search-icon {
    position: absolute;
    left: 12px;
    top: 50%;
    transform: translateY(-50%);
    color: #9ca3af;
    pointer-events: none;
    z-index: 1;
}

.search-input {
    width: 100%;
    padding: 10px 16px 10px 40px;
    border: 2px solid #e5e7eb;
    border-radius: 12px;
    font-size: 0.9rem;
    background: #f9fafb;
    transition: all 0.3s ease;
    box-sizing: border-box;
}

.search-input:focus {
    outline: none;
    border-color: #667eea;
    background: white;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.search-input:hover {
    border-color: #d1d5db;
    background: white;
}

.clear-search-btn {
    position: absolute;
    right: 8px;
    top: 50%;
    transform: translateY(-50%);
    background: #6b7280;
    color: white;
    border: none;
    border-radius: 6px;
    width: 24px;
    height: 24px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.2s ease;
    padding: 0;
}

.clear-search-btn:hover {
    background: #374151;
    transform: translateY(-50%) scale(1.1);
}

/* === 토글 버튼 스타일 === */
.filter-toggle {
    display: flex;
    align-items: center;
    gap: 6px;
    padding: 8px 16px;
    border: 2px solid #e5e7eb;
    border-radius: 12px;
    background: #f9fafb;
    color: #6b7280;
    font-size: 0.875rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    white-space: nowrap;
}

.filter-toggle:hover {
    border-color: #d1d5db;
    background: white;
    color: #374151;
}

/* 긴급도 토글 활성화 */
.filter-toggle.active#urgency-toggle {
    background: linear-gradient(135deg, #ef4444, #dc2626);
    border-color: #dc2626;
    color: white;
    box-shadow: 0 4px 15px rgba(239, 68, 68, 0.3);
}

.filter-toggle.active#urgency-toggle:hover {
    background: linear-gradient(135deg, #dc2626, #b91c1c);
    transform: translateY(-1px);
    box-shadow: 0 6px 20px rgba(239, 68, 68, 0.4);
}

/* 상태 토글 활성화 */
.filter-toggle.active#status-toggle {
    background: linear-gradient(135deg, #10b981, #059669);
    border-color: #059669;
    color: white;
    box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3);
}

.filter-toggle.active#status-toggle:hover {
    background: linear-gradient(135deg, #059669, #047857);
    transform: translateY(-1px);
    box-shadow: 0 6px 20px rgba(16, 185, 129, 0.4);
}

.toggle-icon {
    font-size: 1rem;
}

.toggle-text {
    font-weight: 600;
}

/* === 정렬 버튼 그룹 === */
.sort-group {
    display: flex;
    gap: 4px;
    background: #f3f4f6;
    border-radius: 12px;
    padding: 4px;
    border: 1px solid #e5e7eb;
}

.filter-sort {
    display: flex;
    align-items: center;
    gap: 6px;
    padding: 8px 12px;
    border: none;
    border-radius: 8px;
    background: transparent;
    color: #6b7280;
    font-size: 0.875rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    white-space: nowrap;
}

.filter-sort:hover {
    background: #e5e7eb;
    color: #374151;
}

.filter-sort.active {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3);
}

.filter-sort.active:hover {
    background: linear-gradient(135deg, #5b67d8, #6b46c1);
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
}

.sort-icon {
    font-size: 1rem;
}

.sort-text {
    font-weight: 600;
}

/* === 액션 버튼 === */
.filter-actions {
    display: flex;
    gap: 8px;
    margin-left: auto;
}

.filter-action-btn {
    background: #f3f4f6;
    border: 2px solid #e5e7eb;
    border-radius: 12px;
    width: 44px;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.3s ease;
    color: #6b7280;
}

.filter-action-btn:hover {
    background: #667eea;
    border-color: #667eea;
    color: white;
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}

.filter-action-btn:active {
    transform: translateY(0);
}

/* === 페이지네이션 푸터 === */
.inquiry-modal-footer {
    background: white;
    border-top: 1px solid #e5e7eb;
    padding: 16px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
    box-shadow: 0 -2px 8px rgba(0, 0, 0, 0.05);
}

.pagination-info {
    color: #6b7280;
    font-size: 0.875rem;
    font-weight: 500;
}

.pagination-controls {
    display: flex;
    align-items: center;
    gap: 8px;
}

.pagination-btn {
    background: #f9fafb;
    border: 2px solid #e5e7eb;
    border-radius: 8px;
    padding: 8px 12px;
    font-size: 0.875rem;
    font-weight: 600;
    color: #374151;
    cursor: pointer;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    gap: 6px;
}

.pagination-btn:hover:not(:disabled) {
    background: #667eea;
    border-color: #667eea;
    color: white;
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}

.pagination-btn:disabled {
    background: #f3f4f6;
    color: #9ca3af;
    cursor: not-allowed;
    opacity: 0.6;
}

.page-numbers {
    display: flex;
    gap: 4px;
    align-items: center;
}

.page-number-btn {
    background: #f9fafb;
    border: 2px solid #e5e7eb;
    border-radius: 8px;
    width: 36px;
    height: 36px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.875rem;
    font-weight: 600;
    color: #374151;
    cursor: pointer;
    transition: all 0.3s ease;
}

.page-number-btn:hover:not(.active):not(:disabled) {
    background: #e5e7eb;
    transform: translateY(-1px);
}

.page-number-btn.active {
    background: #667eea;
    border-color: #667eea;
    color: white;
    box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}

.page-ellipsis {
    color: #9ca3af;
    font-weight: 600;
    padding: 0 8px;
}

.items-per-page-select {
    padding: 6px 28px 6px 10px;
    border: 2px solid #e5e7eb;
    border-radius: 8px;
    background: #f9fafb;
    font-size: 0.8rem;
    font-weight: 500;
    color: #374151;
    cursor: pointer;
    transition: all 0.3s ease;
    appearance: none;
    background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 20 20'%3e%3cpath stroke='%236b7280' stroke-linecap='round' stroke-linejoin='round' stroke-width='1.5' d='m6 8 4 4 4-4'/%3e%3c/svg%3e");
    background-position: right 6px center;
    background-repeat: no-repeat;
    background-size: 14px;
}

.items-per-page-select:hover {
    border-color: #d1d5db;
    background-color: white;
}

.items-per-page-select:focus {
    outline: none;
    border-color: #667eea;
    background-color: white;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

/* === 반응형 - 태블릿 === */
@media (max-width: 768px) {
    .inquiry-modal-filters {
        padding: 12px 16px;
        gap: 10px;
        flex-direction: column;
        align-items: stretch;
    }
    
    .search-group {
        min-width: auto;
        max-width: 100%;
        order: 1;
    }
    
    .filter-group:not(.search-group):not(.filter-actions) {
        order: 2;
        justify-content: center;
    }
    
    .filter-actions {
        order: 3;
        margin-left: 0;
        justify-content: center;
    }
    
    .filter-toggle {
        flex: 1;
        justify-content: center;
        min-height: 44px;
    }
    
    .sort-group {
        width: 100%;
        justify-content: center;
    }
    
    .filter-sort {
        flex: 1;
        justify-content: center;
        min-height: 40px;
    }
    
    .filter-action-btn {
        width: 50px;
        height: 50px;
    }
    
    .inquiry-modal-footer {
        padding: 12px 16px;
        flex-direction: column;
        align-items: stretch;
        gap: 10px;
    }
    
    .pagination-info {
        text-align: center;
        order: 2;
    }
    
    .pagination-controls {
        order: 1;
        justify-content: center;
    }
    
    .results-per-page {
        order: 3;
        text-align: center;
    }
}

/* === 반응형 - 모바일 === */
@media (max-width: 480px) {
    .inquiry-modal-filters {
        padding: 10px 12px;
        gap: 8px;
    }
    
    .search-input {
        padding: 8px 14px 8px 36px;
        font-size: 0.85rem;
    }
    
    .search-icon {
        left: 10px;
        width: 14px;
        height: 14px;
    }
    
    .clear-search-btn {
        right: 6px;
        width: 20px;
        height: 20px;
    }
    
    .filter-toggle {
        padding: 6px 12px;
        font-size: 0.8rem;
        gap: 4px;
        min-height: 40px;
    }
    
    .toggle-icon,
    .sort-icon {
        font-size: 0.9rem;
    }
    
    .filter-sort {
        padding: 6px 10px;
        font-size: 0.8rem;
        gap: 4px;
        min-height: 36px;
    }
    
    .sort-group {
        padding: 3px;
    }
    
    .filter-action-btn {
        width: 44px;
        height: 44px;
    }
    
    .inquiry-modal-footer {
        padding: 10px 12px;
    }
    
    .pagination-btn {
        padding: 6px 10px;
        font-size: 0.8rem;
    }
    
    .page-number-btn {
        width: 32px;
        height: 32px;
        font-size: 0.8rem;
    }
    
    .items-per-page-select {
        font-size: 0.75rem;
        padding: 5px 24px 5px 8px;
    }
}
"""