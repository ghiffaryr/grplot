from grplot.features.add.log_label_add.log_label_add_type import log_label_add_type
import pytest

@pytest.mark.parametrize('_ax, input, expected', [
    (
        ['time', 'freq'],
        {
            'axis': 'x',
            'add': None,
            'axislabel': 'time',
            'axes': None
        },
        ['time', 'freq']
    ), (
        ['time', 'freq'],
        {
            'axis': 'x',
            'add': 'log',
            'axislabel': 'time',
            'axes': None
        },
        ['log (time)', 'freq']
    ), (
        ['time', 'freq'],
        {
            'axis': 'x',
            'add': [],
            'axislabel': 'time',
            'axes': None
        },
        None
    )
], indirect=['_ax'])
def test_log_label_add_type(_ax, input, expected):
    try:
        ax = log_label_add_type(_ax, **input)
    except:
        with pytest.raises(Exception):
            log_label_add_type(_ax, **input)
    else:
        expected_xlabel, expected_ylabel = expected
        assert ax.get_xlabel() == expected_xlabel
        assert ax.get_ylabel() == expected_ylabel