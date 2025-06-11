import pandas as pd, textwrap as tw
from typing import Dict

def _short(txt, n=150):
    return txt if len(txt) <= n else txt[:n] + "..."

def category_analysis(df: pd.DataFrame) -> Dict:
    if {"sub_category", "question_content"}.difference(df.columns):
        return {"error": "필요한 컬럼이 없습니다."}

    result = {}
    for cat, sub in df.groupby("sub_category"):
        info = {
            "total_inquiries": len(sub),
            "urgent_count": int(sub["is_urgent"].sum()) if "is_urgent" in sub else 0,
            "avg_content_length": round(sub["content_length"].mean(), 1) if "content_length" in sub else 0,
        }
        teams = sub["assigned_team"].value_counts().to_dict() if "assigned_team" in sub else {}

        samples = [{
            "inquiry_id": r.get("inquiry_id", "N/A"),
            "content": _short(r["question_content"]),
            "assigned_team": r.get("assigned_team", "N/A"),
            "length": r.get("content_length", 0),
            "is_urgent": r.get("is_urgent", False),
        } for _, r in sub.head(2).iterrows()]

        result[cat] = {"basic_info": info,
                       "team_distribution": teams,
                       "sample_inquiries": samples}
    return result
