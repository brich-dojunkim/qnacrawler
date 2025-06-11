# html_reporter/styles/components/accordion.py (개선된 디자인 적용)
"""팀별 아코디언 스타일 - 개선된 상세 분석 섹션"""

def get_accordion_styles():
    return """
/* === 개선된 상세 분석 섹션 === */
.detailed-analysis-section {
    background: linear-gradient(135deg, #f8fafc, #f1f5f9);
    border-top: 1px solid #e2e8f0;
    margin-top: 0;
}

.section-header {
    background: white;
    padding: 24px 30px;
    border-bottom: 1px solid #e2e8f0;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.section-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: #1e293b;
    display: flex;
    align-items: center;
    gap: 12px;
    margin: 0;
}

.section-title::before {
    content: '📊';
    font-size: 1.3rem;
}

/* === 통합된 컨트롤 바 === */
.controls-bar {
    background: white;
    padding: 16px 30px;
    border-bottom: 1px solid #e2e8f0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 20px;
}

.view-toggle-group {
    display: flex;
    align-items: center;
    gap: 12px;
}

.view-toggle-label {
    font-size: 0.9rem;
    font-weight: 600;
    color: #64748b;
}

.view-toggle-controls {
    display: flex;
    background: #f1f5f9;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid #e2e8f0;
}

.view-toggle-controls input[type="radio"] {
    display: none;
}

.toggle-btn {
    padding: 8px 16px;
    font-size: 0.9rem;
    font-weight: 600;
    color: #64748b;
    background: transparent;
    border: none;
    cursor: pointer;
    transition: all 0.3s ease;
    white-space: nowrap;
    text-align: center;
}

.view-toggle-controls input[type="radio"]:checked + .toggle-btn {
    color: white;
    background: linear-gradient(135deg, #667eea, #764ba2);
    box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3);
}

.toggle-btn:hover:not(.view-toggle-controls input[type="radio"]:checked + .toggle-btn) {
    background: rgba(102, 126, 234, 0.1);
    color: #374151;
}

.bulk-controls {
    display: flex;
    gap: 8px;
}

.bulk-control-btn {
    padding: 6px 12px;
    border: 1px solid #d1d5db;
    background: white;
    border-radius: 6px;
    cursor: pointer;
    font-size: 0.8rem;
    font-weight: 500;
    color: #374151;
    transition: all 0.2s ease;
}

.bulk-control-btn:hover {
    border-color: #667eea;
    color: #667eea;
    background: #f8fafc;
}

/* === 아코디언 컨텐츠 영역 === */
.accordion-content-area {
    background: #f8fafc;
    padding: 20px 30px 30px;
    min-height: 300px;
}

.analysis-view {
    transition: opacity 0.3s ease;
}

.analysis-view:not(.active) {
    display: none;
}

/* === 팀별/여정별 아코디언 컨테이너 === */
.teams-accordion-container,
.journey-accordion-container {
    display: flex;
    flex-direction: column;
    gap: 12px;
}

/* === 아코디언 아이템 (팀별/여정별 공통) === */
.team-accordion-item,
.journey-accordion-item {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    overflow: hidden;
    transition: all 0.3s ease;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}

.team-accordion-item:hover,
.journey-accordion-item:hover {
    border-color: #c7d2fe;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
}

/* === 아코디언 헤더 (팀별/여정별 공통) === */
.team-accordion-header,
.journey-accordion-header {
    display: flex;
    align-items: center;
    padding: 18px 20px;
    cursor: pointer;
    background: linear-gradient(135deg, #f8fafc, #f1f5f9);
    transition: background 0.3s ease;
}

.team-accordion-header:hover,
.journey-accordion-header:hover {
    background: linear-gradient(135deg, #e0f2fe, #e3f2fd);
}

.team-accordion-item.expanded .team-accordion-header,
.journey-accordion-item.expanded .journey-accordion-header {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
}

.team-summary-info,
.journey-summary-info {
    display: flex;
    align-items: center;
    gap: 12px;
    min-width: 200px;
}

.team-name,
.journey-name {
    font-size: 1.1rem;
    font-weight: 600;
    color: #374151;
}

.team-accordion-item.expanded .team-name,
.journey-accordion-item.expanded .journey-name {
    color: white;
}

.team-count,
.journey-count {
    font-size: 0.9rem;
    color: #64748b;
    font-weight: 500;
}

.team-accordion-item.expanded .team-count,
.journey-accordion-item.expanded .journey-count {
    color: rgba(255, 255, 255, 0.9);
}

/* === 프로그레스 컨테이너 (팀별/여정별 공통) === */
.team-progress-container,
.journey-progress-container {
    flex: 1;
    display: flex;
    align-items: center;
    gap: 16px;
    margin: 0 20px;
}

.team-progress-bar,
.journey-progress-bar {
    flex: 1;
    height: 8px;
    background: #e2e8f0;
    border-radius: 4px;
    overflow: hidden;
}

.team-accordion-item.expanded .team-progress-bar,
.journey-accordion-item.expanded .journey-progress-bar {
    background: rgba(255, 255, 255, 0.3);
}

.team-progress-fill,
.journey-progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #667eea, #764ba2);
    border-radius: 4px;
    transition: width 0.5s ease;
}

.team-accordion-item.expanded .team-progress-fill,
.journey-accordion-item.expanded .journey-progress-fill {
    background: linear-gradient(90deg, #ffffff, #f1f5f9);
}

.team-percentage,
.journey-percentage {
    font-size: 0.95rem;
    font-weight: 600;
    color: #667eea;
    min-width: 60px;
    text-align: right;
}

.team-accordion-item.expanded .team-percentage,
.journey-accordion-item.expanded .journey-percentage {
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

.team-accordion-item.expanded .accordion-toggle-btn:hover,
.journey-accordion-item.expanded .accordion-toggle-btn:hover {
    background: rgba(255, 255, 255, 0.2);
}

.toggle-icon {
    font-size: 0.8rem;
    color: #64748b;
    transition: transform 0.3s ease;
}

.team-accordion-item.expanded .toggle-icon,
.journey-accordion-item.expanded .toggle-icon {
    color: white;
    transform: rotate(180deg);
}

/* === 아코디언 콘텐츠 (팀별/여정별 공통) === */
.team-accordion-content,
.journey-accordion-content {
    border-top: 1px solid #e2e8f0;
    background: white;
}

.team-detail-box,
.journey-detail-box {
    padding: 24px;
}

.team-metrics-grid,
.journey-metrics-grid {
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
    .section-header,
    .controls-bar,
    .accordion-content-area {
        padding-left: 20px;
        padding-right: 20px;
    }
    
    .controls-bar {
        flex-direction: column;
        gap: 12px;
        align-items: stretch;
    }
    
    .view-toggle-group {
        justify-content: center;
    }
    
    .bulk-controls {
        justify-content: center;
    }
    
    .team-accordion-header,
    .journey-accordion-header {
        flex-direction: column;
        gap: 12px;
        padding: 16px 20px;
    }
    
    .team-summary-info,
    .journey-summary-info {
        align-self: stretch;
        justify-content: space-between;
        min-width: auto;
    }
    
    .team-progress-container,
    .journey-progress-container {
        align-self: stretch;
        margin: 0;
    }
    
    .team-metrics-grid,
    .journey-metrics-grid {
        grid-template-columns: 1fr;
        gap: 12px;
    }
    
    .team-detail-box,
    .journey-detail-box {
        padding: 16px;
    }
}

@media (max-width: 480px) {
    .section-header {
        padding: 16px 20px;
    }
    
    .section-title {
        font-size: 1.3rem;
    }
    
    .controls-bar {
        padding: 12px 20px;
    }
    
    .view-toggle-label {
        font-size: 0.85rem;
    }
    
    .toggle-btn {
        padding: 6px 12px;
        font-size: 0.85rem;
    }
    
    .bulk-control-btn {
        padding: 5px 10px;
        font-size: 0.75rem;
    }
    
    .team-accordion-header,
    .journey-accordion-header {
        padding: 12px 16px;
    }
    
    .team-name,
    .journey-name {
        font-size: 1rem;
    }
    
    .team-count,
    .journey-count {
        font-size: 0.85rem;
    }
}
"""