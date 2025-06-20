# html_reporter/styles/components/inquiry_modal/layout.py
"""
문의 상세보기 모달 레이아웃 스타일 - 스크롤 및 여백 문제 해결
"""

def get_layout_styles():
    """모달 레이아웃 및 오버레이 스타일 - 스크롤 및 여백 문제 수정"""
    return """
/* === 문의 상세보기 모달 레이아웃 === */
.inquiry-modal-overlay {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.7);
    backdrop-filter: blur(8px);
    z-index: 10000;
    justify-content: center;
    align-items: center;
    padding: 20px;
    box-sizing: border-box;
}

.inquiry-modal-overlay.active {
    display: flex;
}

.inquiry-modal-content {
    background: white;
    border-radius: 20px;
    width: 100%;
    max-width: 1200px;
    height: 90vh;
    max-height: 900px;
    display: flex;
    flex-direction: column;
    box-shadow: 0 25px 80px rgba(0, 0, 0, 0.3);
    overflow: hidden;
    position: relative;
}

/* === 모달 본문 영역 === */
.inquiry-modal-body {
    flex: 1;
    overflow: hidden;
    background: #f8fafc;
    position: relative;
    /* 🔧 최소 높이 설정 */
    min-height: 400px;
}

/* 🚨 핵심 수정: 스크롤 컨테이너 */
.inquiry-list-container {
    height: 100%;
    /* 🔧 스크롤 설정 - 올바른 스크롤 영역 */
    overflow-y: auto;
    overflow-x: hidden;
    padding: 20px;  /* 🔧 좌우 여백 복원 */
    /* 스크롤 성능 개선 */
    -webkit-overflow-scrolling: touch;
    scroll-behavior: smooth;
    /* 🔧 박스 사이징 추가 */
    box-sizing: border-box;
}

/* 🚨 핵심 수정: inquiry-list 스타일 */
.inquiry-list {
    display: flex;
    flex-direction: column;
    gap: 16px;
    padding: 0;
    margin: 0;
    /* 🔧 높이 제한 완전 제거 */
    min-height: auto;
    max-height: none;
    height: auto;
    /* 🔧 하단 패딩 추가로 마지막 카드까지 스크롤 보장 */
    padding-bottom: 40px;
}

/* 🔧 문의 카드 여백 보정 */
.inquiry-card {
    margin: 0;  /* 기본 마진 제거 */
    /* flex gap으로 간격 제어됨 */
}

/* === 로딩 및 빈 상태 === */
.inquiry-loading {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 200px;
    color: #6b7280;
    font-size: 0.9rem;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 80%;
}

.loading-spinner {
    width: 40px;
    height: 40px;
    border: 3px solid #e5e7eb;
    border-top: 3px solid #667eea;
    border-radius: 50%;
    animation: spin 1s linear infinite;
    margin-bottom: 12px;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

.no-inquiries {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 300px;
    text-align: center;
    color: #6b7280;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 80%;
}

.no-inquiries-icon {
    font-size: 4rem;
    margin-bottom: 16px;
    opacity: 0.5;
}

.no-inquiries-text {
    font-size: 1.1rem;
    font-weight: 500;
    margin-bottom: 20px;
    color: #374151;
}

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

/* === 스크롤바 스타일 === */
.inquiry-list-container::-webkit-scrollbar {
    width: 8px;
}

.inquiry-list-container::-webkit-scrollbar-track {
    background: #f1f5f9;
    border-radius: 4px;
}

.inquiry-list-container::-webkit-scrollbar-thumb {
    background: linear-gradient(135deg, #667eea, #764ba2);
    border-radius: 4px;
}

.inquiry-list-container::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(135deg, #5a67d8, #6b46c1);
}

/* === 🔧 디버깅용 시각적 확인 (개발 완료 후 제거) === */
/*
.inquiry-modal-body {
    border: 3px solid red;
}

.inquiry-list-container {
    border: 2px solid blue;
}

.inquiry-list {
    border: 1px solid green;
}

.inquiry-card {
    border: 1px dotted orange;
}
*/

/* === 반응형 - 태블릿 === */
@media (max-width: 768px) {
    .inquiry-modal-overlay {
        padding: 10px;
    }
    
    .inquiry-modal-content {
        width: 100%;
        height: 95vh;
        border-radius: 16px;
    }
    
    .inquiry-list-container {
        padding: 16px;  /* 모바일에서도 여백 유지 */
    }
    
    .inquiry-list {
        gap: 12px;
        padding-bottom: 30px;  /* 모바일에서는 조금 줄임 */
    }
    
    .no-inquiries {
        height: 250px;
    }
    
    .no-inquiries-icon {
        font-size: 3rem;
    }
    
    .no-inquiries-text {
        font-size: 1rem;
    }
}

/* === 반응형 - 모바일 === */
@media (max-width: 480px) {
    .inquiry-modal-overlay {
        padding: 5px;
    }
    
    .inquiry-modal-content {
        height: 98vh;
        border-radius: 12px;
    }
    
    .inquiry-list-container {
        padding: 12px;  /* 모바일에서도 최소 여백 유지 */
    }
    
    .inquiry-list {
        gap: 10px;
        padding-bottom: 25px;
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
        margin-bottom: 12px;
    }
    
    .no-inquiries-text {
        font-size: 0.9rem;
        margin-bottom: 16px;
    }
    
    .clear-filters-btn {
        padding: 8px 16px;
        font-size: 0.9rem;
    }
}
"""