# html_reporter/utils/__init__.py
"""Utils 패키지 공통 인터페이스"""

# 계산 함수들
from .calculations import (
    calculate_answer_rate,
    calculate_urgent_rate,
    calculate_percentage,
    calculate_pending_rate
)

# 포맷팅 함수들
from .formatters import (
    format_number,
    format_percentage,
    format_metric_value
)

# 매핑 및 상수
from .mappings import (
    USER_JOURNEY_MAPPING,
    JOURNEY_ORDER,
    METRICS_CONFIG,
    get_journey_for_category
)

# 데이터 처리 (processors 서브모듈에서 직접 import)
from .processors import (
    process_overview_data,
    process_team_data,
    process_journey_data,
    process_category_data
)

# HTML 생성
from .html_generators import (
    HTMLGenerator,
    generate_team_options,
    generate_rank_tables,
    generate_sub_categories_html
)

__all__ = [
    # 계산 함수들
    'calculate_answer_rate',
    'calculate_urgent_rate',
    'calculate_percentage',
    'calculate_pending_rate',
    
    # 포맷팅 함수들
    'format_number',
    'format_percentage',
    'format_metric_value',
    
    # 매핑 및 상수
    'USER_JOURNEY_MAPPING',
    'JOURNEY_ORDER',
    'METRICS_CONFIG',
    'get_journey_for_category',
    
    # 클래스들 (제거)
    # 'DataProcessor',  # 더 이상 사용하지 않음
    'HTMLGenerator',
    
    # 하위 호환성 함수들 (기존 인터페이스 유지)
    'process_overview_data',
    'process_team_data',
    'process_journey_data',
    'process_category_data',
    'generate_team_options',
    'generate_rank_tables',
    'generate_sub_categories_html'
]