from grplot.features.statdesc.statdesc_plot_def import statdesc_plot_def;
import pytest

@pytest.mark.parametrize('_ax,input,expected', [
    (
        (0, 0),
        {
            'axis': 'x',
            'stat': 0.5,
            'color': 'green',
            'stat_label': 'hola',
            'stat_fmt': 'amigo'
        }, ('green', ':')
    ), (
        (1, 0),
        {
            'axis': 'y',
            'stat': 0.5,
            'color': 'green',
            'stat_label': 'hola',
            'stat_fmt': 'amigo'
        }, ('green', ':')
    ),
    (
        (1, 1),
        {
            'axis': None,
            'stat': None,
            'color': None,
            'stat_label': 'hola',
            'stat_fmt': 'amigo'
        }, ('white', '-')
    ), (
        (0, 1),
        {
            'axis': 'halo',
            'stat': 0.5,
            'color': 'green',
            'stat_label': 'hola',
            'stat_fmt': 'amigo'
        }, (None)
    )
], indirect=['_ax'])
def test_statdesc_plot_def(_ax, input, expected):
    try:
        new_plot = statdesc_plot_def(_ax, **input)
    except(Exception):
        with pytest.raises(Exception):
            statdesc_plot_def(_ax, **input)
    else:
        assert new_plot.get_lines()[0].get_color() == expected[0]
        assert new_plot.get_lines()[0].get_linestyle() == expected[1]
