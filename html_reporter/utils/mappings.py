# html_reporter/utils/mappings.py (여정 순서 추가)
"""상수 및 매핑 데이터 - 여정 시간 순서 포함"""

import pandas as pd

# 유저 여정 매핑
USER_JOURNEY_MAPPING = {
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

# 여정 순서 (기존)
JOURNEY_ORDER = ['계정·입점', '상품·콘텐츠', '주문·배송', '반품·취소', '정산', '기타']

# 여정 시간 순서 (새로 추가 - 비즈니스 플로우 순서)
JOURNEY_TIME_ORDER = [
    '계정·입점',    # 1단계: 서비스 시작/계정 생성
    '상품·콘텐츠',  # 2단계: 상품 준비/등록
    '주문·배송',    # 3단계: 거래 진행/배송
    '반품·취소',    # 4단계: 사후 처리
    '정산',         # 5단계: 거래 완료/정산
    '기타'          # 6단계: 분류 불가
]

# 메트릭 정의
METRICS_CONFIG = {
    'team_metrics': ['total_inquiries', 'urgent_count', 'answered_count', 'answer_rate', 'avg_content_length'],
    'journey_metrics': ['total_inquiries', 'urgent_count', 'answered_count', 'answer_rate', 'avg_content_length'],
    'category_metrics': ['total_inquiries', 'urgent_count', 'urgent_rate', 'avg_content_length'],
    'overview_metrics': ['total_inquiries', 'urgent_count', 'answered_count', 'pending_count']
}

def get_journey_for_category(category_name: str) -> str:
    """세부 카테고리를 유저 여정으로 매핑"""
    if pd.isna(category_name):
        return '기타'
    
    for journey, categories in USER_JOURNEY_MAPPING.items():
        if category_name in categories:
            return journey
    
    return '기타'

def get_journey_time_order_index(journey_name: str) -> int:
    """여정의 시간 순서 인덱스 반환 (정렬용)"""
    try:
        return JOURNEY_TIME_ORDER.index(journey_name)
    except ValueError:
        return len(JOURNEY_TIME_ORDER)  # '기타'나 정의되지 않은 여정은 마지막으로