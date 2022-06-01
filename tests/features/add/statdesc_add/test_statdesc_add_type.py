from grplot.features.add.statdesc_add.statdesc_add_type import statdesc_add_type
import pytest

@pytest.mark.parametrize('input, expected', [
    (
        {
            'num': 10000,
            'add': None,
            'axislabel': 'time',
            'axes': None
        },
        10000
    ), (
        {
            'num': 10000,
            'add': 'Rp (_)',
            'axislabel': 'time',
            'axes': None
        },
        'Rp 10000'
    ), (
        {
            'num': 10000,
            'add': [],
            'axislabel': 'time',
            'axes': None
        },
        None
    )
])
def test_statdesc_add_type(input, expected):
    try:
        num = statdesc_add_type(**input)
    except:
        with pytest.raises(Exception):
            statdesc_add_type(**input)
    else:
        assert num == expected