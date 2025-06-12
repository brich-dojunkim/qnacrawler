# html_reporter/utils/__init__.py (import 경로 수정)
"""Utils 패키지 공통 인터페이스 - 사용하는 것만"""

# 계산 함수들 (사용됨)
try:
    from .calculations import (
        calculate_answer_rate,
        calculate_urgent_rate,
        calculate_percentage,
        calculate_pending_rate
    )
except ImportError as e:
    print(f"Warning: calculations import 오류: {e}")
    def calculate_answer_rate(answered, total): return 0.0
    def calculate_urgent_rate(urgent, total): return 0.0
    def calculate_percentage(part, total): return 0.0
    def calculate_pending_rate(pending, total): return 0.0

# 포맷팅 함수들 (사용됨)
try:
    from .formatters import (
        format_number,
        format_percentage,
        format_metric_value
    )
except ImportError as e:
    print(f"Warning: formatters import 오류: {e}")
    def format_number(num): return str(num)
    def format_percentage(value): return f"{value}%"
    def format_metric_value(value, metric_type): return str(value)

# 매핑 및 상수 (사용됨)
try:
    from .mappings import (
        USER_JOURNEY_MAPPING,
        JOURNEY_ORDER,
        METRICS_CONFIG,
        get_journey_for_category
    )
except ImportError as e:
    print(f"Warning: mappings import 오류: {e}")
    USER_JOURNEY_MAPPING = {}
    JOURNEY_ORDER = []
    METRICS_CONFIG = {}
    def get_journey_for_category(category): return "기타"

# 실제로 사용하는 데이터 처리만
try:
    from .processors import (
        process_overview_data,
        process_category_data
    )
except ImportError as e:
    print(f"Warning: processors import 오류: {e}")
    def process_overview_data(data): return {}
    def process_category_data(data): return []

# 실제로 사용하는 HTML 생성만
try:
    from .html_generators import (
        HTMLGenerator,
        generate_team_options
    )
except ImportError as e:
    print(f"Warning: html_generators import 오류: {e}")
    class HTMLGenerator:
        @staticmethod
        def generate_team_options(results): return ""
    def generate_team_options(results): return ""

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