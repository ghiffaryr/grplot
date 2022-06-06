from grplot.features.dt.check_dt import check_dt
import pytest

@pytest.mark.parametrize('input, expected', [
    (
        {
            'dt': None,
            'xdt': '%Y/%m/%d',
            'ydt': '%Y/%m/%d',
            'xaxislabel': 'x',
            'yaxislabel': 'y',
            'axes': None
        },
        ['2022/01/01', '1970/01/01']
    ), (
        {
            'dt': '%Y/%m/%d',
            'xdt': None,
            'ydt': None,
            'xaxislabel': 'x',
            'yaxislabel': 'y',
            'axes': None
        },
        ['2022/01/01', '1970/01/01']
    ), (
        {
            'dt': '%Y/%m/%d',
            'xdt': None,
            'ydt': None,
            'xaxislabel': None,
            'yaxislabel': None,
            'axes': None
        },
        ['2022-01-01', '0.5']
    ),
])
def test_dt_type(_ax, input, expected):
    ax, fig = _ax
    ax = check_dt(ax, **input)
    fig.canvas.draw()

    assert ax.get_xticklabels()[0].get_text() == expected[0]
    assert ax.get_yticklabels()[0].get_text() == expected[1]