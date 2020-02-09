import numpy as np
import pandas as pd
import pytest

from janitor.utils import skipna


@pytest.mark.functions
def test_skipna():
    df = pd.DataFrame({"x": ["a", "b", "c", np.nan], "y": [1, 2, 3, np.nan]})

    def func(s):
        return s + "1"

    # Verify that applying function causes error
    with pytest.raises(Exception):
        df["x"].apply(func)

    result = df["x"].apply(skipna(func))
    assert (
        result.values[:-1] == np.array(["a1", "b1", "c1"])
    ).all() and np.isnan(result.values[-1])
