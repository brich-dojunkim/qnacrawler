# html_reporter/scripts/drawer/base.py
"""
드로어 기본 열기/닫기 기능
"""

def get_drawer_base_scripts():
    """드로어 기본 열기/닫기 스크립트"""
    return """
// ─────────── 전역 변수 ───────────
let currentInquiryData = [];
let filteredInquiryData = [];
let currentCategory = null;
let currentInquiryDetail = null;

// ─────────── 드로어 열기/닫기 ───────────
function openInquiryDrawer(categoryName, inquiryData) {
    console.log(`📂 드로어 열기: ${categoryName} (${inquiryData.length}건)`);
    
    currentCategory = categoryName;
    currentInquiryData = inquiryData;
    filteredInquiryData = [...inquiryData];
    
    // 드로어 UI 업데이트
    updateDrawerHeader();
    renderInquiryList();
    
    // 드로어 열기 애니메이션
    const drawer = document.getElementById('inquiry-drawer');
    const mainSection = document.querySelector('.detailed-analysis-section');
    
    drawer.classList.add('open');
    mainSection.classList.add('drawer-open');
    
    // 검색 입력 초기화
    const searchInput = document.getElementById('drawer-search-input');
    if (searchInput) {
        searchInput.value = '';
    }
    
    // 목록 뷰로 초기화
    showInquiryList();
}

function closeInquiryDrawer() {
    console.log('❌ 드로어 닫기');
    
    const drawer = document.getElementById('inquiry-drawer');
    const mainSection = document.querySelector('.detailed-analysis-section');
    
    drawer.classList.remove('open');
    mainSection.classList.remove('drawer-open');
    
    // 상태 초기화
    currentCategory = null;
    currentInquiryData = [];
    filteredInquiryData = [];
    currentInquiryDetail = null;
    
    // 뷰 초기화
    showInquiryList();
}

// ─────────── 뷰 전환 ───────────
function showInquiryList() {
    const listView = document.getElementById('inquiry-list-view');
    const detailView = document.getElementById('inquiry-detail-view');
    
    if (listView) listView.classList.remove('detail-mode');
    if (detailView) detailView.classList.remove('active');
}

function showInquiryDetail() {
    const listView = document.getElementById('inquiry-list-view');
    const detailView = document.getElementById('inquiry-detail-view');
    
    if (listView) listView.classList.add('detail-mode');
    if (detailView) detailView.classList.add('active');
}

// ─────────── 외부 연동 함수 (기존 카테고리 버튼과 연결) ───────────
window.openCategoryDrawer = function(categoryName, subCategoryName) {
    console.log(`🎯 카테고리 드로어 열기 요청: ${categoryName} > ${subCategoryName}`);
    
    // 실제 데이터는 window.rawInquiryData에서 가져온다고 가정
    if (!window.rawInquiryData) {
        console.error('❌ 원본 문의 데이터를 찾을 수 없습니다.');
        alert('문의 데이터를 불러올 수 없습니다.');
        return;
    }
    
    console.log(`📊 전체 데이터 수: ${window.rawInquiryData.length}건`);
    
    // 해당 카테고리의 문의들만 필터링
    const categoryInquiries = window.rawInquiryData.filter(inquiry => {
        // 다양한 필드명 패턴 지원
        let inquiryCategory = null;
        
        // 1. category.sub_category (중첩 구조)
        if (inquiry.category && inquiry.category.sub_category) {
            inquiryCategory = inquiry.category.sub_category;
        }
        // 2. sub_category (평면 구조)
        else if (inquiry.sub_category) {
            inquiryCategory = inquiry.sub_category;
        }
        // 3. category (문자열)
        else if (typeof inquiry.category === 'string') {
            inquiryCategory = inquiry.category;
        }
        
        // 디버깅용 로그 (첫 5개만)
        if (window.rawInquiryData.indexOf(inquiry) < 5) {
            console.log(`🔍 문의 ${inquiry.inquiry_id}: 카테고리 = "${inquiryCategory}", 찾는 카테고리 = "${subCategoryName}"`);
        }
        
        return inquiryCategory === subCategoryName;
    });
    
    console.log(`🔍 필터링 결과: ${categoryInquiries.length}건 (전체 ${window.rawInquiryData.length}건 중)`);
    
    if (categoryInquiries.length === 0) {
        // 디버깅 정보 제공
        console.log('❌ 필터링 결과가 0건입니다. 디버깅 정보:');
        console.log(`   찾는 카테고리: "${subCategoryName}"`);
        
        // 실제 존재하는 카테고리들 확인
        const existingCategories = new Set();
        window.rawInquiryData.slice(0, 10).forEach(inquiry => {
            if (inquiry.category && inquiry.category.sub_category) {
                existingCategories.add(inquiry.category.sub_category);
            } else if (inquiry.sub_category) {
                existingCategories.add(inquiry.sub_category);
            } else if (typeof inquiry.category === 'string') {
                existingCategories.add(inquiry.category);
            }
        });
        
        console.log('   실제 존재하는 카테고리들 (샘플 10개):', Array.from(existingCategories));
        
        alert(`'${subCategoryName}' 카테고리에 해당하는 문의가 없습니다.\\n\\n디버깅 정보:\\n- 전체 문의: ${window.rawInquiryData.length}건\\n- 필터링 결과: 0건\\n\\n콘솔을 확인해주세요.`);
        return;
    }
    
    openInquiryDrawer(subCategoryName, categoryInquiries);
};

console.log('✅ 드로어 기본 기능 로딩 완료');
"""