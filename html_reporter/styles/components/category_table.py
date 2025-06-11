# html_reporter/styles/components/category_table.py (새 파일)
"""카테고리 테이블 스타일"""

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

/* === 테이블 필터 헤더 === */
.table-filter-header {
    background: linear-gradient(135deg, #f8fafc, #e2e8f0);
    display: grid;
    grid-template-columns: 2.5fr 1.2fr 1.2fr 0.8fr 0.8fr 0.6fr;
    gap: 15px;
    padding: 12px 20px;
    border-bottom: 2px solid #667eea;
}

.filter-column {
    display: flex;
    flex-direction: column;
    gap: 4px;
}

.column-label {
    font-weight: bold;
    color: #495057;
    font-size: 0.85rem;
    margin-bottom: 2px;
}

/* === 필터 컨트롤들 === */
.filter-input {
    padding: 4px 8px;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    background: white;
    font-size: 0.8rem;
    width: 100%;
    transition: border-color 0.2s ease;
}

.filter-input:focus {
    outline: none;
    border-color: #667eea;
    box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.1);
}

.filter-dropdown {
    padding: 4px 8px;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    background: white;
    font-size: 0.8rem;
    width: 100%;
    cursor: pointer;
    transition: border-color 0.2s ease;
}

.filter-dropdown:focus {
    outline: none;
    border-color: #667eea;
}

.sort-button {
    padding: 4px 8px;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    background: white;
    font-size: 0.8rem;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    transition: all 0.2s ease;
}

.sort-button:hover {
    border-color: #667eea;
    background: #f8fafc;
}

.sort-button.active {
    background: #667eea;
    color: white;
    border-color: #667eea;
}

.sort-button.desc::after {
    content: "↓";
    font-weight: bold;
}

.sort-button.asc::after {
    content: "↑";
    font-weight: bold;
}

.filter-button {
    padding: 4px;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    background: white;
    cursor: pointer;
    font-size: 0.8rem;
    width: 100%;
    text-align: center;
    transition: all 0.2s ease;
}

.filter-button:hover {
    border-color: #667eea;
    background: #f8fafc;
}

/* === 테이블 데이터 로우 === */
.category-table-body {
    max-height: 600px;
    overflow-y: auto;
}

.category-table-row {
    display: grid;
    grid-template-columns: 2.5fr 1.2fr 1.2fr 0.8fr 0.8fr 0.6fr;
    gap: 15px;
    padding: 15px 20px;
    border-bottom: 1px solid #f1f3f4;
    transition: background 0.2s ease;
    cursor: pointer;
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
    color: #495057;
    line-height: 1.3;
}

.team-badge, .journey-badge {
    padding: 3px 8px;
    border-radius: 12px;
    font-size: 0.75rem;
    font-weight: bold;
    display: inline-block;
}

.team-badge {
    background: #fff3cd;
    color: #856404;
}

.journey-badge {
    background: #d4edda;
    color: #155724;
}

.metric-value {
    font-weight: 600;
    color: #667eea;
}

.urgent-rate {
    font-weight: 600;
}

.urgent-rate.high {
    color: #dc3545;
}

.urgent-rate.medium {
    color: #ffc107;
}

.urgent-rate.low {
    color: #28a745;
}

.action-btn {
    background: #667eea;
    color: white;
    border: none;
    border-radius: 4px;
    padding: 4px 8px;
    cursor: pointer;
    font-size: 0.75rem;
    transition: background 0.2s ease;
}

.action-btn:hover {
    background: #5a6fd8;
}

/* === 필터 상태 표시 === */
.table-filter-status {
    background: #e3f2fd;
    padding: 10px 20px;
    margin: 0 20px;
    border-radius: 6px 6px 0 0;
    font-size: 0.9rem;
    color: #1565c0;
    border: 1px solid #bbdefb;
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
    color: #5a6fd8;
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
.category-table-body::-webkit-scrollbar {
    width: 6px;
}

.category-table-body::-webkit-scrollbar-track {
    background: #f1f3f4;
}

.category-table-body::-webkit-scrollbar-thumb {
    background: #c1c8cd;
    border-radius: 3px;
}

.category-table-body::-webkit-scrollbar-thumb:hover {
    background: #a8b0b5;
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
}

@media (max-width: 480px) {
    .table-filter-header, 
    .category-table-row {
        padding: 10px 15px;
    }
    
    .filter-input, 
    .filter-dropdown, 
    .sort-button, 
    .filter-button {
        padding: 6px;
        font-size: 0.85rem;
    }
}
"""