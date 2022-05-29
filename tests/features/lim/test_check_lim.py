from grplot.features.lim.check_lim import check_lim
import pytest

@pytest.mark.parametrize('input, expected', [
    (
        {
            'lim': [0, 3],
            'xlim': None,
            'ylim': None,
            'xaxislabel': 'time',
            'yaxislabel': 'freq',
            'axes': None
        },
        [3, 3]
    ), (
        {
            'lim': [0, 3],
            'xlim': [0, 3],
            'ylim': [0, 3],
            'xaxislabel': 'time',
            'yaxislabel': 'freq',
            'axes': None
        },
        [3, 3]
    ), (
        {
            'lim': [0, 3],
            'xlim': [0, 3],
            'ylim': [0, 3],
            'xaxislabel': None,
            'yaxislabel': None,
            'axes': None
        },
        [6, 6]
    )
])
def test_check_lim(_ax, input, expected):
    ax = check_lim(_ax, **input)

    assert ax.get_xticks()[-1] == expected[0]
    assert ax.get_yticks()[-1] == expected[1]
