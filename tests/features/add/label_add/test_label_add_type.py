from grplot.features.add.label_add.label_add_type import label_add_type
import pytest


class TestLabelAddType:
    @pytest.mark.parametrize("_ax", [(["time", "freq"])], indirect=["_ax"])
    def test_add_is_none(self, _ax):
        ax = label_add_type(ax=_ax, add=None, axes=None, axis="x", axislabel="time")

        assert ax.get_xlabel() == "time"
        assert ax.get_ylabel() == "freq"

    @pytest.mark.parametrize("_ax", [(["time", "freq"])], indirect=["_ax"])
    def test_add_has_value(self, _ax):
        ax = label_add_type(ax=_ax, add="_ (Hz)", axes=None, axis="y", axislabel="freq")

        assert ax.get_xlabel() == "time"
        assert ax.get_ylabel() == "freq (Hz)"

    @pytest.mark.parametrize("_ax", [(["time", "freq"])], indirect=["_ax"])
    def test_unknown_label_add_argument(self, _ax):
        with pytest.raises(Exception) as exc_info:
            label_add_type(ax=_ax, add=[], axes=None, axis="y", axislabel="freq")

        assert str(exc_info.value) == "Unknown label add argument!"
