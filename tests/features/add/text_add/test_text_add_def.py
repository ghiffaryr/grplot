from grplot.features.add.text_add.text_add_def import text_add_def
import pytest


class TestTextAddDef:
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
    def test_add_underscore_in_parenthesis(self, input, expected):
        num = text_add_def(**input)
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
    def test_add_underscore(self, input, expected):
        num = text_add_def(**input)
        assert num == expected

    def test_unknown_text_add_argument(self):
        with pytest.raises(Exception) as exc_info:
            text_add_def(add="ave", num=10000)

        assert str(exc_info.value) == "Unknown text add argument!"
