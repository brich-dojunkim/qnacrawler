# html_reporter/utils/html_generators.py (완료율 칼럼 추가 + 아코디언 세부카테고리 버튼 수정)
"""HTML 문자열 생성 함수들 - 완료율 칼럼 포함 + 세부카테고리 드로어 연동"""

from typing import Dict, List
from .formatters import format_number
from .mappings import get_journey_for_category
from .calculations import calculate_urgent_rate, calculate_answer_rate

class HTMLGenerator:
    """HTML 생성 클래스"""
    
    @staticmethod
    def generate_team_options(results: Dict) -> str:
        """팀 옵션 HTML 생성"""
        if 'team_analysis' not in results:
            return ""
        
        teams = list(results['team_analysis'].keys())
        teams = [team for team in teams if team != '기타']
        teams.sort()
        
        team_options_html = ""
        for team in teams:
            team_options_html += f'<option value="team-{team}">{team}</option>\n                        '
        
        return team_options_html.rstrip()
    
    @staticmethod
    def generate_sub_categories_html(sub_categories: Dict, results: Dict = None, max_items: int = 10) -> str:
        """세부 카테고리 테이블 형태 HTML 생성 - 문의율 칼럼 포함 + 드로어 연동"""
        if not sub_categories:
            return ""
        
        # 카테고리 분석 데이터 가져오기
        category_analysis = results.get('category_analysis', {}) if results else {}
        
        # 전체 문의 수 계산 (비율 계산용)
        total_inquiries_for_percentage = 0
        if results and 'overall_summary' in results:
            total_inquiries_for_percentage = results['overall_summary'].get('total_inquiries', 1)
        else:
            # 전체 문의 수를 구할 수 없으면 현재 세부 카테고리들의 합으로 계산
            total_inquiries_for_percentage = sum(sub_categories.values())
        
        html = '''<div class="sub-categories-table">
            <h5 class="sub-categories-title">📂 세부 카테고리 상세</h5>
            <div class="sub-categories-table-container">
                <div class="sub-categories-table-header">
                    <div class="sub-cat-column">카테고리명</div>
                    <div class="sub-cat-column">담당팀</div>
                    <div class="sub-cat-column">유저여정</div>
                    <div class="sub-cat-column">문의율</div>
                    <div class="sub-cat-column">긴급률</div>
                    <div class="sub-cat-column">완료율</div>
                    <div class="sub-cat-column">상세보기</div>
                </div>
                <div class="sub-categories-table-body">'''
        
        # 문의량 순으로 정렬
        sorted_categories = sorted(sub_categories.items(), key=lambda x: x[1], reverse=True)
        
        for category_name, count in sorted_categories[:max_items]:
            # 카테고리별 상세 정보 가져오기
            category_info = category_analysis.get(category_name, {})
            basic_info = category_info.get('basic_info', {})
            
            # 담당팀 추출 (가장 많은 문의를 처리하는 팀)
            team_distribution = category_info.get('team_distribution', {})
            main_team = list(team_distribution.keys())[0] if team_distribution else '미분류'
            
            # 유저여정 매핑
            main_journey = get_journey_for_category(category_name)
            
            # 문의율 계산 (전체 대비 비율)
            inquiry_rate = round((count / total_inquiries_for_percentage * 100), 1) if total_inquiries_for_percentage > 0 else 0
            
            # 긴급률 계산
            urgent_count = basic_info.get('urgent_count', 0)
            urgent_rate = calculate_urgent_rate(urgent_count, count)
            
            # 완료율 계산 (추정치)
            answered_count = basic_info.get('answered_count', 0)
            if not answered_count and results and 'team_analysis' in results:
                # 팀별 평균 완료율로 추정
                team_data = results['team_analysis'].get(main_team, {})
                team_basic_info = team_data.get('basic_info', {})
                team_answer_rate = calculate_answer_rate(
                    team_basic_info.get('answered_count', 0),
                    team_basic_info.get('total_inquiries', 1)
                )
                answered_count = int(count * (team_answer_rate / 100))
            
            answer_rate = calculate_answer_rate(answered_count, count)
            
            # 긴급률 레벨 계산
            if urgent_rate >= 20:
                urgent_level = 'high'
            elif urgent_rate >= 10:
                urgent_level = 'medium'
            else:
                urgent_level = 'low'
            
            # 완료율 레벨 계산
            if answer_rate >= 80:
                complete_level = 'high'
            elif answer_rate >= 50:
                complete_level = 'medium'
            else:
                complete_level = 'low'
            
            # JavaScript에서 안전하게 사용할 수 있도록 카테고리명 이스케이프
            safe_category_name = category_name.replace("'", "\\'").replace('"', '\\"')
            
            html += f'''
                    <div class="sub-category-row" 
                         data-category="{category_name}"
                         data-team="{main_team}" 
                         data-journey="{main_journey}" 
                         data-inquiries="{count}" 
                         data-urgent="{urgent_rate}"
                         data-complete="{answer_rate}">
                        <div class="sub-cat-cell category-name">{category_name}</div>
                        <div class="sub-cat-cell"><span class="team-badge">{main_team}</span></div>
                        <div class="sub-cat-cell"><span class="journey-badge">{main_journey}</span></div>
                        <div class="sub-cat-cell metric-value">{inquiry_rate}%</div>
                        <div class="sub-cat-cell urgent-rate {urgent_level}">{urgent_rate}%</div>
                        <div class="sub-cat-cell complete-rate {complete_level}">{answer_rate}%</div>
                        <div class="sub-cat-cell">
                            <button class="sub-cat-action-btn" onclick="openSubCategoryDrawer('{safe_category_name}')" title="상세 문의 보기">
                                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                                    <circle cx="11" cy="11" r="8"></circle>
                                    <path d="m21 21-4.35-4.35"></path>
                                </svg>
                            </button>
                        </div>
                    </div>'''
        
        # 남은 카테고리들이 있으면 요약 표시
        if len(sorted_categories) > max_items:
            remaining_count = len(sorted_categories) - max_items
            remaining_total = sum(count for _, count in sorted_categories[max_items:])
            remaining_percentage = round((remaining_total / total_inquiries_for_percentage * 100), 1) if total_inquiries_for_percentage > 0 else 0
            
            html += f'''
                    <div class="sub-category-summary">
                        기타 {remaining_count}개 카테고리 (총 {remaining_percentage}%)
                    </div>'''
        
        html += '''
                </div>
            </div>
        </div>'''
        
        return html
    
    @staticmethod
    def generate_rank_tables(results: Dict) -> str:
        """순위표 생성 - 나머지 팀들 한 줄에 표시"""
        rank_tables = ""
        
        # 팀별 분포 순위표
        if 'team_analysis' in results:
            team_data = results['team_analysis']
            if team_data:
                sorted_teams = sorted(team_data.items(), 
                                    key=lambda x: x[1]['basic_info']['total_inquiries'], 
                                    reverse=True)
                
                total_inquiries_check = sum(team_data[team]['basic_info']['total_inquiries'] for team in team_data.keys())
                
                team_table_html = '''
                <div class="distribution-card">
                    <h4 class="distribution-card-title">🏢 팀별 워크로드</h4>'''
                
                # 상위 4개 팀은 개별 표시
                for idx, (team_name, team_info) in enumerate(sorted_teams[:4], 1):
                    count = team_info['basic_info']['total_inquiries']
                    percentage = round((count / total_inquiries_check * 100), 1) if total_inquiries_check > 0 else 0
                    
                    # 최대값 대비 진행률 계산
                    max_count = sorted_teams[0][1]['basic_info']['total_inquiries'] if sorted_teams else 1
                    progress_width = (count / max_count * 100) if max_count > 0 else 0
                    
                    team_table_html += f'''
                    <div class="simple-rank-item" style="--progress-width: {progress_width}%;">
                        <div class="simple-rank-number">{idx}</div>
                        <div class="simple-rank-content">
                            <div class="simple-rank-name">{team_name}</div>
                            <div class="simple-rank-details">
                                <span class="simple-rank-count">{count:,}건</span>
                                <span class="simple-rank-percentage">({percentage}%)</span>
                            </div>
                        </div>
                    </div>'''
                
                # 5위부터는 한 줄에 표시
                if len(sorted_teams) > 4:
                    remaining_teams = sorted_teams[4:]
                    remaining_teams_html = []
                    
                    for idx, (team_name, team_info) in enumerate(remaining_teams, 5):
                        count = team_info['basic_info']['total_inquiries']
                        percentage = round((count / total_inquiries_check * 100), 1) if total_inquiries_check > 0 else 0
                        remaining_teams_html.append(f"{team_name} ({count}건, {percentage}%)")
                    
                    team_table_html += f'''
                    <div class="simple-rank-item">
                        <div class="simple-rank-number">5+</div>
                        <div class="simple-rank-content">
                            <div class="simple-rank-name">기타 {len(remaining_teams)}개 팀</div>
                            <div class="simple-rank-details">
                                <div class="remaining-teams-detail">{' • '.join(remaining_teams_html)}</div>
                            </div>
                        </div>
                    </div>'''
                
                # 요약 정보 추가
                team_table_html += f'''
                    <div class="rank-summary">
                        전체 {len(team_data)}개 팀 | 총 {total_inquiries_check:,}건
                    </div>
                </div>'''
                
                rank_tables += team_table_html
        
        # 유저 여정별 분포 순위표
        if 'journey_analysis' in results:
            journey_data = results['journey_analysis']
            if journey_data:
                sorted_journeys = sorted(journey_data.items(), 
                                       key=lambda x: x[1]['basic_info']['total_inquiries'], 
                                       reverse=True)
                
                # 문의가 있는 여정만 필터링
                filtered_journeys = [(name, data) for name, data in sorted_journeys 
                                   if data['basic_info']['total_inquiries'] > 0]
                
                total_inquiries_check = sum(data['basic_info']['total_inquiries'] for _, data in filtered_journeys)
                
                journey_table_html = '''
                <div class="distribution-card">
                    <h4 class="distribution-card-title">🎯 고객 여정별 분포</h4>'''
                
                for idx, (journey_name, journey_info) in enumerate(filtered_journeys, 1):
                    count = journey_info['basic_info']['total_inquiries']
                    percentage = round((count / total_inquiries_check * 100), 1) if total_inquiries_check > 0 else 0
                    
                    # 최대값 대비 진행률 계산
                    max_count = filtered_journeys[0][1]['basic_info']['total_inquiries'] if filtered_journeys else 1
                    progress_width = (count / max_count * 100) if max_count > 0 else 0
                    
                    journey_table_html += f'''
                    <div class="simple-rank-item" style="--progress-width: {progress_width}%;">
                        <div class="simple-rank-number">{idx}</div>
                        <div class="simple-rank-content">
                            <div class="simple-rank-name">{journey_name}</div>
                            <div class="simple-rank-details">
                                <span class="simple-rank-count">{count:,}건</span>
                                <span class="simple-rank-percentage">({percentage}%)</span>
                            </div>
                        </div>
                    </div>'''
                
                # 요약 정보 추가
                journey_table_html += f'''
                    <div class="rank-summary">
                        총 {len(filtered_journeys)}개 여정 단계 | 총 {total_inquiries_check:,}건
                    </div>
                </div>'''
                
                rank_tables += journey_table_html
        
        return rank_tables

# 하위 호환성을 위한 함수들
def generate_team_options(results: Dict) -> str:
    """하위 호환성을 위한 래퍼 함수"""
    return HTMLGenerator.generate_team_options(results)

def generate_rank_tables(results: Dict) -> str:
    """하위 호환성을 위한 래퍼 함수"""
    return HTMLGenerator.generate_rank_tables(results)

def generate_sub_categories_html(sub_categories: Dict, results: Dict = None, max_items: int = 10) -> str:
    """하위 호환성을 위한 래퍼 함수 - results 파라미터 추가"""
    return HTMLGenerator.generate_sub_categories_html(sub_categories, results, max_items)