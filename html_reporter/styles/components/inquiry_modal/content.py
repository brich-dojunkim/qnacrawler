# html_reporter/styles/components/inquiry_modal/content.py
"""
문의 상세보기 모달 콘텐츠 스타일 (문의 목록 및 카드)
"""

def get_content_styles():
    """문의 목록 및 카드 스타일"""
    return """
/* === 문의 목록 === */
.inquiry-list {
    display: flex;
    flex-direction: column;
    gap: 16px;
}

/* === 문의 카드 === */
.inquiry-card {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 16px;
    padding: 20px;
    transition: all 0.3s ease;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
    position: relative;
    overflow: hidden;
}

.inquiry-card:hover {
    border-color: #667eea;
    box-shadow: 0 8px 30px rgba(102, 126, 234, 0.15);
    transform: translateY(-2px);
}

/* === 카드 헤더 === */
.inquiry-card-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 16px;
    flex-wrap: wrap;
    gap: 12px;
}

.inquiry-meta {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    align-items: center;
    flex: 1;
}

.inquiry-actions {
    display: flex;
    align-items: center;
    gap: 8px;
}

/* === 배지 스타일 === */
.urgency-badge, .team-badge, .category-badge, .date-badge, .status-badge {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    padding: 4px 8px;
    border-radius: 8px;
    font-size: 0.75rem;
    font-weight: 600;
    white-space: nowrap;
}

.urgency-badge.urgent {
    background: linear-gradient(135deg, #fee2e2, #fecaca);
    color: #dc2626;
    border: 1px solid #f87171;
}

.urgency-badge.normal {
    background: linear-gradient(135deg, #f0f9ff, #e0f2fe);
    color: #0369a1;
    border: 1px solid #38bdf8;
}

.team-badge {
    background: linear-gradient(135deg, #f3e8ff, #e9d5ff);
    color: #7c3aed;
    border: 1px solid #a78bfa;
}

.category-badge {
    background: linear-gradient(135deg, #ecfdf5, #d1fae5);
    color: #059669;
    border: 1px solid #34d399;
}

.date-badge {
    background: linear-gradient(135deg, #f9fafb, #f3f4f6);
    color: #374151;
    border: 1px solid #d1d5db;
}

.status-badge.completed {
    background: linear-gradient(135deg, #ecfdf5, #d1fae5);
    color: #059669;
    border: 1px solid #34d399;
}

.status-badge.pending {
    background: linear-gradient(135deg, #fef3c7, #fde68a);
    color: #d97706;
    border: 1px solid #f59e0b;
}

.status-badge.in-progress {
    background: linear-gradient(135deg, #dbeafe, #bfdbfe);
    color: #2563eb;
    border: 1px solid #60a5fa;
}

/* === 카드 본문 === */
.inquiry-card-body {
    margin-bottom: 16px;
}

.inquiry-content {
    margin-bottom: 16px;
}

.content-preview, .full-content {
    font-size: 0.9rem;
    line-height: 1.6;
    color: #374151;
    margin-bottom: 8px;
}

.full-content {
    background: #f9fafb;
    padding: 12px;
    border-radius: 8px;
    border-left: 3px solid #667eea;
}

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

.expand-icon {
    transition: transform 0.3s ease;
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
}

.answer-meta {
    font-size: 0.75rem;
    color: #6b7280;
    font-weight: 500;
}

.answer-preview, .full-answer {
    font-size: 0.85rem;
    line-height: 1.5;
    color: #4b5563;
    margin-bottom: 8px;
}

.full-answer {
    background: white;
    padding: 12px;
    border-radius: 8px;
    border-left: 3px solid #10b981;
}

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

/* === 카드 푸터 === */
.inquiry-card-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
    padding-top: 16px;
    border-top: 1px solid #f3f4f6;
}

.inquiry-stats {
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
}

.stat-item {
    display: flex;
    align-items: center;
    gap: 4px;
    font-size: 0.75rem;
    color: #6b7280;
    font-weight: 500;
}

.stat-item svg {
    opacity: 0.7;
}

.inquiry-actions-footer {
    display: flex;
    gap: 8px;
}

.action-btn {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 6px 12px;
    border-radius: 8px;
    font-size: 0.75rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    border: none;
    text-decoration: none;
}

.action-btn.primary {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3);
}

.action-btn.primary:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
}

.action-btn.secondary {
    background: #f3f4f6;
    color: #374151;
    border: 1px solid #e5e7eb;
}

.action-btn.secondary:hover {
    background: #e5e7eb;
    color: #111827;
    transform: translateY(-1px);
}

/* === 검색어 하이라이팅 === */
.search-highlight {
    background: linear-gradient(135deg, #fef3c7, #fde68a);
    color: #92400e;
    padding: 2px 4px;
    border-radius: 4px;
    font-weight: 600;
}

/* === 반응형 - 태블릿 === */
@media (max-width: 768px) {
    .inquiry-card {
        padding: 16px;
        border-radius: 12px;
    }
    
    .inquiry-card-header {
        flex-direction: column;
        align-items: stretch;
        gap: 10px;
    }
    
    .inquiry-meta {
        justify-content: flex-start;
        gap: 6px;
    }
    
    .inquiry-actions {
        justify-content: flex-end;
    }
    
    .urgency-badge, .team-badge, .category-badge, .date-badge, .status-badge {
        font-size: 0.7rem;
        padding: 3px 6px;
    }
    
    .content-preview, .full-content {
        font-size: 0.85rem;
    }
    
    .answer-section {
        padding: 12px;
    }
    
    .inquiry-card-footer {
        flex-direction: column;
        align-items: stretch;
        gap: 10px;
    }
    
    .inquiry-stats {
        justify-content: center;
        gap: 12px;
    }
    
    .inquiry-actions-footer {
        justify-content: center;
    }
    
    .action-btn {
        flex: 1;
        justify-content: center;
        padding: 8px 12px;
    }
}

/* === 반응형 - 모바일 === */
@media (max-width: 480px) {
    .inquiry-list {
        gap: 12px;
    }
    
    .inquiry-card {
        padding: 12px;
        border-radius: 10px;
    }
    
    .inquiry-card-header {
        margin-bottom: 12px;
        gap: 8px;
    }
    
    .inquiry-meta {
        gap: 4px;
        flex-direction: column;
        align-items: stretch;
    }
    
    .urgency-badge, .team-badge, .category-badge, .date-badge, .status-badge {
        font-size: 0.65rem;
        padding: 2px 5px;
        text-align: center;
    }
    
    .content-preview, .full-content {
        font-size: 0.8rem;
        line-height: 1.5;
    }
    
    .show-full-content, .show-full-answer {
        font-size: 0.7rem;
        padding: 3px 6px;
    }
    
    .answer-section {
        padding: 10px;
        margin-top: 10px;
    }
    
    .answer-header {
        flex-direction: column;
        align-items: stretch;
        gap: 6px;
        margin-bottom: 6px;
    }
    
    .answer-label {
        font-size: 0.8rem;
    }
    
    .answer-meta {
        font-size: 0.7rem;
        text-align: center;
    }
    
    .answer-preview, .full-answer {
        font-size: 0.75rem;
    }
    
    .inquiry-card-footer {
        padding-top: 12px;
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
    }
    
    .action-btn {
        font-size: 0.7rem;
        padding: 6px 10px;
    }
}

/* === 애니메이션 효과 === */
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

/* === 접근성 개선 === */
.inquiry-card:focus-within {
    outline: 2px solid #667eea;
    outline-offset: 2px;
}

.action-btn:focus {
    outline: 2px solid #667eea;
    outline-offset: 2px;
}

.show-full-content:focus,
.show-full-answer:focus {
    outline: 2px solid #667eea;
    outline-offset: 1px;
}

/* === 인쇄 지원 === */
@media print {
    .inquiry-card {
        break-inside: avoid;
        box-shadow: none;
        border: 1px solid #ccc;
    }
    
    .inquiry-actions-footer {
        display: none;
    }
    
    .action-btn {
        display: none;
    }
    
    .show-full-content,
    .show-full-answer {
        display: none;
    }
    
    .full-content,
    .full-answer {
        display: block !important;
    }
    
    .content-preview,
    .answer-preview {
        display: none;
    }
}

/* === 다크 모드 대응 === */
@media (prefers-color-scheme: dark) {
    .inquiry-card {
        background: #1f2937;
        border-color: #374151;
        color: #f9fafb;
    }
    
    .inquiry-card:hover {
        border-color: #667eea;
        background: #111827;
    }
    
    .content-preview, .full-content {
        color: #e5e7eb;
    }
    
    .full-content {
        background: #374151;
        border-left-color: #667eea;
    }
    
    .answer-section {
        background: #374151;
        border-color: #4b5563;
    }
    
    .full-answer {
        background: #1f2937;
        border-left-color: #10b981;
        color: #e5e7eb;
    }
    
    .answer-preview, .full-answer {
        color: #d1d5db;
    }
    
    .inquiry-card-footer {
        border-top-color: #4b5563;
    }
    
    .stat-item {
        color: #9ca3af;
    }
    
    .action-btn.secondary {
        background: #374151;
        color: #e5e7eb;
        border-color: #4b5563;
    }
    
    .action-btn.secondary:hover {
        background: #4b5563;
        color: #f9fafb;
    }
}

.seller-badge, .author-badge {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    padding: 4px 8px;
    border-radius: 8px;
    font-size: 0.75rem;
    font-weight: 600;
    white-space: nowrap;
}

.seller-badge {
    background: linear-gradient(135deg, #e0f2fe, #bae6fd);
    color: #0369a1;
    border: 1px solid #38bdf8;
}

.author-badge {
    background: linear-gradient(135deg, #f0fdf4, #dcfce7);
    color: #15803d;
    border: 1px solid #4ade80;
    transition: all 0.2s ease;
}

.author-badge:hover {
    background: linear-gradient(135deg, #dcfce7, #bbf7d0);
    transform: translateY(-1px);
    box-shadow: 0 2px 4px rgba(21, 128, 61, 0.2);
}
"""