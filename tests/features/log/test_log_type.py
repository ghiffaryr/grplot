from grplot.features.log.log_type import log_type
import numpy
import pytest

@pytest.mark.parametrize('input, expected', [
    (
        {
            'axis': 'x',
            'log': None,
            'axislabel': 'time',
            'axes': None
        },
        [-2.5,  0. ,  2.5,  5. ,  7.5, 10. , 12.5]
    ), (
        {
            'axis': 'x',
            'log': 'logit',
            'axislabel': 'time',
            'axes': None
        },
        [0.01, 0.1,  0.5,  0.9,  0.99]
    ), (
        {
            'axis': 'x',
            'log': [],
            'axislabel': 'time',
            'axes': None
        },
        None
    )
])
def test_log_type(_ax, input, expected):
    try:
        ax = log_type(_ax, **input)
    except:
        with pytest.raises(Exception):
            log_type(_ax, **input)
    else:
        numpy.testing.assert_array_equal(ax.get_xticks(), expected)