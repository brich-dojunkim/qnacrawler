# html_reporter/utils/processors/__init__.py
"""데이터 처리 모듈 패키지 - 실제 사용하는 것만"""

try:
    from .overview import process_overview_data
except ImportError as e:
    print(f"Warning: overview processor import 오류: {e}")
    def process_overview_data(results): return {}

try:
    from .category import process_category_data
except ImportError as e:
    print(f"Warning: category processor import 오류: {e}")
    def process_category_data(results): return []

__all__ = [
    'process_overview_data',
    'process_category_data'
]