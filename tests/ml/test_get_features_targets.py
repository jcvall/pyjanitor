import pytest
from hypothesis import given

import janitor.ml
from janitor.testing_utils.strategies import df_strategy


@pytest.mark.ml
@given(df=df_strategy())
def test_get_features_targets(df):
    X, y = df.clean_names().get_features_targets(
        target_column_names="bell_chart"
    )
    assert X.shape[1] == 4
    assert len(y.shape) == 1


@pytest.mark.ml
@given(df=df_strategy())
def test_get_features_targets_multi_features(df):
    X, y = df.clean_names().get_features_targets(
        feature_column_names=["animals@#$%^", "cities"],
        target_column_names="bell_chart",
    )
    assert X.shape[1] == 2
    assert len(y.shape) == 1


@pytest.mark.ml
@given(df=df_strategy())
def test_get_features_target_multi_columns(df):
    X, y = df.clean_names().get_features_targets(
        target_column_names=["a", "bell_chart"]
    )
    assert X.shape[1] == 3
    assert y.shape[1] == 2
