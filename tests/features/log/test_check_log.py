from grplot.features.log.check_log import check_log
import numpy
import pytest

@pytest.mark.parametrize('input, expected', [
    (
        {
            'log': 'logit',
            'xlog': 'logit',
            'ylog': 'logit',
            'xaxislabel': 'time',
            'yaxislabel': 'freq',
            'axes': None
        },
        [
            [0.01, 0.1,  0.5,  0.9,  0.99],
            [0.001 , 0.01  , 0.1   , 0.5   , 0.9   , 0.99  , 0.999 , 0.9999]
        ]
    ), (
        {
            'log': 'logit',
            'xlog': None,
            'ylog': None,
            'xaxislabel': 'time',
            'yaxislabel': 'freq',
            'axes': None
        },
        [
            [0.01, 0.1,  0.5,  0.9,  0.99],
            [0.001 , 0.01  , 0.1   , 0.5   , 0.9   , 0.99  , 0.999 , 0.9999]
        ]
    ), (
        {
            'log': 'logit',
            'xlog': None,
            'ylog': None,
            'xaxislabel': None,
            'yaxislabel': None,
            'axes': None
        },
        [
            [-2.5,  0. ,  2.5,  5. ,  7.5, 10. , 12.5],
            [-1.5, -1. , -0.5,  0. ,  0.5,  1. ,  1.5]
        ]
    )
])
def test_check_log(_ax, input, expected):
    try:
        ax = check_log(_ax, **input)
    except:
        with pytest.raises(Exception):
            check_log(_ax, **input)
    else:
        expected_x, expected_y = expected
        numpy.testing.assert_array_equal(ax.get_xticks(), expected_x)
        numpy.testing.assert_array_equal(ax.get_yticks(), expected_y)