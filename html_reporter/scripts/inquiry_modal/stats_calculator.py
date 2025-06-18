# html_reporter/scripts/inquiry_modal/stats_calculator.py
"""
문의 통계 계산 시스템 - 헤더 통계만 흰색 적용
"""

def get_stats_calculator_scripts():
    """통계 계산 시스템 스크립트 - 헤더 통계만 흰색 적용"""
    return """
// ─────────── 통계 계산 시스템 ───────────
console.log('📊 통계 계산 시스템 로딩 중...');

// ─────────── 메인 통계 계산 함수 ───────────
function calculateInquiryStats(inquiries) {
    if (!inquiries || inquiries.length === 0) {
        return { total: 0, urgent: 0, completed: 0, avgLength: 0 };
    }
    
    console.log(`📊 통계 계산 시작: ${inquiries.length}건`);
    
    const stats = {
        total: inquiries.length,
        urgent: 0,
        completed: 0,
        totalLength: 0,
        processedCount: 0
    };
    
    inquiries.forEach((inquiry, index) => {
        try {
            processInquiryForStats(inquiry, stats, index);
        } catch (error) {
            console.warn(`⚠️ 문의 ${inquiry.inquiry_id} 통계 계산 중 오류:`, error);
        }
    });
    
    const avgLength = stats.processedCount > 0 ? Math.round(stats.totalLength / stats.processedCount) : 0;
    
    const finalStats = {
        total: stats.total,
        urgent: stats.urgent,
        completed: stats.completed,
        avgLength
    };
    
    logCalculationResults(finalStats, inquiries.length);
    
    return finalStats;
}

// ─────────── 개별 문의 통계 처리 ───────────
function processInquiryForStats(inquiry, stats, index) {
    // 긴급 문의 카운트
    if (isUrgentInquiry(inquiry)) {
        stats.urgent++;
    }
    
    // 완료된 문의 카운트
    if (isCompletedInquiry(inquiry)) {
        stats.completed++;
    }
    
    // 문의 내용 길이 계산
    const contentLength = getContentLength(inquiry);
    stats.totalLength += contentLength;
    stats.processedCount++;
    
    // 디버깅용 로그 (첫 3개만)
    if (index < 3) {
        logInquiryStats(inquiry, contentLength);
    }
}

// ─────────── 긴급 문의 판별 ───────────
function isUrgentInquiry(inquiry) {
    return inquiry.is_urgent === true || 
           inquiry.is_urgent === 'true' || 
           inquiry.is_urgent === 1;
}

// ─────────── 완료된 문의 판별 ───────────
function isCompletedInquiry(inquiry) {
    // 1순위: answer_status 필드 확인
    if (inquiry.answer_status === '답변완료') {
        return true;
    }
    // 2순위: answers 배열 확인
    if (inquiry.answers && Array.isArray(inquiry.answers) && inquiry.answers.length > 0) {
        return true;
    }
    
    return false;
}

// ─────────── 문의 내용 길이 계산 ───────────
function getContentLength(inquiry) {
    const content = inquiry.question_content;
    return content ? content.length : 0;
}

// ─────────── 개별 문의 통계 로그 ───────────
function logInquiryStats(inquiry, contentLength) {
    console.log(`📋 문의 ${inquiry.inquiry_id}:`, {
        is_urgent: inquiry.is_urgent,
        answer_status: inquiry.answer_status,
        answers_count: inquiry.answers?.length || 0,
        content_length: contentLength,
        isCompleted: isCompletedInquiry(inquiry)
    });
}

// ─────────── 계산 결과 로그 ───────────
function logCalculationResults(finalStats, totalProcessed) {
    console.log(`📊 통계 계산 완료:`, {
        ...finalStats,
        urgentRate: `${((finalStats.urgent / finalStats.total) * 100).toFixed(1)}%`,
        completedRate: `${((finalStats.completed / finalStats.total) * 100).toFixed(1)}%`,
        totalProcessed
    });
}

// ─────────── 🔧 통계 업데이트 함수 수정 (헤더만 적용) ───────────
window.updateInquiryStats = function(total, urgent, completed, avgLength) {
    console.log('📊 통계 업데이트:', { total, urgent, completed, avgLength });
    
    // 🚨 중요: HTML 구조에 맞게 올바른 요소 업데이트
    const elements = {
        'total-inquiries-count': total,
        'urgent-inquiries-count': urgent, 
        'completed-inquiries-count': completed,
        'avg-length': avgLength
    };
    
    Object.entries(elements).forEach(([id, value]) => {
        const element = document.getElementById(id);
        if (element) {
            // 🔧 숫자 포맷팅 및 텍스트 업데이트
            const formattedValue = typeof value === 'number' ? value.toLocaleString() : value;
            element.textContent = formattedValue;
            
            console.log(`✅ 통계 업데이트: ${id} = ${formattedValue}`);
        } else {
            console.warn(`⚠️ 요소를 찾을 수 없습니다: ${id}`);
        }
    });
    
    // 🔧 헤더 통계 부분만 흰색으로 설정 (카드 푸터는 제외)
    setTimeout(() => {
        const headerStatValues = document.querySelectorAll('.inquiry-modal-header #total-inquiries-count, .inquiry-modal-header #urgent-inquiries-count, .inquiry-modal-header #completed-inquiries-count, .inquiry-modal-header #avg-length');
        headerStatValues.forEach(element => {
            element.style.setProperty('color', '#ffffff', 'important');
            element.style.fontWeight = '700';
        });
    }, 100);
};

// ─────────── 팀 필터 옵션 업데이트 ───────────
function updateTeamFilterOptions(inquiries) {
    const teamFilter = document.getElementById('team-filter');
    if (!teamFilter) {
        console.warn('⚠️ team-filter 요소를 찾을 수 없습니다.');
        return;
    }
    
    console.log(`👥 팀 필터 옵션 업데이트: ${inquiries.length}개 문의`);
    
    const teams = extractTeamsFromInquiries(inquiries);
    const sortedTeams = Array.from(teams).sort();
    
    generateTeamFilterHTML(teamFilter, sortedTeams);
    
    console.log(`👥 팀 필터 업데이트 완료: ${sortedTeams.length}개 팀`);
    console.log(`📋 발견된 팀 목록:`, sortedTeams);
}

// ─────────── 문의에서 팀 목록 추출 ───────────
function extractTeamsFromInquiries(inquiries) {
    const teams = new Set();
    
    inquiries.forEach((inquiry, index) => {
        try {
            const team = getTeamFromInquiry(inquiry);
            
            if (team && typeof team === 'string' && team.trim()) {
                teams.add(team.trim());
            } else {
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
            teams.add('미분류');
        }
    });
    
    return teams;
}

// ─────────── 개별 문의에서 팀 정보 추출 ───────────
function getTeamFromInquiry(inquiry) {
    let team = null;
    
    // category 객체에서 추출 (null 체크 추가)
    if (inquiry.category && inquiry.category.assigned_team && inquiry.category.assigned_team !== null) {
        team = inquiry.category.assigned_team;
    }
    // 직접 필드에서 추출
    else if (inquiry.assigned_team && inquiry.assigned_team !== null) {
        team = inquiry.assigned_team;
    }
    
    return team;
}

// ─────────── 팀 필터 HTML 생성 ───────────
function generateTeamFilterHTML(teamFilter, sortedTeams) {
    let optionsHtml = '<option value="">👥 모든 팀</option>';
    
    sortedTeams.forEach(team => {
        optionsHtml += `<option value="${team}">${team}</option>`;
    });
    
    teamFilter.innerHTML = optionsHtml;
}

// ─────────── 통계 비교 분석 ───────────
function compareStats(currentStats, previousStats = null) {
    if (!previousStats) {
        return currentStats;
    }
    
    const comparison = {
        ...currentStats,
        changes: {
            total: currentStats.total - previousStats.total,
            urgent: currentStats.urgent - previousStats.urgent,
            completed: currentStats.completed - previousStats.completed,
            avgLength: currentStats.avgLength - previousStats.avgLength
        }
    };
    
    console.log('📊 통계 비교 분석:', comparison);
    return comparison;
}

// ─────────── 통계 유효성 검증 ───────────
function validateStats(stats) {
    const errors = [];
    
    if (stats.total < 0) errors.push('총 문의 수가 음수입니다');
    if (stats.urgent < 0) errors.push('긴급 문의 수가 음수입니다');
    if (stats.completed < 0) errors.push('완료 문의 수가 음수입니다');
    if (stats.urgent > stats.total) errors.push('긴급 문의 수가 총 문의 수보다 큽니다');
    if (stats.completed > stats.total) errors.push('완료 문의 수가 총 문의 수보다 큽니다');
    if (stats.avgLength < 0) errors.push('평균 길이가 음수입니다');
    
    if (errors.length > 0) {
        console.error('❌ 통계 유효성 검증 실패:', errors);
        return false;
    }
    
    return true;
}

// ─────────── 통계 디버깅 함수 ───────────
window.debugInquiryStats = function(inquiries) {
    console.log('🔍 문의 통계 디버깅:');
    
    if (!inquiries || inquiries.length === 0) {
        console.log('❌ 문의 데이터가 없습니다.');
        return;
    }
    
    const stats = calculateInquiryStats(inquiries);
    const isValid = validateStats(stats);
    
    // 상세 분석
    const urgentInquiries = inquiries.filter(isUrgentInquiry);
    const completedInquiries = inquiries.filter(isCompletedInquiry);
    const teams = extractTeamsFromInquiries(inquiries);
    
    const debugInfo = {
        basicStats: stats,
        isValid,
        breakdown: {
            urgentSample: urgentInquiries.slice(0, 3).map(inq => ({
                id: inq.inquiry_id,
                is_urgent: inq.is_urgent,
                content_preview: (inq.question_content || '').substring(0, 50)
            })),
            completedSample: completedInquiries.slice(0, 3).map(inq => ({
                id: inq.inquiry_id,
                answer_status: inq.answer_status,
                answers_count: inq.answers?.length || 0
            })),
            teamDistribution: Object.fromEntries(
                Array.from(teams).map(team => [
                    team, 
                    inquiries.filter(inq => getTeamFromInquiry(inq) === team).length
                ])
            )
        }
    };
    
    console.log('📊 통계 디버깅 결과:', debugInfo);
    return debugInfo;
};

// ─────────── 성능 측정 ───────────
function measureStatsPerformance(inquiries) {
    const startTime = performance.now();
    const stats = calculateInquiryStats(inquiries);
    const endTime = performance.now();
    
    const duration = Math.round((endTime - startTime) * 100) / 100;
    console.log(`⏱️ 통계 계산 성능: ${inquiries.length}건 처리에 ${duration}ms 소요`);
    
    return { stats, duration };
}

console.log('✅ 통계 계산 시스템 로딩 완료');
"""