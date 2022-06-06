from grplot.features.dt.dt_def import dt_def
import pytest

@pytest.mark.parametrize('input, expected', [
    (
        {
            'axis': 'x',
            'dt': '%Y/%m/%d'
        },
        '2022/01/01'
    ), (
        {
            'axis': 'y',
            'dt': '%Y/%m/%d'
        },
        '1970/01/01'
    ), (
        {
            'axis': 'hola',
            'dt': '%Y/%m/%d'
        },
        None
    ), 
])
def test_dt_def(_ax, input, expected):
    try:
        ax, fig = _ax
        ax = dt_def(ax, **input)
        fig.canvas.draw()
    except:
        with pytest.raises(Exception):
            dt_def(_ax, **input)
    else:
        if input['axis'] == 'x':
            assert ax.get_xticklabels()[0].get_text() == expected
        if input['axis'] == 'y':
            assert ax.get_yticklabels()[0].get_text() == expected