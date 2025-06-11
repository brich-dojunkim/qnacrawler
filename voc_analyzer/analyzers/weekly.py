import pandas as pd
from typing import Dict

def weekly_trends(df: pd.DataFrame, recent_weeks: int = 12) -> Dict:
    if "registration_date" not in df.columns:
        return {"error": "registration_date 컬럼이 없습니다."}

    df = df.copy()
    df["year_week"] = df["registration_date"].dt.to_period("W-MON")
    weeks = sorted(df["year_week"].dropna().unique())[-recent_weeks:]

    stats = {}
    for w in weeks:
        sub = df[df["year_week"] == w]
        info = {
            "total_inquiries": len(sub),
            "urgent_count": int(sub["is_urgent"].sum()) if "is_urgent" in sub else 0,
            "avg_content_length": round(sub["content_length"].mean(), 1) if "content_length" in sub else 0,
        }
        if "assigned_team" in sub.columns:
            info["top_teams"] = sub["assigned_team"].value_counts().head(3).to_dict()
        stats[str(w)] = info
    return stats
