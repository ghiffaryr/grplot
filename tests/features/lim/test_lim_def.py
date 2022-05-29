from grplot.features.lim.lim_def import lim_def
import pytest

@pytest.mark.parametrize('input, expected', [
    (
        {
            'axis': 'x',
            'lim': (0, 3)
        },
        3
    ), (
        {
            'axis': 'y',
            'lim': (0, 3)
        },
        3
    ), (
        {
            'axis': 'x',
            'lim': 'asd'
        },
        None
    ), (
        {
            'axis': 'y',
            'lim': 'asd'
        },
        None
    ), (
        {
            'axis': 'sdasd',
            'lim': 'asd'
        },
        None
    )
])
def test_lim_def(_ax, input, expected):
    try:
        ax = lim_def(_ax, **input)
    except:
        with pytest.raises(Exception):
            lim_def(_ax, *input)
    else:
        if input['axis'] == 'x':
            assert ax.get_xticks()[-1] == expected
        if input['axis'] == 'y':
            assert ax.get_yticks()[-1] == expected
