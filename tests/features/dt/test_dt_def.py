from grplot.features.dt.dt_def import dt_def
import pytest


class TestDtDef:
    def test_set_xaxis_formatter(self, _ax):
        ax, fig = _ax
        ax = dt_def(
            ax=ax,
            axis='x',
            dt='%Y/%m/%d'
        )
        fig.canvas.draw()

        assert ax.get_xticklabels()[0].get_text() == '2022/01/01'

    def test_set_yaxis_formatter(self, _ax):
        ax, fig = _ax
        ax = dt_def(
            ax=ax,
            axis='y',
            dt='%Y/%m/%d'
        )
        fig.canvas.draw()

        assert ax.get_yticklabels()[0].get_text() == '1970/01/01'

    def test_unsupported_axis(self, _ax):
        ax, _ = _ax
        with pytest.raises(Exception) as exc_info:
            dt_def(
                ax=ax,
                axis='kk',
                dt='%Y/%m/%d'
            )

        assert str(exc_info.value) == 'Unsupported axis!'
