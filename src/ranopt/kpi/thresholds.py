"""Threshold configuration used by the explainable health scorer."""

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass(frozen=True)
class RangeThreshold:
    """Acceptable range for a KPI."""

    minimum: float
    maximum: float


class ThresholdConfig:
    """Collection of KPI ranges loaded from YAML configuration."""

    def __init__(self, thresholds: dict[str, RangeThreshold]):
        self._thresholds = thresholds

    @classmethod
    def from_yaml(cls, path: str | Path) -> "ThresholdConfig":
        data: dict[str, Any] = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
        raw = data.get("kpi", {}).get("thresholds", {})
        thresholds = {
            name: RangeThreshold(float(values["min"]), float(values["max"]))
            for name, values in raw.items()
        }
        return cls(thresholds)

    def get(self, name: str) -> RangeThreshold:
        return self._thresholds[name]

    def as_dict(self) -> dict[str, dict[str, float]]:
        return {
            name: {"min": item.minimum, "max": item.maximum}
            for name, item in self._thresholds.items()
        }
