# html_reporter/scripts/drawer/search.py
"""
드로어 검색 및 필터링 기능
"""

def get_drawer_search_scripts():
    """드로어 검색 관련 스크립트"""
    return """
// ─────────── 검색 및 필터 제어 함수들 ───────────
function handleSearchInput(event) {
    const searchTerm = event.target.value;
    const clearBtn = document.getElementById('search-clear');
    
    // 검색어 지우기 버튼 표시/숨김
    if (clearBtn) {
        if (searchTerm) {
            clearBtn.classList.remove('hidden');
        } else {
            clearBtn.classList.add('hidden');
        }
    }
    
    // 검색 실행 (디바운스 적용)
    applyDrawerFilters();
}

function clearSearchInput() {
    const searchInput = document.getElementById('drawer-search-input');
    const clearBtn = document.getElementById('search-clear');
    
    if (searchInput) {
        searchInput.value = '';
        searchInput.focus();
    }
    
    if (clearBtn) {
        clearBtn.classList.add('hidden');
    }
    
    // 필터 다시 적용
    applyDrawerFilters();
}

function handleStatusFilterChange(event) {
    console.log(`🔍 상태 필터 변경: ${event.target.value}`);
    applyDrawerFilters();
}

function handleSortChange(event) {
    console.log(`📊 정렬 변경: ${event.target.value}`);
    applyDrawerFilters();
}

// ─────────── 고급 검색 기능 ───────────
function searchInquiries(searchTerm, filters = {}) {
    if (!searchTerm && Object.keys(filters).length === 0) {
        return currentInquiryData;
    }
    
    let results = [...currentInquiryData];
    
    // 텍스트 검색
    if (searchTerm) {
        const lowercaseSearch = searchTerm.toLowerCase();
        results = results.filter(inquiry => {
            // 문의 내용에서 검색
            const contentMatch = inquiry.question_content?.toLowerCase().includes(lowercaseSearch);
            // 미리보기에서 검색
            const previewMatch = inquiry.question_preview?.toLowerCase().includes(lowercaseSearch);
            // 판매자명에서 검색
            const sellerMatch = inquiry.seller?.toLowerCase().includes(lowercaseSearch);
            // 문의 ID에서 검색
            const idMatch = inquiry.inquiry_id?.toString().includes(searchTerm);
            
            return contentMatch || previewMatch || sellerMatch || idMatch;
        });
    }
    
    // 상태 필터
    if (filters.status && filters.status !== 'all') {
        if (filters.status === 'answered') {
            results = results.filter(item => item.answer_status === '답변완료');
        } else if (filters.status === 'unanswered') {
            results = results.filter(item => item.answer_status === '미답변');
        }
    }
    
    // 긴급도 필터
    if (filters.urgent !== undefined) {
        results = results.filter(item => item.is_urgent === filters.urgent);
    }
    
    // 날짜 범위 필터 (필요시 확장)
    if (filters.dateFrom || filters.dateTo) {
        results = results.filter(item => {
            const itemDate = new Date(item.registration_date);
            let inRange = true;
            
            if (filters.dateFrom) {
                inRange = inRange && (itemDate >= new Date(filters.dateFrom));
            }
            
            if (filters.dateTo) {
                inRange = inRange && (itemDate <= new Date(filters.dateTo));
            }
            
            return inRange;
        });
    }
    
    return results;
}

// ─────────── 검색 결과 하이라이팅 ───────────
function highlightSearchTerm(text, searchTerm) {
    if (!searchTerm || !text) return text;
    
    const regex = new RegExp(`(${searchTerm})`, 'gi');
    return text.replace(regex, '<mark>$1</mark>');
}

// ─────────── 검색 통계 ───────────
function getSearchStats() {
    return {
        total: currentInquiryData.length,
        filtered: filteredInquiryData.length,
        answered: filteredInquiryData.filter(item => item.answer_status === '답변완료').length,
        unanswered: filteredInquiryData.filter(item => item.answer_status === '미답변').length,
        urgent: filteredInquiryData.filter(item => item.is_urgent).length
    };
}

function updateSearchStats() {
    const stats = getSearchStats();
    console.log('📊 검색 통계:', stats);
    
    // 통계 UI 업데이트 (필요시 확장)
    const statsElement = document.getElementById('search-stats');
    if (statsElement) {
        statsElement.innerHTML = `
            <div class="search-stats-content">
                <span>총 ${stats.total}건 중 ${stats.filtered}건 표시</span>
                <span>답변완료: ${stats.answered}건</span>
                <span>미답변: ${stats.unanswered}건</span>
                <span>긴급: ${stats.urgent}건</span>
            </div>
        `;
    }
}

// ─────────── 검색 기록 관리 (선택사항) ───────────
let searchHistory = [];
const MAX_SEARCH_HISTORY = 10;

function addToSearchHistory(searchTerm) {
    if (!searchTerm || searchTerm.length < 2) return;
    
    // 중복 제거
    searchHistory = searchHistory.filter(term => term !== searchTerm);
    
    // 맨 앞에 추가
    searchHistory.unshift(searchTerm);
    
    // 최대 개수 제한
    if (searchHistory.length > MAX_SEARCH_HISTORY) {
        searchHistory = searchHistory.slice(0, MAX_SEARCH_HISTORY);
    }
    
    // 로컬 스토리지에 저장 (브라우저 지원시)
    try {
        localStorage.setItem('drawer_search_history', JSON.stringify(searchHistory));
    } catch (e) {
        // 로컬 스토리지 지원하지 않는 환경에서는 무시
        console.log('검색 기록 저장 불가 (로컬 스토리지 미지원)');
    }
}

function loadSearchHistory() {
    try {
        const saved = localStorage.getItem('drawer_search_history');
        if (saved) {
            searchHistory = JSON.parse(saved);
        }
    } catch (e) {
        // 로컬 스토리지 지원하지 않는 환경에서는 무시
        searchHistory = [];
    }
}

// ─────────── 키보드 단축키 ───────────
function handleSearchKeyDown(event) {
    switch(event.key) {
        case 'Enter':
            // 엔터키로 검색 실행
            const searchTerm = event.target.value.trim();
            if (searchTerm) {
                addToSearchHistory(searchTerm);
            }
            break;
            
        case 'Escape':
            // ESC키로 검색창 클리어
            clearSearchInput();
            break;
            
        case 'ArrowDown':
            // 아래 화살표로 검색 기록 표시 (확장 가능)
            event.preventDefault();
            showSearchSuggestions();
            break;
    }
}

function showSearchSuggestions() {
    // 검색 기록을 드롭다운으로 표시하는 기능 (확장 가능)
    console.log('검색 기록:', searchHistory);
}

console.log('✅ 드로어 검색 기능 로딩 완료');
"""