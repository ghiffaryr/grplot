from grplot.features.add.log_label_add.log_label_add_type import log_label_add_type
import pytest


class TestLogLabelAddType:
    @pytest.mark.parametrize("_ax", [(["time", "freq"])], indirect=["_ax"])
    def test_add_is_none(self, _ax):
        axislabel = "time"
        ax = log_label_add_type(_ax, axis="x", add=None, axislabel=axislabel, axes=None)
        assert ax.get_xlabel() == axislabel

    @pytest.mark.parametrize("_ax", [(["time", "freq"])], indirect=["_ax"])
    def test_add_has_value(self, _ax):
        ax = log_label_add_type(_ax, axis="x", add="log", axislabel="time", axes=None)
        assert ax.get_xlabel() == "log (time)"

    @pytest.mark.parametrize("_ax", [(["time", "freq"])], indirect=["_ax"])
    def test_unknown_log_label_argument(self, _ax):
        with pytest.raises(Exception) as exc_info:
            log_label_add_type(_ax, axis="x", add=[], axislabel="time", axes=None)
        assert str(exc_info.value) == "Unknown log label add argument!"
