import pandas as pd
from typing import Dict
from ..mappings import USER_JOURNEY

def _map(subcat: str) -> str:
    if pd.isna(subcat):
        return "기타"
    for j, cats in USER_JOURNEY.items():
        if subcat in cats:
            return j
    return "기타"

def journey_analysis(df: pd.DataFrame) -> Dict:
    if {"sub_category", "question_content"}.difference(df.columns):
        return {"error": "필요한 컬럼이 없습니다."}

    df = df.copy()
    df["user_journey"] = df["sub_category"].apply(_map)
    result = {}

    for j, jdf in df.groupby("user_journey"):
        info = {
            "total_inquiries": len(jdf),
            "urgent_count": int(jdf["is_urgent"].sum()) if "is_urgent" in jdf else 0,
            "answered_count": int((jdf["answer_status"] == "답변완료").sum()) if "answer_status" in jdf else 0,
            "avg_content_length": round(jdf["content_length"].mean(), 1) if "content_length" in jdf else 0,
        }

        # 대표 0.3, 0.7 지점
        samples = []
        if "content_length" in jdf:
            q = jdf.sort_values("content_length")
            for quant in (0.3, 0.7):
                idx = int(len(q) * quant)
                if idx < len(q):
                    r = q.iloc[idx]
                    samples.append({
                        "inquiry_id": r.get("inquiry_id", "N/A"),
                        "content": r["question_content"],
                        "length": r["content_length"],
                        "sub_category": r.get("sub_category", "N/A"),
                        "assigned_team": r.get("assigned_team", "N/A"),
                        "is_urgent": r.get("is_urgent", False),
                    })

        subcats = jdf["sub_category"].value_counts().head(5).to_dict()
        teams   = jdf["assigned_team"].value_counts().to_dict() if "assigned_team" in jdf else {}

        result[j] = {"basic_info": info,
                     "sample_inquiries": samples,
                     "sub_categories": subcats,
                     "team_distribution": teams}
    return result
