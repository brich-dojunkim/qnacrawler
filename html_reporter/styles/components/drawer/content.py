# html_reporter/styles/components/drawer/content.py
"""
드로어 콘텐츠 영역 및 뷰 전환 스타일
"""

def get_drawer_content_styles():
    """드로어 콘텐츠 영역 스타일"""
    return """
/* === 드로어 콘텐츠 === */
.drawer-content {
    flex: 1;
    overflow: hidden;
    position: relative;
}

/* === 스크롤바 스타일 === */
.inquiry-list::-webkit-scrollbar,
.inquiry-detail-content::-webkit-scrollbar {
    width: 6px;
}

.inquiry-list::-webkit-scrollbar-track,
.inquiry-detail-content::-webkit-scrollbar-track {
    background: #f1f5f9;
}

.inquiry-list::-webkit-scrollbar-thumb,
.inquiry-detail-content::-webkit-scrollbar-thumb {
    background: #cbd5e1;
    border-radius: 3px;
}

.inquiry-list::-webkit-scrollbar-thumb:hover,
.inquiry-detail-content::-webkit-scrollbar-thumb:hover {
    background: #94a3b8;
}
"""

def get_drawer_view_styles():
    """드로어 뷰 전환 스타일"""
    return """
/* === 뷰 전환 시스템 === */
.inquiry-list-view,
.inquiry-detail-view {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: white;
    transition: transform 0.3s ease;
}

.inquiry-detail-view {
    transform: translateX(100%);
}

.inquiry-detail-view.active {
    transform: translateX(0);
}

.inquiry-list-view.detail-mode {
    transform: translateX(-100%);
}

/* === 상세보기 헤더 === */
.detail-header {
    padding: 16px 20px;
    border-bottom: 1px solid #e2e8f0;
    background: #f8fafc;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.back-btn {
    background: none;
    border: none;
    color: #667eea;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 4px;
    font-size: 0.9rem;
    font-weight: 500;
    padding: 6px 8px;
    border-radius: 6px;
    transition: background 0.2s ease;
}

.back-btn:hover {
    background: #e0f2fe;
}

.detail-inquiry-info {
    display: flex;
    align-items: center;
    gap: 8px;
}

.detail-inquiry-id {
    font-weight: 600;
    color: #374151;
}

.inquiry-detail-content {
    height: calc(100% - 60px);
    overflow-y: auto;
    padding: 20px;
}
"""