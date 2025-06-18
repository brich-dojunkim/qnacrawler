# styles/components/inquiry_modal/content/list.py
"""
문의 목록 컨테이너 스타일 - 높이 제한 해제
"""

def get_list_styles():
    """문의 목록 기본 레이아웃 스타일 - 높이 제한 제거"""
    return """
/* === 문의 목록 컨테이너 === */
.inquiry-list {
    display: flex;
    flex-direction: column;
    gap: 16px;
    padding: 0;
    margin: 0;
    /* 🔧 높이 제한 제거 - 모든 카드가 표시되도록 */
    min-height: auto;
    max-height: none;
    height: auto;
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

/* === 목록 스크롤 영역 === */
.inquiry-list-container {
    position: relative;
    /* 🔧 높이 제한 해제 */
    height: auto;
    min-height: 300px;
    max-height: 70vh; /* 뷰포트 높이의 70%까지만 제한 */
    overflow-y: auto;
    overflow-x: hidden;
    padding: 0;
    margin: 0;
}

/* 가상화된 목록 지원 */
.inquiry-list.virtualized {
    overflow-y: visible; /* 🔧 스크롤 제한 해제 */
    max-height: none;
}

/* 목록 아이템 간격 조정 */
.inquiry-list > .inquiry-card:first-child {
    margin-top: 0;
}

.inquiry-list > .inquiry-card:last-child {
    margin-bottom: 0;
}

/* === 디버깅용 스타일 === */
.inquiry-list {
    /* 디버깅: 목록 경계 표시 */
    /* border: 2px dashed red; */
}

.inquiry-card {
    /* 디버깅: 카드 경계 표시 */  
    /* border: 1px solid blue; */
    /* 카드 높이 제한 해제 */
    min-height: auto;
    max-height: none;
}
"""