# html_reporter/styles/components/accordion/base.py
"""
기본 아코디언 구조 및 레이아웃 스타일 - 극한 여백 최소화 (거의 붙도록)
"""

def get_accordion_base_layout():
    """상세 분석 섹션 기본 레이아웃 - 극한 여백 최소화"""
    return """
/* === 타이트한 상세 분석 섹션 === */
.detailed-analysis-section {
    background: white;
    margin-top: 0;
}

/* === 아코디언 콘텐츠 영역 (극한 여백 최소화) === */
.accordion-content-area {
    background: white;
    padding: 20px 30px 30px;
    min-height: 300px;
}

/* 드로어가 열렸을 때 극한 여백 최소화 + 콘텐츠 최대 확장 */
.detailed-analysis-section.drawer-open .accordion-content-area {
    padding-left: 5px;    /* 30px → 5px로 극한 감소 */
    padding-right: 0;     /* 우측 패딩 완전 제거 */
    margin-right: 0;      /* 우측 마진 완전 제거 */
    margin-left: 0;       /* 좌측 마진도 제거 */
    
    /* 콘텐츠가 거의 끝까지 확장 */
    width: calc(100% + 55px);  /* 최대한 확장 */
    box-sizing: border-box;
}

.analysis-view {
    transition: opacity 0.3s ease;
}

.analysis-view:not(.active) {
    display: none;
}

/* 드로어 열릴 때 분석 뷰도 최대 확장 */
.detailed-analysis-section.drawer-open .analysis-view {
    margin-right: 0;
    padding-right: 0;
    margin-left: 0;
    width: calc(100% + 15px);
}

/* === 팀별/여정별 아코디언 컨테이너 === */
.teams-accordion-container,
.journey-accordion-container {
    display: flex;
    flex-direction: column;
    gap: 12px;
}

/* 드로어 열릴 때 아코디언 컨테이너도 최대 확장 */
.detailed-analysis-section.drawer-open .teams-accordion-container,
.detailed-analysis-section.drawer-open .journey-accordion-container {
    margin-right: 0;
    padding-right: 0;
    margin-left: 0;
    width: calc(100% + 15px);
}
"""

def get_accordion_item_structure():
    """아코디언 아이템 기본 구조 (팀별/여정별 공통) - 최대 확장"""
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

/* 드로어 열릴 때 아코디언 아이템들도 최대 확장 */
.detailed-analysis-section.drawer-open .team-accordion-item,
.detailed-analysis-section.drawer-open .journey-accordion-item {
    margin-right: 0;
    margin-left: 0;
    width: calc(100% + 15px);
    max-width: none;
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

/* 드로어 열릴 때 세부카테고리 테이블도 최대 확장 */
.detailed-analysis-section.drawer-open .sub-categories-table {
    margin-right: 0;
    margin-left: 0;
    width: calc(100% + 15px);
}
"""