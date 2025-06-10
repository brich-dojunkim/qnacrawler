# html_reporter/styles/components/modals.py
"""모달 스타일"""

def get_modal_styles():
    return """
/* === 모달 오버레이 === */
.modal-overlay {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.6);
    backdrop-filter: blur(8px);
    z-index: 1000;
    justify-content: center;
    align-items: center;
}

.modal-overlay.active {
    display: flex;
}

/* === 모달 컨텐츠 === */
.modal-content {
    background: white;
    border-radius: 20px;
    width: 90%;
    max-width: 900px;
    max-height: 85vh;
    overflow: hidden;
    box-shadow: 0 25px 80px rgba(0, 0, 0, 0.3);
}

/* === 모달 헤더 === */
.modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 25px 30px;
    border-bottom: 1px solid #e2e8f0;
    background: linear-gradient(135deg, #f8fafc, #e2e8f0);
}

.modal-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: #1e293b;
}

.modal-close {
    background: none;
    border: none;
    font-size: 1.8rem;
    cursor: pointer;
    color: #64748b;
    padding: 8px;
    border-radius: 8px;
    transition: all 0.2s ease;
}

.modal-close:hover {
    background: #f1f5f9;
    color: #374151;
    transform: scale(1.1);
}

/* === 모달 본문 === */
.modal-body {
    padding: 30px;
    max-height: 65vh;
    overflow-y: auto;
}

/* === 스크롤바 스타일 === */
.modal-body::-webkit-scrollbar {
    width: 8px;
}

.modal-body::-webkit-scrollbar-track {
    background: #f1f5f9;
    border-radius: 4px;
}

.modal-body::-webkit-scrollbar-thumb {
    background: linear-gradient(135deg, #667eea, #764ba2);
    border-radius: 4px;
}

.modal-body::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(135deg, #5a67d8, #6b46c1);
}
"""