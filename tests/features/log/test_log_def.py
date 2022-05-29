from grplot.features.log.log_def import log_def
import numpy
import pytest

@pytest.mark.parametrize('input, expected', [
    (
        {
            'axis': 'x',
            'log': 'logit'
        },
        [0.01, 0.1,  0.5,  0.9,  0.99]
    ), (
        {
            'axis': 'y',
            'log': 'logit'
        },
        [0.001, 0.01, 0.1, 0.5, 0.9, 0.99, 0.999, 0.9999]
    ), (
        {
            'axis': 'x',
            'log': 'alakazam'
        },
        None
    ), (
        {
            'axis': 'y',
            'log': 'alakazam'
        },
        None
    ), (
        {
            'axis': 'sas',
            'log': 'alakazam'
        },
        None
    )
])
def test_log_def(_ax, input, expected):
    try:
        ax = log_def(_ax, **input)
    except:
        with pytest.raises(Exception):
            log_def(_ax, **input)
    else:
        if input['axis'] == 'x':
            numpy.testing.assert_array_equal(ax.get_xticks(), expected)
        
        if input['axis'] == 'y':
            numpy.testing.assert_array_equal(ax.get_yticks(), expected)