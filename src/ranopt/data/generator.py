"""Deterministic synthetic RAN KPI generation for development and tests."""

from datetime import datetime, timedelta, timezone

import numpy as np
import pandas as pd


KPI_COLUMNS = [
    "cell_id",
    "timestamp",
    "rsrp_dbm",
    "rsrq_db",
    "sinr_db",
    "dl_throughput_mbps",
    "ul_throughput_mbps",
    "drop_rate_pct",
    "handover_success_pct",
    "availability_pct",
]


def generate_synthetic_ran_data(
    cells: int = 12, samples_per_cell: int = 24, seed: int = 42
) -> pd.DataFrame:
    """Generate reproducible hourly KPI observations for synthetic cells."""
    if cells < 1 or samples_per_cell < 1:
        raise ValueError("cells and samples_per_cell must be positive")

    rng = np.random.default_rng(seed)
    start = datetime(2026, 1, 1, tzinfo=timezone.utc)
    rows: list[dict] = []

    for cell_idx in range(1, cells + 1):
        cell_id = f"CELL-{cell_idx:03d}"
        for sample_idx in range(samples_per_cell):
            load = float(rng.uniform(0.1, 0.95))
            rsrp = float(np.clip(rng.normal(-85 - 20 * load, 4), -120, -60))
            rsrq = float(np.clip(rng.normal(-6 - 8 * load, 1.5), -20, -1))
            sinr = float(np.clip(rng.normal(25 - 22 * load, 3), -5, 35))
            dl = float(np.clip(120 * (1 - load) + rng.normal(0, 5), 1, 150))
            ul = float(np.clip(35 * (1 - load) + rng.normal(0, 2), 0.5, 50))
            drop = float(np.clip(0.5 + 5 * load + rng.normal(0, 0.4), 0, 100))
            ho = float(np.clip(99.5 - 4 * load + rng.normal(0, 0.3), 0, 100))
            availability = float(np.clip(99.95 - 0.8 * load + rng.normal(0, 0.05), 0, 100))
            rows.append(
                {
                    "cell_id": cell_id,
                    "timestamp": start + timedelta(hours=sample_idx),
                    "rsrp_dbm": rsrp,
                    "rsrq_db": rsrq,
                    "sinr_db": sinr,
                    "dl_throughput_mbps": dl,
                    "ul_throughput_mbps": ul,
                    "drop_rate_pct": drop,
                    "handover_success_pct": ho,
                    "availability_pct": availability,
                }
            )
    return pd.DataFrame(rows, columns=KPI_COLUMNS)
