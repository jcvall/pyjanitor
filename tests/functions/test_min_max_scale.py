import pytest


@pytest.mark.functions
def test_min_max_scale(dataframe):
    df = dataframe.min_max_scale(column_name="a")
    assert df["a"].min() == 0
    assert df["a"].max() == 1


@pytest.mark.functions
def test_min_max_scale_custom_new_min_max(dataframe):
    df = dataframe.min_max_scale(column_name="a", new_min=1, new_max=2)
    assert df["a"].min() == 1
    assert df["a"].max() == 2


@pytest.mark.functions
def test_min_max_old_min_max_errors(dataframe):
    with pytest.raises(ValueError):
        dataframe.min_max_scale(column_name="a", old_min=10, old_max=0)


@pytest.mark.functions
def test_min_max_new_min_max_errors(dataframe):
    with pytest.raises(ValueError):
        dataframe.min_max_scale(column_name="a", new_min=10, new_max=0)
