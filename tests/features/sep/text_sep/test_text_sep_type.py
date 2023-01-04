from grplot.features.sep.text_sep.text_sep_type import text_sep_type
import pandas as pd
import pytest


class TestStatdescSepType:
    df = pd.DataFrame({"concentration": [1, 2], "time": [10, 20]})

    def test_unknown_sep_argument(self):
        with pytest.raises(Exception) as exc_info:
            text_sep_type("pieplot", self.df, 10000, [], "time", axes=None)
        assert str(exc_info.value) == "Unknown sep argument!"

    def test_sep_has_value(self):
        num = text_sep_type("pieplot", self.df, 10000, ".", "time", axes=None)
        assert num == "10.000"

    @pytest.mark.parametrize("num, expected", [(10000, 10000), (10000.0, "10000"), (10000.1, "10000.1")])
    def test_sep_is_none(self, num, expected):
        num = text_sep_type("pieplot", self.df, num, None, "time", axes=None)
        assert num == expected
