# html_reporter/utils/html_generators.py
"""HTML 문자열 생성 함수들"""

from typing import Dict, List
from .formatters import format_number

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
    def generate_sub_categories_html(sub_categories: Dict, max_items: int = 5) -> str:
        """세부 카테고리 HTML 생성"""
        if not sub_categories:
            return ""
        
        html = '<div class="simple-list"><h5 class="simple-list-title">세부 카테고리 분포</h5>'
        
        sorted_categories = sorted(sub_categories.items(), key=lambda x: x[1], reverse=True)
        
        for idx, (category, count) in enumerate(sorted_categories[:max_items], 1):
            html += f'''<div class="simple-item"><span class="simple-rank">{idx}</span><span class="simple-name">{category}</span><span class="simple-value">{count}건</span></div>'''
        
        html += '</div>'
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