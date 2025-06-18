# styles/components/inquiry_modal/content/actions.py
"""
문의 카드 액션 버튼 및 인터랙션 요소 스타일
"""

def get_actions_styles():
    """액션 버튼 및 인터랙션 요소 스타일"""
    return """
/* === 액션 버튼 기본 스타일 === */
.action-btn {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 6px 12px;
    border-radius: 8px;
    font-size: 0.75rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    border: none;
    text-decoration: none;
    white-space: nowrap;
}

.action-btn:focus {
    outline: 2px solid currentColor;
    outline-offset: 2px;
}

/* === 주요 액션 버튼 === */
.action-btn.primary {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3);
}

.action-btn.primary:hover {
    background: linear-gradient(135deg, #5b67d8, #6b46c1);
    transform: translateY(-1px);
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
}

.action-btn.primary:active {
    transform: translateY(0);
    box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3);
}

/* === 보조 액션 버튼 === */
.action-btn.secondary {
    background: #f3f4f6;
    color: #374151;
    border: 1px solid #e5e7eb;
}

.action-btn.secondary:hover {
    background: #e5e7eb;
    color: #111827;
    transform: translateY(-1px);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

/* === 위험 액션 버튼 === */
.action-btn.danger {
    background: linear-gradient(135deg, #ef4444, #dc2626);
    color: white;
    box-shadow: 0 2px 8px rgba(239, 68, 68, 0.3);
}

.action-btn.danger:hover {
    background: linear-gradient(135deg, #dc2626, #b91c1c);
    transform: translateY(-1px);
    box-shadow: 0 4px 15px rgba(239, 68, 68, 0.4);
}

/* === 성공 액션 버튼 === */
.action-btn.success {
    background: linear-gradient(135deg, #10b981, #059669);
    color: white;
    box-shadow: 0 2px 8px rgba(16, 185, 129, 0.3);
}

.action-btn.success:hover {
    background: linear-gradient(135deg, #059669, #047857);
    transform: translateY(-1px);
    box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4);
}

/* === 버튼 크기 변형 === */
.action-btn.small {
    padding: 4px 8px;
    font-size: 0.7rem;
    gap: 4px;
}

.action-btn.large {
    padding: 8px 16px;
    font-size: 0.8rem;
    gap: 8px;
}

/* === 아이콘 전용 버튼 === */
.action-btn.icon-only {
    padding: 6px;
    min-width: 32px;
    justify-content: center;
}

.action-btn.icon-only svg {
    margin: 0;
}

/* === 버튼 비활성화 상태 === */
.action-btn:disabled {
    opacity: 0.5;
    cursor: not-allowed;
    transform: none !important;
    box-shadow: none !important;
}

.action-btn:disabled:hover {
    transform: none;
    box-shadow: none;
}

/* === 텍스트 링크 스타일 === */
.text-link {
    color: #667eea;
    text-decoration: none;
    font-weight: 500;
    transition: color 0.2s ease;
}

.text-link:hover {
    color: #5b67d8;
    text-decoration: underline;
}

/* === 토글 버튼 (확장/축소) === */
.toggle-btn {
    background: none;
    border: none;
    color: #6b7280;
    cursor: pointer;
    padding: 2px;
    border-radius: 4px;
    transition: all 0.2s ease;
    display: inline-flex;
    align-items: center;
    gap: 4px;
}

.toggle-btn:hover {
    color: #374151;
    background: #f3f4f6;
}

.toggle-btn:focus {
    outline: 2px solid #667eea;
    outline-offset: 1px;
}

/* === 드롭다운 트리거 === */
.dropdown-trigger {
    position: relative;
}

.dropdown-trigger::after {
    content: '';
    position: absolute;
    top: 50%;
    right: 8px;
    transform: translateY(-50%);
    width: 0;
    height: 0;
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-top: 4px solid currentColor;
    transition: transform 0.2s ease;
}

.dropdown-trigger[aria-expanded="true"]::after {
    transform: translateY(-50%) rotate(180deg);
}

/* === 액션 그룹 === */
.action-group {
    display: flex;
    gap: 8px;
    align-items: center;
}

.action-group .action-btn:not(:last-child) {
    border-top-right-radius: 0;
    border-bottom-right-radius: 0;
    border-right: 1px solid rgba(255, 255, 255, 0.2);
}

.action-group .action-btn:not(:first-child) {
    border-top-left-radius: 0;
    border-bottom-left-radius: 0;
    margin-left: -1px;
}

/* === 플로팅 액션 버튼 === */
.floating-action {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 56px;
    height: 56px;
    border-radius: 50%;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    border: none;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 20px rgba(102, 126, 234, 0.4);
    transition: all 0.3s ease;
    z-index: 1000;
}

.floating-action:hover {
    transform: scale(1.1);
    box-shadow: 0 6px 25px rgba(102, 126, 234, 0.5);
}

/* === 로딩 상태 버튼 === */
.action-btn.loading {
    pointer-events: none;
    opacity: 0.7;
}

.action-btn.loading::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 16px;
    height: 16px;
    margin: -8px 0 0 -8px;
    border: 2px solid transparent;
    border-top: 2px solid currentColor;
    border-radius: 50%;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

/* === 컨텍스트 메뉴 트리거 === */
.context-menu-trigger {
    background: none;
    border: none;
    color: #6b7280;
    cursor: pointer;
    padding: 4px;
    border-radius: 4px;
    transition: all 0.2s ease;
}

.context-menu-trigger:hover {
    color: #374151;
    background: #f3f4f6;
}

/* === 키보드 네비게이션 지원 === */
.action-btn:focus-visible {
    outline: 2px solid #667eea;
    outline-offset: 2px;
}

/* === 터치 디바이스 최적화 === */
@media (hover: none) and (pointer: coarse) {
    .action-btn {
        min-height: 44px; /* 터치 친화적 크기 */
        padding: 8px 16px;
    }
    
    .action-btn:hover {
        transform: none; /* 터치에서는 호버 효과 제거 */
    }
}"""