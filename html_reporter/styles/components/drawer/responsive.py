# html_reporter/styles/components/drawer/responsive.py
"""
드로어 반응형 스타일 - 확장된 너비 대응
"""

def get_drawer_responsive_styles():
    """드로어 반응형 스타일 - 확장된 너비 대응"""
    return """
/* === 태블릿 반응형 (768px 이하) === */
@media (max-width: 768px) {
    .inquiry-drawer {
        width: 100vw;
        left: 0;
        right: auto;
    }
    
    .drawer-panel {
        width: 100vw;
        transform: translateX(100vw);
    }
    
    .inquiry-drawer.open .drawer-panel {
        transform: translateX(0);
    }
    
    .detailed-analysis-section.drawer-open {
        margin-right: 0;
    }
    
    .drawer-overlay {
        left: 0;
        width: 100vw;
    }
    
    .drawer-header {
        padding: 16px 20px;  /* 모바일에서는 기본 패딩 유지 */
    }
    
    .drawer-title-section {
        margin-bottom: 12px;
    }
    
    .drawer-category-name {
        font-size: 1.1rem;
    }
    
    .drawer-controls {
        flex-wrap: wrap;
        gap: 6px;
    }
    
    .drawer-select {
        font-size: 0.75rem;
        padding: 5px 8px;
    }
    
    .drawer-search {
        padding: 12px 20px;  /* 모바일에서는 기본 패딩 유지 */
    }
    
    .drawer-search-input {
        font-size: 0.85rem;
    }
    
    .inquiry-item {
        padding: 12px 20px;  /* 모바일에서는 기본 패딩 유지 */
    }
    
    .inquiry-item-header {
        flex-direction: column;
        gap: 8px;
        align-items: flex-start;
    }
    
    .inquiry-meta {
        align-items: flex-start;
        flex-direction: row;
        gap: 8px;
    }
    
    .inquiry-detail-content {
        padding: 16px 20px;  /* 모바일에서는 기본 패딩 유지 */
    }
    
    .inquiry-header-info {
        padding: 12px;
    }
    
    .inquiry-meta-row {
        flex-direction: column;
        gap: 8px;
    }
    
    .answer-item {
        padding: 12px;
    }
    
    .answer-header {
        flex-direction: column;
        align-items: flex-start;
        gap: 4px;
    }
    
    .detail-header {
        padding: 12px 20px;  /* 모바일에서는 기본 패딩 유지 */
    }
}

/* === 모바일 반응형 (480px 이하) === */
@media (max-width: 480px) {
    .drawer-header {
        padding: 12px 16px;
    }
    
    .drawer-category-name {
        font-size: 1rem;
    }
    
    .drawer-inquiry-count {
        font-size: 0.75rem;
        padding: 3px 8px;
    }
    
    .drawer-controls {
        width: 100%;
        justify-content: space-between;
    }
    
    .drawer-select {
        flex: 1;
        min-width: 0;
        margin-right: 8px;
    }
    
    .drawer-search {
        padding: 10px 16px;
    }
    
    .drawer-search-input {
        font-size: 0.8rem;
        padding: 6px 30px 6px 30px;
    }
    
    .search-icon {
        left: 8px;
    }
    
    .search-clear-btn {
        right: 6px;
        font-size: 0.8rem;
    }
    
    .inquiry-item {
        padding: 10px 16px;
    }
    
    .inquiry-id {
        font-size: 0.8rem;
    }
    
    .inquiry-badges {
        flex-wrap: wrap;
    }
    
    .urgent-badge,
    .status-badge {
        font-size: 0.65rem;
        padding: 1px 4px;
    }
    
    .inquiry-preview-text {
        font-size: 0.8rem;
        -webkit-line-clamp: 3;
    }
    
    .inquiry-item-footer {
        flex-direction: column;
        gap: 8px;
        align-items: flex-start;
    }
    
    .view-detail-btn {
        font-size: 0.7rem;
        padding: 4px 8px;
        align-self: flex-end;
    }
    
    .detail-header {
        padding: 12px 16px;
        flex-direction: column;
        gap: 8px;
        align-items: flex-start;
    }
    
    .back-btn {
        font-size: 0.8rem;
        padding: 4px 6px;
    }
    
    .detail-inquiry-info {
        align-self: flex-end;
    }
    
    .detail-inquiry-id {
        font-size: 0.9rem;
    }
    
    .inquiry-detail-content {
        padding: 12px 16px;
        height: calc(100% - 80px);
    }
    
    .inquiry-detail-full {
        gap: 16px;
    }
    
    .inquiry-title {
        font-size: 1rem;
    }
    
    .section-title {
        font-size: 0.9rem;
    }
    
    .inquiry-text {
        font-size: 0.8rem;
    }
    
    .answer-text {
        font-size: 0.75rem;
        padding: 8px;
    }
    
    .meta-item {
        font-size: 0.75rem;
    }
    
    .contact-item {
        font-size: 0.75rem;
    }
}

/* === 매우 작은 화면 (320px 이하) === */
@media (max-width: 320px) {
    .drawer-title-section {
        flex-direction: column;
        gap: 8px;
        align-items: flex-start;
    }
    
    .drawer-controls {
        flex-direction: column;
        width: 100%;
        gap: 8px;
    }
    
    .drawer-select {
        width: 100%;
        margin-right: 0;
    }
    
    .drawer-close-btn {
        align-self: flex-end;
        margin-left: 0;
    }
    
    .inquiry-item-header {
        gap: 6px;
    }
    
    .inquiry-badges {
        gap: 2px;
    }
    
    .inquiry-item-footer {
        gap: 6px;
    }
    
    .order-info {
        font-size: 0.7rem;
        word-break: break-all;
    }
}

/* === 가로 모드 대응 (높이 480px 이하) === */
@media (max-height: 480px) and (orientation: landscape) {
    .drawer-header {
        padding: 8px 30px;  /* 확장된 너비에서도 패딩 유지 */
    }
    
    .drawer-title-section {
        margin-bottom: 8px;
    }
    
    .drawer-search {
        padding: 8px 30px;  /* 확장된 너비에서도 패딩 유지 */
    }
    
    .inquiry-item {
        padding: 8px 30px;  /* 확장된 너비에서도 패딩 유지 */
    }
    
    .inquiry-detail-content {
        padding: 12px 30px;  /* 확장된 너비에서도 패딩 유지 */
    }
    
    .inquiry-detail-full {
        gap: 12px;
    }
    
    .inquiry-header-info {
        padding: 10px;
    }
    
    .answer-item {
        padding: 10px;
    }
    
    .detail-header {
        padding: 8px 30px;  /* 확장된 너비에서도 패딩 유지 */
    }
}

/* === 데스크톱 큰 화면 (1400px 이상) === */
@media (min-width: 1400px) {
    /* 큰 화면에서는 드로어를 더 넓게 확장할 수 있음 */
    .inquiry-drawer {
        width: 480px;  /* 460px → 480px로 추가 확장 */
    }
    
    .drawer-panel {
        width: 480px;  /* 460px → 480px로 추가 확장 */
    }
    
    .detailed-analysis-section.drawer-open {
        margin-right: 480px;  /* 460px → 480px로 추가 확장 */
    }
    
    /* 큰 화면에서는 패딩도 더 넉넉하게 */
    .drawer-header,
    .drawer-search {
        padding-left: 40px;
        padding-right: 40px;
    }
    
    .inquiry-item {
        padding-left: 40px;
        padding-right: 40px;
    }
    
    .inquiry-detail-content {
        padding-left: 40px;
        padding-right: 40px;
    }
    
    .detail-header {
        padding-left: 40px;
        padding-right: 40px;
    }
}
"""