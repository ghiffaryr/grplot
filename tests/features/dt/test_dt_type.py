from grplot.features.dt.dt_type import dt_type
import pytest

@pytest.mark.parametrize('input, expected', [
    (
        {
            'axis': 'x',
            'dt': None,
            'axislabel': 'x',
            'axes': None
        },
        '2022-01-01'
    ), (
        {
            'axis': 'x',
            'dt': '%Y/%m/%d',
            'axislabel': 'x',
            'axes': None
        },
        '2022/01/01'
    ), (
        {
            'axis': 'x',
            'dt': [],
            'axislabel': 'x',
            'axes': None
        },
        None
    )
])
def test_dt_type(_ax, input, expected):
    try:
        ax, fig = _ax
        ax = dt_type(ax, **input)
        fig.canvas.draw()
    except:
        with pytest.raises(Exception):
            dt_type(_ax, **input)
    else:
        assert ax.get_xticklabels()[0].get_text() == expected