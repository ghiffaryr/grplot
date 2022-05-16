import pytest
from grplot.features.title.title_def import title_def
import matplotlib as mpl

@pytest.mark.parametrize('input,expected', [
    (('halo', None), ('halo')),
    (('halo', 15), ('halo')),
    (('halo', 'amigos'), (None))
])
def test_title_def(_ax: mpl.axes._axes.Axes, input: tuple[any, any], expected: any):
    try:
        title_def(_ax, *input)
    except:
        with pytest.raises(Exception):
            title_def(_ax, *input)
    else:
        assert _ax.get_title() == expected
