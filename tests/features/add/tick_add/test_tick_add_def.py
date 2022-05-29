from grplot.features.add.tick_add.tick_add_def import tick_add_def
import pytest

@pytest.mark.parametrize('_ax, input, expected', [
    (
        ['time', 'freq'],
        {
            'axis': 'x',
            'add': 'Rp (_)',
        },
        ['Rp 12', '1.25']
    ), (
         ['time', 'freq'],
        {
            'axis': 'x',
            'add': '(_) km',
        },
        ['12 km', '1.25']
    ), (
         ['time', 'freq'],
        {
            'axis': 'x',
            'add': 'huge (_) km',
        },
        ['huge 12 km', '1.25']
    ), (
        ['time', 'freq'],
        {
            'axis': 'x',
            'add': 'Rp _',
        },
        ['Rp 12', '1.25']
    ), (
         ['time', 'freq'],
        {
            'axis': 'x',
            'add': '_ km',
        },
        ['12 km', '1.25']
    ), (
         ['time', 'freq'],
        {
            'axis': 'x',
            'add': 'huge _ km',
        },
        ['huge 12 km', '1.25']
    ), (
        ['time', 'freq'],
        {
            'axis': 'y',
            'add': 'Rp (_)',
        },
        ['12', 'Rp 1.25']
    ), (
         ['time', 'freq'],
        {
            'axis': 'y',
            'add': '(_) km',
        },
        ['12', '1.25 km']
    ), (
         ['time', 'freq'],
        {
            'axis': 'y',
            'add': 'huge (_) km',
        },
        ['12', 'huge 1.25 km']
    ), (
        ['time', 'freq'],
        {
            'axis': 'y',
            'add': 'Rp _',
        },
        ['12', 'Rp 1.25']
    ), (
        ['time', 'freq'],
        {
            'axis': 'y',
            'add': '_ km',
        },
        ['12', '1.25 km']
    ), (
        ['time', 'freq'],
        {
            'axis': 'y',
            'add': 'huge _ km',
        },
        ['12', 'huge 1.25 km']
    ), (
        ['time', 'freq'],
        {
            'axis': 'x',
            'add': 'huge',
        },
        None
    ), (
        ['time', 'freq'],
        {
            'axis': 'y',
            'add': 'huge',
        },
        None
    ), (
        ['time', 'freq'],
        {
            'axis': 'soy',
            'add': 'huge',
        },
        None
    )
], indirect=['_ax'])
def test_tick_add_def(_ax, input, expected):
    try:
        ax = tick_add_def(_ax, **input)
    except:
        with pytest.raises(Exception):
            tick_add_def(_ax, **input)
    else:
        expected_xlabel, expected_ylabel = expected
        assert ax.get_xticklabels()[-1].get_text() == expected_xlabel
        assert ax.get_yticklabels()[-1].get_text() == expected_ylabel