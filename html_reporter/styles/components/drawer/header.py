# html_reporter/styles/components/drawer/header.py
"""
드로어 헤더 및 검색 영역 스타일 - 확장된 너비에 맞춘 패딩 조정
"""

def get_drawer_header_styles():
    """드로어 헤더 스타일 - 확장된 너비에 맞춘 패딩"""
    return """
/* === 드로어 헤더 === */
.drawer-header {
    padding: 20px 30px;  /* 좌우 패딩 20px → 30px로 증가 */
    border-bottom: 1px solid #e2e8f0;
    background: linear-gradient(135deg, #ffffff, #f8fafc);
}

.drawer-title-section {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 16px;
}

.drawer-category-name {
    font-size: 1.2rem;
    font-weight: 700;
    color: #374151;
    margin: 0;
}

.drawer-inquiry-count {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    padding: 4px 10px;
    border-radius: 12px;
    font-size: 0.8rem;
    font-weight: 600;
}

.drawer-controls {
    display: flex;
    align-items: center;
    gap: 8px;
}

.drawer-select {
    padding: 6px 10px;
    border: 1px solid #d1d5db;
    border-radius: 6px;
    background: white;
    font-size: 0.8rem;
    color: #374151;
    cursor: pointer;
}

.drawer-select:focus {
    outline: none;
    border-color: #667eea;
    box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.1);
}

.drawer-close-btn {
    background: none;
    border: none;
    padding: 6px;
    border-radius: 4px;
    cursor: pointer;
    color: #6b7280;
    transition: all 0.2s ease;
    margin-left: auto;
}

.drawer-close-btn:hover {
    background: #f3f4f6;
    color: #374151;
}
"""

def get_drawer_search_styles():
    """드로어 검색 영역 스타일 - 확장된 너비에 맞춘 패딩"""
    return """
/* === 검색 영역 === */
.drawer-search {
    padding: 16px 30px;  /* 좌우 패딩 20px → 30px로 증가 */
    border-bottom: 1px solid #e2e8f0;
    background: white;
}

.search-input-wrapper {
    position: relative;
    display: flex;
    align-items: center;
}

.search-icon {
    position: absolute;
    left: 10px;
    color: #9ca3af;
    pointer-events: none;
}

.drawer-search-input {
    width: 100%;
    padding: 8px 35px 8px 35px;
    border: 1px solid #d1d5db;
    border-radius: 8px;
    background: #f9fafb;
    font-size: 0.9rem;
    transition: all 0.2s ease;
}

.drawer-search-input:focus {
    outline: none;
    border-color: #667eea;
    background: white;
    box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.1);
}

.drawer-search-input::placeholder {
    color: #9ca3af;
}

.search-clear-btn {
    position: absolute;
    right: 8px;
    background: none;
    border: none;
    color: #9ca3af;
    cursor: pointer;
    padding: 4px;
    border-radius: 3px;
    font-size: 0.9rem;
    transition: all 0.2s ease;
}

.search-clear-btn:hover {
    background: #f3f4f6;
    color: #374151;
}
"""