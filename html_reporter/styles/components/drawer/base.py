# html_reporter/styles/components/drawer/base.py
"""
드로어 기본 구조 및 레이아웃 스타일
"""

def get_drawer_base_styles():
    """드로어 기본 구조 스타일"""
    return """
/* === 메인 콘텐츠 래퍼 === */
.main-content-wrapper {
    position: relative;
    display: flex;
    min-height: 100vh;
}

.detailed-analysis-section {
    flex: 1;
    transition: margin-right 0.3s ease;
}

.detailed-analysis-section.drawer-open {
    margin-right: 400px;
}

/* === 사이드 드로어 === */
.inquiry-drawer {
    position: fixed;
    top: 0;
    right: 0;
    width: 400px;
    height: 100vh;
    z-index: 1000;
    pointer-events: none;
}

.inquiry-drawer.open {
    pointer-events: all;
}

/* === 드로어 오버레이 === */
.drawer-overlay {
    position: absolute;
    top: 0;
    left: -100vw;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.3);
    opacity: 0;
    transition: opacity 0.3s ease;
    pointer-events: none;
}

.inquiry-drawer.open .drawer-overlay {
    opacity: 1;
    pointer-events: all;
}

/* === 숨김 클래스 === */
.hidden {
    display: none !important;
}
"""

def get_drawer_panel_styles():
    """드로어 패널 스타일"""
    return """
/* === 드로어 패널 === */
.drawer-panel {
    position: absolute;
    top: 0;
    right: 0;
    width: 400px;
    height: 100vh;
    background: white;
    box-shadow: -4px 0 20px rgba(0, 0, 0, 0.15);
    transform: translateX(100%);
    transition: transform 0.3s ease;
    display: flex;
    flex-direction: column;
}

.inquiry-drawer.open .drawer-panel {
    transform: translateX(0);
}

/* === 바디 상태 === */
body.drawer-open {
    overflow: hidden;
}
"""