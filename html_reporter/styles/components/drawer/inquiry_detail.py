# html_reporter/styles/components/drawer/inquiry_detail.py
"""
문의 상세보기 및 답변 스타일
"""

def get_inquiry_detail_styles():
    """문의 상세보기 스타일"""
    return """
/* === 상세보기 콘텐츠 === */
.inquiry-detail-full {
    display: flex;
    flex-direction: column;
    gap: 24px;
}

/* === 문의 헤더 정보 === */
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

.meta-item strong {
    color: #374151;
}

/* === 주문 및 연락처 정보 === */
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

.contact-item strong {
    color: #374151;
}

/* === 섹션 제목 === */
.section-title {
    font-size: 1rem;
    font-weight: 600;
    color: #374151;
    margin: 0 0 12px 0;
    display: flex;
    align-items: center;
    gap: 6px;
}

/* === 문의 내용 섹션 === */
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

/* === 답변 섹션 === */
.answers-section {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    overflow: hidden;
}

.answers-list {
    padding: 0;
}

/* === 상세보기 상태 배지 === */
.detail-inquiry-status {
    padding: 4px 8px;
    border-radius: 10px;
    font-size: 0.8rem;
    font-weight: 600;
}

.detail-inquiry-status.status-answered {
    background: #f0fdf4;
    color: #059669;
    border: 1px solid #bbf7d0;
}

.detail-inquiry-status.status-unanswered {
    background: #fef3c7;
    color: #d97706;
    border: 1px solid #fde68a;
}
"""

def get_answer_styles():
    """답변 관련 스타일"""
    return """
/* === 개별 답변 아이템 === */
.answer-item {
    padding: 16px;
    border-bottom: 1px solid #f1f5f9;
}

.answer-item:last-child {
    border-bottom: none;
}

/* === 답변 헤더 === */
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

.answer-author strong {
    color: #374151;
    font-size: 0.9rem;
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

/* === 답변 내용 === */
.answer-content {
    margin-top: 8px;
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

/* === 답변 없음 상태 === */
.answers-section .empty-state {
    padding: 24px;
    text-align: center;
}

.answers-section .empty-state p {
    color: #9ca3af;
    font-size: 0.9rem;
    margin: 0;
}
"""