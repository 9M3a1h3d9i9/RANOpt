"""Explainable cell-health scoring."""

from typing import Iterable

import pandas as pd

from .thresholds import ThresholdConfig


HIGHER_IS_BETTER = {
    "rsrp_dbm": True,
    "rsrq_db": True,
    "sinr_db": True,
    "dl_throughput_mbps": True,
    "ul_throughput_mbps": True,
    "drop_rate_pct": False,
    "handover_success_pct": True,
    "availability_pct": True,
}


def _score_value(value: float, minimum: float, maximum: float, higher_is_better: bool) -> float:
    if maximum <= minimum:
        raise ValueError("threshold maximum must be greater than minimum")
    if higher_is_better:
        score = (value - minimum) / (maximum - minimum)
    else:
        score = (maximum - value) / (maximum - minimum)
    return float(max(0.0, min(1.0, score)))


def score_row(row: pd.Series, thresholds: ThresholdConfig) -> dict[str, float]:
    """Return per-KPI normalized scores in the [0, 1] range."""
    scores = {}
    for name, higher_is_better in HIGHER_IS_BETTER.items():
        threshold = thresholds.get(name)
        scores[name] = _score_value(
            float(row[name]), threshold.minimum, threshold.maximum, higher_is_better
        )
    return scores


def add_health_score(frame: pd.DataFrame, thresholds: ThresholdConfig) -> pd.DataFrame:
    """Add a weighted-average cell health score from 0 to 100."""
    result = frame.copy()
    scores: list[float] = []
    for _, row in result.iterrows():
        components = score_row(row, thresholds)
        scores.append(100.0 * sum(components.values()) / len(components))
    result["cell_health_score"] = scores
    return result
