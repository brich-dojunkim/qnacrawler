# html_reporter/styles/components/accordion/headers.py
"""
아코디언 헤더 및 정보 표시 스타일
"""

def get_accordion_header_styles():
    """아코디언 헤더 기본 스타일 (팀별/여정별 공통)"""
    return """
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
"""

def get_summary_info_styles():
    """요약 정보 (팀명, 여정명, 카운트) 스타일"""
    return """
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
"""

def get_progress_bar_styles():
    """프로그레스 바 스타일 (팀별/여정별 공통)"""
    return """
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
"""

def get_toggle_button_styles():
    """토글 버튼 스타일"""
    return """
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
"""