from grplot.features.sep.text_sep.text_sep_data_def import text_sep_data_def
import pandas as pd
import pytest


class TestTextSepDataDef:
    df = pd.DataFrame({"concentration": [1, 2], "time": [10, 20]})

    def test_df_contain_axislabel(self):
        num = text_sep_data_def(
            self.df,
            10000,
            "time",
            ".",
        )
        assert num == "10.000"

    @pytest.mark.parametrize(
        "axislabel, sep, expected",
        [
            ("Probability", ",c", "10,000"),
            ("Probability", ".c", "10.000"),
            ("Probability", ".", "10.000"),
            ("Halo", ".", 10000),
        ],
    )
    def test_axis_label_not_in_df(self, axislabel, sep, expected):
        num = text_sep_data_def(
            self.df,
            10000,
            axislabel,
            sep,
        )
        assert num == expected
