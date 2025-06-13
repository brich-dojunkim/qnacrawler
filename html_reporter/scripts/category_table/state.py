"""
카테고리 테이블 상태 관리 - 내보내기 기능 포함
"""

def get_state_scripts():
    """상태 관리 관련 스크립트 - 내보내기 기능 포함"""
    return """
// ─────────── 테이블 필터 상태 ───────────
let tableFilters = {
    team: '',
    journey: '',
    sort: '',
    sortOrder: ''
};

// ─────────── 필터 적용 메인 함수 (카테고리 검색 제거) ───────────
function applyTableFilters() {
    const rows = Array.from(document.querySelectorAll('.category-table-row'));
    let visibleCount = 0;

    // 필터링
    rows.forEach(row => {
        let show = true;

        // 팀 필터
        if (tableFilters.team) {
            const team = row.dataset.team;
            if (team !== tableFilters.team) {
                show = false;
            }
        }

        // 여정 필터
        if (tableFilters.journey) {
            const journey = row.dataset.journey;
            if (journey !== tableFilters.journey) {
                show = false;
            }
        }

        if (show) {
            row.classList.remove('hidden');
            visibleCount++;
        } else {
            row.classList.add('hidden');
        }
    });

    // 정렬
    if (tableFilters.sort) {
        sortTableRows(rows);
    }

    updateTableFilterStatus(visibleCount, rows.length);
}

// ─────────── 상태 업데이트 (카테고리 검색 제거) ───────────
function updateTableFilterStatus(visible, total) {
    const statusElement = document.getElementById('table-filter-status');
    const countElement = document.getElementById('visible-categories-count');
    const clearBtn = document.querySelector('.clear-table-filters');
    
    if (countElement) {
        countElement.textContent = visible;
    }
    
    let statusText = '';
    let filterDescription = '';
    
    // 적용된 필터들 수집 (카테고리 검색 제외)
    const activeFilters = [];
    if (tableFilters.team) {
        activeFilters.push(`팀: ${tableFilters.team}`);
    }
    if (tableFilters.journey) {
        activeFilters.push(`여정: ${tableFilters.journey}`);
    }
    
    if (activeFilters.length > 0) {
        filterDescription = activeFilters.join(' | ');
        statusText = `📂 <strong>필터 적용</strong>: ${filterDescription} (${total}개 중 ${visible}개 표시)`;
        if (clearBtn) clearBtn.style.display = 'inline';
    } else {
        statusText = `📂 <strong>전체 카테고리</strong> 표시 중 (${visible}개)`;
        if (clearBtn) clearBtn.style.display = 'none';
    }
    
    if (statusElement) {
        statusElement.innerHTML = statusText + (clearBtn && clearBtn.style.display === 'inline' ? clearBtn.outerHTML : '');
    }
}

// ─────────── 개선된 내보내기 기능 (컨펌 팝업 포함) ───────────
function exportTableData() {
    console.log('📊 카테고리 테이블 데이터 내보내기 요청');
    
    try {
        // 현재 보이는 행들만 수집
        const visibleRows = document.querySelectorAll('.category-table-row:not(.hidden)');
        
        if (visibleRows.length === 0) {
            alert('내보낼 데이터가 없습니다.');
            return;
        }
        
        // 현재 필터 정보 가져오기
        const filterInfo = getActiveFilterInfo();
        const filterText = filterInfo ? `\\n\\n현재 적용된 필터: ${filterInfo}` : '';
        
        // 컨펌 팝업으로 사용자 확인
        const confirmMessage = `📊 카테고리 데이터를 CSV 파일로 내보내시겠습니까?\\n\\n내보낼 데이터: ${visibleRows.length}개 카테고리${filterText}\\n\\n파일 형식: CSV (Excel에서 열 수 있음)`;
        
        if (!confirm(confirmMessage)) {
            console.log('사용자가 내보내기를 취소했습니다.');
            return;
        }
        
        // CSV 헤더 생성
        const headers = ['카테고리명', '담당팀', '유저여정', '문의수', '긴급률(%)', '완료율(%)', '등록일'];
        let csvContent = headers.join(',') + '\\n';
        
        // 데이터 행 생성
        visibleRows.forEach(row => {
            const categoryName = row.querySelector('.category-name').textContent.trim();
            const team = row.dataset.team || '';
            const journey = row.dataset.journey || '';
            const inquiries = row.dataset.inquiries || '0';
            const urgentRate = row.dataset.urgent || '0';
            const completeRate = row.dataset.complete || '0';
            const exportDate = new Date().toLocaleDateString('ko-KR');
            
            // CSV 행 생성 (쉼표가 포함된 데이터는 따옴표로 감쌈)
            const rowData = [
                `"${categoryName}"`,
                `"${team}"`,
                `"${journey}"`,
                inquiries,
                urgentRate,
                completeRate,
                `"${exportDate}"`
            ];
            
            csvContent += rowData.join(',') + '\\n';
        });
        
        // 파일 다운로드
        const timestamp = new Date().toISOString().slice(0, 19).replace(/[:-]/g, '');
        const filename = `category_analysis_${timestamp}.csv`;
        
        // Blob 생성 및 다운로드
        const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
        const link = document.createElement('a');
        
        if (link.download !== undefined) {
            const url = URL.createObjectURL(blob);
            link.setAttribute('href', url);
            link.setAttribute('download', filename);
            link.style.visibility = 'hidden';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
            
            console.log(`✅ ${visibleRows.length}개 카테고리 데이터 내보내기 완료: ${filename}`);
            
            // 성공 알림
            alert(`✅ 내보내기 완료!\\n\\n파일명: ${filename}\\n데이터: ${visibleRows.length}개 카테고리\\n\\n다운로드 폴더를 확인해주세요.`);
            
        } else {
            throw new Error('브라우저에서 파일 다운로드를 지원하지 않습니다.');
        }
        
    } catch (error) {
        console.error('❌ 내보내기 중 오류:', error);
        alert(`❌ 내보내기 중 오류가 발생했습니다:\\n\\n${error.message}\\n\\n다시 시도해주세요.`);
    }
}

// ─────────── 현재 필터 정보 가져오기 ───────────
function getActiveFilterInfo() {
    const activeFilters = [];
    
    if (tableFilters.team) {
        activeFilters.push(`팀: ${tableFilters.team}`);
    }
    if (tableFilters.journey) {
        activeFilters.push(`여정: ${tableFilters.journey}`);
    }
    if (tableFilters.sort) {
        const sortName = tableFilters.sort === 'inquiries' ? '문의수' : 
                        tableFilters.sort === 'urgent' ? '긴급률' : 
                        tableFilters.sort === 'complete' ? '완료율' : tableFilters.sort;
        const sortOrder = tableFilters.sortOrder === 'desc' ? '내림차순' : '오름차순';
        activeFilters.push(`정렬: ${sortName} ${sortOrder}`);
    }
    
    return activeFilters.length > 0 ? activeFilters.join(', ') : null;
}
"""