from grplot.features.add.text_add.text_add_def import text_add_def
import pytest

@pytest.mark.parametrize('input, expected', [
    (
        {
            'num': 10000,
            'add': 'Rp (_)'
        },
        'Rp 10000'
    ), (
        {
            'num': '-10000',
            'add': 'Rp (_)'
        },
        '(Rp 10000)'
    ), (
        {
            'num': 10000,
            'add': '(_) km'
        },
        '10000 km'
    ), (
        {
            'num': -10000,
            'add': '(_) km'
        },
        '(10000 km)'
    ), (
        {
            'num': 10000,
            'add': 'huge (_) km'
        },
        'huge 10000 km'
    ), (
        {
            'num': -10000,
            'add': 'huge (_) km'
        },
        '(huge 10000 km)'
    ), (
        {
            'num': 10000,
            'add': 'Rp _'
        },
        'Rp 10000'
    ), (
        {
            'num': -10000,
            'add': 'Rp _'
        },
        '-Rp 10000'
    ), (
        {
            'num': 10000,
            'add': '_ km'
        },
        '10000 km'
    ), (
        {
            'num': 10000,
            'add': 'huge _ km'
        },
        'huge 10000 km'
    ), (
        {
            'num': -10000,
            'add': 'huge _ km'
        },
        '-huge 10000 km'
    ), (
        {
            'num': 10000,
            'add': 'skadnasjkdnaskdj'
        },
        None
    )
])
def test_text_add_def(input, expected):
    try:
        num = text_add_def(**input)
    except:
        with pytest.raises(Exception):
            text_add_def(**input)
    else:
        assert num == expected