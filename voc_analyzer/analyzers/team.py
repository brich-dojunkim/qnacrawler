import pandas as pd
from typing import Dict

def team_analysis(df: pd.DataFrame) -> Dict:
    if {"assigned_team", "question_content"}.difference(df.columns):
        return {"error": "필요한 컬럼이 없습니다."}

    result = {}
    for team, sub in df.groupby("assigned_team"):
        info = {
            "total_inquiries": len(sub),
            "urgent_count": int(sub["is_urgent"].sum()) if "is_urgent" in sub else 0,
            "answered_count": int((sub["answer_status"] == "답변완료").sum()) if "answer_status" in sub else 0,
            "avg_content_length": round(sub["content_length"].mean(), 1) if "content_length" in sub else 0,
        }

        # 대표 사례 2개
        samples = []
        if "content_length" in sub:
            q = sub.sort_values("content_length")
            for quant in (0.3, 0.7):
                idx = int(len(q) * quant)
                if idx < len(q):
                    row = q.iloc[idx]
                    samples.append({
                        "inquiry_id": row.get("inquiry_id", "N/A"),
                        "content": row["question_content"],
                        "length": row["content_length"],
                        "sub_category": row.get("sub_category", "N/A"),
                        "is_urgent": row.get("is_urgent", False),
                    })

        # 상위 5개 세부 카테고리
        subcats = sub["sub_category"].value_counts().head(5).to_dict() if "sub_category" in sub else {}

        result[team] = {"basic_info": info,
                        "sample_inquiries": samples,
                        "sub_categories": subcats}
    return result
