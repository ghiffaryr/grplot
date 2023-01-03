from grplot.features.sep.statdesc_sep.statdesc_sep_type import statdesc_sep_type
import pytest


class TestStatdescSepType:
    def test_unknown_sep_argument(self):
        with pytest.raises(Exception) as exc_info:
            statdesc_sep_type(axes=None, axislabel="x", num=10000, sep=[], stat_label="count")
        assert str(exc_info.value) == "Unknown sep argument!"

    def test_sep_is_none(self):
        num = statdesc_sep_type(axes=None, axislabel="x", num=10000, sep=None, stat_label="count")
        assert num == 10000

    def test_sep_has_value(self):
        num = statdesc_sep_type(axes=None, axislabel="x", num=10000, sep=".c", stat_label="count")
        assert num == "10.000"
