from grplot.features.sep.statdesc_sep.statdesc_sep_def import statdesc_sep_def
import pytest


class TestStatdescSepDef:
    def test_unknown_sep_argument(self):
        with pytest.raises(Exception) as exc_info:
            statdesc_sep_def(num=1000, sep="oy")
        assert str(exc_info.value) == "Unknown sep argument!"

    class TestSepComma:
        @pytest.mark.parametrize("num, expected", [(0.02, "0.02"), (0.0006, "0.0006")])
        def test_less_than_one(self, num, expected):
            num = statdesc_sep_def(num=num, sep=",c")
            assert num == expected

        @pytest.mark.parametrize(
            "num, sep, expected",
            [(10000, ",c", "10,000.00"), (10000, ",", "10,000"), (1000.0, ",", "1,000"), (1000.1, ",", "1,000.1")],
        )
        def test_more_than_one(self, num, sep, expected):
            num = statdesc_sep_def(num=num, sep=sep)
            assert num == expected

    class TestSepDot:
        @pytest.mark.parametrize("num, expected", [(0.02, "0,02"), (0.0006, "0,0006")])
        def test_less_than_one(self, num, expected):
            num = statdesc_sep_def(num=num, sep=".c")
            assert num == expected

        @pytest.mark.parametrize(
            "num, sep, expected",
            [(10000, ".c", "10.000,00"), (10000, ".", "10.000"), (1000.0, ".", "1.000"), (1000.1, ".", "1.000,1")],
        )
        def test_more_than_one(self, num, sep, expected):
            num = statdesc_sep_def(num=num, sep=sep)
            assert num == expected
