import pytest

from ranopt.data.generator import generate_synthetic_ran_data
from ranopt.data.validation import validate_kpi_frame


def test_generator_is_deterministic():
    first = generate_synthetic_ran_data(cells=2, samples_per_cell=3, seed=7)
    second = generate_synthetic_ran_data(cells=2, samples_per_cell=3, seed=7)
    assert first.equals(second)


def test_generator_has_expected_shape():
    frame = generate_synthetic_ran_data(cells=3, samples_per_cell=4)
    assert frame.shape == (12, 10)
    assert frame["cell_id"].nunique() == 3


def test_validation_rejects_missing_columns():
    frame = generate_synthetic_ran_data(cells=1, samples_per_cell=1).drop(columns=["sinr_db"])
    with pytest.raises(ValueError, match="Missing required KPI columns"):
        validate_kpi_frame(frame)
