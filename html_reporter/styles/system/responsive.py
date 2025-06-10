# html_reporter/styles/system/responsive.py
"""반응형 시스템 - 미디어 쿼리 기반 반응형 처리"""

def get_responsive_styles():
    return """
/* === 반응형 디자인 === */

/* 1200px 이하 - 태블릿 */
@media (max-width: 1200px) {
    .main-stats-grid {
        grid-template-columns: 1fr 1fr;
        gap: 16px;
    }
    
    .stat-card-large {
        grid-column: 1 / -1;
        padding: 24px;
    }
    
    .stat-number-large {
        font-size: 2.5rem;
    }
    
    .distribution-grid {
        grid-template-columns: 1fr;
        gap: 20px;
    }
    
    .teams-layout .entity-card,
    .teams-layout .entity-card:nth-child(n+4) {
        flex: 1 1 calc(50% - 24px);
    }
}

/* 768px 이하 - 모바일 */
@media (max-width: 768px) {
    body {
        padding: 10px;
    }
    
    .container {
        border-radius: 16px;
    }
    
    .header {
        padding: 30px 20px;
    }
    
    .header h1 {
        font-size: 2rem;
    }
    
    .main-content {
        padding: 20px;
    }
    
    .tab-content {
        padding: 20px;
    }
    
    .main-stats-grid {
        grid-template-columns: 1fr;
        gap: 12px;
    }
    
    .stat-card-large {
        flex-direction: column;
        text-align: center;
        padding: 20px;
    }
    
    .stat-number-large {
        font-size: 2rem;
    }
    
    .stat-number-medium {
        font-size: 1.5rem;
    }
    
    .simple-rank-item {
        flex-direction: column;
        gap: 12px;
        text-align: center;
        padding: 20px;
    }
    
    .simple-rank-number {
        margin-right: 0;
        margin-bottom: 8px;
    }
    
    .simple-rank-content {
        flex-direction: column;
        gap: 8px;
        width: 100%;
    }
    
    .grid-2, .grid-3, .grid-4, .grid-5 { 
        grid-template-columns: 1fr; 
    }
    
    .teams-layout .entity-card {
        flex: 1 1 100%;
    }
    
    .filter-buttons {
        flex-wrap: wrap;
        justify-content: center;
        gap: 8px;
    }
    
    .filter-btn {
        padding: 8px 16px;
        font-size: 0.85rem;
    }
    
    .tab-nav {
        justify-content: space-between;
    }
    
    .tab-btn {
        flex: 1;
        padding: 14px 12px;
        font-size: 0.9rem;
    }
    
    .modal-content {
        width: 95%;
        margin: 20px;
        border-radius: 16px;
    }
    
    .modal-header {
        padding: 20px;
    }
    
    .modal-body {
        padding: 20px;
    }
    
    .modal-title {
        font-size: 1.3rem;
    }
    
    .entity-card {
        padding: 16px;
    }
    
    .metrics-list li {
        padding: 10px 12px;
    }
    
    /* === 헤더 배지 그룹 반응형 === */
    .header-badges {
        align-items: center;
        min-width: auto;
    }
    
    .entity-card-header {
        flex-direction: column;
        align-items: stretch;
        text-align: center;
        gap: 12px;
    }
    
    .entity-card-title {
        padding-right: 0;
    }
    
    .header-badges .team-badges {
        justify-content: center;
    }
}

/* 480px 이하 - 작은 모바일 */
@media (max-width: 480px) {
    .header h1 {
        font-size: 1.8rem;
    }
    
    .entity-card-title {
        font-size: 1.1rem;
    }
    
    .stat-number-large {
        font-size: 1.8rem;
    }
}
"""