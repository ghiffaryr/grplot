from grplot.features.lim.lim_def import lim_def
import pytest


class TestLimDef:
    def test_x_lim(self, _ax):
        ax = lim_def(
            ax=_ax,
            axis='x',
            lim=(0, 3)
        )

        assert ax.get_xticks()[-1] == 3

    def test_y_lim(self, _ax):
        ax = lim_def(
            ax=_ax,
            axis='y',
            lim=(0, 3)
        )

        assert ax.get_yticks()[-1] == 3

    @pytest.mark.parametrize('axis', [('x'), ('y')])
    def test_unknown_lim_argument(self, _ax, axis):
        with pytest.raises(Exception) as exc_info:
            lim_def(
                ax=_ax,
                axis=axis,
                lim='yoyo'
            )

        assert str(exc_info.value) == "Unknown lim argument!"

    def test_unsupported_axis(self, _ax):
        with pytest.raises(Exception) as exc_info:
            lim_def(
                ax=_ax,
                axis='y2k',
                lim=(0, 3)
            )

        assert str(exc_info.value) == "Unsupported axis!"
