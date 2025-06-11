# html_reporter/utils/processors/category.py
"""카테고리별 데이터 처리"""

from typing import Dict, List

from ..calculations import calculate_answer_rate, calculate_urgent_rate
from ..mappings import get_journey_for_category

def process_category_data(results: Dict) -> List[Dict]:
    """카테고리별 데이터 처리 - 답변률 데이터 포함"""
    if 'category_analysis' not in results:
        return []
    
    category_cards = []
    sorted_categories = sorted(results['category_analysis'].items(), 
                             key=lambda x: x[1]['basic_info']['total_inquiries'], 
                             reverse=True)
    
    for category_name, category_info in sorted_categories:
        basic_info = category_info['basic_info']
        
        # 긴급률 계산
        urgent_rate = calculate_urgent_rate(basic_info['urgent_count'], basic_info['total_inquiries'])
        
        # 답변률 계산 (추정)
        answered_count = 0
        if 'team_analysis' in results:
            for team_data in results['team_analysis'].values():
                if category_name in team_data.get('sub_categories', {}):
                    team_answer_rate = calculate_answer_rate(
                        team_data['basic_info'].get('answered_count', 0),
                        team_data['basic_info']['total_inquiries']
                    )
                    category_inquiries = team_data['sub_categories'][category_name]
                    answered_count += int(category_inquiries * (team_answer_rate / 100))
        
        answer_rate = calculate_answer_rate(answered_count, basic_info['total_inquiries'])
        
        # 담당팀 배지 생성
        team_badges_html = ""
        if category_info.get('team_distribution'):
            for team, count in list(category_info['team_distribution'].items())[:3]:
                team_badges_html += f'<span class="team-badge">{team}</span>'
        
        main_team = list(category_info.get('team_distribution', {}).keys())[0] if category_info.get('team_distribution') else '기타'
        main_journey = get_journey_for_category(category_name)
        
        # 모달 ID 생성 (안전한 ID)
        safe_id = category_name.replace(' ', '-').replace('/', '-').replace('(', '').replace(')', '').replace('·', '-').replace('&', 'and')
        modal_id = f"modal-{safe_id}"
        
        # 모달 콘텐츠 생성
        modal_content = ""
        if category_info.get('sample_inquiries'):
            for sample in category_info['sample_inquiries']:
                urgency_class = "urgency-urgent" if sample.get('is_urgent', False) else "urgency-normal"
                urgency_text = "긴급" if sample.get('is_urgent', False) else "일반"
                
                # 문의 내용 안전하게 처리
                content = sample.get('content', '') or sample.get('question_content', '') or sample.get('question_preview', '')
                if len(content) > 300:
                    content = content[:300] + '...'
                
                modal_content += f'''
                <div class="inquiry-card">
                    <div class="inquiry-header">
                        <span>{sample.get('assigned_team', 'N/A')}</span>
                        <span class="urgency-badge {urgency_class}">{urgency_text}</span>
                    </div>
                    <div class="inquiry-content">{content}</div>
                </div>'''
        
        if not modal_content:
            modal_content = '<div class="inquiry-card"><div class="inquiry-content">문의 내용 샘플이 없습니다.</div></div>'
        
        category_cards.append({
            'name': category_name,
            'total_inquiries': basic_info['total_inquiries'],
            'urgent_count': basic_info['urgent_count'],
            'urgent_rate': urgent_rate,
            'answer_rate': answer_rate,
            'avg_content_length': round(basic_info['avg_content_length']),
            'main_team': main_team,
            'main_journey': main_journey,
            'team_badges': team_badges_html,
            'modal_id': modal_id,
            'modal_content': modal_content
        })
    
    return category_cards