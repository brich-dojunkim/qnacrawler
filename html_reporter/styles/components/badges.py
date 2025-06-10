# html_reporter/styles/components/badges.py
"""배지 스타일"""

def get_badge_styles():
    return """
/* === 유저 여정 배지 === */
.journey-badge {
    background: linear-gradient(135deg, #10b981, #059669);
    color: white;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
    box-shadow: 0 2px 8px rgba(16, 185, 129, 0.3);
}

/* === 팀 배지 === */
.team-badges {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin: 12px 0;
}

.team-badge {
    background: linear-gradient(135deg, #f59e0b, #d97706);
    color: white;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
    box-shadow: 0 2px 8px rgba(245, 158, 11, 0.3);
}

/* === 긴급도 배지 === */
.urgency-badge {
    padding: 4px 10px;
    border-radius: 12px;
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.urgency-urgent {
    background: linear-gradient(135deg, #fee2e2, #fecaca);
    color: #dc2626;
    border: 1px solid #fca5a5;
}

.urgency-normal {
    background: linear-gradient(135deg, #e0f2fe, #bae6fd);
    color: #0369a1;
    border: 1px solid #7dd3fc;
}

/* === 메타 인라인 레이아웃 === */
.meta-inline {
    display: flex;
    align-items: center;
    gap: 12px;
    flex-wrap: wrap;
    margin: 16px 0;
}

.meta-inline .team-badges {
    margin: 0;
}

.meta-inline .journey-badge {
    margin: 0;
}

.metrics-list + .meta-inline {
    margin-top: 8px;
}
"""