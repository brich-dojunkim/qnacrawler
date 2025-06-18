# html_reporter/styles/components/inquiry_modal/content/list.py
"""
문의 목록 컨테이너 스타일 - 스크롤 및 간격 문제 해결
"""

def get_list_styles():
    """문의 목록 기본 레이아웃 스타일 - 스크롤 및 간격 수정"""
    return """
/* === 문의 목록 컨테이너 === */
.inquiry-list {
    display: flex;
    flex-direction: column;
    gap: 16px;
    padding: 0;
    margin: 0;
    /* 🔧 높이 제한 완전 제거 */
    min-height: auto;
    max-height: none;
    height: auto;
    /* 🚨 핵심: 하단 패딩으로 마지막 카드까지 스크롤 보장 */
    padding-bottom: 50px;
    /* 🔧 좌우 여백은 부모(.inquiry-list-container)에서 제공 */
    padding-left: 0;
    padding-right: 0;
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

/* === 문의 카드 여백 정리 === */
.inquiry-card {
    /* 🔧 개별 카드 마진 제거 - gap으로 간격 제어 */
    margin: 0;
    margin-bottom: 0;
    /* 카드 높이 제한 해제 */
    min-height: auto;
    max-height: none;
}

/* 첫 번째/마지막 카드 특별 여백 제거 */
.inquiry-list > .inquiry-card:first-child {
    margin-top: 0;
}

.inquiry-list > .inquiry-card:last-child {
    margin-bottom: 0;
}

/* === 가상화된 목록 지원 === */
.inquiry-list.virtualized {
    overflow-y: visible;
    max-height: none;
    padding-bottom: 30px;  /* 가상화된 경우 패딩 조금 줄임 */
}

/* === 스크롤 성능 최적화 === */
.inquiry-list {
    /* GPU 가속 활용 */
    transform: translateZ(0);
    /* 스크롤 최적화 */
    will-change: transform;
}

/* === 🔧 디버깅용 시각적 확인 (필요시 주석 해제) === */
/*
.inquiry-list {
    border: 2px dashed green;
    background: rgba(0, 255, 0, 0.1);
}

.inquiry-card {
    border: 1px solid orange;
    background: rgba(255, 165, 0, 0.1);
}
*/

/* === 반응형 스타일 === */
@media (max-width: 768px) {
    .inquiry-list {
        gap: 12px;
        padding-bottom: 40px;
    }
}

@media (max-width: 480px) {
    .inquiry-list {
        gap: 10px;
        padding-bottom: 35px;
    }
}

/* === 접근성 및 포커스 관리 === */
.inquiry-list:focus-within {
    outline: none;
}

.inquiry-card:focus-within {
    outline: 2px solid #667eea;
    outline-offset: 2px;
    border-radius: 16px;
}

/* === 인쇄 최적화 === */
@media print {
    .inquiry-list {
        gap: 8px;
        padding-bottom: 0;
    }
    
    .inquiry-card {
        break-inside: avoid;
        margin-bottom: 8px;
    }
}
"""