from grplot.features.statdesc.statdesc_plot_def import statdesc_plot_def
import pytest


class TestStatdescPlotDef:
    @pytest.mark.parametrize('_ax', [((0, 0))], indirect=['_ax'])
    def test_color_is_none(self, _ax):
        new_plot = statdesc_plot_def(
            _ax,
            axis=None,
            stat=None,
            color=None,
            stat_label='hola',
            stat_fmt='amigo'
        )

        assert new_plot.get_lines()[0].get_color() == 'white'
        assert new_plot.get_lines()[0].get_linestyle() == '-'

    @pytest.mark.parametrize('_ax', [((0, 1))], indirect=['_ax'])
    def test_x_axis(self, _ax):
        new_plot = statdesc_plot_def(
            _ax,
            axis='x',
            stat=0.5,
            color='green',
            stat_label='hola',
            stat_fmt='amigo'
        )

        assert new_plot.get_lines()[0].get_color() == 'green'
        assert new_plot.get_lines()[0].get_linestyle() == ':'

    @pytest.mark.parametrize('_ax', [((1, 0))], indirect=['_ax'])
    def test_y_axis(self, _ax):
        new_plot = statdesc_plot_def(
            _ax,
            axis='x',
            stat=0.5,
            color='green',
            stat_label='hola',
            stat_fmt='amigo'
        )

        assert new_plot.get_lines()[0].get_color() == 'green'
        assert new_plot.get_lines()[0].get_linestyle() == ':'

    @pytest.mark.parametrize('_ax', [((1, 0))], indirect=['_ax'])
    def test_axis_unsupported(self, _ax):
        with pytest.raises(Exception) as exc_info:
            statdesc_plot_def(
                _ax,
                axis='halo',
                stat=0.5,
                color='green',
                stat_label='hola',
                stat_fmt='amigo'
            )

        assert str(exc_info.value) == 'Unsupported axis!'
