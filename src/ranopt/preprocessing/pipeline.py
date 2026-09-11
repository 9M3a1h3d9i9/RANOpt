"""Small, deterministic preprocessing helpers."""

import pandas as pd


def sort_by_cell_time(frame: pd.DataFrame) -> pd.DataFrame:
    """Return observations sorted by cell and timestamp."""
    required = {"cell_id", "timestamp"}
    missing = required - set(frame.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    result = frame.copy()
    result["timestamp"] = pd.to_datetime(result["timestamp"], utc=True)
    return result.sort_values(["cell_id", "timestamp"]).reset_index(drop=True)


def deduplicate_observations(frame: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate cell/timestamp observations while preserving first occurrence."""
    result = sort_by_cell_time(frame)
    return result.drop_duplicates(subset=["cell_id", "timestamp"], keep="first").reset_index(drop=True)
