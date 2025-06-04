# html_reporter/utils.py
"""데이터 처리 유틸리티 - 단순화된 버전"""

import pandas as pd
from datetime import datetime

def format_number(num):
    """숫자 천단위 콤마"""
    return f"{num:,}"

def calculate_answer_rate(answered, total):
    """답변률 계산"""
    if total == 0:
        return 0
    return round((answered / total) * 100, 1)

def calculate_urgent_rate(urgent, total):
    """긴급률 계산"""
    if total == 0:
        return 0
    return round((urgent / total) * 100, 1)

def process_overview_data(results):
    """개요 데이터 처리"""
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
    
    overview_data = {
        'total_inquiries': total_inquiries,
        'urgent_count': urgent_count,
        'answered_count': answered_count,
        'pending_count': pending_count,
        'analysis_date': results.get('analysis_timestamp', datetime.now().isoformat())[:19].replace('T', ' ')
    }
    
    # 순위표 생성
    rank_tables = ""
    
    # 팀별 분포 순위표
    if 'team_analysis' in results:
        team_data = results['team_analysis']
        if team_data:
            sorted_teams = sorted(team_data.items(), 
                                key=lambda x: x[1]['basic_info']['total_inquiries'], 
                                reverse=True)
            
            total_inquiries_check = sum(team_data[team]['basic_info']['total_inquiries'] for team in team_data.keys())
            
            team_table_html = '<h4 class="rank-table-title">팀별 문의 분포</h4>'
            
            for idx, (team_name, team_info) in enumerate(sorted_teams[:10], 1):  # 상위 10개만
                count = team_info['basic_info']['total_inquiries']
                percentage = (count / total_inquiries_check * 100) if total_inquiries_check > 0 else 0
                
                team_table_html += f'''
                <div class="rank-row">
                    <div class="rank-number">{idx}</div>
                    <div class="rank-name">{team_name}</div>
                    <div class="rank-value">{count:,}건 ({percentage:.1f}%)</div>
                </div>'''
            
            rank_tables += f'<div class="entity-card" style="margin-bottom: 1rem;">{team_table_html}</div>'
    
    # 유저 여정별 분포 순위표
    if 'journey_analysis' in results:
        journey_data = results['journey_analysis']
        if journey_data:
            sorted_journeys = sorted(journey_data.items(), 
                                   key=lambda x: x[1]['basic_info']['total_inquiries'], 
                                   reverse=True)
            
            total_inquiries_check = sum(data['basic_info']['total_inquiries'] for _, data in sorted_journeys)
            
            journey_table_html = '<h4 class="rank-table-title">유저 여정별 문의 분포</h4>'
            
            for idx, (journey_name, journey_info) in enumerate(sorted_journeys, 1):
                count = journey_info['basic_info']['total_inquiries']
                if count == 0:  # 빈 여정은 제외
                    continue
                percentage = (count / total_inquiries_check * 100) if total_inquiries_check > 0 else 0
                
                journey_table_html += f'''
                <div class="rank-row">
                    <div class="rank-number">{idx}</div>
                    <div class="rank-name">{journey_name}</div>
                    <div class="rank-value">{count:,}건 ({percentage:.1f}%)</div>
                </div>'''
            
            rank_tables += f'<div class="entity-card">{journey_table_html}</div>'
    
    overview_data['rank_tables'] = rank_tables
    return overview_data

def process_team_data(results):
    """팀별 데이터 처리"""
    if 'team_analysis' not in results:
        return []
    
    team_cards = []
    for team_name, team_info in results['team_analysis'].items():
        basic_info = team_info['basic_info']
        
        # 답변률 계산
        answer_rate = calculate_answer_rate(basic_info.get('answered_count', 0), basic_info['total_inquiries'])
        
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
            'answer_rate': answer_rate,
            'avg_content_length': round(basic_info['avg_content_length']),
            'sub_categories': sub_categories_html
        })
    
    # 문의량 순으로 정렬
    team_cards.sort(key=lambda x: x['total_inquiries'], reverse=True)
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
        
        # 긴급률 계산
        urgent_rate = calculate_urgent_rate(basic_info['urgent_count'], basic_info['total_inquiries'])
        
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
            'avg_content_length': round(basic_info['avg_content_length']),
            'main_team': main_team,
            'main_journey': main_journey,
            'team_badges': team_badges_html,
            'modal_id': modal_id,
            'modal_content': modal_content
        })
    
    return category_cards

def process_journey_data(results):
    """유저 여정별 데이터 처리"""
    if 'journey_analysis' not in results:
        return []
    
    journey_cards = []
    
    # 유저 여정 순서 정의
    journey_order = ['계정·입점', '상품·콘텐츠', '주문·배송', '반품·취소', '정산', '기타']
    
    # 순서대로 정렬
    sorted_journeys = []
    for journey in journey_order:
        if journey in results['journey_analysis']:
            sorted_journeys.append((journey, results['journey_analysis'][journey]))
    
    for journey_name, journey_info in sorted_journeys:
        basic_info = journey_info['basic_info']
        
        # 문의가 없는 여정은 제외
        if basic_info['total_inquiries'] == 0:
            continue
        
        # 답변률 계산
        answer_rate = calculate_answer_rate(basic_info.get('answered_count', 0), basic_info['total_inquiries'])
        
        # 세부 카테고리 처리
        sub_categories_html = ""
        if journey_info.get('sub_categories'):
            sub_categories_html = '<div class="simple-list"><h5 class="simple-list-title">세부 카테고리 분포</h5>'
            for idx, (category, count) in enumerate(sorted(journey_info['sub_categories'].items(), key=lambda x: x[1], reverse=True)[:5], 1):
                sub_categories_html += f'<div class="simple-item"><span class="simple-rank">{idx}</span><span class="simple-name">{category}</span><span class="simple-value">{count}건</span></div>'
            sub_categories_html += '</div>'
        
        journey_cards.append({
            'name': journey_name,
            'total_inquiries': basic_info['total_inquiries'],
            'urgent_count': basic_info['urgent_count'],
            'answered_count': basic_info['answered_count'],
            'answer_rate': answer_rate,
            'avg_content_length': round(basic_info['avg_content_length']),
            'sub_categories': sub_categories_html
        })
    
    return journey_cards

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