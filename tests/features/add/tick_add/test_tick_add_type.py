from grplot.features.add.tick_add.tick_add_type import tick_add_type
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
        ['12', '1.25']
    ), (
        ['time', 'freq'],
        {
            'axis': 'y',
            'add': '_ km',
            'axislabel': 'freq',
            'axes': None 
        },
        ['12', '1.25 km']
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
def test_tick_add_type(_ax, input, expected):
    try:
        ax = tick_add_type(_ax, **input)
    except:
        with pytest.raises(Exception):
            tick_add_type(_ax, **input)
    else:
        expected_xlabel, expected_ylabel = expected
        assert ax.get_xticklabels()[-1].get_text() == expected_xlabel
        assert ax.get_yticklabels()[-1].get_text() == expected_ylabel