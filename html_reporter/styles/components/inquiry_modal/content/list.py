# styles/components/inquiry_modal/content/list.py
"""
문의 목록 컨테이너 스타일
"""

def get_list_styles():
    """문의 목록 기본 레이아웃 스타일"""
    return """
/* === 문의 목록 컨테이너 === */
.inquiry-list {
    display: flex;
    flex-direction: column;
    gap: 16px;
    padding: 0;
    margin: 0;
}

/* 목록이 비어있을 때 */
.inquiry-list:empty {
    display: none;
}

/* 목록 애니메이션 */
.inquiry-list.loading {
    opacity: 0.6;
    pointer-events: none;
}

.inquiry-list.loaded {
    opacity: 1;
    pointer-events: auto;
    transition: opacity 0.3s ease;
}

/* 목록 스크롤 영역 */
.inquiry-list-container {
    position: relative;
    height: 100%;
    overflow: hidden;
}

/* 가상화된 목록 지원 */
.inquiry-list.virtualized {
    overflow-y: auto;
    max-height: 100%;
}

/* 목록 아이템 간격 조정 */
.inquiry-list > .inquiry-card:first-child {
    margin-top: 0;
}

.inquiry-list > .inquiry-card:last-child {
    margin-bottom: 0;
}
"""