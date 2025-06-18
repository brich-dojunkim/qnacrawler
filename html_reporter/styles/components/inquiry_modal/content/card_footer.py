# styles/components/inquiry_modal/content/card_footer.py
"""
문의 카드 푸터 (통계 및 액션 버튼) 스타일
"""

def get_card_footer_styles():
    """카드 푸터 영역 스타일"""
    return """
/* === 카드 푸터 === */
.inquiry-card-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
    padding-top: 16px;
    border-top: 1px solid #f3f4f6;
    margin-top: 16px;
}

/* === 통계 정보 영역 === */
.inquiry-stats {
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
    flex: 1;
    min-width: 0;
}

.stat-item {
    display: flex;
    align-items: center;
    gap: 4px;
    font-size: 0.75rem;
    color: #6b7280;
    font-weight: 500;
    white-space: nowrap;
}

.stat-item svg {
    opacity: 0.7;
    flex-shrink: 0;
}

.stat-item .stat-value {
    font-weight: 600;
    color: #374151;
}

/* 통계 항목별 색상 */
.stat-item.inquiry-id {
    color: #6b7280;
}

.stat-item.content-length {
    color: #7c3aed;
}

.stat-item.answer-count {
    color: #059669;
}

.stat-item.urgency {
    color: #dc2626;
}

/* === 액션 버튼 영역 === */
.inquiry-actions-footer {
    display: flex;
    gap: 8px;
    flex-shrink: 0;
}

/* 푸터 레이아웃 우선순위 */
.inquiry-stats {
    order: 1;
}

.inquiry-actions-footer {
    order: 2;
}

/* 컴팩트 모드 */
.inquiry-card.compact .inquiry-card-footer {
    padding-top: 12px;
    margin-top: 12px;
    gap: 8px;
}

.inquiry-card.compact .inquiry-stats {
    gap: 12px;
}

.inquiry-card.compact .stat-item {
    font-size: 0.7rem;
}

/* 통계 정보 툴팁 지원 */
.stat-item[title] {
    cursor: help;
}

.stat-item[title]:hover {
    color: #374151;
}

/* 푸터 아이콘 일관성 */
.inquiry-card-footer svg {
    width: 12px;
    height: 12px;
    stroke-width: 2;
}

/* 정렬 및 정돈 */
.inquiry-stats .stat-item:not(:last-child)::after {
    content: "•";
    margin-left: 8px;
    color: #d1d5db;
    font-weight: normal;
}

/* 빈 푸터 숨김 */
.inquiry-card-footer:empty {
    display: none;
}

/* 푸터만 있는 경우 상단 보더 제거 */
.inquiry-card-footer:first-child {
    border-top: none;
    padding-top: 0;
    margin-top: 0;
}
"""