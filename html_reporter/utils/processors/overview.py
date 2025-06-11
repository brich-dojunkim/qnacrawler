# html_reporter/utils/processors/overview.py
"""개요 데이터 처리"""

from typing import Dict
from datetime import datetime

from ..calculations import calculate_answer_rate, calculate_urgent_rate
from ..html_generators import HTMLGenerator

def process_overview_data(results: Dict) -> Dict:
    """개요 데이터 처리 - 단순화된 버전"""
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
    
    # 순위표 생성
    rank_tables = HTMLGenerator.generate_rank_tables(results)
    overview_data['rank_tables'] = rank_tables
    
    return overview_data