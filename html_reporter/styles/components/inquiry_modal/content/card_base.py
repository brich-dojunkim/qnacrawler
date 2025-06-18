# html_reporter/styles/components/inquiry_modal/content/card_base.py
"""
문의 카드 기본 구조 및 레이아웃 스타일 - 다크모드 제거
"""

def get_card_base_styles():
    """문의 카드 기본 구조 스타일 - 다크모드 제거"""
    return """
/* === 문의 카드 기본 구조 === */
.inquiry-card {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 16px;
    padding: 20px;
    transition: all 0.3s ease;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
    position: relative;
    overflow: hidden;
    /* 🚨 핵심 수정: 카드 간격을 gap으로만 제어 */
    margin: 0;
    margin-bottom: 0;
    /* 🔧 카드 너비 및 박스 사이징 */
    width: 100%;
    box-sizing: border-box;
}

/* 호버 효과 */
.inquiry-card:hover {
    border-color: #667eea;
    box-shadow: 0 8px 30px rgba(102, 126, 234, 0.15);
    transform: translateY(-2px);
}

/* 포커스 상태 (접근성) */
.inquiry-card:focus-within {
    outline: 2px solid #667eea;
    outline-offset: 2px;
}

/* 선택된 카드 */
.inquiry-card.selected {
    border-color: #667eea;
    background: #f8faff;
    box-shadow: 0 4px 20px rgba(102, 126, 234, 0.2);
}

/* 오류 카드 */
.inquiry-card.error-card {
    border-color: #fca5a5;
    background: #fef2f2;
}

.inquiry-card.error-card:hover {
    border-color: #f87171;
    transform: none;
}

/* 로딩 중인 카드 */
.inquiry-card.loading {
    opacity: 0.6;
    pointer-events: none;
}

/* 🔧 카드 내부 기본 간격 최적화 */
.inquiry-card > * + * {
    margin-top: 16px;
}

/* 🔧 카드 데이터 속성 지원 - 왼쪽 보더 색상 */
.inquiry-card[data-urgency="urgent"] {
    border-left: 4px solid #ef4444;
}

.inquiry-card[data-urgency="normal"] {
    border-left: 4px solid #667eea;
}

.inquiry-card[data-status="completed"] {
    border-left-color: #10b981;
}

.inquiry-card[data-status="pending"] {
    border-left-color: #f59e0b;
}

/* === 🔧 카드 반응형 여백 === */
@media (max-width: 768px) {
    .inquiry-card {
        padding: 16px;
        border-radius: 12px;
    }
}

@media (max-width: 480px) {
    .inquiry-card {
        padding: 12px;
        border-radius: 10px;
    }
}

/* === 카드 애니메이션 최적화 === */
.inquiry-card {
    /* GPU 가속 활용 */
    transform: translateZ(0);
    will-change: transform;
}

/* === 인쇄용 카드 스타일 === */
@media print {
    .inquiry-card {
        break-inside: avoid;
        box-shadow: none;
        border: 1px solid #ccc;
        margin-bottom: 1rem;
        transform: none;
    }
    
    .inquiry-card:hover {
        transform: none;
        box-shadow: none;
    }
}
"""