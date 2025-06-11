# html_reporter/styles/components/accordion.py
"""팀별 아코디언 스타일"""

def get_accordion_styles():
    return """
/* === 팀별 아코디언 섹션 === */
.teams-accordion-section {
    margin-top: 40px;
}

.teams-accordion-container {
    display: flex;
    flex-direction: column;
    gap: 12px;
}

/* === 아코디언 아이템 === */
.team-accordion-item {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    overflow: hidden;
    transition: all 0.3s ease;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.team-accordion-item:hover {
    border-color: #c7d2fe;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

/* === 아코디언 헤더 === */
.team-accordion-header {
    display: flex;
    align-items: center;
    padding: 20px 24px;
    cursor: pointer;
    background: linear-gradient(135deg, #f8fafc, #f1f5f9);
    transition: background 0.3s ease;
}

.team-accordion-header:hover {
    background: linear-gradient(135deg, #e0f2fe, #e3f2fd);
}

.team-accordion-item.expanded .team-accordion-header {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
}

.team-summary-info {
    display: flex;
    align-items: center;
    gap: 12px;
    min-width: 200px;
}

.team-name {
    font-size: 1.1rem;
    font-weight: 600;
    color: #374151;
}

.team-accordion-item.expanded .team-name {
    color: white;
}

.team-count {
    font-size: 0.9rem;
    color: #64748b;
    font-weight: 500;
}

.team-accordion-item.expanded .team-count {
    color: rgba(255, 255, 255, 0.9);
}

/* === 프로그레스 컨테이너 === */
.team-progress-container {
    flex: 1;
    display: flex;
    align-items: center;
    gap: 16px;
    margin: 0 20px;
}

.team-progress-bar {
    flex: 1;
    height: 8px;
    background: #e2e8f0;
    border-radius: 4px;
    overflow: hidden;
}

.team-accordion-item.expanded .team-progress-bar {
    background: rgba(255, 255, 255, 0.3);
}

.team-progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #667eea, #764ba2);
    border-radius: 4px;
    transition: width 0.5s ease;
}

.team-accordion-item.expanded .team-progress-fill {
    background: linear-gradient(90deg, #ffffff, #f1f5f9);
}

.team-percentage {
    font-size: 0.95rem;
    font-weight: 600;
    color: #667eea;
    min-width: 60px;
    text-align: right;
}

.team-accordion-item.expanded .team-percentage {
    color: white;
}

/* === 토글 버튼 === */
.accordion-toggle-btn {
    background: none;
    border: none;
    padding: 8px;
    cursor: pointer;
    border-radius: 50%;
    width: 36px;
    height: 36px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s ease;
}

.accordion-toggle-btn:hover {
    background: rgba(102, 126, 234, 0.1);
}

.team-accordion-item.expanded .accordion-toggle-btn:hover {
    background: rgba(255, 255, 255, 0.2);
}

.toggle-icon {
    font-size: 0.8rem;
    color: #64748b;
    transition: transform 0.3s ease;
}

.team-accordion-item.expanded .toggle-icon {
    color: white;
    transform: rotate(180deg);
}

/* === 아코디언 콘텐츠 === */
.team-accordion-content {
    border-top: 1px solid #e2e8f0;
    background: white;
}

.team-detail-box {
    padding: 24px;
}

.team-metrics-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 16px;
    margin-bottom: 24px;
}

.metric-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 16px;
    background: linear-gradient(135deg, #f8fafc, #f1f5f9);
    border-radius: 8px;
    border: 1px solid #e2e8f0;
}

.metric-label {
    font-size: 0.9rem;
    color: #64748b;
    font-weight: 500;
}

.metric-value {
    font-size: 1rem;
    font-weight: 600;
    color: #667eea;
}

/* === 반응형 === */
@media (max-width: 768px) {
    .team-accordion-header {
        flex-direction: column;
        gap: 12px;
        padding: 16px 20px;
    }
    
    .team-summary-info {
        align-self: stretch;
        justify-content: space-between;
        min-width: auto;
    }
    
    .team-progress-container {
        align-self: stretch;
        margin: 0;
    }
    
    .team-metrics-grid {
        grid-template-columns: 1fr;
        gap: 12px;
    }
    
    .team-detail-box {
        padding: 16px;
    }
}

@media (max-width: 480px) {
    .team-accordion-header {
        padding: 12px 16px;
    }
    
    .team-name {
        font-size: 1rem;
    }
    
    .team-count {
        font-size: 0.85rem;
    }
}
"""