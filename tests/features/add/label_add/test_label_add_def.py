from grplot.features.add.label_add.label_add_def import label_add_def
import pytest


class TestLabelAddDef:
    @pytest.mark.parametrize("_ax", [(["time", "freq"])], indirect=["_ax"])
    def test_unsupported_axis(self, _ax):
        with pytest.raises(Exception) as exc_info:
            label_add_def(add="mantap", ax=_ax, axis="halo")

        assert str(exc_info.value) == "Unsupported axis!"

    @pytest.mark.parametrize(
        "_ax, axis",
        [(["time", "freq"], "x"), (["time", "freq"], "y")],
        indirect=["_ax"],
    )
    def test_unknown_label_argument(self, _ax, axis):
        with pytest.raises(Exception) as exc_info:
            label_add_def(ax=_ax, add="mantap", axis=axis)

        assert str(exc_info.value) == "Unknown label add argument!"

    @pytest.mark.parametrize(
        "_ax, input, expected",
        [
            (["time", "freq"], {"axis": "x", "add": "mantap(_)"}, "mantap(time)"),
            (["time", "freq"], {"axis": "x", "add": "huge _"}, "huge time"),
            (["time", "freq"], {"axis": "x", "add": "_(ms)"}, "time(ms)"),
        ],
        indirect=["_ax"],
    )
    def test_add_prefix_suffix_in_x_label(self, _ax, input, expected):
        ax = label_add_def(_ax, **input)
        assert ax.get_xlabel() == expected

    @pytest.mark.parametrize(
        "_ax, input, expected",
        [
            (["time", "freq"], {"axis": "y", "add": "mantap(_)"}, "mantap(freq)"),
            (["time", "freq"], {"axis": "y", "add": "huge _"}, "huge freq"),
            (["time", "freq"], {"axis": "y", "add": "_(Hz)"}, "freq(Hz)"),
        ],
        indirect=["_ax"],
    )
    def test_add_prefix_suffix_in_y_label(self, _ax, input, expected):
        ax = label_add_def(_ax, **input)
        assert ax.get_ylabel() == expected
