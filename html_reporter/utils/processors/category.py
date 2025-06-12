# html_reporter/utils/processors/category.py
"""카테고리별 데이터 처리 - 모달 정보 포함"""

from typing import Dict, List

from ..calculations import calculate_answer_rate, calculate_urgent_rate
from ..mappings import get_journey_for_category

def process_category_data(results: Dict) -> List[Dict]:
    """카테고리별 데이터 처리 - 답변률 데이터 및 모달 정보 포함"""
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
        
        # 안전한 ID 생성
        safe_id = category_name.replace(' ', '-').replace('/', '-').replace('(', '').replace(')', '').replace('·', '-').replace('&', 'and')
        modal_id = f"modal-{safe_id}"
        
        # 향상된 모달 콘텐츠 생성
        modal_content = generate_enhanced_modal_content(category_name, category_info, main_team, main_journey, urgent_rate)
        
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

def generate_enhanced_modal_content(category_name: str, category_info: Dict, main_team: str, main_journey: str, urgent_rate: float) -> str:
    """향상된 모달 콘텐츠 생성"""
    basic_info = category_info.get('basic_info', {})
    total_inquiries = basic_info.get('total_inquiries', 0)
    
    # 팀별 분포 정보
    team_distribution_html = ""
    if category_info.get('team_distribution'):
        team_distribution_html = '<div style="margin-top: 16px;"><h6 style="margin: 0 0 8px 0; color: #374151;">👥 팀별 분포</h6>'
        for team, count in category_info['team_distribution'].items():
            percentage = round((count / total_inquiries * 100), 1) if total_inquiries > 0 else 0
            team_distribution_html += f'<div style="display: flex; justify-content: space-between; padding: 4px 0; border-bottom: 1px solid #f3f4f6;"><span>{team}</span><span>{count}건 ({percentage}%)</span></div>'
        team_distribution_html += '</div>'
    
    # 샘플 문의 생성
    sample_inquiries_html = ""
    if category_info.get('sample_inquiries'):
        sample_inquiries_html = '<div style="margin-top: 16px;"><h6 style="margin: 0 0 8px 0; color: #374151;">📝 샘플 문의</h6>'
        
        for idx, sample in enumerate(category_info['sample_inquiries'][:3], 1):
            urgency_class = "urgent" if sample.get('is_urgent', False) else "normal"
            urgency_color = "#ef4444" if sample.get('is_urgent', False) else "#667eea"
            urgency_text = "🚨 긴급" if sample.get('is_urgent', False) else "📋 일반"
            
            # 문의 내용 안전하게 처리
            content = sample.get('content', '') or sample.get('question_content', '') or sample.get('question_preview', '')
            if len(content) > 200:
                content = content[:200] + '...'
            
            sample_inquiries_html += f'''
            <div style="background: white; padding: 12px; border-radius: 6px; border-left: 4px solid {urgency_color}; margin-bottom: 8px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <span style="font-size: 0.8rem; color: #6b7280;">[샘플 {idx}] {sample.get('assigned_team', main_team)}</span>
                    <span style="font-size: 0.75rem; color: {urgency_color}; font-weight: 600;">{urgency_text}</span>
                </div>
                <div style="color: #374151; line-height: 1.4; font-size: 0.9rem;">{content}</div>
                <div style="margin-top: 6px; font-size: 0.75rem; color: #9ca3af;">
                    길이: {sample.get('length', 0)}자 | ID: {sample.get('inquiry_id', 'N/A')}
                </div>
            </div>'''
        sample_inquiries_html += '</div>'
    else:
        # 샘플 데이터가 없는 경우 기본 메시지
        sample_inquiries_html = '''
        <div style="margin-top: 16px;">
            <h6 style="margin: 0 0 8px 0; color: #374151;">📝 샘플 문의</h6>
            <div style="background: #f8fafc; padding: 16px; border-radius: 6px; text-align: center; color: #6b7280;">
                현재 이 카테고리의 샘플 문의 데이터가 없습니다.
            </div>
        </div>'''
    
    # 통계 요약
    stats_summary = f'''
    <div style="margin-bottom: 20px; padding: 16px; background: linear-gradient(135deg, #f8fafc, #e2e8f0); border-radius: 8px;">
        <h4 style="margin: 0 0 12px 0; color: #374151;">📊 {category_name} 상세 정보</h4>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 12px;">
            <div style="text-align: center;">
                <div style="font-size: 1.5rem; font-weight: bold; color: #667eea;">{total_inquiries}</div>
                <div style="font-size: 0.85rem; color: #6b7280;">총 문의</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 1.5rem; font-weight: bold; color: #ef4444;">{urgent_rate}%</div>
                <div style="font-size: 0.85rem; color: #6b7280;">긴급률</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 1rem; font-weight: bold; color: #f59e0b;">{main_team}</div>
                <div style="font-size: 0.85rem; color: #6b7280;">주담당팀</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 1rem; font-weight: bold; color: #10b981;">{main_journey}</div>
                <div style="font-size: 0.85rem; color: #6b7280;">유저여정</div>
            </div>
        </div>
        {team_distribution_html}
    </div>'''
    
    return stats_summary + sample_inquiries_html