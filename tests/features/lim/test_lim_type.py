from grplot.features.lim.lim_type import lim_type
import pytest


class TestLimType:
    def test_lim_is_none(self, _ax):
        ax = lim_type(
            ax=_ax,
            axis='x',
            axes=None,
            axislabel='time',
            lim=None
        )

        assert ax.get_xticks()[-1] == 6

    def test_lim_has_array_value(self, _ax):
        lim = [0, 3]
        ax = lim_type(
            ax=_ax,
            axis='x',
            axes=None,
            axislabel='time',
            lim=lim
        )

        assert ax.get_xticks()[-1] == lim[-1]

    def test_unknown_lim_argument(self, _ax):
        with pytest.raises(Exception) as exc_info:
            lim_type(
                ax=_ax,
                axis='x',
                axes=None,
                axislabel='time',
                lim='yo'
            )

        assert str(exc_info.value) == 'Unknown lim argument!'
