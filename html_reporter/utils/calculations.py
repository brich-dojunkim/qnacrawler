# html_reporter/utils/calculations.py
"""계산 관련 유틸리티 함수들"""

def calculate_answer_rate(answered: int, total: int) -> float:
    """답변률 계산"""
    if total == 0:
        return 0
    return round((answered / total) * 100, 1)

def calculate_urgent_rate(urgent: int, total: int) -> float:
    """긴급률 계산"""
    if total == 0:
        return 0
    return round((urgent / total) * 100, 1)

def calculate_percentage(part: int, total: int) -> float:
    """백분율 계산"""
    if total == 0:
        return 0
    return round((part / total) * 100, 1)

def calculate_pending_rate(pending: int, total: int) -> float:
    """답변 대기율 계산"""
    return calculate_percentage(pending, total)