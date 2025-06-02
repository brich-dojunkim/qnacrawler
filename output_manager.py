# output_manager.py
"""출력 파일 관리 - 간단 버전"""

import os
from datetime import datetime

def setup_output_dirs():
    """output 폴더들 생성"""
    dirs = ["output", "output/analysis", "output/reports", "output/crawl_data"]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
    print("📁 output 폴더 생성 완료")

def get_analysis_filename():
    """분석 결과 JSON 파일명"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"output/analysis/voc_analysis_{timestamp}.json"

def get_report_filename():
    """HTML 보고서 파일명"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"output/reports/voc_report_{timestamp}.html"

def get_crawl_filename():
    """크롤링 데이터 파일명"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"output/crawl_data/qna_data_{timestamp}.json"