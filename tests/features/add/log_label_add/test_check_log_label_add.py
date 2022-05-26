from grplot.features.add.log_label_add.check_log_label_add import check_log_label_add
import pytest

@pytest.mark.parametrize('_ax, input, expected', [
    (
        ['time', 'freq'],
        {
            'add': None,
            'axes': None,
            'xadd': 'log',
            'yadd': 'log' ,
            'xaxislabel': 'time',
            'yaxislabel': 'freq',
        },
        ['log (time)', 'log (freq)']
    ), (
        ['time', 'freq'],
        {
            'add': 'log',
            'axes': None,
            'xadd': None,
            'yadd': None ,
            'xaxislabel': 'time',
            'yaxislabel': 'freq',
        },
        ['log (time)', 'log (freq)']
    ), (
        ['time', 'freq'],
        {
            'add': 'log',
            'axes': None,
            'xadd': None,
            'yadd': None ,
            'xaxislabel': None,
            'yaxislabel': None,
        },
        ['time', 'freq']
    )
], indirect=['_ax'])
def test_check_log_label_add(_ax, input, expected):
    try:
        ax = check_log_label_add(_ax, **input)
    except:
        with pytest.raises(Exception):
            check_log_label_add(_ax, **input)
    else:
        expected_xlabel, expected_ylabel = expected
        assert ax.get_xlabel() == expected_xlabel
        assert ax.get_ylabel() == expected_ylabel