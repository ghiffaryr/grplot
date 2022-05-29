from grplot.features.add.text_add.text_add_type import text_add_type
import pytest

@pytest.mark.parametrize('input, expected', [
    (
        {
            'plot': 'pieplot',
            'num': 10000,
            'add': None,
            'axislabel': 'time',
            'axes': None
        },
        10000
    ), (
        {
            'plot': 'line',
            'num': 10000,
            'add': 'Rp (_)',
            'axislabel': 'time',
            'axes': None
        },
        'Rp 10000'
    ), (
        {
            'plot': 'pieplot',
            'num': 10000,
            'add': [],
            'axislabel': 'time',
            'axes': None
        },
        None
    )
])
def test_text_add_type(input, expected):
    try:
        num = text_add_type(**input)
    except:
        with pytest.raises(Exception):
            text_add_type(**input)
    else:
        assert num == expected