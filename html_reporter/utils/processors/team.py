# html_reporter/utils/processors/team.py
"""팀별 데이터 처리"""

from typing import Dict, List

from ..calculations import calculate_answer_rate

def process_team_data(results: Dict) -> List[Dict]:
    """팀별 데이터 처리"""
    if 'team_analysis' not in results:
        return []
    
    team_cards = []
    for team_name, team_info in results['team_analysis'].items():
        basic_info = team_info['basic_info']
        
        # 답변률 계산
        answer_rate = calculate_answer_rate(basic_info.get('answered_count', 0), basic_info['total_inquiries'])
        
        team_cards.append({
            'name': team_name,
            'total_inquiries': basic_info['total_inquiries'],
            'urgent_count': basic_info['urgent_count'],
            'answered_count': basic_info['answered_count'],
            'answer_rate': answer_rate,
            'avg_content_length': round(basic_info['avg_content_length']),
            'sub_categories': team_info.get('sub_categories', {})
        })
    
    # 문의량 순으로 정렬
    team_cards.sort(key=lambda x: x['total_inquiries'], reverse=True)
    return team_cards