# html_reporter/scripts/inquiry_modal/data_matcher.py
"""
카테고리별 문의 데이터 매칭 시스템
"""

def get_data_matcher_scripts():
    """데이터 매칭 시스템 스크립트"""
    return """
// ─────────── 데이터 매칭 시스템 ───────────
console.log('🎯 데이터 매칭 시스템 로딩 중...');

// ─────────── 메인 매칭 함수 ───────────
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
            return performCategoryMatch(inquiry, normalizedCategoryName);
        } catch (e) {
            console.warn('⚠️ 필터링 중 오류:', e, 'inquiry:', inquiry.inquiry_id);
            return false;
        }
    });
    
    console.log(`✅ 매칭 결과: ${matchedInquiries.length}건`);
    
    // 매칭된 문의의 샘플 로그
    if (matchedInquiries.length > 0) {
        logMatchedSamples(matchedInquiries);
    }
    
    return matchedInquiries;
}

// ─────────── 실제 매칭 로직 ───────────
function performCategoryMatch(inquiry, normalizedCategoryName) {
    const categoryData = extractCategoryData(inquiry);
    
    // 디버깅용 로그 (첫 5개만)
    if (window.rawInquiryData.indexOf(inquiry) < 5) {
        console.log(`📝 문의 ${inquiry.inquiry_id}:`, categoryData);
    }
    
    if (!categoryData.subCategory) {
        if (window.rawInquiryData.indexOf(inquiry) < 5) {
            console.warn(`⚠️ 문의 ${inquiry.inquiry_id}: sub_category가 없음`);
        }
        return false;
    }
    
    return testCategoryMatches(categoryData, normalizedCategoryName);
}

// ─────────── 카테고리 데이터 추출 ───────────
function extractCategoryData(inquiry) {
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
    
    return {
        subCategory,
        fullText,
        assignedTeam,
        hasCategory: !!inquiry.category
    };
}

// ─────────── 매칭 테스트 수행 ───────────
function testCategoryMatches(categoryData, targetCategory) {
    const categoryLower = targetCategory;
    const subCategoryLower = categoryData.subCategory.trim().toLowerCase();
    const fullTextLower = categoryData.fullText.trim().toLowerCase();
    
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
}

// ─────────── 매칭 샘플 로그 ───────────
function logMatchedSamples(matchedInquiries) {
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

// ─────────── 매칭 통계 계산 ───────────
function calculateMatchingStats(inquiries) {
    const totalCount = window.rawInquiryData ? window.rawInquiryData.length : 0;
    const matchedCount = inquiries.length;
    const matchRate = totalCount > 0 ? ((matchedCount / totalCount) * 100).toFixed(1) : 0;
    
    console.log(`📊 매칭 통계:`);
    console.log(`  - 전체 문의: ${totalCount}건`);
    console.log(`  - 매칭된 문의: ${matchedCount}건`);
    console.log(`  - 매칭률: ${matchRate}%`);
    
    return {
        totalCount,
        matchedCount,
        matchRate: parseFloat(matchRate)
    };
}

// ─────────── 매칭 품질 검증 ───────────
function validateMatchingQuality(inquiries, categoryName) {
    if (inquiries.length === 0) {
        console.warn(`⚠️ "${categoryName}"에 대한 매칭 결과가 없습니다.`);
        return false;
    }
    
    // 카테고리 일치도 검증
    const categoryMatches = inquiries.filter(inquiry => {
        const subCat = inquiry.category?.sub_category || inquiry.sub_category || '';
        return subCat.toLowerCase().includes(categoryName.toLowerCase());
    });
    
    const matchQuality = (categoryMatches.length / inquiries.length) * 100;
    console.log(`🎯 매칭 품질: ${matchQuality.toFixed(1)}% (${categoryMatches.length}/${inquiries.length})`);
    
    if (matchQuality < 80) {
        console.warn(`⚠️ 매칭 품질이 낮습니다: ${matchQuality.toFixed(1)}%`);
    }
    
    return matchQuality >= 50; // 50% 이상이면 유효한 매칭으로 간주
}

// ─────────── 디버깅 함수 ───────────
window.debugCategoryMatching = function(categoryName) {
    console.log(`🔍 카테고리 매칭 디버깅: "${categoryName}"`);
    
    if (!window.rawInquiryData || window.rawInquiryData.length === 0) {
        console.error('❌ 원본 데이터가 없습니다.');
        return;
    }
    
    const matchedInquiries = filterInquiriesByCategory(categoryName);
    const stats = calculateMatchingStats(matchedInquiries);
    const isValid = validateMatchingQuality(matchedInquiries, categoryName);
    
    console.log(`📋 디버깅 결과:`, {
        categoryName,
        ...stats,
        isValidMatch: isValid,
        sampleMatches: matchedInquiries.slice(0, 5).map(inq => ({
            id: inq.inquiry_id,
            category: inq.category?.sub_category || inq.sub_category,
            team: inq.category?.assigned_team || inq.assigned_team
        }))
    });
    
    return {
        matchedInquiries,
        stats,
        isValid
    };
};

console.log('✅ 데이터 매칭 시스템 로딩 완료');
"""