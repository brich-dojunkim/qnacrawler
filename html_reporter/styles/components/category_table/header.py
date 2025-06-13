"""
카테고리 테이블 헤더 스타일 - 아코디언 내 테이블과 통일
"""

def get_header_styles():
    """테이블 헤더 관련 스타일 - 둥근 모서리 및 중앙정렬 적용"""
    return """
/* === 텍스트 옆 아이콘 테이블 필터 헤더 (완료율 칼럼 추가) === */
.table-filter-header {
    background: linear-gradient(135deg, #f1f5f9, #e2e8f0);
    display: grid;
    grid-template-columns: 2fr 1fr 1.2fr 0.8fr 0.8fr 0.8fr 0.6fr;
    gap: 0;
    padding: 12px 0;
    border-bottom: 1px solid #e2e8f0;
    /* 헤더는 둥근 모서리 없음 - 아코디언 내부 테이블과 동일 */
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
    justify-content: center; /* 상세보기 중앙 정렬 */
}

.column-header {
    display: flex;
    align-items: center;
    gap: 6px;
    min-height: 32px;
    justify-content: flex-start; /* 기본 왼쪽 정렬 */
}

/* 마지막 칼럼(상세보기)만 중앙 정렬 */
.filter-column:last-child .column-header {
    justify-content: center;
}

.column-label {
    font-weight: 700;
    color: #374151;
    font-size: 0.9rem;
    line-height: 1.2;
}

/* === 필터 상태 표시 (이중 여백 제거) === */
.table-filter-status {
    font-size: 1rem;
    font-weight: 700;
    color: #374151;
    padding: 16px 20px;
    margin: 0; /* 마진 제거 - accordion-content-area에서 이미 여백 적용됨 */
    background: linear-gradient(135deg, #f8fafc, #e2e8f0);
    border: 1px solid #e2e8f0;
    border-bottom: 1px solid #e2e8f0; /* 하단 경계선 명확히 */
    border-radius: 8px 8px 0 0; /* 상단만 둥글게 */
    display: flex;
    align-items: center;
    gap: 8px;
}

.clear-table-filters {
    background: none;
    border: none;
    color: #667eea;
    cursor: pointer;
    text-decoration: underline;
    font-size: 0.85rem;
    font-weight: 500;
    margin-left: 10px;
}

.clear-table-filters:hover {
    color: #5b67d8;
}
"""

def get_filter_button_styles():
    """필터 및 정렬 버튼 스타일"""
    return """
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
"""