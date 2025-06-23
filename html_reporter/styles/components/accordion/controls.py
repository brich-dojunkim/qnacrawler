# html_reporter/styles/components/accordion/controls.py
"""
아코디언 컨트롤 바 및 토글 스타일 - 극한 여백 최소화 (거의 붙도록)
"""

def get_controls_bar_styles():
    """통합된 컨트롤 바 스타일 - 극한 여백 최소화"""
    return """
/* === 통합된 컨트롤 바 (상단 여백 제거) === */
.controls-bar {
    background: white;
    padding: 16px 30px;
    border-bottom: 1px solid #e2e8f0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 32px;  /* 20px -> 32px로 증가 */
}

/* 드로어 열릴 때 컨트롤 바 극한 여백 최소화 */
.detailed-analysis-section.drawer-open .controls-bar {
    padding-left: 5px;    /* 30px → 5px로 극한 감소 */
    padding-right: 2px;   /* 2px만 남김 */
    margin-right: 0;
    margin-left: 0;
    
    /* 컨트롤 바가 거의 끝까지 확장 */
    width: calc(100% + 58px);
    box-sizing: border-box;
}

.bulk-controls {
    display: flex;
    gap: 8px;
    align-items: center;
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

/* === 아코디언 정렬 버튼 스타일 === */
.accordion-sort-controls {
    display: flex;
    gap: 6px;
    align-items: center;
    margin-right: 12px;
    padding-right: 12px;
    border-right: 1px solid #e2e8f0;
}

.accordion-sort-btn {
    padding: 6px 10px;
    border: 1px solid #d1d5db;
    background: white;
    border-radius: 6px;
    cursor: pointer;
    font-size: 0.75rem;
    font-weight: 500;
    color: #6b7280;
    transition: all 0.2s ease;
    display: flex;
    align-items: center;
    gap: 4px;
    position: relative;
}

.accordion-sort-btn:hover {
    border-color: #9ca3af;
    color: #374151;
    background: #f9fafb;
}

.accordion-sort-btn.active {
    background: linear-gradient(135deg, #667eea, #764ba2);
    border-color: #667eea;
    color: white;
    box-shadow: 0 2px 4px rgba(102, 126, 234, 0.3);
}

.accordion-sort-btn.active:hover {
    background: linear-gradient(135deg, #5b67d8, #6b46c1);
    border-color: #5b67d8;
}

/* === 여정순서 버튼 특별 스타일 (오렌지/골드 테마) === */
.accordion-sort-btn.journey-only {
    background: linear-gradient(135deg, #f59e0b, #d97706);
    border-color: #f59e0b;
    color: white;
    box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);
    font-weight: 600;
    display: none; /* 초기에는 숨김 - JavaScript에서 여정별 뷰일 때만 표시 */
}

.accordion-sort-btn.journey-only:hover {
    background: linear-gradient(135deg, #d97706, #b45309);
    border-color: #d97706;
    box-shadow: 0 3px 6px rgba(245, 158, 11, 0.4);
    transform: translateY(-1px);
}

/* 여정순서 버튼은 활성화 상태가 별도로 없음 (항상 고정 스타일) */
.accordion-sort-btn.journey-only.active {
    background: linear-gradient(135deg, #f59e0b, #d97706);
    border-color: #f59e0b;
    color: white;
    box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);
}

.accordion-sort-btn.journey-only.active:hover {
    background: linear-gradient(135deg, #d97706, #b45309);
    border-color: #d97706;
}

/* 여정순서 버튼에서 화살표 아이콘 숨김 */
.accordion-sort-btn.journey-only .sort-direction {
    display: none;
}

/* === 정렬 방향 아이콘 === */
.sort-direction {
    font-size: 0.6rem;
    font-weight: 700;
    margin-left: 2px;
    transition: transform 0.2s ease;
}

.sort-direction.asc {
    transform: rotate(180deg);
}

.sort-direction.desc {
    transform: rotate(0deg);
}

/* === 테이블 컨트롤 버튼 - 아코디언과 동일한 간격 === */
.table-controls {
    display: none;
}

.table-controls.active {
    display: flex;
    gap: 8px; /* 아코디언 버튼과 동일한 간격 */
}

/* === 강제 적용하되 마진은 제거 === */
.controls-bar .bulk-controls .table-controls.active {
    display: flex !important;
    gap: 8px !important;
}

/* === 기존 마진 제거 (gap만 사용) === */
.controls-bar .bulk-controls .table-controls.active .bulk-control-btn {
    margin-right: 0 !important;
    margin-left: 0 !important;
}

.accordion-controls.hidden {
    display: none;
}

/* === 정렬 컨트롤과 벌크 컨트롤 구분 === */
.accordion-controls {
    display: flex;
    align-items: center;
    gap: 0;
}

.accordion-controls .accordion-sort-controls {
    margin-right: 12px;
}

.accordion-controls .bulk-actions {
    display: flex;
    gap: 8px;
}
"""

def get_view_toggle_styles():
    """뷰 토글 컨트롤 스타일"""
    return """
.view-toggle-group {
    display: flex;
    align-items: center;
    gap: 32px;
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

.view-toggle-controls .toggle-btn {
   padding: 6px 12px;
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

.view-toggle-controls .toggle-btn:hover:not(.view-toggle-controls input[type="radio"]:checked + .toggle-btn) {
   background: rgba(102, 126, 234, 0.1);
   color: #374151;
}
"""