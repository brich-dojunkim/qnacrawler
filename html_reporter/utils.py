# html_reporter/utils.py
"""데이터 처리 유틸리티"""

import pandas as pd
from datetime import datetime

def format_number(num):
    """숫자 천단위 콤마"""
    return f"{num:,}"

def process_overview_data(results):
    """개요 데이터 처리"""
    overall_summary = results.get('overall_summary', {})
    return {
        'total_inquiries': overall_summary.get('total_inquiries', 0),
        'urgent_count': overall_summary.get('urgent_count', 0),
        'analysis_date': results.get('analysis_timestamp', datetime.now().isoformat())[:19].replace('T', ' ')
    }

def process_team_data(results):
    """팀별 데이터 처리"""
    if 'team_analysis' not in results:
        return []
    
    team_cards = []
    for team_name, team_info in results['team_analysis'].items():
        basic_info = team_info['basic_info']
        
        # 세부 카테고리 처리
        sub_categories_html = ""
        if team_info.get('sub_categories'):
            sub_categories_html = '<div class="simple-list"><h5 class="simple-list-title">세부 카테고리 분포</h5>'
            for idx, (category, count) in enumerate(sorted(team_info['sub_categories'].items(), key=lambda x: x[1], reverse=True)[:5], 1):
                sub_categories_html += f'<div class="simple-item"><span class="simple-rank">{idx}</span><span class="simple-name">{category}</span><span class="simple-value">{count}건</span></div>'
            sub_categories_html += '</div>'
        
        team_cards.append({
            'name': team_name,
            'total_inquiries': basic_info['total_inquiries'],
            'urgent_count': basic_info['urgent_count'],
            'answered_count': basic_info['answered_count'],
            'avg_content_length': round(basic_info['avg_content_length']),
            'sub_categories': sub_categories_html
        })
    
    return team_cards

def process_category_data(results):
    """카테고리별 데이터 처리"""
    if 'category_analysis' not in results:
        return []
    
    category_cards = []
    sorted_categories = sorted(results['category_analysis'].items(), 
                             key=lambda x: x[1]['basic_info']['total_inquiries'], 
                             reverse=True)
    
    for category_name, category_info in sorted_categories:
        basic_info = category_info['basic_info']
        
        # 담당팀 배지 생성
        team_badges_html = ""
        if category_info.get('team_distribution'):
            for team, count in list(category_info['team_distribution'].items())[:3]:
                team_badges_html += f'<span class="team-badge">{team}</span>'
        
        main_team = list(category_info.get('team_distribution', {}).keys())[0] if category_info.get('team_distribution') else '기타'
        main_journey = get_journey_for_category(category_name)
        
        # 모달 ID 생성
        modal_id = f"modal-{category_name.replace(' ', '-').replace('/', '-').replace('(', '').replace(')', '')}"
        
        # 모달 콘텐츠 생성
        modal_content = ""
        for sample in category_info.get('sample_inquiries', []):
            urgency_class = "urgency-urgent" if sample.get('is_urgent', False) else "urgency-normal"
            urgency_text = "긴급" if sample.get('is_urgent', False) else "일반"
            modal_content += f'''
            <div class="inquiry-card">
                <div class="inquiry-header">
                    <span>{sample.get('assigned_team', 'N/A')}</span>
                    <span class="urgency-badge {urgency_class}">{urgency_text}</span>
                </div>
                <div class="inquiry-content">{sample.get('content', '')}</div>
            </div>'''
        
        category_cards.append({
            'name': category_name,
            'total_inquiries': basic_info['total_inquiries'],
            'urgent_count': basic_info['urgent_count'],
            'avg_content_length': round(basic_info['avg_content_length']),
            'main_team': main_team,
            'main_journey': main_journey,
            'team_badges': team_badges_html,
            'modal_id': modal_id,
            'modal_content': modal_content
        })
    
    return category_cards

def get_journey_for_category(category_name):
    """세부 카테고리를 유저 여정으로 매핑"""
    journey_mapping = {
        '계정·입점': [
            '입점관리', '스토어관리', '플랜관리', '신규회원가입',
            '사업자정보/양도양수', '탈퇴/재가입', '브랜드권한신청'
        ],
        '상품·콘텐츠': [
            '상품등록', '상품등록 실패', '상품 조회 및 수정', '채널상품연동',
            '브리치 기획전신청', '채널딜 진행관리', '상품문의(브리치)', '상품문의(채널)'
        ],
        '주문·배송': [
            '발주/발송관리', '배송현황관리', '배송지연 관리 (결품취소)',
            '송장등록 실패/ 송장번호 수정', '주문조회', '긴급문의', '배송정책 관리'
        ],
        '반품·취소': [
            '취소관리', '교환관리/교환철회', '반품관리/환불보류'
        ],
        '정산': [
            '구매확정관리', '정산통합', '특약매입정산', '판매대행정산'
        ]
    }
    
    if pd.isna(category_name):
        return '기타'
    
    for journey, categories in journey_mapping.items():
        if category_name in categories:
            return journey
    
    return '기타'