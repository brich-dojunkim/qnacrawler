# html_reporter/scripts/inquiry_modal/data_loader.py (수정된 버전)
"""
문의 데이터 로딩 및 카테고리 매칭 스크립트 - 실제 JSON 구조에 맞게 대폭 수정
"""

def get_data_loader_scripts():
    """데이터 로딩 관련 스크립트 - 실제 JSON 구조에 맞게 대폭 수정"""
    return """
// ─────────── 데이터 로딩 및 매칭 (실제 JSON 구조 완전 반영) ───────────
console.log('📊 데이터 로더 시스템 로딩 중... (JSON 구조 대폭 수정)');

// 카테고리별 문의 로딩 메인 함수
window.loadCategoryInquiries = function(categoryName) {
    console.log(`📋 카테고리 문의 로딩: "${categoryName}"`);
    
    try {
        // 원본 데이터 확인
        if (!window.rawInquiryData || !Array.isArray(window.rawInquiryData)) {
            console.error('❌ 원본 문의 데이터가 없습니다.');
            console.log('🔍 window.rawInquiryData 상태:', typeof window.rawInquiryData, window.rawInquiryData);
            hideInquiryLoading();
            showEmptyState();
            return;
        }
        
        console.log(`📦 전체 원본 데이터: ${window.rawInquiryData.length}건`);
        
        // 🔧 수정: 실제 JSON 구조에 맞춘 카테고리 필터링
        const categoryInquiries = filterInquiriesByCategory(categoryName);
        console.log(`🎯 "${categoryName}" 매칭 문의: ${categoryInquiries.length}건`);
        
        if (categoryInquiries.length === 0) {
            console.log('📭 해당 카테고리의 문의가 없습니다.');
            hideInquiryLoading();
            showEmptyState();
            updateInquiryStats(0, 0, 0, 0);
            return;
        }
        
        // 상태 업데이트
        window.inquiryModalState.allInquiries = categoryInquiries;
        window.inquiryModalState.totalItems = categoryInquiries.length;
        
        // 🔧 수정: 실제 JSON 구조에 맞춘 통계 계산
        const stats = calculateInquiryStats(categoryInquiries);
        updateInquiryStats(stats.total, stats.urgent, stats.completed, stats.avgLength);
        
        // 🔧 수정: 실제 JSON 구조에 맞춘 팀 필터 옵션 업데이트
        updateTeamFilterOptions(categoryInquiries);
        
        // 필터링 및 렌더링
        applyAllFiltersAndRender();
        
        console.log('✅ 카테고리 데이터 로딩 완료');
        
    } catch (error) {
        console.error('❌ 카테고리 문의 로딩 오류:', error);
        console.log('❌ 오류 스택:', error.stack);
        hideInquiryLoading();
        showEmptyState();
    }
};

// ─────────── 🔧 완전히 수정된 카테고리별 문의 필터링 ───────────
function filterInquiriesByCategory(categoryName) {
    console.log(`🔍 카테고리 필터링 시작: "${categoryName}"`);
    
    // 카테고리명 정규화 (소문자, 공백 제거)
    const normalizedCategoryName = categoryName.trim().toLowerCase();
    console.log(`🔧 정규화된 카테고리명: "${normalizedCategoryName}"`);
    
    // 첫 번째 데이터의 구조 확인
    if (window.rawInquiryData.length > 0) {
        const firstItem = window.rawInquiryData[0];
        console.log('📊 첫 번째 데이터 구조 확인:');
        console.log('  - inquiry_id:', firstItem.inquiry_id);
        console.log('  - category 객체:', firstItem.category);
        console.log('  - 직접 sub_category:', firstItem.sub_category);
        console.log('  - 직접 assigned_team:', firstItem.assigned_team);
    }
    
    const matchedInquiries = window.rawInquiryData.filter(inquiry => {
        if (!inquiry) {
            console.warn('⚠️ 빈 문의 데이터 발견');
            return false;
        }
        
        try {
            // 🔧 수정: 실제 JSON 구조에 맞춘 필드 추출
            let subCategory = null;
            let fullText = '';
            let assignedTeam = null;
            
            // category 객체가 있는 경우
            if (inquiry.category && typeof inquiry.category === 'object') {
                subCategory = inquiry.category.sub_category;
                fullText = inquiry.category.full_text || '';
                assignedTeam = inquiry.category.assigned_team;
            }
            
            // category 객체가 없거나 필드가 없는 경우 직접 필드에서 추출
            if (!subCategory) {
                subCategory = inquiry.sub_category;
            }
            if (!assignedTeam) {
                assignedTeam = inquiry.assigned_team;
            }
            
            // 디버깅용 로그 (첫 5개만)
            if (window.rawInquiryData.indexOf(inquiry) < 5) {
                console.log(`📝 문의 ${inquiry.inquiry_id}:`, {
                    subCategory,
                    fullText,
                    assignedTeam,
                    hasCategory: !!inquiry.category
                });
            }
            
            if (!subCategory) {
                if (window.rawInquiryData.indexOf(inquiry) < 5) {
                    console.warn(`⚠️ 문의 ${inquiry.inquiry_id}: sub_category가 없음`);
                }
                return false;
            }
            
            // 🔧 수정: 더 유연한 매칭 로직
            const categoryLower = normalizedCategoryName;
            const subCategoryLower = subCategory.trim().toLowerCase();
            const fullTextLower = fullText.trim().toLowerCase();
            
            // 1. 정확한 매칭
            if (subCategoryLower === categoryLower) {
                return true;
            }
            
            // 2. 부분 매칭 (양방향)
            if (subCategoryLower.includes(categoryLower) || categoryLower.includes(subCategoryLower)) {
                return true;
            }
            
            // 3. full_text에서 매칭
            if (fullTextLower.includes(categoryLower)) {
                return true;
            }
            
            // 4. 특수 케이스: 한글 띄어쓰기 무시 매칭
            const categoryNoSpace = categoryLower.replace(/\s+/g, '');
            const subCategoryNoSpace = subCategoryLower.replace(/\s+/g, '');
            
            if (categoryNoSpace === subCategoryNoSpace || 
                categoryNoSpace.includes(subCategoryNoSpace) || 
                subCategoryNoSpace.includes(categoryNoSpace)) {
                return true;
            }
            
            return false;
                   
        } catch (e) {
            console.warn('⚠️ 필터링 중 오류:', e, 'inquiry:', inquiry.inquiry_id);
            return false;
        }
    });
    
    console.log(`✅ 매칭 결과: ${matchedInquiries.length}건`);
    
    // 매칭된 문의의 샘플 로그 (더 자세히)
    if (matchedInquiries.length > 0) {
        console.log('📝 매칭된 문의 샘플 (상위 3개):');
        matchedInquiries.slice(0, 3).forEach((inquiry, index) => {
            const id = inquiry.inquiry_id || 'N/A';
            const subCat = inquiry.category?.sub_category || inquiry.sub_category || 'N/A';
            const team = inquiry.category?.assigned_team || inquiry.assigned_team || 'N/A';
            const content = (inquiry.question_content || '').substring(0, 50) + '...';
            const answerStatus = inquiry.answer_status || 'N/A';
            console.log(`  ${index + 1}. ID: ${id}`);
            console.log(`     카테고리: ${subCat}`);
            console.log(`     팀: ${team}`);
            console.log(`     상태: ${answerStatus}`);
            console.log(`     내용: ${content}`);
        });
    }
    
    return matchedInquiries;
}

// ─────────── 🔧 실제 JSON 구조에 맞춘 통계 계산 ───────────
function calculateInquiryStats(inquiries) {
    if (!inquiries || inquiries.length === 0) {
        return { total: 0, urgent: 0, completed: 0, avgLength: 0 };
    }
    
    console.log(`📊 통계 계산 시작: ${inquiries.length}건`);
    
    const total = inquiries.length;
    let urgent = 0;
    let completed = 0;
    let totalLength = 0;
    let processedCount = 0;
    
    inquiries.forEach((inquiry, index) => {
        try {
            // 🔧 수정: 긴급 문의 카운트 (실제 JSON 구조)
            if (inquiry.is_urgent === true || inquiry.is_urgent === 'true' || inquiry.is_urgent === 1) {
                urgent++;
            }
            
            // 🔧 수정: 완료된 문의 카운트 (실제 JSON 구조 - answer_status 우선, answers 배열 보조)
            let isCompleted = false;
            
            // 1순위: answer_status 필드 확인
            if (inquiry.answer_status === '답변완료') {
                isCompleted = true;
            }
            // 2순위: answers 배열 확인
            else if (inquiry.answers && Array.isArray(inquiry.answers) && inquiry.answers.length > 0) {
                isCompleted = true;
            }
            
            if (isCompleted) {
                completed++;
            }
            
            // 문의 내용 길이 계산
            const contentLength = inquiry.question_content ? inquiry.question_content.length : 0;
            totalLength += contentLength;
            processedCount++;
            
            // 디버깅용 로그 (첫 3개만)
            if (index < 3) {
                console.log(`📋 문의 ${inquiry.inquiry_id}:`, {
                    is_urgent: inquiry.is_urgent,
                    answer_status: inquiry.answer_status,
                    answers_count: inquiry.answers?.length || 0,
                    content_length: contentLength,
                    isCompleted
                });
            }
            
        } catch (error) {
            console.warn(`⚠️ 문의 ${inquiry.inquiry_id} 통계 계산 중 오류:`, error);
        }
    });
    
    const avgLength = processedCount > 0 ? Math.round(totalLength / processedCount) : 0;
    
    console.log(`📊 통계 계산 완료:`, {
        total,
        urgent,
        completed,
        avgLength,
        urgentRate: `${((urgent / total) * 100).toFixed(1)}%`,
        completedRate: `${((completed / total) * 100).toFixed(1)}%`
    });
    
    return { total, urgent, completed, avgLength };
}

// ─────────── 🔧 실제 JSON 구조에 맞춘 팀 필터 옵션 업데이트 ───────────
function updateTeamFilterOptions(inquiries) {
    const teamFilter = document.getElementById('team-filter');
    if (!teamFilter) {
        console.warn('⚠️ team-filter 요소를 찾을 수 없습니다.');
        return;
    }
    
    console.log(`👥 팀 필터 옵션 업데이트: ${inquiries.length}개 문의`);
    
    // 🔧 수정: 실제 JSON 구조에 맞춘 고유한 팀 목록 추출
    const teams = new Set();
    
    inquiries.forEach((inquiry, index) => {
        try {
            let team = null;
            
            // category 객체에서 추출 (null 체크 추가)
            if (inquiry.category && inquiry.category.assigned_team && inquiry.category.assigned_team !== null) {
                team = inquiry.category.assigned_team;
            }
            // 직접 필드에서 추출
            else if (inquiry.assigned_team && inquiry.assigned_team !== null) {
                team = inquiry.assigned_team;
            }

            if (team && typeof team === 'string' && team.trim()) {
                teams.add(team.trim());
            } else {
                // null인 경우 '미분류'로 처리
                teams.add('미분류');
            }
            
            // 디버깅용 로그 (첫 5개만)
            if (index < 5) {
                console.log(`👤 문의 ${inquiry.inquiry_id} 팀:`, {
                    category_team: inquiry.category?.assigned_team,
                    direct_team: inquiry.assigned_team,
                    selected_team: team
                });
            }
            
        } catch (error) {
            console.warn(`⚠️ 문의 ${inquiry.inquiry_id} 팀 추출 중 오류:`, error);
        }
    });
    
    // 팀 필터 옵션 생성
    const sortedTeams = Array.from(teams).sort();
    let optionsHtml = '<option value="">👥 모든 팀</option>';
    
    sortedTeams.forEach(team => {
        optionsHtml += `<option value="${team}">${team}</option>`;
    });
    
    teamFilter.innerHTML = optionsHtml;
    
    console.log(`👥 팀 필터 업데이트 완료: ${sortedTeams.length}개 팀`);
    console.log(`📋 발견된 팀 목록:`, sortedTeams);
}

// ─────────── 검색어 하이라이팅 (기존 유지) ───────────
window.highlightSearchTerm = function(text, searchTerm) {
    if (!searchTerm || !text) return text;
    
    try {
        const regex = new RegExp(`(${searchTerm.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&')})`, 'gi');
        return text.replace(regex, '<mark class="search-highlight">$1</mark>');
    } catch (error) {
        console.warn('⚠️ 검색어 하이라이팅 오류:', error);
        return text;
    }
};

// ─────────── 🔧 강화된 디버깅 함수 ───────────
window.debugInquiryData = function() {
    console.log('🔍 문의 데이터 디버깅 정보:');
    console.log(`📦 전체 원본 데이터: ${window.rawInquiryData?.length || 0}건`);
    console.log(`🎯 현재 카테고리: ${window.inquiryModalState.currentCategory}`);
    console.log(`📊 필터링된 문의: ${window.inquiryModalState.allInquiries?.length || 0}건`);
    console.log(`📄 현재 페이지 문의: ${window.inquiryModalState.currentPageInquiries?.length || 0}건`);
    
    if (window.rawInquiryData && window.rawInquiryData.length > 0) {
        console.log('📋 첫 번째 원본 데이터 구조:');
        const firstData = window.rawInquiryData[0];
        console.log('  - inquiry_id:', firstData.inquiry_id);
        console.log('  - is_urgent:', firstData.is_urgent);
        console.log('  - answer_status:', firstData.answer_status);
        console.log('  - category 객체:', firstData.category);
        console.log('  - 직접 assigned_team:', firstData.assigned_team);
        console.log('  - 직접 sub_category:', firstData.sub_category);
        console.log('  - answers 배열:', firstData.answers?.length || 0, '개');
        console.log('  - question_content 길이:', firstData.question_content?.length || 0, '자');
    }
    
    if (window.inquiryModalState.allInquiries && window.inquiryModalState.allInquiries.length > 0) {
        console.log('📊 필터링된 첫 번째 데이터:');
        const firstFiltered = window.inquiryModalState.allInquiries[0];
        console.log('  - inquiry_id:', firstFiltered.inquiry_id);
        console.log('  - 매칭된 카테고리:', firstFiltered.category?.sub_category || firstFiltered.sub_category);
        console.log('  - 팀:', firstFiltered.category?.assigned_team || firstFiltered.assigned_team);
    }
    
    // 카테고리별 분포 확인
    if (window.rawInquiryData && window.rawInquiryData.length > 0) {
        const categoryCount = {};
        window.rawInquiryData.forEach(inquiry => {
            const category = inquiry.category?.sub_category || inquiry.sub_category || '알 수 없음';
            categoryCount[category] = (categoryCount[category] || 0) + 1;
        });
        
        console.log('📊 전체 카테고리 분포 (상위 10개):');
        Object.entries(categoryCount)
            .sort((a, b) => b[1] - a[1])
            .slice(0, 10)
            .forEach(([category, count]) => {
                console.log(`  - ${category}: ${count}건`);
            });
    }
};

// 자동으로 디버깅 정보 출력 (개발용)
setTimeout(() => {
    if (window.rawInquiryData) {
        console.log('🚀 데이터 로더 자동 디버깅:');
        window.debugInquiryData();
    }
}, 1000);

console.log('✅ 데이터 로더 시스템 로딩 완료 (JSON 구조 대폭 수정)');
"""