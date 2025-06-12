# html_reporter/styles/components/accordion/controls.py
"""
아코디언 컨트롤 바 및 토글 스타일
"""

def get_controls_bar_styles():
    """통합된 컨트롤 바 스타일"""
    return """
/* === 통합된 컨트롤 바 (상단 여백 제거) === */
.controls-bar {
    background: white;
    padding: 16px 30px;
    border-bottom: 1px solid #e2e8f0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 20px;
}

.bulk-controls {
    display: flex;
    gap: 8px;
}

.bulk-control-btn {
    padding: 6px 12px;
    border: 1px solid #d1d5db;
    background: white;
    border-radius: 6px;
    cursor: pointer;
    font-size: 0.8rem;
    font-weight: 500;
    color: #374151;
    transition: all 0.2s ease;
}

.bulk-control-btn:hover {
    border-color: #667eea;
    color: #667eea;
    background: #f8fafc;
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
"""

def get_view_toggle_styles():
    """뷰 토글 컨트롤 스타일"""
    return """
.view-toggle-group {
    display: flex;
    align-items: center;
    gap: 12px;
}

.view-toggle-label {
    font-size: 0.9rem;
    font-weight: 600;
    color: #64748b;
}

.view-toggle-controls {
    display: flex;
    background: #f1f5f9;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid #e2e8f0;
}

.view-toggle-controls input[type="radio"] {
    display: none;
}

.toggle-btn {
    padding: 8px 16px;
    font-size: 0.9rem;
    font-weight: 600;
    color: #64748b;
    background: transparent;
    border: none;
    cursor: pointer;
    transition: all 0.3s ease;
    white-space: nowrap;
    text-align: center;
}

.view-toggle-controls input[type="radio"]:checked + .toggle-btn {
    color: white;
    background: linear-gradient(135deg, #667eea, #764ba2);
    box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3);
}

.toggle-btn:hover:not(.view-toggle-controls input[type="radio"]:checked + .toggle-btn) {
    background: rgba(102, 126, 234, 0.1);
    color: #374151;
}
"""