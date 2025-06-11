import pandas as pd
from typing import Dict

def overall_summary(df: pd.DataFrame) -> Dict:
    summ = {"total_inquiries": len(df)}

    if "registration_date" in df.columns:
        summ["date_range"] = {
            "start": str(df["registration_date"].min().date()),
            "end": str(df["registration_date"].max().date()),
        }

    if "assigned_team" in df.columns:
        teams = df["assigned_team"].dropna().unique()
        summ["teams"] = {"count": len(teams), "list": teams.tolist()}

    if "sub_category" in df.columns:
        cats = df["sub_category"].dropna().unique()
        summ["categories"] = {"count": len(cats), "list": cats.tolist()}

    if "is_urgent" in df.columns:
        summ["urgent_count"] = int(df["is_urgent"].sum())

    if "answer_status" in df.columns:
        summ["answer_status_distribution"] = df["answer_status"].value_counts().to_dict()

    if "content_length" in df.columns:
        summ["content_length_stats"] = {
            "mean": round(df["content_length"].mean(), 1),
            "median": round(df["content_length"].median(), 1),
            "min": int(df["content_length"].min()),
            "max": int(df["content_length"].max()),
        }

    return summ
