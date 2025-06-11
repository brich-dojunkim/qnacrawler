# html_reporter/utils/processors/overview.py (아이디어 2 적용)
"""개요 데이터 처리 - 팀별 아코디언 통합"""

from typing import Dict
from datetime import datetime

from ..calculations import calculate_answer_rate, calculate_urgent_rate
from ..html_generators import HTMLGenerator, generate_sub_categories_html

def process_overview_data(results: Dict) -> Dict:
    """개요 데이터 처리 - 팀별 아코디언 포함"""
    overall_summary = results.get('overall_summary', {})
    
    # 기본 데이터
    total_inquiries = overall_summary.get('total_inquiries', 0)
    urgent_count = overall_summary.get('urgent_count', 0)
    
    # 답변 완료/대기 계산
    answered_count = 0
    if 'team_analysis' in results:
        for team_data in results['team_analysis'].values():
            answered_count += team_data['basic_info'].get('answered_count', 0)
    
    pending_count = total_inquiries - answered_count
    
    # 비율 계산
    urgent_rate = calculate_urgent_rate(urgent_count, total_inquiries)
    answer_rate = calculate_answer_rate(answered_count, total_inquiries)
    pending_rate = calculate_urgent_rate(pending_count, total_inquiries)
    
    overview_data = {
        'total_inquiries': total_inquiries,
        'urgent_count': urgent_count,
        'answered_count': answered_count,
        'pending_count': pending_count,
        'urgent_rate': urgent_rate,
        'answer_rate': answer_rate,
        'pending_rate': pending_rate,
        'analysis_date': results.get('analysis_timestamp', datetime.now().isoformat())[:19].replace('T', ' ')
    }
    
    # 팀별 아코디언 아이템들 생성
    team_accordion_items = generate_team_accordion_items(results)
    overview_data['team_accordion_items'] = team_accordion_items
    
    # 여정별 아코디언 아이템들 생성
    journey_accordion_items = generate_journey_accordion_items(results)
    overview_data['journey_accordion_items'] = journey_accordion_items
    
    return overview_data

def generate_team_accordion_items(results: Dict) -> str:
    """팀별 아코디언 아이템들 생성"""
    if 'team_analysis' not in results:
        return ""
    
    team_data = results['team_analysis']
    if not team_data:
        return ""
    
    # 팀별 데이터를 문의량 순으로 정렬
    sorted_teams = sorted(team_data.items(), 
                         key=lambda x: x[1]['basic_info']['total_inquiries'], 
                         reverse=True)
    
    total_inquiries_check = sum(team_data[team]['basic_info']['total_inquiries'] for team in team_data.keys())
    
    accordion_html = ""
    
    for team_name, team_info in sorted_teams:
        basic_info = team_info['basic_info']
        count = basic_info['total_inquiries']
        percentage = round((count / total_inquiries_check * 100), 1) if total_inquiries_check > 0 else 0
        
        # 최대값 대비 진행률 계산
        max_count = sorted_teams[0][1]['basic_info']['total_inquiries'] if sorted_teams else 1
        progress_width = (count / max_count * 100) if max_count > 0 else 0
        
        # 답변률 계산
        team_answer_rate = calculate_answer_rate(basic_info.get('answered_count', 0), basic_info['total_inquiries'])
        
        # 세부 카테고리 HTML 생성
        sub_categories_html = ""
        if team_info.get('sub_categories'):
            sub_categories_html = generate_sub_categories_html(team_info['sub_categories'])
        
        # 안전한 팀명 ID 생성
        safe_team_id = team_name.replace(' ', '').replace('팀', '').replace('·', '')
        
        accordion_html += f'''
        <div class="team-accordion-item">
            <div class="team-accordion-header" onclick="toggleTeamAccordion('{safe_team_id}')">
                <div class="team-summary-info">
                    <span class="team-name">{team_name}</span>
                    <span class="team-count">({count:,}건)</span>
                </div>
                <div class="team-progress-container">
                    <div class="team-progress-bar">
                        <div class="team-progress-fill" style="width: {progress_width}%"></div>
                    </div>
                    <span class="team-percentage">{percentage}%</span>
                </div>
                <button class="accordion-toggle-btn" id="btn-{safe_team_id}">
                    <span class="toggle-icon">▼</span>
                </button>
            </div>
            <div class="team-accordion-content" id="content-{safe_team_id}" style="display: none;">
                <div class="team-detail-box">
                    <div class="team-metrics-grid">
                        <div class="metric-item">
                            <span class="metric-label">총 문의</span>
                            <span class="metric-value">{basic_info['total_inquiries']:,}건</span>
                        </div>
                        <div class="metric-item">
                            <span class="metric-label">긴급 문의</span>
                            <span class="metric-value">{basic_info['urgent_count']:,}건</span>
                        </div>
                        <div class="metric-item">
                            <span class="metric-label">답변 완료</span>
                            <span class="metric-value">{basic_info.get('answered_count', 0):,}건</span>
                        </div>
                        <div class="metric-item">
                            <span class="metric-label">답변률</span>
                            <span class="metric-value">{team_answer_rate}%</span>
                        </div>
                        <div class="metric-item">
                            <span class="metric-label">평균 길이</span>
                            <span class="metric-value">{round(basic_info['avg_content_length'])}자</span>
                        </div>
                    </div>
                    {sub_categories_html}
                </div>
            </div>
        </div>'''
    
    return accordion_html

def generate_journey_accordion_items(results: Dict) -> str:
    """여정별 아코디언 아이템들 생성"""
    if 'journey_analysis' not in results:
        return ""
    
    journey_data = results['journey_analysis']
    if not journey_data:
        return ""
    
    # 여정별 데이터를 문의량 순으로 정렬 (문의가 있는 것만)
    sorted_journeys = sorted(journey_data.items(), 
                           key=lambda x: x[1]['basic_info']['total_inquiries'], 
                           reverse=True)
    
    # 문의가 있는 여정만 필터링
    filtered_journeys = [(name, data) for name, data in sorted_journeys 
                        if data['basic_info']['total_inquiries'] > 0]
    
    total_inquiries_check = sum(data['basic_info']['total_inquiries'] for _, data in filtered_journeys)
    
    accordion_html = ""
    
    for journey_name, journey_info in filtered_journeys:
        basic_info = journey_info['basic_info']
        count = basic_info['total_inquiries']
        percentage = round((count / total_inquiries_check * 100), 1) if total_inquiries_check > 0 else 0
        
        # 최대값 대비 진행률 계산
        max_count = filtered_journeys[0][1]['basic_info']['total_inquiries'] if filtered_journeys else 1
        progress_width = (count / max_count * 100) if max_count > 0 else 0
        
        # 답변률 계산
        journey_answer_rate = calculate_answer_rate(basic_info.get('answered_count', 0), basic_info['total_inquiries'])
        
        # 세부 카테고리 HTML 생성
        sub_categories_html = ""
        if journey_info.get('sub_categories'):
            sub_categories_html = generate_sub_categories_html(journey_info['sub_categories'])
        
        # 안전한 여정명 ID 생성
        safe_journey_id = journey_name.replace('·', '').replace(' ', '').replace('/', '')
        
        accordion_html += f'''
        <div class="journey-accordion-item">
            <div class="journey-accordion-header" onclick="toggleJourneyAccordion('{safe_journey_id}')">
                <div class="journey-summary-info">
                    <span class="journey-name">{journey_name}</span>
                    <span class="journey-count">({count:,}건)</span>
                </div>
                <div class="journey-progress-container">
                    <div class="journey-progress-bar">
                        <div class="journey-progress-fill" style="width: {progress_width}%"></div>
                    </div>
                    <span class="journey-percentage">{percentage}%</span>
                </div>
                <button class="accordion-toggle-btn" id="journey-btn-{safe_journey_id}">
                    <span class="toggle-icon">▼</span>
                </button>
            </div>
            <div class="journey-accordion-content" id="journey-content-{safe_journey_id}" style="display: none;">
                <div class="journey-detail-box">
                    <div class="journey-metrics-grid">
                        <div class="metric-item">
                            <span class="metric-label">총 문의</span>
                            <span class="metric-value">{basic_info['total_inquiries']:,}건</span>
                        </div>
                        <div class="metric-item">
                            <span class="metric-label">긴급 문의</span>
                            <span class="metric-value">{basic_info['urgent_count']:,}건</span>
                        </div>
                        <div class="metric-item">
                            <span class="metric-label">답변 완료</span>
                            <span class="metric-value">{basic_info.get('answered_count', 0):,}건</span>
                        </div>
                        <div class="metric-item">
                            <span class="metric-label">답변률</span>
                            <span class="metric-value">{journey_answer_rate}%</span>
                        </div>
                        <div class="metric-item">
                            <span class="metric-label">평균 길이</span>
                            <span class="metric-value">{round(basic_info['avg_content_length'])}자</span>
                        </div>
                    </div>
                    {sub_categories_html}
                </div>
            </div>
        </div>'''
    
    return accordion_html