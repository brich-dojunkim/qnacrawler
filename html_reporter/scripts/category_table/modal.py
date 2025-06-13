"""
카테고리 테이블 모달 시스템 - 드로어로 변경 + 아코디언 세부카테고리 지원
"""

def get_modal_scripts():
    """모달 관련 스크립트 - 드로어 연동으로 변경 + 세부카테고리 지원"""
    return """
// ─────────── 개선된 모달 시스템 (드로어로 변경) ───────────
function openCategoryModal(button) {
    // 메인 카테고리 테이블에서 호출된 경우
    const row = button.closest('.category-table-row');
    if (row) {
        openMainCategoryDrawer(button, row);
        return;
    }
    
    // 세부카테고리 테이블에서 호출된 경우 (기존 방식)
    const subRow = button.closest('.sub-category-row');
    if (subRow) {
        openSubCategoryDrawer(button, subRow);
        return;
    }
    
    console.log('❌ 카테고리 행을 찾을 수 없습니다.');
}

function openMainCategoryDrawer(button, row) {
    const categoryName = row.dataset.categoryName;
    const team = row.dataset.team;
    const journey = row.dataset.journey;
    
    console.log(`📂 메인 카테고리 드로어 열기: ${categoryName}`);
    
    // 드로어 열기 함수 호출
    if (window.openCategoryDrawer) {
        window.openCategoryDrawer('카테고리', categoryName);
    } else {
        console.error('❌ 드로어 시스템이 로드되지 않았습니다.');
        // Fallback: 기존 모달 방식
        openMainCategoryModal(button, row);
    }
}

function openSubCategoryDrawer(button, row) {
    const categoryName = row.dataset.category;
    const team = row.dataset.team;
    const journey = row.dataset.journey;
    
    console.log(`📂 세부 카테고리 드로어 열기 (기존 방식): ${categoryName}`);
    
    // 드로어 열기 함수 호출
    if (window.openCategoryDrawer) {
        window.openCategoryDrawer('세부카테고리', categoryName);
    } else {
        console.error('❌ 드로어 시스템이 로드되지 않았습니다.');
        // Fallback: 기존 모달 방식
        openSubCategoryModal(button, row);
    }
}

// ─────────── 아코디언에서 직접 호출하는 함수 (개선됨) ───────────
window.openSubCategoryDrawer = function(subCategoryName) {
    console.log(`🎯 아코디언에서 세부카테고리 드로어 열기: ${subCategoryName}`);
    
    // 입력값 검증
    if (!subCategoryName || typeof subCategoryName !== 'string') {
        console.error('❌ 유효하지 않은 카테고리명:', subCategoryName);
        alert('유효하지 않은 카테고리명입니다.');
        return;
    }
    
    if (window.openCategoryDrawer) {
        window.openCategoryDrawer('세부카테고리', subCategoryName);
    } else {
        console.error('❌ 드로어 시스템이 로드되지 않았습니다.');
        alert('드로어 시스템을 불러올 수 없습니다.');
    }
};

// ─────────── 기존 모달 방식 (Fallback용) ───────────
function openMainCategoryModal(button, row) {
    const categoryName = row.dataset.categoryName;
    const team = row.dataset.team;
    const journey = row.dataset.journey;
    const inquiries = row.dataset.inquiries;
    const urgentRate = row.dataset.urgent;
    
    console.log(`📋 메인 카테고리 모달 열기 (Fallback): ${categoryName}`);
    
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
    
    console.log(`📋 세부 카테고리 모달 열기 (Fallback): ${categoryName}`);
    
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
            <h5 style="margin: 0 0 12px 0; color: #374151;">📝 안내</h5>
            <div style="background: white; padding: 12px; border-radius: 6px; border-left: 4px solid #667eea;">
                <div style="color: #374151; line-height: 1.5;">
                    더 자세한 문의 내용을 보시려면 드로어를 사용해주세요.
                    현재는 기본 정보만 표시됩니다.
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

// ─────────── 디버깅 및 검증 함수 ───────────
function debugCategoryButton(element) {
    console.log('🔍 버튼 디버깅:', {
        element: element,
        elementType: typeof element,
        tagName: element?.tagName,
        closest_row: element?.closest?.('.sub-category-row, .category-table-row'),
        data_category: element?.closest?.('.sub-category-row')?.dataset?.category,
        data_categoryName: element?.closest?.('.category-table-row')?.dataset?.categoryName
    });
}

// 전역 함수로 등록하여 HTML에서 접근 가능하게 함
window.debugCategoryButton = debugCategoryButton;

console.log('✅ 카테고리 모달 시스템 로딩 완료 (드로어 + 아코디언 지원)');
"""