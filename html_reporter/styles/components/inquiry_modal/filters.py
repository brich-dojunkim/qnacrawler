# html_reporter/styles/components/inquiry_modal/filters.py
"""
문의 상세보기 모달 필터 바 스타일 - 3-Way 탭 스위치 - 화살표 애니메이션 문제 해결
"""

def get_filters_styles():
    """3-Way 탭 스위치가 적용된 필터 바 스타일 - 화살표 애니메이션 문제 해결"""
    return """
/* === 필터 바 기본 === */
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

/* === 정렬 그룹 컨테이너 === */
.filter-group.sort-group {
    display: flex !important;
    flex-direction: row !important;
    gap: 12px;
    align-items: center;
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

/* === 3-Way 탭 스위치 === */
.bordered-tab-group {
    display: flex;
    border: 1px solid #d1d5db;
    border-radius: 6px;
    overflow: hidden;
    background: white;
}

.bordered-tab-btn {
    flex: 1;
    padding: 8px 16px;
    background: white;
    border: none;
    border-right: 1px solid #d1d5db;
    font-size: 0.875rem;
    font-weight: 500;
    color: #6b7280;
    cursor: pointer;
    transition: all 0.2s ease;
    min-width: 60px;
    text-align: center;
    white-space: nowrap;
}

.bordered-tab-btn:last-child {
    border-right: none;
}

/* 호버 효과 */
.bordered-tab-btn:hover:not(.active) {
    background: #f9fafb;
    color: #374151;
}

/* 활성화된 탭 기본 */
.bordered-tab-btn.active {
    font-weight: 700;
    color: white;
}

/* 타입별 활성화 색상 */
.bordered-tab-btn.active.all { 
    background: #667eea; 
}

.bordered-tab-btn.active.urgent { 
    background: #ef4444; 
}

.bordered-tab-btn.active.normal { 
    background: #3b82f6; 
}

.bordered-tab-btn.active.completed { 
    background: #10b981; 
}

.bordered-tab-btn.active.pending { 
    background: #f59e0b; 
}

/* === 정렬 버튼 (기존 스타일 유지) === */
.accordion-filter-sort {
    display: inline-flex !important; /* inline-flex로 강제 적용 */
    align-items: center;
    gap: 8px;
    padding: 8px 12px;
    border: 1px solid #d1d5db;
    border-radius: 6px;
    background: white;
    color: #6b7280;
    font-size: 0.875rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s ease;
    white-space: nowrap;
    margin: 0; /* 기본 마진 제거 */
}

.accordion-filter-sort:hover {
    border-color: #9ca3af;
    color: #374151;
    background: #f9fafb;
}

.accordion-filter-sort.active {
    background: linear-gradient(135deg, #667eea, #764ba2);
    border-color: #667eea;
    color: white;
    box-shadow: 0 2px 4px rgba(102, 126, 234, 0.3);
}

.accordion-filter-sort.active:hover {
    background: linear-gradient(135deg, #5b67d8, #6b46c1);
    border-color: #5b67d8;
    transform: translateY(-1px);
    box-shadow: 0 3px 6px rgba(102, 126, 234, 0.4);
}

/* 정렬 방향 아이콘 (애니메이션 문제 해결) */
.sort-direction {
    font-size: 0.7rem;
    font-weight: 700;
    margin-left: 2px;
    /* 🔧 핵심 수정: transform 관련 속성 제거 */
    transform: none !important;
    transition: none !important;
}

/* 🔧 asc/desc 클래스의 transform 제거 */
.sort-direction.asc {
    /* transform 제거 - textContent로만 제어 */
}

.sort-direction.desc {
    /* transform 제거 - textContent로만 제어 */
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

    .bordered-tab-btn {
        flex: 1;
        justify-content: center;
        min-height: 44px;
        padding: 10px 12px;
    }

    .accordion-filter-sort {
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

    .bordered-tab-btn {
        padding: 8px 10px;
        font-size: 0.8rem;
        min-height: 40px;
        min-width: 50px;
    }

    .accordion-filter-sort {
        padding: 6px 10px;
        font-size: 0.8rem;
        gap: 4px;
        min-height: 36px;
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