# html_reporter/utils/formatters.py
"""데이터 포맷팅 유틸리티"""

def format_number(num: int) -> str:
    """숫자 천단위 콤마 포맷팅"""
    return f"{num:,}"

def format_percentage(value: float) -> str:
    """백분율 포맷팅"""
    return f"{value}%"

def format_metric_value(value, metric_type: str) -> str:
    """메트릭 타입에 따른 값 포맷팅"""
    if metric_type in ['rate', 'percentage']:
        return format_percentage(value)
    elif metric_type == 'count':
        return format_number(value)
    return str(value)