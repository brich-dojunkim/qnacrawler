"""
카테고리 테이블 모달 스타일
"""

def get_modal_styles():
    """새 모달 스타일"""
    return """
/* === 새 모달 스타일 === */
.new-modal-overlay {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.6);
    backdrop-filter: blur(8px);
    z-index: 10000;
    justify-content: center;
    align-items: center;
}

.new-modal-overlay.active {
    display: flex;
}

.new-modal-content {
    background: white;
    border-radius: 16px;
    width: 90%;
    max-width: 800px;
    max-height: 80vh;
    overflow: hidden;
    box-shadow: 0 25px 80px rgba(0, 0, 0, 0.3);
}

.new-modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 24px;
    border-bottom: 1px solid #e2e8f0;
    background: linear-gradient(135deg, #f8fafc, #e2e8f0);
}

.new-modal-title {
    font-size: 1.4rem;
    font-weight: 700;
    color: #1e293b;
    margin: 0;
}

.new-modal-close {
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    color: #64748b;
    padding: 4px;
    border-radius: 4px;
    transition: all 0.2s ease;
}

.new-modal-close:hover {
    background: #f1f5f9;
    color: #374151;
}

.new-modal-body {
    padding: 24px;
    max-height: 60vh;
    overflow-y: auto;
}

/* === 모달 스크롤바 스타일 === */
.new-modal-body::-webkit-scrollbar {
    width: 6px;
}

.new-modal-body::-webkit-scrollbar-track {
    background: #f1f5f9;
}

.new-modal-body::-webkit-scrollbar-thumb {
    background: #cbd5e1;
    border-radius: 3px;
}

.new-modal-body::-webkit-scrollbar-thumb:hover {
    background: #94a3b8;
}
"""