# html_reporter/styles/components/accordion/base.py
"""
기본 아코디언 구조 및 레이아웃 스타일 - 드로어 연동 패딩 조정
"""

def get_accordion_base_layout():
    """상세 분석 섹션 기본 레이아웃 - 드로어 패딩 조정"""
    return """
/* === 타이트한 상세 분석 섹션 === */
.detailed-analysis-section {
    background: white;
    margin-top: 0;
}

/* === 아코디언 콘텐츠 영역 (드로어 연동 패딩) === */
.accordion-content-area {
    background: white;
    padding: 20px 30px 30px;
    min-height: 300px;
}

/* 드로어가 열렸을 때 우측 패딩 완전 제거 */
.detailed-analysis-section.drawer-open .accordion-content-area {
    padding-right: 0;
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
"""

def get_accordion_item_structure():
    """아코디언 아이템 기본 구조 (팀별/여정별 공통)"""
    return """
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
"""