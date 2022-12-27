from grplot.features.dt.dt_type import dt_type
import pytest


class TestDtType:
    def test_dt_is_none(self, _ax):
        ax, fig = _ax
        ax = dt_type(
            ax=ax,
            axes=None,
            dt=None,
            axis='x',
            axislabel='x'
        )
        fig.canvas.draw()

        assert ax.get_xticklabels()[0].get_text() == '2022-01-01'

    def test_dt_has_value(self, _ax):
        ax, fig = _ax
        ax = dt_type(
            ax=ax,
            axes=None,
            dt='%Y/%m/%d',
            axis='x',
            axislabel='x'
        )
        fig.canvas.draw()

        assert ax.get_xticklabels()[0].get_text() == '2022/01/01'

    def test_unknown_dt_argument(self, _ax):
        ax, _ = _ax
        with pytest.raises(Exception) as exc_info:
            dt_type(
                ax=ax,
                axes=None,
                dt=[],
                axis='x',
                axislabel='x'
            )

        assert str(exc_info.value) == "Unknown dt argument!"
