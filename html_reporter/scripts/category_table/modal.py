"""
카테고리 테이블 모달 시스템
"""

def get_modal_scripts():
    """모달 관련 스크립트"""
    return """
// ─────────── 개선된 모달 시스템 (세부카테고리 테이블 지원) ───────────
function openCategoryModal(button) {
    // 메인 카테고리 테이블에서 호출된 경우
    const row = button.closest('.category-table-row');
    if (row) {
        openMainCategoryModal(button, row);
        return;
    }
    
    // 세부카테고리 테이블에서 호출된 경우
    const subRow = button.closest('.sub-category-row');
    if (subRow) {
        openSubCategoryModal(button, subRow);
        return;
    }
    
    console.log('❌ 카테고리 행을 찾을 수 없습니다.');
}

function openMainCategoryModal(button, row) {
    const categoryName = row.dataset.categoryName;
    const team = row.dataset.team;
    const journey = row.dataset.journey;
    const inquiries = row.dataset.inquiries;
    const urgentRate = row.dataset.urgent;
    
    console.log(`메인 카테고리 모달 열기: ${categoryName}`);
    
    const modalContent = generateCategoryModalContent(categoryName, team, journey, inquiries, urgentRate);
    createNewModal(`category-modal-${categoryName.replace(/[^a-zA-Z0-9]/g, '')}`, 
                   `📂 ${categoryName} 상세 보기`, 
                   modalContent);
}

function openSubCategoryModal(button, row) {
    const categoryName = row.dataset.category;
    const team = row.dataset.team;
    const journey = row.dataset.journey;
    const inquiries = row.dataset.inquiries;
    const urgentRate = row.dataset.urgent;
    
    console.log(`세부 카테고리 모달 열기: ${categoryName}`);
    
    const modalContent = generateCategoryModalContent(categoryName, team, journey, inquiries, urgentRate);
    createNewModal(`sub-category-modal-${categoryName.replace(/[^a-zA-Z0-9]/g, '')}`, 
                   `📋 ${categoryName} 상세 보기`, 
                   modalContent);
}

function generateCategoryModalContent(categoryName, team, journey, inquiries, urgentRate) {
    return `
        <div style="margin-bottom: 20px; padding: 16px; background: linear-gradient(135deg, #f8fafc, #e2e8f0); border-radius: 8px;">
            <h4 style="margin: 0 0 12px 0; color: #374151;">📊 ${categoryName} 상세 정보</h4>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 12px;">
                <div style="text-align: center;">
                    <div style="font-size: 1.5rem; font-weight: bold; color: #667eea;">${inquiries}</div>
                    <div style="font-size: 0.85rem; color: #6b7280;">총 문의</div>
                </div>
                <div style="text-align: center;">
                    <div style="font-size: 1.5rem; font-weight: bold; color: #ef4444;">${urgentRate}%</div>
                    <div style="font-size: 0.85rem; color: #6b7280;">긴급률</div>
                </div>
                <div style="text-align: center;">
                    <div style="font-size: 1rem; font-weight: bold; color: #f59e0b;">${team}</div>
                    <div style="font-size: 0.85rem; color: #6b7280;">담당팀</div>
                </div>
                <div style="text-align: center;">
                    <div style="font-size: 1rem; font-weight: bold; color: #10b981;">${journey}</div>
                    <div style="font-size: 0.85rem; color: #6b7280;">유저여정</div>
                </div>
            </div>
        </div>
        
        <div style="background: #f8fafc; padding: 16px; border-radius: 8px;">
            <h5 style="margin: 0 0 12px 0; color: #374151;">📝 문의 샘플</h5>
            <div style="background: white; padding: 12px; border-radius: 6px; border-left: 4px solid #667eea;">
                <div style="font-size: 0.9rem; color: #6b7280; margin-bottom: 8px;">
                    <strong>샘플 문의 내용:</strong>
                </div>
                <div style="color: #374151; line-height: 1.5;">
                    이 카테고리에 해당하는 실제 고객 문의 내용이 여기에 표시됩니다. 
                    현재는 샘플 데이터로 표시되고 있으며, 실제 구현 시에는 해당 카테고리의 
                    대표적인 문의 사례들이 표시될 예정입니다.
                </div>
                <div style="margin-top: 8px; font-size: 0.8rem; color: #9ca3af;">
                    등록일: 2024-01-15 | 상태: 답변완료
                </div>
            </div>
            <div style="background: white; padding: 12px; border-radius: 6px; border-left: 4px solid #f59e0b; margin-top: 8px;">
                <div style="font-size: 0.9rem; color: #6b7280; margin-bottom: 8px;">
                    <strong>긴급 문의 샘플:</strong>
                </div>
                <div style="color: #374151; line-height: 1.5;">
                    긴급하게 처리가 필요한 문의 사례입니다. 
                    이런 유형의 문의들이 전체 문의 중 ${urgentRate}%를 차지하고 있습니다.
                </div>
                <div style="margin-top: 8px; font-size: 0.8rem; color: #ef4444;">
                    등록일: 2024-01-16 | 상태: 처리중 | 🚨 긴급
                </div>
            </div>
        </div>
    `;
}

function createNewModal(modalId, title, content) {
    // 기존 모달이 있다면 제거
    const existingModal = document.getElementById(modalId);
    if (existingModal) {
        existingModal.remove();
    }
    
    // 새 모달 생성
    const modal = document.createElement('div');
    modal.id = modalId;
    modal.className = 'new-modal-overlay';
    modal.innerHTML = `
        <div class="new-modal-content">
            <div class="new-modal-header">
                <h3 class="new-modal-title">${title}</h3>
                <button class="new-modal-close" onclick="closeNewModal('${modalId}')">&times;</button>
            </div>
            <div class="new-modal-body">
                ${content}
            </div>
        </div>
    `;
    
    // body에 추가
    document.body.appendChild(modal);
    
    // 모달 표시
    setTimeout(() => {
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
    }, 10);
}

function closeNewModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.remove('active');
        document.body.style.overflow = 'auto';
        setTimeout(() => {
            modal.remove();
        }, 300);
    }
}
"""