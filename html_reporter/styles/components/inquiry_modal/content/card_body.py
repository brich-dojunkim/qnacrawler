# html_reporter/styles/components/inquiry_modal/content/card_body.py
"""
문의 카드 본문 (내용 및 답변 섹션) 스타일 - 다크모드 제거
"""

def get_card_body_styles():
    """카드 본문 영역 스타일 - 다크모드 제거"""
    return """
/* === 카드 본문 === */
.inquiry-card-body {
    margin-bottom: 16px;
}

/* === 문의 내용 섹션 === */
.inquiry-content {
    margin-bottom: 16px;
}

.content-preview, 
.full-content {
    font-size: 0.9rem;
    line-height: 1.6;
    color: #374151;
    margin-bottom: 8px;
    word-break: break-word;
    overflow-wrap: break-word;
}

.full-content {
    background: #f9fafb;
    padding: 12px;
    border-radius: 8px;
    border-left: 3px solid #667eea;
    margin-top: 8px;
}

/* 내용 확장/축소 버튼 */
.show-full-content {
    background: none;
    border: none;
    color: #667eea;
    font-size: 0.8rem;
    font-weight: 600;
    cursor: pointer;
    padding: 4px 8px;
    border-radius: 6px;
    transition: all 0.2s ease;
    display: inline-flex;
    align-items: center;
    gap: 4px;
}

.show-full-content:hover {
    background: #f3f4f6;
    color: #4c51bf;
}

.show-full-content:focus {
    outline: 2px solid #667eea;
    outline-offset: 1px;
}

.expand-icon {
    transition: transform 0.3s ease;
    width: 12px;
    height: 12px;
}

.show-full-content[aria-expanded="true"] .expand-icon {
    transform: rotate(180deg);
}

/* === 답변 섹션 === */
.answer-section {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 16px;
    margin-top: 12px;
}

.answer-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
    flex-wrap: wrap;
    gap: 8px;
}

.answer-label {
    font-weight: 600;
    color: #374151;
    font-size: 0.875rem;
    display: flex;
    align-items: center;
    gap: 4px;
}

.answer-meta {
    font-size: 0.75rem;
    color: #6b7280;
    font-weight: 500;
}

.answer-preview, 
.full-answer {
    font-size: 0.85rem;
    line-height: 1.5;
    color: #4b5563;
    margin-bottom: 8px;
    word-break: break-word;
    overflow-wrap: break-word;
}

.full-answer {
    background: white;
    padding: 12px;
    border-radius: 8px;
    border-left: 3px solid #10b981;
    margin-top: 8px;
}

/* 답변 확장/축소 버튼 */
.show-full-answer {
    background: none;
    border: none;
    color: #10b981;
    font-size: 0.75rem;
    font-weight: 600;
    cursor: pointer;
    padding: 4px 8px;
    border-radius: 6px;
    transition: all 0.2s ease;
}

.show-full-answer:hover {
    background: #ecfdf5;
    color: #059669;
}

.show-full-answer:focus {
    outline: 2px solid #10b981;
    outline-offset: 1px;
}

/* 답변 작성자 정보 */
.answer-author {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    font-size: 0.75rem;
    color: #6b7280;
    margin-top: 4px;
}

.answer-author-avatar {
    width: 16px;
    height: 16px;
    border-radius: 50%;
    background: #e5e7eb;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.6rem;
    color: #9ca3af;
}

/* 다중 답변 지원 */
.multiple-answers {
    border-top: 1px solid #e5e7eb;
    margin-top: 12px;
    padding-top: 12px;
}

.answer-count {
    font-size: 0.75rem;
    color: #6b7280;
    margin-bottom: 8px;
}

/* 답변 상태 표시 */
.answer-section[data-status="draft"] {
    background: #fef3c7;
    border-color: #fde68a;
}

.answer-section[data-status="published"] {
    background: #ecfdf5;
    border-color: #d1fae5;
}
"""