"""
카테고리 테이블 필터 및 드롭다운 스타일
"""

def get_dropdown_styles():
    """드롭다운 메뉴 스타일"""
    return """
/* === 드롭다운 래퍼 === */
.filter-dropdown-wrapper {
    position: relative;
    display: inline-block;
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
"""

def get_control_styles():
    """테이블 컨트롤 버튼 스타일"""
    return """
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
"""