from cmath import exp
from grplot.features.font.check_fontsize import check_fontsize
import pytest
import numpy as np

@pytest.mark.parametrize('input, expected', [
    (
        {
            'fontsize': None,
            'tick_fontsize': 14,
            'legend_fontsize': 14,
            'text_fontsize': 14,
            'label_fontsize': 14,
            'title_fontsize': 14,
            'axes': None
        },
        [14 for i in range(5)]
    ), (
        {
            'fontsize': 15,
            'tick_fontsize': None,
            'legend_fontsize': None,
            'text_fontsize': None,
            'label_fontsize': None,
            'title_fontsize': None,
            'axes': None
        },
        [15 for i in range(5)]
    )
])
def test_check_fontsize(input, expected):
    font_sizes = check_fontsize(**input)
    np.testing.assert_array_almost_equal(font_sizes, expected)

