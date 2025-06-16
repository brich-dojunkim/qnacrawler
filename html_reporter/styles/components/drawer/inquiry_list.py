# html_reporter/styles/components/drawer/inquiry_list.py
"""
문의 목록 및 아이템 스타일 - 확장된 너비에 맞춘 패딩 조정
"""

def get_inquiry_list_styles():
    """문의 목록 컨테이너 스타일"""
    return """
/* === 문의 목록 === */
.inquiry-list {
    height: 100%;
    overflow-y: auto;
    padding: 0;
    background: white;
}

/* === 빈 상태 === */
.inquiry-list-empty {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    padding: 40px 30px;  /* 좌우 패딩 20px → 30px로 증가 */
    background: white;
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
    background: white;
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
"""

def get_inquiry_item_styles():
    """개별 문의 아이템 스타일 - 확장된 너비에 맞춘 패딩"""
    return """
/* === 개별 문의 아이템 === */
.inquiry-item {
    padding: 16px 30px;  /* 좌우 패딩 20px → 30px로 증가 */
    border-bottom: 1px solid #f1f5f9;
    cursor: pointer;
    transition: background 0.2s ease;
    background: white;
}

.inquiry-item:hover {
    background: #f8fafc;
}

.inquiry-item:last-child {
    border-bottom: none;
}

/* === 문의 아이템 헤더 === */
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

/* === 문의 메타 정보 === */
.inquiry-meta {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 2px;
    font-size: 0.75rem;
    color: #6b7280;
}

.inquiry-date {
    font-weight: 500;
}

.inquiry-seller {
    color: #9ca3af;
}

/* === 문의 미리보기 === */
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

/* === 문의 아이템 푸터 === */
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
"""