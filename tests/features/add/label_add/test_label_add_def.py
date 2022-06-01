from grplot.features.add.label_add.label_add_def import label_add_def
import pytest


@pytest.mark.parametrize('_ax, input, expected', [
    (
        ['time', 'freq'],
        {
            'axis': 'x',
            'add': 'mantap(_)'
        },
        ['mantap(time)', 'freq']
    ), (
        ['time', 'freq'],
        {
            'axis': 'x',
            'add': 'huge _'
        },
        ['huge time', 'freq']
    ), (
        ['time', 'freq'],
        {
            'axis': 'x',
            'add': '_(ms)'
        },
        ['time(ms)', 'freq']
    ), (
        ['time', 'freq'],
        {
            'axis': 'y',
            'add': 'mantap(_)'
        },
        ['time', 'mantap(freq)']
    ), (
        ['time', 'freq'],
        {
            'axis': 'y',
            'add': 'huge _'
        },
        ['time', 'huge freq']
    ), (
        ['time', 'freq'],
        {
            'axis': 'y',
            'add': '_(Hz)'
        },
        ['time', 'freq(Hz)']
    ), (
        ['time', 'freq'],
        {
            'axis': 'x',
            'add': 'mantap'
        },
            None
    ), (
        ['time', 'freq'],
        {
            'axis': 'y',
            'add': 'mantap'
        },
        None
    ), (
        ['time', 'freq'],
        {
            'axis': 'halo',
            'add': 'mantap'
        },
        None
    )
], indirect=['_ax'])
def test_label_add_def(_ax, input, expected):
    try:
        ax = label_add_def(_ax, **input)
    except:
        with pytest.raises(Exception):
            label_add_def(_ax, **input)
    else:
        expected_xlabel, expected_ylabel = expected
        assert ax.get_xlabel() == expected_xlabel
        assert ax.get_ylabel() == expected_ylabel