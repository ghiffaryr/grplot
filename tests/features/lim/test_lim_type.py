from grplot.features.lim.lim_type import lim_type
import pytest

@pytest.mark.parametrize('input, expected', [
    (
        {
            'axis': 'x',
            'lim': None,
            'axislabel': 'time',
            'axes': None
        },
        6
    ), (
        {
            'axis': 'x',
            'lim': [0, 3],
            'axislabel': 'time',
            'axes': None
        },
        3
    ), (
        {
            'axis': 'x',
            'lim': 'sadds',
            'axislabel': 'time',
            'axes': None
        },
        3
    )
])
def test_lim_type(_ax, input, expected):
    try:
        ax = lim_type(_ax, **input)
    except:
        with pytest.raises(Exception):
            lim_type(_ax, *input)
    else:
        assert ax.get_xticks()[-1] == expected
