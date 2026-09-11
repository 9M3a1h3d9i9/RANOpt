from ranopt.data.generator import generate_synthetic_ran_data
from ranopt.kpi.health import add_health_score
from ranopt.kpi.thresholds import ThresholdConfig


def test_health_score_is_bounded():
    frame = generate_synthetic_ran_data(cells=2, samples_per_cell=2)
    thresholds = ThresholdConfig.from_yaml("configs/default.yaml")
    scored = add_health_score(frame, thresholds)
    assert scored["cell_health_score"].between(0, 100).all()


def test_health_score_column_is_added_without_mutating_input():
    frame = generate_synthetic_ran_data(cells=1, samples_per_cell=2)
    original_columns = list(frame.columns)
    thresholds = ThresholdConfig.from_yaml("configs/default.yaml")
    scored = add_health_score(frame, thresholds)
    assert "cell_health_score" in scored
    assert list(frame.columns) == original_columns
