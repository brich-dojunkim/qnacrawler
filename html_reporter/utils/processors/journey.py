# html_reporter/utils/processors/journey.py
"""유저 여정별 데이터 처리"""

from typing import Dict, List

from ..calculations import calculate_answer_rate
from ..mappings import JOURNEY_ORDER

def process_journey_data(results: Dict) -> List[Dict]:
    """유저 여정별 데이터 처리"""
    if 'journey_analysis' not in results:
        return []
    
    journey_cards = []
    
    # 순서대로 정렬
    sorted_journeys = []
    for journey in JOURNEY_ORDER:
        if journey in results['journey_analysis']:
            sorted_journeys.append((journey, results['journey_analysis'][journey]))
    
    for journey_name, journey_info in sorted_journeys:
        basic_info = journey_info['basic_info']
        
        # 문의가 없는 여정은 제외
        if basic_info['total_inquiries'] == 0:
            continue
        
        # 답변률 계산
        answer_rate = calculate_answer_rate(basic_info.get('answered_count', 0), basic_info['total_inquiries'])
        
        journey_cards.append({
            'name': journey_name,
            'total_inquiries': basic_info['total_inquiries'],
            'urgent_count': basic_info['urgent_count'],
            'answered_count': basic_info['answered_count'],
            'answer_rate': answer_rate,
            'avg_content_length': round(basic_info['avg_content_length']),
            'sub_categories': journey_info.get('sub_categories', {})
        })
    
    return journey_cards