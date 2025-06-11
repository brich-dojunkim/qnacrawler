# html_reporter/styles/components/buttons.py
"""버튼 스타일 - 세그먼트 선택 + 정렬 기준 방식"""

def get_button_styles():
    return """
/* === 모달 트리거 버튼 === */
.modal-trigger {
    width: 100%;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 12px 20px;
    margin-top: 16px;
    font-size: 0.95rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
}

.modal-trigger:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
}

/* === 기존 필터 버튼 === */
.filter-buttons {
    display: flex;
    gap: 12px;
    margin-bottom: 24px;
    justify-content: center;
    flex-wrap: wrap;
}

.filter-btn {
    padding: 10px 20px;
    border: 2px solid #e2e8f0;
    background: white;
    border-radius: 25px;
    cursor: pointer;
    font-size: 0.9rem;
    font-weight: 600;
    color: #64748b;
    transition: all 0.3s ease;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

.filter-btn:hover {
    border-color: #667eea;
    color: #667eea;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.2);
}

.filter-btn.active {
    background: linear-gradient(135deg, #667eea, #764ba2);
    border-color: #667eea;
    color: white;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
}

/* === 개선된 필터 컨트롤 === */
.filter-controls {
    display: flex;
    gap: 40px;
    margin-bottom: 24px;
    padding: 24px;
    background: linear-gradient(135deg, #f8fafc, #f1f5f9);
    border-radius: 16px;
    border: 1px solid #e2e8f0;
    flex-wrap: wrap;
    align-items: flex-end;
}

.filter-group {
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.filter-label {
    font-size: 0.9rem;
    font-weight: 600;
    color: #374151;
    margin-bottom: 4px;
}

/* === 세그먼트 선택 드롭다운 === */
.segment-selector {
    position: relative;
}

.segment-dropdown {
    min-width: 180px;
    padding: 10px 16px;
    border: 2px solid #e2e8f0;
    border-radius: 12px;
    background: white;
    font-size: 0.9rem;
    font-weight: 600;
    color: #374151;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.segment-dropdown:hover {
    border-color: #667eea;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.2);
}

.segment-dropdown:focus {
    outline: none;
    border-color: #667eea;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.segment-dropdown optgroup {
    font-weight: 700;
    color: #64748b;
    background: #f8fafc;
}

.segment-dropdown option {
    padding: 8px 12px;
    font-weight: 500;
    color: #374151;
}

/* === 정렬 기준 세그먼트 컨트롤 === */
.segment-control {
    display: flex;
    background: white;
    border-radius: 12px;
    border: 2px solid #e2e8f0;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    position: relative;
}

.segment-control input[type="radio"] {
    display: none;
}

.segment-item {
    padding: 10px 16px;
    font-size: 0.9rem;
    font-weight: 600;
    color: #64748b;
    background: white;
    border: none;
    cursor: pointer;
    transition: all 0.3s ease;
    position: relative;
    z-index: 2;
    white-space: nowrap;
    text-align: center;
    min-width: 80px;
}

.segment-control input[type="radio"]:checked + .segment-item {
    color: white;
    background: linear-gradient(135deg, #667eea, #764ba2);
    box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3);
}

.segment-item:hover:not(.segment-control input[type="radio"]:checked + .segment-item) {
    background: #f1f5f9;
    color: #374151;
}

/* 세그먼트 사이 구분선 */
.segment-item:not(:last-child) {
    border-right: 1px solid #e2e8f0;
}

.segment-control input[type="radio"]:checked + .segment-item:not(:last-child) {
    border-right: 1px solid rgba(255, 255, 255, 0.3);
}

/* === 현재 세그먼트 정보 표시 === */
.current-segment-info {
    margin-bottom: 20px;
    padding: 12px 20px;
    background: linear-gradient(135deg, #e0f2fe, #bae6fd);
    border-radius: 12px;
    border-left: 4px solid #0369a1;
}

.segment-indicator {
    font-size: 0.9rem;
    font-weight: 600;
    color: #0c4a6e;
    display: flex;
    align-items: center;
    gap: 8px;
}

/* === 반응형 스타일 === */
@media (max-width: 768px) {
    .filter-controls {
        flex-direction: column;
        gap: 20px;
        padding: 16px;
    }
    
    .filter-group {
        width: 100%;
    }
    
    .segment-dropdown {
        width: 100%;
        min-width: auto;
    }
    
    .segment-control {
        width: 100%;
    }
    
    .segment-item {
        flex: 1;
        padding: 8px 12px;
        font-size: 0.85rem;
        min-width: auto;
    }
    
    .current-segment-info {
        padding: 10px 16px;
    }
    
    .segment-indicator {
        font-size: 0.85rem;
        flex-wrap: wrap;
    }
}

@media (max-width: 480px) {
    .segment-item {
        padding: 6px 8px;
        font-size: 0.8rem;
    }
    
    .segment-dropdown {
        padding: 8px 12px;
        font-size: 0.85rem;
    }
    
    .filter-controls {
        padding: 12px;
    }
}
"""