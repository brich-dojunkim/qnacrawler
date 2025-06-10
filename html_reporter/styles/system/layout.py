# html_reporter/styles/system/layout.py
"""레이아웃 시스템 - 그리드, 플렉스, 배치 규칙"""

def get_layout_styles():
    return """
/* === 그리드 시스템 === */
.grid {
    display: grid;
    gap: 24px;
}

.grid-2 { grid-template-columns: repeat(2, 1fr); }
.grid-3 { grid-template-columns: repeat(3, 1fr); }
.grid-4 { grid-template-columns: repeat(4, 1fr); }
.grid-5 { grid-template-columns: repeat(5, 1fr); }

/* === 팀별 탭 특별 레이아웃 === */
.teams-layout {
    display: flex;
    flex-wrap: wrap;
    gap: 24px;
}

.teams-layout .entity-card {
    /* 상위 3개(1~3) */
    flex: 1 1 calc(33.333% - 24px);
}

.teams-layout .entity-card:nth-child(n+4) {
    /* 하위 4개(4~7) */
    flex: 1 1 calc(25% - 24px);
}

/* === 심플 리스트 레이아웃 === */
.simple-list {
    margin: 16px 0;
}

.simple-list-title {
    font-size: 0.9rem;
    font-weight: 700;
    margin-bottom: 12px;
    color: #374151;
}

.simple-item {
    display: flex;
    align-items: center;
    margin-bottom: 6px;
    padding: 8px 12px;
    background: #f8fafc;
    border-radius: 8px;
    font-size: 0.85rem;
    transition: background 0.2s ease;
}

.simple-item:hover {
    background: #e0f2fe;
}

.simple-rank {
    min-width: 24px;
    font-weight: 700;
    color: #667eea;
}

.simple-name {
    flex: 1;
    margin-left: 8px;
    color: #374151;
    font-weight: 500;
}

.simple-value {
    min-width: 60px;
    text-align: right;
    font-weight: 700;
    color: #667eea;
}
"""