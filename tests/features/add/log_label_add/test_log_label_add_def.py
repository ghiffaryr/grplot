from grplot.features.add.log_label_add.log_label_add_def import log_label_add_def
import pytest


class TestLogLabelAddDef:
    @pytest.mark.parametrize("_ax", [(["time", "freq"])], indirect=["_ax"])
    def test_set_x_label(self, _ax):
        ax = log_label_add_def(_ax, axis="x", add="log")
        assert ax.get_xlabel() == "log (time)"

    @pytest.mark.parametrize("_ax", [(["time", "freq"])], indirect=["_ax"])
    def test_set_y_label(self, _ax):
        ax = log_label_add_def(_ax, axis="y", add="log")
        assert ax.get_ylabel() == "log (freq)"

    @pytest.mark.parametrize("_ax", [(["time", "freq"])], indirect=["_ax"])
    def test_unsupported_axis(self, _ax):
        with pytest.raises(Exception) as exc_info:
            log_label_add_def(_ax, axis=None, add="log")

        assert str(exc_info.value) == "Unsupported axis!"
