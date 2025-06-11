"""
voc_analyzer.loader
JSON → pandas DataFrame 로더 + 1차 전처리
"""

from __future__ import annotations

import json
import pandas as pd
import warnings

warnings.filterwarnings("ignore")

__all__ = ["load_qna_json"]


# ────────────────────────────────────────────────────────────
# 내부 헬퍼
# ────────────────────────────────────────────────────────────
def _flatten_category(df: pd.DataFrame) -> pd.DataFrame:
    """
    JSON 안에 `category: { ... }` 딕셔너리가 있으면
    이를 컬럼으로 분해해 DataFrame에 병합한다.
    """
    if "category" not in df.columns:
        return df

    cat_df = pd.json_normalize(df["category"])
    return pd.concat([df.drop("category", axis=1), cat_df], axis=1)


# ────────────────────────────────────────────────────────────
# public API
# ────────────────────────────────────────────────────────────
def load_qna_json(path: str) -> pd.DataFrame:
    """
    Q&A 크롤링 JSON 파일을 읽어 DataFrame으로 반환한다.

    지원 구조
    1) { "data": [ {...}, {...} ] }          – 기존 크롤러 구조
    2) [ {...}, {...} ]                      – 리스트가 최상위
    3) { ... }                               – 단일 딕셔너리

    Args:
        path: JSON 파일 경로

    Returns:
        pd.DataFrame
    """
    with open(path, "r", encoding="utf-8") as f:
        raw = json.load(f)

    # ── 구조 분기 ─────────────────────────────────────────────
    if isinstance(raw, list):
        records = raw
    elif isinstance(raw, dict):
        records = raw.get("data", raw)  # 'data' 키가 있으면 그 값, 없으면 dict 자체
        # dict 자체가 단일 레코드라면 리스트로 감싼다
        if isinstance(records, dict):
            records = [records]
    else:
        raise ValueError("지원하지 않는 JSON 구조입니다.")

    # ── DataFrame 변환 ───────────────────────────────────────
    df = pd.DataFrame(records)
    df = _flatten_category(df)

    # 날짜·텍스트 길이 기본 처리
    if "registration_date" in df.columns:
        df["registration_date"] = pd.to_datetime(df["registration_date"], errors="coerce")

    if "question_content" in df.columns:
        df["content_length"] = df["question_content"].astype(str).str.len()

    print(f"✅ 데이터 로드 완료: {len(df)}개 문의")
    print(f"📊 사용 가능한 컬럼: {list(df.columns)}")
    return df
