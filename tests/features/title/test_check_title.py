import pytest
from grplot.features.title.check_title import check_title
import matplotlib as mpl

@pytest.mark.parametrize('input,expected', [
    ((None, None, None), (None)),
    (('halo', None, None), ('halo')),
    ((1, None, None), (None)),
])
def test_check_title_is_None(_ax: mpl.axes._axes.Axes, input: tuple, expected: any):
    try:
        axes = check_title(_ax, *input)
    except:
        with pytest.raises(Exception):
            check_title(_ax, *input)
    else:
        if input[1] is None :
            assert axes == _ax
        else:
            _ax.get_title == expected
        