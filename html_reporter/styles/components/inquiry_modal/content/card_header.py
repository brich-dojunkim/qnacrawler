# styles/components/inquiry_modal/content/card_header.py
"""
문의 카드 헤더 (메타정보 및 배지) 스타일
"""

def get_card_header_styles():
    """카드 헤더 영역 스타일"""
    return """
/* === 카드 헤더 === */
.inquiry-card-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 16px;
    flex-wrap: wrap;
    gap: 12px;
}

/* 메타정보 영역 */
.inquiry-meta {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    align-items: center;
    flex: 1;
    min-width: 0; /* flex 축소 허용 */
}

/* 액션 영역 */
.inquiry-actions {
    display: flex;
    align-items: center;
    gap: 8px;
    flex-shrink: 0; /* 액션은 축소되지 않음 */
}

/* 메타정보 레이아웃 최적화 */
.inquiry-meta > * {
    flex-shrink: 0; /* 배지들이 축소되지 않도록 */
}

/* 헤더 내 텍스트 요소 */
.inquiry-card-header .inquiry-id {
    font-family: 'Monaco', 'Consolas', monospace;
    font-size: 0.8rem;
    color: #6b7280;
    font-weight: 500;
}

.inquiry-card-header .inquiry-date {
    font-size: 0.75rem;
    color: #9ca3af;
    white-space: nowrap;
}

/* 우선순위 표시 */
.inquiry-card-header .priority-high {
    order: -1; /* 항상 맨 앞에 표시 */
}

.inquiry-card-header .priority-normal {
    order: 0;
}

/* 상태 표시 */
.inquiry-card-header .status-info {
    margin-left: auto; /* 오른쪽 정렬 */
    order: 999; /* 가장 뒤에 표시 */
}
"""