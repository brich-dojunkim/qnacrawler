# html_reporter/styles/components/inquiry_modal/header.py
"""
문의 상세보기 모달 헤더 및 통계 스타일 - 모든 배지 스타일 통일
"""

def get_header_styles():
    """모달 헤더 및 통계 영역 스타일 - 모든 배지 스타일 통일"""
    return """
/* === 모달 헤더 (확장된 통계 지원) === */
.inquiry-modal-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 20px 24px;
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    border-radius: 20px 20px 0 0;
    position: relative;
    box-shadow: 0 4px 20px rgba(102, 126, 234, 0.2);
}

.inquiry-modal-title-section {
    flex: 1;
    margin-right: 20px;
}

.inquiry-modal-title {
    font-size: 1.4rem;
    font-weight: 700;
    margin: 0 0 16px 0;
    display: flex;
    align-items: center;
    gap: 8px;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* === 확장된 통계 영역 (2줄 지원) === */
.inquiry-modal-stats {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-top: 8px;
    /* 2줄까지 허용 */
    max-width: 100%;
}

/* === 통일된 배지 스타일 (모든 stat-item 포함) === */
.stat-item,
.stat-item.team-journey-badge {
    display: flex;
    align-items: center;
    gap: 6px;
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 12px;
    padding: 8px 12px;
    font-size: 0.875rem !important;
    font-weight: 500;
    transition: all 0.3s ease;
    white-space: nowrap;
    flex: 0 0 auto;
    color: #ffffff !important;
}

/* === 통일된 호버 효과 === */
.stat-item:hover,
.stat-item.team-journey-badge:hover {
    background: rgba(255, 255, 255, 0.25);
    border-color: rgba(255, 255, 255, 0.3);
    transform: translateY(-1px);
}

.stat-icon {
    font-size: 1rem !important;
    opacity: 1;
    color: #ffffff;
}

/* === 통일된 텍스트 스타일 === */
.inquiry-modal-header .stat-label {
    color: #ffffff !important;
    font-weight: 400;
    font-size: 0.875rem !important;
}

.inquiry-modal-header .stat-value {
    font-weight: 700;
    color: #ffffff !important;
    font-size: 0.875rem !important;
}

.inquiry-modal-header .stat-item {
    color: #ffffff !important;
    font-size: 0.875rem !important;
}

/* === 닫기 버튼 === */
.inquiry-modal-close {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 12px;
    width: 44px;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.3s ease;
    color: white;
    flex-shrink: 0;
}

.inquiry-modal-close:hover {
    background: rgba(255, 255, 255, 0.25);
    transform: scale(1.05);
}

.inquiry-modal-close:active {
    transform: scale(0.95);
}

.inquiry-modal-close svg {
    width: 20px;
    height: 20px;
    stroke-width: 2.5;
}

/* === 반응형 - 태블릿 === */
@media (max-width: 768px) {
    .inquiry-modal-header {
        padding: 16px 20px;
        flex-direction: column;
        align-items: stretch;
        gap: 16px;
    }
    
    .inquiry-modal-title-section {
        margin-right: 0;
    }
    
    .inquiry-modal-title {
        font-size: 1.25rem;
        margin-bottom: 12px;
    }
    
    .inquiry-modal-stats {
        gap: 12px;
        justify-content: flex-start;
    }
    
    .stat-item,
    .stat-item.team-journey-badge {
        padding: 6px 10px;
        font-size: 0.875rem !important;
    }
    
    .stat-icon {
        font-size: 1rem !important;
    }
    
    .inquiry-modal-close {
        position: absolute;
        top: 16px;
        right: 20px;
        width: 36px;
        height: 36px;
    }
    
    .inquiry-modal-close svg {
        width: 18px;
        height: 18px;
    }
}

/* === 반응형 - 모바일 === */
@media (max-width: 480px) {
    .inquiry-modal-header {
        padding: 14px 16px;
        border-radius: 12px 12px 0 0;
    }
    
    .inquiry-modal-title {
        font-size: 1.1rem;
        margin-bottom: 10px;
        padding-right: 45px; /* 닫기 버튼 공간 확보 */
    }
    
    .inquiry-modal-stats {
        gap: 8px;
        flex-wrap: wrap;
    }
    
    .stat-item,
    .stat-item.team-journey-badge {
        padding: 5px 8px;
        font-size: 0.875rem !important;
        border-radius: 8px;
        flex: 1 1 calc(50% - 4px);
        min-width: 120px;
    }
    
    .stat-icon {
        font-size: 1rem !important;
    }
    
    .inquiry-modal-close {
        top: 14px;
        right: 16px;
        width: 32px;
        height: 32px;
    }
    
    .inquiry-modal-close svg {
        width: 16px;
        height: 16px;
        stroke-width: 3;
    }
}

/* === 애니메이션 효과 === */
@keyframes statsSlideIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.stat-item {
    animation: statsSlideIn 0.3s ease-out;
}

.stat-item:nth-child(1) { animation-delay: 0.1s; }
.stat-item:nth-child(2) { animation-delay: 0.2s; }
.stat-item:nth-child(3) { animation-delay: 0.3s; }
.stat-item:nth-child(4) { animation-delay: 0.4s; }

/* === 접근성 개선 === */
.inquiry-modal-close:focus {
    outline: 2px solid rgba(255, 255, 255, 0.5);
    outline-offset: 2px;
}

.stat-item:focus-within {
    background: rgba(255, 255, 255, 0.25);
    outline: 2px solid rgba(255, 255, 255, 0.3);
    outline-offset: 1px;
}
"""