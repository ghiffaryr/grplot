from grplot.features.add.label_add.label_add_type import label_add_type
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
            'axis': 'y',
            'add': '_ (Hz)',
            'axislabel': 'freq',
            'axes': None 
        },
        ['time', 'freq (Hz)']
    ), (
         ['time', 'freq'],
        {
            'axis': 'y',
            'add': [],
            'axislabel': 'freq',
            'axes': None 
        },
        None
    )
], indirect=['_ax'])
def test_label_add_type(_ax, input, expected):
    try:
        ax = label_add_type(_ax, **input)
    except:
        with pytest.raises(Exception):
            label_add_type(_ax, **input)
    else:
        expected_xlabel, expected_ylabel = expected
        assert ax.get_xlabel() == expected_xlabel
        assert ax.get_ylabel() == expected_ylabel