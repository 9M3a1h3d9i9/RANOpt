"""Validation utilities for tabular RAN KPI observations."""

import pandas as pd

from .models import RANKPI


REQUIRED_COLUMNS = list(RANKPI.model_fields)


def validate_kpi_frame(frame: pd.DataFrame) -> pd.DataFrame:
    """Validate required columns and every KPI row; return a clean copy."""
    missing = [column for column in REQUIRED_COLUMNS if column not in frame.columns]
    if missing:
        raise ValueError(f"Missing required KPI columns: {missing}")

    clean = frame[REQUIRED_COLUMNS].copy()
    clean["timestamp"] = pd.to_datetime(clean["timestamp"], utc=True)
    for column in REQUIRED_COLUMNS:
        if column not in {"cell_id", "timestamp"}:
            clean[column] = pd.to_numeric(clean[column], errors="raise")

    for record in clean.to_dict(orient="records"):
        RANKPI.model_validate(record)
    return clean
