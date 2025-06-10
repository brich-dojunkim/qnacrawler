# html_reporter/styles/tabs.py
"""탭 네비게이션 스타일"""

def get_tab_styles():
    return """
/* === 탭 네비게이션 === */
.tab-navigation {
    background: linear-gradient(135deg, #f8fafc, #e2e8f0);
    border-bottom: 1px solid #e2e8f0;
    padding: 0;
}

.tab-nav {
    display: flex;
    gap: 0;
    overflow-x: auto;
}

.tab-btn {
    padding: 18px 28px;
    border: none;
    background: none;
    font-size: 1rem;
    font-weight: 600;
    color: #64748b;
    cursor: pointer;
    border-bottom: 4px solid transparent;
    transition: all 0.3s ease;
    white-space: nowrap;
    position: relative;
}

.tab-btn::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1));
    opacity: 0;
    transition: opacity 0.3s ease;
}

.tab-btn:hover::before {
    opacity: 1;
}

.tab-btn.active {
    color: #667eea;
    border-bottom-color: #667eea;
    background: white;
    box-shadow: 0 -2px 8px rgba(102, 126, 234, 0.1);
}

.tab-btn:hover:not(.active) {
    color: #374151;
    background: rgba(255,255,255,0.7);
}

/* === 탭 콘텐츠 === */
.tab-content {
    display: none;
    padding: 30px;
}

.tab-content.active {
    display: block;
}
"""