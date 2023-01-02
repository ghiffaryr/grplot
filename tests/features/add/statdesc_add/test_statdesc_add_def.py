from ast import Num
from grplot.features.add.statdesc_add.statdesc_add_def import statdesc_add_def
import pytest


class TestStatdescAddDef:
    @pytest.mark.parametrize(
        "input, expected",
        [
            ({"num": 10000, "add": "Rp (_)"}, "Rp 10000"),
            ({"num": "-10000", "add": "Rp (_)"}, "(Rp 10000)"),
            ({"num": 10000, "add": "(_) km"}, "10000 km"),
            ({"num": -10000, "add": "(_) km"}, "(10000 km)"),
            ({"num": 10000, "add": "huge (_) km"}, "huge 10000 km"),
            ({"num": -10000, "add": "huge (_) km"}, "(huge 10000 km)"),
        ],
    )
    def test_add_with_underscore_in_parenthesis(self, input, expected):
        num = statdesc_add_def(**input)
        assert num == expected

    @pytest.mark.parametrize(
        "input, expected",
        [
            ({"num": 10000, "add": "Rp _"}, "Rp 10000"),
            ({"num": -10000, "add": "Rp _"}, "-Rp 10000"),
            ({"num": 10000, "add": "_ km"}, "10000 km"),
            ({"num": 10000, "add": "huge _ km"}, "huge 10000 km"),
            ({"num": -10000, "add": "huge _ km"}, "-huge 10000 km"),
        ],
    )
    def test_add_with_underscore(self, input, expected):
        num = statdesc_add_def(**input)
        assert num == expected

    def test_unknown_statdesc_add_argument(self):
        with pytest.raises(Exception) as exc_info:
            statdesc_add_def(num=10000, add="skadnasjkdnaskdj")
        assert str(exc_info.value) == "Unknown statdesc add argument!"
