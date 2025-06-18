# styles/components/inquiry_modal/content/states.py
"""
문의 모달 특수 상태 스타일 (로딩, 빈 상태, 오류 상태)
"""

def get_states_styles():
    """특수 상태 스타일"""
    return """
/* === 로딩 상태 === */
.inquiry-loading {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 200px;
    color: #6b7280;
    font-size: 0.9rem;
    gap: 12px;
}

.loading-spinner {
    width: 40px;
    height: 40px;
    border: 3px solid #e5e7eb;
    border-top: 3px solid #667eea;
    border-radius: 50%;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

/* 작은 로딩 스피너 */
.loading-spinner.small {
    width: 24px;
    height: 24px;
    border-width: 2px;
}

/* 로딩 상태 텍스트 */
.loading-text {
    font-weight: 500;
    text-align: center;
    color: #6b7280;
}

/* === 빈 상태 === */
.no-inquiries {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 300px;
    text-align: center;
    color: #6b7280;
    padding: 20px;
}

.no-inquiries-icon {
    font-size: 4rem;
    margin-bottom: 16px;
    opacity: 0.5;
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
}

.no-inquiries-text {
    font-size: 1.1rem;
    font-weight: 500;
    margin-bottom: 20px;
    color: #374151;
    line-height: 1.5;
}

.no-inquiries-subtitle {
    font-size: 0.9rem;
    color: #6b7280;
    margin-bottom: 24px;
    max-width: 400px;
}

/* 빈 상태 액션 버튼 */
.clear-filters-btn {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
}

.clear-filters-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
}

/* === 오류 상태 === */
.error-state {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 250px;
    text-align: center;
    color: #dc2626;
    padding: 20px;
}

.error-icon {
    font-size: 3rem;
    margin-bottom: 16px;
    color: #f87171;
}

.error-title {
    font-size: 1.2rem;
    font-weight: 600;
    margin-bottom: 8px;
    color: #dc2626;
}

.error-message {
    font-size: 0.9rem;
    color: #6b7280;
    margin-bottom: 20px;
    max-width: 400px;
    line-height: 1.5;
}

.retry-btn {
    background: #dc2626;
    color: white;
    border: none;
    border-radius: 6px;
    padding: 8px 16px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
}

.retry-btn:hover {
    background: #b91c1c;
    transform: translateY(-1px);
}

/* === 네트워크 오류 === */
.network-error {
    background: #fef2f2;
    border: 1px solid #fecaca;
    color: #b91c1c;
}

/* === 권한 오류 === */
.permission-error {
    background: #fefbf3;
    border: 1px solid #fed7aa;
    color: #c2410c;
}

/* === 스켈레톤 로딩 === */
.skeleton-card {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 16px;
}

.skeleton-line {
    height: 12px;
    background: linear-gradient(90deg, #f1f5f9 25%, #e2e8f0 50%, #f1f5f9 75%);
    background-size: 200% 100%;
    border-radius: 6px;
    margin-bottom: 8px;
    animation: shimmer 1.5s infinite;
}

.skeleton-line.short {
    width: 60%;
}

.skeleton-line.medium {
    width: 80%;
}

.skeleton-line.long {
    width: 100%;
}

@keyframes shimmer {
    0% { background-position: -200% 0; }
    100% { background-position: 200% 0; }
}

/* 스켈레톤 카드 여러 개 */
.skeleton-container {
    display: flex;
    flex-direction: column;
    gap: 16px;
}

/* === 연결 상태 표시 === */
.connection-status {
    position: fixed;
    top: 10px;
    right: 10px;
    padding: 8px 12px;
    border-radius: 6px;
    font-size: 0.8rem;
    font-weight: 600;
    z-index: 1000;
    transition: all 0.3s ease;
}

.connection-status.online {
    background: #dcfce7;
    color: #166534;
    border: 1px solid #bbf7d0;
}

.connection-status.offline {
    background: #fef2f2;
    color: #991b1b;
    border: 1px solid #fecaca;
}

/* === 진행률 표시 === */
.progress-indicator {
    width: 100%;
    height: 4px;
    background: #e5e7eb;
    border-radius: 2px;
    overflow: hidden;
    margin: 12px 0;
}

.progress-bar {
    height: 100%;
    background: linear-gradient(90deg, #667eea, #764ba2);
    border-radius: 2px;
    transition: width 0.3s ease;
    animation: indeterminate 2s infinite;
}

@keyframes indeterminate {
    0% { transform: translateX(-100%); }
    100% { transform: translateX(300%); }
}

/* === 상태 전환 애니메이션 === */
.state-transition {
    opacity: 0;
    transform: translateY(20px);
    transition: all 0.3s ease;
}

.state-transition.visible {
    opacity: 1;
    transform: translateY(0);
}

/* === 타임아웃 상태 === */
.timeout-state {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 200px;
    text-align: center;
    color: #f59e0b;
    padding: 20px;
}

.timeout-icon {
    font-size: 3rem;
    margin-bottom: 16px;
    opacity: 0.7;
}

.timeout-message {
    font-size: 1rem;
    font-weight: 500;
    margin-bottom: 16px;
    color: #92400e;
}

/* === 반응형 상태 스타일 === */
@media (max-width: 768px) {
    .no-inquiries {
        height: 250px;
        padding: 16px;
    }
    
    .no-inquiries-icon {
        font-size: 3rem;
        margin-bottom: 12px;
    }
    
    .no-inquiries-text {
        font-size: 1rem;
        margin-bottom: 16px;
    }
    
    .error-state {
        height: 200px;
        padding: 16px;
    }
    
    .error-icon {
        font-size: 2.5rem;
    }
    
    .error-title {
        font-size: 1.1rem;
    }
}

@media (max-width: 480px) {
    .inquiry-loading {
        height: 150px;
    }
    
    .loading-spinner {
        width: 32px;
        height: 32px;
        border-width: 2px;
    }
    
    .no-inquiries {
        height: 200px;
    }
    
    .no-inquiries-icon {
        font-size: 2.5rem;
        margin-bottom: 10px;
    }
    
    .no-inquiries-text {
        font-size: 0.9rem;
    }
    
    .clear-filters-btn {
        padding: 8px 16px;
        font-size: 0.9rem;
    }
}
"""