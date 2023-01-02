from grplot.features.add.statdesc_add.statdesc_add_type import statdesc_add_type
import pytest


class TestStatdescAddType:
    def test_add_is_none(self):
        num = statdesc_add_type(add=None, axislabel="time", num=10000, axes=None)
        assert num == 10000

    def test_add_has_value(self):
        num = statdesc_add_type(add="Rp (_)", axislabel="time", num=10000, axes=None)
        assert num == "Rp 10000"

    def test_unknown_statdesc_add_argument(self):
        with pytest.raises(Exception) as exc_info:
            statdesc_add_type(
                add=[],
                axes=None,
                axislabel="time",
                num=10000,
            )
        assert str(exc_info.value) == "Unknown statdesc add argument!"
