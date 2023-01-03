from grplot.features.add.text_add.text_add_type import text_add_type
import pytest


class TestTextAddType:
    def test_pieplot_add_is_none(self):
        num = text_add_type(
            **{
                "plot": "pieplot",
                "num": 10000,
                "add": None,
                "axislabel": "time",
                "axes": None,
            }
        )

        assert num == 10000

    def test_lineplot_add_has_value(self):
        num = text_add_type(
            **{
                "plot": "line",
                "num": 10000,
                "add": "Rp (_)",
                "axislabel": "time",
                "axes": None,
            }
        )

        assert num == "Rp 10000"

    def test_unknown_text_add_argument(self):
        with pytest.raises(Exception) as exc_info:
            text_add_type(
                **{
                    "plot": "pieplot",
                    "num": 10000,
                    "add": [],
                    "axislabel": "time",
                    "axes": None,
                }
            )

        assert str(exc_info.value) == "Unknown text add argument!"
