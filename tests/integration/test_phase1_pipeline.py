from ranopt.data.generator import generate_synthetic_ran_data
from ranopt.data.validation import validate_kpi_frame
from ranopt.kpi.health import add_health_score
from ranopt.kpi.thresholds import ThresholdConfig
from ranopt.preprocessing.pipeline import deduplicate_observations


def test_phase1_pipeline():
    frame = generate_synthetic_ran_data(cells=3, samples_per_cell=4, seed=42)
    validated = validate_kpi_frame(frame)
    prepared = deduplicate_observations(validated)
    thresholds = ThresholdConfig.from_yaml("configs/default.yaml")
    scored = add_health_score(prepared, thresholds)

    assert len(scored) == 12
    assert scored["cell_id"].nunique() == 3
    assert scored["cell_health_score"].notna().all()
