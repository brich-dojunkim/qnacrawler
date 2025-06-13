"""
터미널에서 python -m voc_analyzer.cli 로 실행 가능
(원래 voc_analyzer.py가 하던 일을 여기로 옮겼습니다)
"""
from datetime import datetime
from pathlib import Path
import os, json

import pandas as pd
from .loader import load_qna_json
from .analyzers import team_analysis, category_analysis, journey_analysis, weekly_trends
from .summarizer import overall_summary
from output_manager import setup_output_dirs, get_analysis_filename

class CategoryBasedVoCAnalyzer:
    def __init__(self, json_path: str):
        self.json_path = json_path
        self.df = load_qna_json(json_path)

    # 래핑 메서드들 --------------------------------------------------------
    def analyze_by_assigned_team(self):   return team_analysis(self.df)
    def analyze_by_sub_category(self):    return category_analysis(self.df)
    def analyze_by_user_journey(self):    return journey_analysis(self.df)
    def analyze_weekly_trends(self):      return weekly_trends(self.df)
    def get_overall_summary(self):        return overall_summary(self.df)

    # 통합 실행 ------------------------------------------------------------
    def generate(self, verbose=False):
        if verbose: print("🎯 카테고리 기반 VoC 분석 시작…")
        res = {
            "analysis_timestamp": datetime.now().isoformat(),
            "data_source": self.json_path,
            "overall_summary": self.get_overall_summary(),
            "team_analysis": self.analyze_by_assigned_team(),
            "category_analysis": self.analyze_by_sub_category(),
            "journey_analysis": self.analyze_by_user_journey(),
            "weekly_trends": self.analyze_weekly_trends(),
        }
        if verbose:
            fname = get_analysis_filename()
            with open(fname, "w", encoding="utf-8") as f:
                json.dump(res, f, ensure_ascii=False, indent=2, default=str)
            print(f"✅ 분석 결과 저장: {fname}")
        return res

# -------------------------------------------------------------------------
def _find_latest_qna_json() -> str | None:
    files = [p for p in Path(".").glob("*qna*.json")]
    files += list(Path("output/crawl_data").glob("*.json"))
    return max(files, key=os.path.getctime) if files else None

def main():
    setup_output_dirs()
    json_path = _find_latest_qna_json()
    if not json_path:
        print("❌ Q&A JSON 파일을 찾을 수 없습니다.")
        return

    print(f"📁 분석할 파일: {json_path}")
    analyzer = CategoryBasedVoCAnalyzer(str(json_path))
    results  = analyzer.generate(verbose=True)

    # HTML 리포트 (JSON 경로 전달 추가)
    try:
        from voc_html_reporter import CategoryVoCHTMLReporter
        html = CategoryVoCHTMLReporter(analyzer.df, json_path=str(json_path))  # JSON 경로 추가
        html.save_and_open_html_report(results)
        print("\n🎉 2단계 통합 분석 완료!")
    except ImportError as e:
        print(f"HTML 리포터 import 오류: {e}\n(voc_html_reporter.py 위치 확인)")

if __name__ == "__main__":
    main()
