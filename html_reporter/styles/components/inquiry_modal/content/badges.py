# styles/components/inquiry_modal/content/badges.py
"""
문의 카드 배지 스타일 (긴급도, 상태, 팀, 카테고리 등)
"""

def get_badges_styles():
    """모든 배지 스타일"""
    return """
/* === 배지 공통 스타일 === */
.urgency-badge, 
.team-badge, 
.category-badge, 
.date-badge, 
.status-badge,
.seller-badge,
.author-badge {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    padding: 4px 8px;
    border-radius: 8px;
    font-size: 0.75rem;
    font-weight: 600;
    white-space: nowrap;
    transition: all 0.2s ease;
}

/* === 긴급도 배지 === */
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

.urgency-icon {
    font-size: 0.8rem;
}

/* === 상태 배지 === */
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

.status-icon {
    font-size: 0.8rem;
}

/* === 팀 배지 === */
.team-badge {
    background: linear-gradient(135deg, #f3e8ff, #e9d5ff);
    color: #7c3aed;
    border: 1px solid #a78bfa;
}

/* === 카테고리 배지 === */
.category-badge {
    background: linear-gradient(135deg, #ecfdf5, #d1fae5);
    color: #059669;
    border: 1px solid #34d399;
}

/* === 날짜 배지 === */
.date-badge {
    background: linear-gradient(135deg, #f9fafb, #f3f4f6);
    color: #374151;
    border: 1px solid #d1d5db;
}

/* === 판매자 배지 === */
.seller-badge {
    background: linear-gradient(135deg, #e0f2fe, #bae6fd);
    color: #0369a1;
    border: 1px solid #38bdf8;
}

/* === 작성자 배지 === */
.author-badge {
    background: linear-gradient(135deg, #f0fdf4, #dcfce7);
    color: #15803d;
    border: 1px solid #4ade80;
    cursor: pointer;
    transition: all 0.2s ease;
}

.author-badge:hover {
    background: linear-gradient(135deg, #dcfce7, #bbf7d0);
    transform: translateY(-1px);
    box-shadow: 0 2px 4px rgba(21, 128, 61, 0.2);
}

/* === 배지 크기 변형 === */
.badge-small {
    padding: 2px 6px;
    font-size: 0.65rem;
    border-radius: 6px;
}

.badge-large {
    padding: 6px 12px;
    font-size: 0.8rem;
    border-radius: 10px;
}

/* === 배지 그룹 레이아웃 === */
.badge-group {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    align-items: center;
}

.badge-group .badge-priority {
    order: -1; /* 우선순위 배지는 앞으로 */
}

.badge-group .badge-status {
    order: 999; /* 상태 배지는 뒤로 */
}

/* === 배지 호버 효과 === */
.urgency-badge:hover,
.status-badge:hover,
.team-badge:hover,
.category-badge:hover {
    transform: translateY(-1px);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* === 배지 애니메이션 === */
@keyframes badgePulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.7; }
}

.urgency-badge.urgent {
    animation: badgePulse 2s infinite;
}

/* === 배지 상태별 특수 효과 === */
.status-badge.completed {
    position: relative;
}

.status-badge.completed::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(45deg, transparent 30%, rgba(255, 255, 255, 0.3) 50%, transparent 70%);
    animation: shimmer 2s infinite;
    border-radius: inherit;
}

@keyframes shimmer {
    0% { transform: translateX(-100%); }
    100% { transform: translateX(100%); }
}

/* === 접근성 개선 === */
.urgency-badge[title],
.status-badge[title],
.team-badge[title],
.category-badge[title] {
    cursor: help;
}

/* === 다크 모드 대응 === */
@media (prefers-color-scheme: dark) {
    .urgency-badge.urgent {
        background: linear-gradient(135deg, #7f1d1d, #991b1b);
        color: #fca5a5;
        border-color: #dc2626;
    }
    
    .urgency-badge.normal {
        background: linear-gradient(135deg, #1e3a8a, #1d4ed8);
        color: #93c5fd;
        border-color: #3b82f6;
    }
    
    .status-badge.completed {
        background: linear-gradient(135deg, #14532d, #166534);
        color: #86efac;
        border-color: #22c55e;
    }
    
    .status-badge.pending {
        background: linear-gradient(135deg, #92400e, #b45309);
        color: #fcd34d;
        border-color: #f59e0b;
    }
    
    .team-badge {
        background: linear-gradient(135deg, #581c87, #6b21a8);
        color: #c4b5fd;
        border-color: #8b5cf6;
    }
    
    .category-badge {
        background: linear-gradient(135deg, #14532d, #166534);
        color: #86efac;
        border-color: #22c55e;
    }
}

/* === 배지 반응형 === */
@media (max-width: 480px) {
    .urgency-badge, 
    .team-badge, 
    .category-badge, 
    .date-badge, 
    .status-badge,
    .seller-badge,
    .author-badge {
        font-size: 0.65rem;
        padding: 2px 5px;
        gap: 2px;
    }
    
    .urgency-icon,
    .status-icon {
        font-size: 0.7rem;
    }
}"""