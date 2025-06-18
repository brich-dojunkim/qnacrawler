# html_reporter/styles/components/inquiry_modal/content/responsive.py
"""
문의 모달 콘텐츠 반응형 스타일 - 다크모드 제거
"""

def get_responsive_styles():
    """반응형 스타일 (모든 화면 크기 대응) - 다크모드 제거"""
    return """
/* === 반응형 - 태블릿 (768px 이하) === */
@media (max-width: 768px) {
    /* 목록 간격 조정 */
    .inquiry-list {
        gap: 12px;
    }
    
    /* 카드 기본 크기 조정 */
    .inquiry-card {
        padding: 16px;
        border-radius: 12px;
    }
    
    /* 헤더 레이아웃 변경 */
    .inquiry-card-header {
        flex-direction: column;
        align-items: stretch;
        gap: 10px;
        margin-bottom: 12px;
    }
    
    .inquiry-meta {
        justify-content: flex-start;
        gap: 6px;
        order: 1;
    }
    
    .inquiry-actions {
        justify-content: flex-end;
        order: 2;
    }
    
    /* 배지 크기 조정 */
    .urgency-badge, 
    .team-badge, 
    .category-badge, 
    .date-badge, 
    .status-badge,
    .seller-badge,
    .author-badge {
        font-size: 0.7rem;
        padding: 3px 6px;
    }
    
    /* 본문 텍스트 크기 조정 */
    .content-preview, 
    .full-content {
        font-size: 0.85rem;
        line-height: 1.5;
    }
    
    /* 답변 섹션 조정 */
    .answer-section {
        padding: 12px;
        margin-top: 10px;
    }
    
    .answer-header {
        flex-direction: column;
        gap: 6px;
        margin-bottom: 6px;
    }
    
    .answer-meta {
        text-align: left;
    }
    
    /* 푸터 레이아웃 변경 */
    .inquiry-card-footer {
        flex-direction: column;
        align-items: stretch;
        gap: 10px;
        padding-top: 12px;
    }
    
    .inquiry-stats {
        justify-content: center;
        gap: 12px;
        order: 1;
    }
    
    .inquiry-actions-footer {
        justify-content: center;
        order: 2;
    }
    
    /* 액션 버튼 조정 */
    .action-btn {
        flex: 1;
        justify-content: center;
        padding: 8px 12px;
        min-height: 44px; /* 터치 친화적 */
    }
    
    /* 토글 버튼 크기 증가 */
    .show-full-content,
    .show-full-answer {
        padding: 6px 10px;
        min-height: 36px;
    }
}

/* === 반응형 - 모바일 (480px 이하) === */
@media (max-width: 480px) {
    /* 목록 및 카드 최적화 */
    .inquiry-list {
        gap: 10px;
    }
    
    .inquiry-card {
        padding: 12px;
        border-radius: 10px;
        margin: 0; /* 모바일에서는 여백 최소화 */
    }
    
    /* 헤더 최적화 */
    .inquiry-card-header {
        margin-bottom: 10px;
        gap: 8px;
    }
    
    .inquiry-meta {
        gap: 4px;
        flex-direction: column;
        align-items: stretch;
    }
    
    /* 배지 모바일 최적화 */
    .urgency-badge, 
    .team-badge, 
    .category-badge, 
    .date-badge, 
    .status-badge,
    .seller-badge,
    .author-badge {
        font-size: 0.65rem;
        padding: 2px 5px;
        text-align: center;
        justify-content: center;
    }
    
    .urgency-icon,
    .status-icon {
        font-size: 0.7rem;
    }
    
    /* 본문 최적화 */
    .content-preview, 
    .full-content {
        font-size: 0.8rem;
        line-height: 1.4;
    }
    
    .full-content {
        padding: 8px;
        margin-top: 6px;
    }
    
    /* 확장 버튼 최적화 */
    .show-full-content, 
    .show-full-answer {
        font-size: 0.7rem;
        padding: 4px 8px;
        gap: 3px;
    }
    
    .expand-icon {
        width: 10px;
        height: 10px;
    }
    
    /* 답변 섹션 최적화 */
    .answer-section {
        padding: 8px;
        margin-top: 8px;
        border-radius: 8px;
    }
    
    .answer-header {
        margin-bottom: 4px;
        gap: 4px;
    }
    
    .answer-label {
        font-size: 0.8rem;
    }
    
    .answer-meta {
        font-size: 0.7rem;
    }
    
    .answer-preview, 
    .full-answer {
        font-size: 0.75rem;
        margin-bottom: 6px;
    }
    
    .full-answer {
        padding: 6px;
    }
    
    /* 푸터 최적화 */
    .inquiry-card-footer {
        padding-top: 10px;
        margin-top: 10px;
        gap: 8px;
    }
    
    .inquiry-stats {
        flex-direction: column;
        gap: 6px;
        text-align: center;
    }
    
    .stat-item {
        justify-content: center;
        font-size: 0.7rem;
        gap: 3px;
    }
    
    .stat-item svg {
        width: 10px;
        height: 10px;
    }
    
    /* 액션 버튼 최적화 */
    .action-btn {
        font-size: 0.7rem;
        padding: 6px 10px;
        gap: 4px;
        min-height: 40px;
    }
    
    .action-btn svg {
        width: 12px;
        height: 12px;
    }
    
    /* 스켈레톤 모바일 최적화 */
    .skeleton-card {
        padding: 12px;
        margin-bottom: 10px;
    }
    
    .skeleton-line {
        height: 10px;
        margin-bottom: 6px;
    }
}

/* === 반응형 - 매우 작은 화면 (360px 이하) === */
@media (max-width: 360px) {
    .inquiry-card {
        padding: 10px;
        border-radius: 8px;
    }
    
    .inquiry-card-header {
        gap: 6px;
        margin-bottom: 8px;
    }
    
    .inquiry-meta {
        gap: 3px;
    }
    
    .urgency-badge, 
    .team-badge, 
    .category-badge, 
    .date-badge, 
    .status-badge,
    .seller-badge,
    .author-badge {
        font-size: 0.6rem;
        padding: 1px 4px;
    }
    
    .content-preview, 
    .full-content {
        font-size: 0.75rem;
    }
    
    .action-btn {
        font-size: 0.65rem;
        padding: 5px 8px;
        min-height: 36px;
    }
    
    .stat-item {
        font-size: 0.65rem;
    }
}

/* === 가로 모드 최적화 === */
@media (max-height: 500px) and (orientation: landscape) {
    .inquiry-card {
        padding: 12px 16px;
    }
    
    .inquiry-card-header {
        margin-bottom: 8px;
    }
    
    .inquiry-card-footer {
        padding-top: 8px;
        margin-top: 8px;
    }
    
    .answer-section {
        padding: 10px;
        margin-top: 6px;
    }
    
    /* 로딩/빈 상태 높이 조정 */
    .inquiry-loading,
    .no-inquiries,
    .error-state {
        height: 120px;
        padding: 10px;
    }
    
    .no-inquiries-icon {
        font-size: 2rem;
        margin-bottom: 8px;
    }
    
    .loading-spinner {
        width: 24px;
        height: 24px;
        border-width: 2px;
    }
}

/* === 고대비 모드 지원 === */
@media (prefers-contrast: high) {
    .inquiry-card {
        border-width: 2px;
        border-color: #000;
    }
    
    .urgency-badge.urgent {
        background: #dc2626;
        color: #fff;
        border-color: #000;
    }
    
    .urgency-badge.normal {
        background: #2563eb;
        color: #fff;
        border-color: #000;
    }
    
    .action-btn.primary {
        background: #1d4ed8;
        border: 2px solid #000;
    }
    
    .action-btn.secondary {
        background: #fff;
        color: #000;
        border: 2px solid #000;
    }
}

/* === 움직임 줄이기 설정 대응 === */
@media (prefers-reduced-motion: reduce) {
    .inquiry-card,
    .action-btn,
    .show-full-content,
    .show-full-answer,
    .urgency-badge,
    .status-badge {
        transition: none;
        animation: none;
    }
    
    .inquiry-card:hover {
        transform: none;
    }
    
    .action-btn:hover {
        transform: none;
    }
    
    .loading-spinner {
        animation: none;
        border-top-color: transparent;
    }
    
    .no-inquiries-icon {
        animation: none;
    }
}

/* === 인쇄 최적화 === */
@media print {
    .inquiry-card {
        break-inside: avoid;
        box-shadow: none;
        border: 1px solid #ccc;
        margin-bottom: 1rem;
    }
    
    .inquiry-actions-footer,
    .action-btn,
    .show-full-content,
    .show-full-answer {
        display: none !important;
    }
    
    .full-content,
    .full-answer {
        display: block !important;
    }
    
    .content-preview,
    .answer-preview {
        display: none;
    }
    
    .urgency-badge.urgent {
        background: #fee2e2 !important;
        color: #dc2626 !important;
        -webkit-print-color-adjust: exact;
    }
    
    .status-badge.completed {
        background: #ecfdf5 !important;
        color: #059669 !important;
        -webkit-print-color-adjust: exact;
    }
}

/* === 애니메이션 효과 (움직임 허용시에만) === */
@media (prefers-reduced-motion: no-preference) {
    @keyframes cardSlideIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .inquiry-card {
        animation: cardSlideIn 0.3s ease-out;
    }
    
    .inquiry-card:nth-child(1) { animation-delay: 0.05s; }
    .inquiry-card:nth-child(2) { animation-delay: 0.1s; }
    .inquiry-card:nth-child(3) { animation-delay: 0.15s; }
    .inquiry-card:nth-child(4) { animation-delay: 0.2s; }
    .inquiry-card:nth-child(5) { animation-delay: 0.25s; }
}
"""