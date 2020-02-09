import pytest


@pytest.mark.functions
def test_filter_string(dataframe):
    df = dataframe.filter_string(
        column_name="animals@#$%^", search_string="bbit"
    )
    assert len(df) == 3


def test_filter_string_complement(dataframe):
    df = dataframe.filter_string(
        column_name="cities", search_string="hang", complement=True
    )
    assert len(df) == 6
