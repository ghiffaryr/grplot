from grplot.features.add.log_label_add.log_label_add_def import log_label_add_def
import pytest

@pytest.mark.parametrize('_ax, input, expected', [
    (
        ['time', 'freq'],
        {
            'axis': 'x',
            'add': 'log'
        },
        ['log (time)', 'freq']
    ), (
        ['time', 'freq'],
        {
            'axis': 'y',
            'add': 'log'
        },
        ['time', 'log (freq)']
    ), (
        ['time', 'freq'],
        {
            'axis': None,
            'add': 'log'
        },
        None
    )
], indirect=['_ax'])
def test_log_label_add_def(_ax, input, expected):
    try:
        ax = log_label_add_def(_ax, **input)
    except:
        with pytest.raises(Exception):
            log_label_add_def(_ax, **input)
    else:
        expected_xlabel, expected_ylabel = expected
        assert ax.get_xlabel() == expected_xlabel
        assert ax.get_ylabel() == expected_ylabel