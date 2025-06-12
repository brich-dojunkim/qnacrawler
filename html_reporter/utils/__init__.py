# html_reporter/utils/__init__.py (정리된 버전)
"""Utils 패키지 공통 인터페이스 - 사용하는 것만"""

# 계산 함수들 (사용됨)
from .calculations import (
    calculate_answer_rate,
    calculate_urgent_rate,
    calculate_percentage,
    calculate_pending_rate
)

# 포맷팅 함수들 (사용됨)
from .formatters import (
    format_number,
    format_percentage,
    format_metric_value
)

# 매핑 및 상수 (사용됨)
from .mappings import (
    USER_JOURNEY_MAPPING,
    JOURNEY_ORDER,
    METRICS_CONFIG,
    get_journey_for_category
)

# 실제로 사용하는 데이터 처리만
from .processors import (
    process_overview_data,
    process_category_data
)

# 실제로 사용하는 HTML 생성만
from .html_generators import (
    HTMLGenerator,
    generate_team_options
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
    
    # 클래스들
    'HTMLGenerator',
    
    # 실제로 사용하는 함수들만
    'process_overview_data',
    'process_category_data',
    'generate_team_options'
]