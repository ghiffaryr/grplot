from grplot.features.sep.text_sep.text_sep_def import text_sep_def
from pandas.api.types import is_float_dtype, is_integer_dtype
import matplotlib
import pytest


class TestTextSepDef:
    def test_unknown_sep_argument(self):
        with pytest.raises(Exception) as exc_info:
            text_sep_def(num=1000, sep="oy")
        assert str(exc_info.value) == "Unknown sep argument!"

    @pytest.mark.parametrize("sep", [(","), (",c")], scope="class")
    class TestSepComma:
        def test_num_less_than_power_of_lower_limit(self, sep):
            num = text_sep_def(num=0.000001, sep=sep)
            assert num == "1.0e-6"

        @pytest.mark.parametrize("num, expected", [(0.001, "0.001"), (0.1, "0.1")], scope="function")
        def test_num_more_than_power_of_lower_limit(self, sep, num, expected):
            if sep == ",c" and abs(num) >= 0.01:
                expected = "0.10"

            if sep == "," and abs(num) >= 0.01:
                expected = "0.1"

            num = text_sep_def(num=num, sep=sep)
            assert num == expected

        @pytest.mark.parametrize(
            "num, expected", [(1000.0, "1,000.00"), (1000, "1,000.00"), (1000.1, "1,000.10")], scope="function"
        )
        def test_num_more_than_one(self, sep, num, expected):
            if sep == ",":
                if is_float_dtype(type(num)):
                    if num.is_integer():
                        expected = "{:,}".format(int(num))
                    else:
                        expected = "{:,.1f}".format(num)
                elif is_integer_dtype(type(num)):
                    expected = "{:,}".format(num)

            num = text_sep_def(num=num, sep=sep)
            assert num == expected

    @pytest.mark.parametrize("sep", [("."), (".c")], scope="class")
    class TestSepDot:
        def test_num_less_than_power_of_lower_limit(self, sep):
            num = text_sep_def(num=0.000001, sep=sep)
            assert num == "1,0e-6"

        @pytest.mark.parametrize("num, expected", [(0.001, "0,001"), (0.1, "0,1")], scope="function")
        def test_num_more_than_power_of_lower_limit(self, sep, num, expected):
            if sep == ".c" and abs(num) >= 0.01:
                expected = "0,10"

            if sep == "." and abs(num) >= 0.01:
                expected = "0,1"

            num = text_sep_def(num=num, sep=sep)
            assert num == expected

        @pytest.mark.parametrize(
            "num, expected", [(1000.0, "1.000,00"), (1000, "1.000,00"), (1000.1, "1.000,10")], scope="function"
        )
        def test_num_more_than_one(self, sep, num, expected):
            if sep == ".":
                if is_float_dtype(type(num)) == True:
                    if num.is_integer() == True:
                        expected = "{:,}".format(int(num)).replace(",", "~").replace(".", ",").replace("~", ".")
                    else:
                        expected = "{:,.1f}".format(num).replace(",", "~").replace(".", ",").replace("~", ".")
                elif is_integer_dtype(type(num)) == True:
                    expected = "{:,}".format(num).replace(",", "~").replace(".", ",").replace("~", ".")

            num = text_sep_def(num=num, sep=sep)
            assert num == expected
