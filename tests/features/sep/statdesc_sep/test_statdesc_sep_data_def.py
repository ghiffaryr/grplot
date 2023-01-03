from grplot.features.sep.statdesc_sep.statdesc_sep_data_def import statdesc_sep_data_def
import pytest


class TestStatdescSepDataDef:
    def test_unsupported_data_type(self):
        with pytest.raises(Exception) as exc_info:
            statdesc_sep_data_def(num="po", stat_label="count", sep=".c")
        assert str(exc_info.value) == "Unsupported data type!"

    def test_unrecognized_statlabel(self):
        num = statdesc_sep_data_def(num=10000, stat_label="yo", sep=".c")
        assert num == "10.000,00"

    @pytest.mark.parametrize("sep, expected", [(".c", "10.000"), (",c", "10,000"), (".", "10.000")])
    def test_recognized_statlabel(self, sep, expected):
        num = statdesc_sep_data_def(num=10000, stat_label="count", sep=sep)
        assert num == expected
