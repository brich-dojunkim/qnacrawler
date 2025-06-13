# html_reporter/styles/components/drawer.py
"""
사이드 드로어 스타일
"""

def get_drawer_styles():
    """사이드 드로어 스타일"""
    return """
/* === 메인 콘텐츠 래퍼 === */
.main-content-wrapper {
    position: relative;
    display: flex;
    min-height: 100vh;
}

.detailed-analysis-section {
    flex: 1;
    transition: margin-right 0.3s ease;
}

.detailed-analysis-section.drawer-open {
    margin-right: 400px;
}

/* === 사이드 드로어 === */
.inquiry-drawer {
    position: fixed;
    top: 0;
    right: 0;
    width: 400px;
    height: 100vh;
    z-index: 1000;
    pointer-events: none;
}

.inquiry-drawer.open {
    pointer-events: all;
}

.drawer-overlay {
    position: absolute;
    top: 0;
    left: -100vw;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.3);
    opacity: 0;
    transition: opacity 0.3s ease;
    pointer-events: none;
}

.inquiry-drawer.open .drawer-overlay {
    opacity: 1;
    pointer-events: all;
}

.drawer-panel {
    position: absolute;
    top: 0;
    right: 0;
    width: 400px;
    height: 100vh;
    background: white;
    box-shadow: -4px 0 20px rgba(0, 0, 0, 0.15);
    transform: translateX(100%);
    transition: transform 0.3s ease;
    display: flex;
    flex-direction: column;
}

.inquiry-drawer.open .drawer-panel {
    transform: translateX(0);
}

/* === 드로어 헤더 === */
.drawer-header {
    padding: 20px;
    border-bottom: 1px solid #e2e8f0;
    background: linear-gradient(135deg, #f8fafc, #f1f5f9);
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

/* === 검색 영역 === */
.drawer-search {
    padding: 16px 20px;
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

.search-clear-btn {
    position: absolute;
    right: 8px;
    background: none;
    border: none;
    color: #9ca3af;
    cursor: pointer;
    padding: 4px;
    border-radius: 3px;
}

.search-clear-btn:hover {
    background: #f3f4f6;
    color: #374151;
}

/* === 드로어 콘텐츠 === */
.drawer-content {
    flex: 1;
    overflow: hidden;
    position: relative;
}

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

/* === 문의 목록 === */
.inquiry-list {
    height: 100%;
    overflow-y: auto;
    padding: 0;
}

.inquiry-item {
    padding: 16px 20px;
    border-bottom: 1px solid #f1f5f9;
    cursor: pointer;
    transition: background 0.2s ease;
}

.inquiry-item:hover {
    background: #f8fafc;
}

.inquiry-item:last-child {
    border-bottom: none;
}

.inquiry-item-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 8px;
}

.inquiry-id-section {
    display: flex;
    flex-direction: column;
    gap: 4px;
}

.inquiry-id {
    font-size: 0.9rem;
    font-weight: 600;
    color: #667eea;
}

.inquiry-badges {
    display: flex;
    gap: 4px;
}

.urgent-badge {
    background: #fef2f2;
    color: #dc2626;
    padding: 2px 6px;
    border-radius: 10px;
    font-size: 0.7rem;
    font-weight: 600;
    border: 1px solid #fca5a5;
}

.status-badge {
    padding: 2px 6px;
    border-radius: 10px;
    font-size: 0.7rem;
    font-weight: 600;
}

.status-answered {
    background: #f0fdf4;
    color: #059669;
    border: 1px solid #bbf7d0;
}

.status-unanswered {
    background: #fef3c7;
    color: #d97706;
    border: 1px solid #fde68a;
}

.inquiry-meta {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 2px;
    font-size: 0.75rem;
    color: #6b7280;
}

.inquiry-preview {
    margin-bottom: 12px;
}

.inquiry-preview-text {
    font-size: 0.85rem;
    color: #374151;
    line-height: 1.4;
    margin: 0;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

.inquiry-item-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.order-info {
    font-size: 0.75rem;
    color: #6b7280;
}

.view-detail-btn {
    background: #667eea;
    color: white;
    border: none;
    padding: 6px 10px;
    border-radius: 6px;
    font-size: 0.75rem;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 4px;
    transition: background 0.2s ease;
}

.view-detail-btn:hover {
    background: #5b67d8;
}

/* === 빈 상태 === */
.inquiry-list-empty {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    padding: 40px 20px;
}

.empty-state {
    text-align: center;
    color: #6b7280;
}

.empty-state svg {
    margin-bottom: 16px;
    color: #d1d5db;
}

.empty-state h4 {
    font-size: 1rem;
    margin: 0 0 8px 0;
    color: #374151;
}

.empty-state p {
    font-size: 0.85rem;
    margin: 0;
}

/* === 로딩 상태 === */
.inquiry-list-loading {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;
    gap: 16px;
    color: #6b7280;
}

.loading-spinner {
    width: 32px;
    height: 32px;
    border: 3px solid #f1f5f9;
    border-top: 3px solid #667eea;
    border-radius: 50%;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

/* === 상세보기 === */
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

/* === 상세 콘텐츠 === */
.inquiry-detail-full {
    display: flex;
    flex-direction: column;
    gap: 24px;
}

.inquiry-header-info {
    background: linear-gradient(135deg, #f8fafc, #f1f5f9);
    padding: 16px;
    border-radius: 8px;
    border: 1px solid #e2e8f0;
}

.inquiry-title {
    font-size: 1.1rem;
    margin: 0 0 12px 0;
    color: #374151;
}

.inquiry-meta-row {
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
    margin-bottom: 12px;
}

.meta-item {
    font-size: 0.85rem;
    color: #6b7280;
}

.inquiry-order-info,
.inquiry-contact-info {
    margin-top: 12px;
    padding-top: 12px;
    border-top: 1px solid #e2e8f0;
}

.contact-item {
    font-size: 0.85rem;
    color: #6b7280;
    margin-bottom: 4px;
}

.section-title {
    font-size: 1rem;
    font-weight: 600;
    color: #374151;
    margin: 0 0 12px 0;
    display: flex;
    align-items: center;
    gap: 6px;
}

.inquiry-content-section {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    overflow: hidden;
}

.inquiry-content {
    padding: 16px;
    background: #f9fafb;
}

.inquiry-text {
    font-family: inherit;
    font-size: 0.9rem;
    line-height: 1.6;
    color: #374151;
    white-space: pre-wrap;
    margin: 0;
}

.answers-section {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    overflow: hidden;
}

.answers-list {
    padding: 0;
}

.answer-item {
    padding: 16px;
    border-bottom: 1px solid #f1f5f9;
}

.answer-item:last-child {
    border-bottom: none;
}

.answer-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
}

.answer-author {
    display: flex;
    align-items: center;
    gap: 6px;
}

.answer-dept {
    color: #6b7280;
    font-size: 0.8rem;
    font-weight: normal;
}

.answer-date {
    font-size: 0.8rem;
    color: #6b7280;
}

.answer-text {
    font-family: inherit;
    font-size: 0.85rem;
    line-height: 1.5;
    color: #374151;
    white-space: pre-wrap;
    margin: 0;
    background: #f8fafc;
    padding: 12px;
    border-radius: 6px;
    border-left: 3px solid #667eea;
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

/* === 숨김 클래스 === */
.hidden {
    display: none !important;
}
"""