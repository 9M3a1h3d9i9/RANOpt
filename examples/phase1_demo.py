"""Run the RANOpt Phase 1 synthetic KPI pipeline."""

from pathlib import Path

from ranopt.data.generator import generate_synthetic_ran_data
from ranopt.data.validation import validate_kpi_frame
from ranopt.kpi.health import add_health_score
from ranopt.kpi.thresholds import ThresholdConfig
from ranopt.preprocessing.pipeline import sort_by_cell_time


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    frame = generate_synthetic_ran_data(cells=4, samples_per_cell=6, seed=42)
    frame = validate_kpi_frame(frame)
    frame = sort_by_cell_time(frame)
    thresholds = ThresholdConfig.from_yaml(ROOT / "configs" / "default.yaml")
    scored = add_health_score(frame, thresholds)

    print("RANOpt Phase 1 demo")
    print(f"Observations: {len(scored)}")
    print(f"Cells: {scored['cell_id'].nunique()}")
    print(f"Mean health score: {scored['cell_health_score'].mean():.2f}/100")
    print(scored[["cell_id", "timestamp", "cell_health_score"]].head(10).to_string(index=False))


if __name__ == "__main__":
    main()
