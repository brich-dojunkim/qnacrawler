# html_reporter/styles/components/category_table.py (최종 스타일)
"""카테고리 테이블 스타일 - 텍스트 옆 아이콘 + 오른쪽 아래 드롭다운"""

def get_category_table_styles():
    return """
/* === 카테고리 테이블 뷰 === */
.category-table-container {
    background: #f8fafc;
    padding: 20px 0;
}

.category-table {
    background: white;
    border-radius: 8px;
    overflow: hidden;
    border: 1px solid #e2e8f0;
    margin: 0 20px;
}

/* === 텍스트 옆 아이콘 테이블 필터 헤더 === */
.table-filter-header {
    background: linear-gradient(135deg, #f8fafc, #e2e8f0);
    display: grid;
    grid-template-columns: 2.5fr 1.2fr 1.2fr 0.8fr 0.8fr 1fr;
    gap: 0;
    padding: 16px 0;
    border-bottom: 2px solid #667eea;
}

.filter-column {
    display: flex;
    flex-direction: column;
    padding: 0 12px;
    border-right: 1px solid #e2e8f0;
    position: relative;
}

.filter-column:last-child {
    border-right: none;
}

.column-header {
    display: flex;
    align-items: center;
    gap: 6px;
    min-height: 32px;
}

.column-label {
    font-weight: 700;
    color: #374151;
    font-size: 0.95rem;
    line-height: 1.2;
}

/* === 드롭다운 래퍼 === */
.filter-dropdown-wrapper {
    position: relative;
    display: inline-block;
}

/* === 텍스트 옆 아이콘 버튼 스타일 === */
.filter-icon-btn, .sort-icon-btn {
    background: none;
    border: 1px solid #d1d5db;
    border-radius: 3px;
    cursor: pointer;
    padding: 2px;
    transition: all 0.2s ease;
    min-width: 16px;
    height: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #6b7280;
    flex-shrink: 0;
}

.filter-icon-btn:hover, .sort-icon-btn:hover {
    background: #f3f4f6;
    border-color: #9ca3af;
    color: #374151;
}

.filter-icon-btn.active {
    background: #667eea;
    border-color: #667eea;
    color: white;
    box-shadow: 0 2px 4px rgba(102, 126, 234, 0.3);
}

.sort-icon-btn.active {
    background: #667eea;
    border-color: #667eea;
    color: white;
    box-shadow: 0 2px 4px rgba(102, 126, 234, 0.3);
}

.sort-icon-btn.asc svg {
    transform: rotate(180deg);
}

/* === SVG 아이콘 크기 조정 === */
.filter-icon-btn svg, .sort-icon-btn svg {
    width: 10px;
    height: 10px;
    stroke-width: 3;
}

.action-btn svg {
    width: 12px;
    height: 12px;
    stroke-width: 2.5;
}

/* === 오른쪽 아래 드롭다운 메뉴 === */
.dropdown-menu {
    position: absolute;
    top: 20px;
    left: 0;
    background: white;
    border: 1px solid #d1d5db;
    border-radius: 6px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    z-index: 1000;
    min-width: 150px;
    padding: 8px;
}

.dropdown-menu.hidden {
    display: none;
}

.dropdown-filter-input {
    width: 100%;
    padding: 6px 8px;
    border: 1px solid #d1d5db;
    border-radius: 4px;
    font-size: 0.85rem;
    outline: none;
}

.dropdown-filter-input:focus {
    border-color: #667eea;
    box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.1);
}

.dropdown-filter-select {
    width: 100%;
    padding: 6px 8px;
    border: 1px solid #d1d5db;
    border-radius: 4px;
    background: white;
    font-size: 0.85rem;
    cursor: pointer;
    outline: none;
}

.dropdown-filter-select:focus {
    border-color: #667eea;
    box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.1);
}

/* === 테이블 데이터 로우 === */
.category-table-body {
    max-height: 600px;
    overflow-y: auto;
}

.category-table-row {
    display: grid;
    grid-template-columns: 2.5fr 1.2fr 1.2fr 0.8fr 0.8fr 1fr;
    gap: 0;
    padding: 12px 0;
    border-bottom: 1px solid #e5e7eb;
    transition: background 0.2s ease;
    cursor: pointer;
}

.category-table-row > div {
    padding: 0 12px;
    display: flex;
    align-items: center;
    border-right: 1px solid #f3f4f6;
    font-size: 0.9rem;
}

.category-table-row > div:last-child {
    border-right: none;
    justify-content: center;
}

.category-table-row:hover {
    background: #f8fafc;
}

.category-table-row:last-child {
    border-bottom: none;
}

.category-table-row.hidden {
    display: none;
}

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

.action-btn {
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

.action-btn:hover {
    background: #5b67d8;
    transform: scale(1.05);
}

/* === 새 모달 스타일 === */
.new-modal-overlay {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.6);
    backdrop-filter: blur(8px);
    z-index: 10000;
    justify-content: center;
    align-items: center;
}

.new-modal-overlay.active {
    display: flex;
}

.new-modal-content {
    background: white;
    border-radius: 16px;
    width: 90%;
    max-width: 800px;
    max-height: 80vh;
    overflow: hidden;
    box-shadow: 0 25px 80px rgba(0, 0, 0, 0.3);
}

.new-modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 24px;
    border-bottom: 1px solid #e2e8f0;
    background: linear-gradient(135deg, #f8fafc, #e2e8f0);
}

.new-modal-title {
    font-size: 1.4rem;
    font-weight: 700;
    color: #1e293b;
    margin: 0;
}

.new-modal-close {
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    color: #64748b;
    padding: 4px;
    border-radius: 4px;
    transition: all 0.2s ease;
}

.new-modal-close:hover {
    background: #f1f5f9;
    color: #374151;
}

.new-modal-body {
    padding: 24px;
    max-height: 60vh;
    overflow-y: auto;
}

/* === 필터 상태 표시 === */
.table-filter-status {
    background: #dbeafe;
    padding: 12px 20px;
    margin: 0 20px;
    border-radius: 6px 6px 0 0;
    font-size: 0.9rem;
    color: #1e40af;
    border: 1px solid #bfdbfe;
    border-bottom: none;
}

.clear-table-filters {
    background: none;
    border: none;
    color: #667eea;
    cursor: pointer;
    text-decoration: underline;
    font-size: 0.85rem;
    margin-left: 10px;
}

.clear-table-filters:hover {
    color: #5b67d8;
}

/* === 테이블 컨트롤 버튼 === */
.table-controls {
    display: none;
}

.table-controls.active {
    display: flex;
}

.accordion-controls.hidden {
    display: none;
}

/* === 스크롤바 스타일 === */
.category-table-body::-webkit-scrollbar,
.new-modal-body::-webkit-scrollbar {
    width: 6px;
}

.category-table-body::-webkit-scrollbar-track,
.new-modal-body::-webkit-scrollbar-track {
    background: #f1f5f9;
}

.category-table-body::-webkit-scrollbar-thumb,
.new-modal-body::-webkit-scrollbar-thumb {
    background: #cbd5e1;
    border-radius: 3px;
}

.category-table-body::-webkit-scrollbar-thumb:hover,
.new-modal-body::-webkit-scrollbar-thumb:hover {
    background: #94a3b8;
}

/* === 반응형 === */
@media (max-width: 768px) {
    .table-filter-header, 
    .category-table-row {
        grid-template-columns: 1fr;
        gap: 8px;
    }
    
    .filter-column {
        margin-bottom: 8px;
        border-right: none;
        border-bottom: 1px solid #e2e8f0;
        padding-bottom: 8px;
    }
    
    .filter-column:last-child {
        border-bottom: none;
    }
    
    .dropdown-menu {
        position: static;
        box-shadow: none;
        border: 1px solid #d1d5db;
        margin-top: 4px;
        width: 100%;
    }
    
    .category-table-container {
        padding: 10px 0;
    }
    
    .category-table {
        margin: 0 10px;
    }
    
    .table-filter-status {
        margin: 0 10px;
        padding: 8px 15px;
    }
    
    .category-table-row > div {
        border-right: none;
        border-bottom: 1px solid #f3f4f6;
        padding: 8px 12px;
    }
    
    .category-table-row > div:last-child {
        border-bottom: none;
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
}

@media (max-width: 480px) {
    .table-filter-header, 
    .category-table-row {
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
    
    .action-btn svg {
        width: 10px;
        height: 10px;
    }
}
"""