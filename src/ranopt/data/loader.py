"""Data loading utilities."""

from pathlib import Path

import pandas as pd

from .validation import validate_kpi_frame


def load_csv(path: str | Path) -> pd.DataFrame:
    """Load and validate a CSV containing canonical RAN KPI columns."""
    frame = pd.read_csv(path)
    return validate_kpi_frame(frame)
