"""고정 매핑·상수"""
USER_JOURNEY = {
    "계정·입점": [
        "입점관리", "스토어관리", "플랜관리", "신규회원가입",
        "사업자정보/양도양수", "탈퇴/재가입", "브랜드권한신청",
    ],
    "상품·콘텐츠": [
        "상품등록", "상품등록 실패", "상품 조회 및 수정",
        "채널상품연동", "브리치 기획전신청", "채널딜 진행관리",
        "상품문의(브리치)", "상품문의(채널)",
    ],
    "주문·배송": [
        "발주/발송관리", "배송현황관리", "배송지연 관리 (결품취소)",
        "송장등록 실패/ 송장번호 수정", "주문조회", "긴급문의", "배송정책 관리",
    ],
    "반품·취소": ["취소관리", "교환관리/교환철회", "반품관리/환불보류"],
    "정산": ["구매확정관리", "정산통합", "특약매입정산", "판매대행정산"],
}
