from ast import Num
from grplot.features.add.statdesc_add.statdesc_add_def import statdesc_add_def
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
def test_statdesc_add_def(input, expected):
    try:
        num = statdesc_add_def(**input)
    except:
        with pytest.raises(Exception):
            statdesc_add_def(**input)
    else:
        assert num == expected