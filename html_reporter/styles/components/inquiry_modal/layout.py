# html_reporter/styles/components/inquiry_modal/layout.py
"""
문의 상세보기 모달 레이아웃 스타일
"""

def get_layout_styles():
    """모달 레이아웃 및 오버레이 스타일"""
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
}

.inquiry-list-container {
    height: 100%;
    overflow-y: auto;
    padding: 16px 20px;
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
        padding: 12px 16px;
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
        padding: 8px 12px;
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