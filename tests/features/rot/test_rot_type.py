from grplot.features.rot.rot_type import rot_type
from grplot.utils.arg_axis_ax_type import arg_axis_ax_type
import pytest

@pytest.mark.parametrize('input,expected', [
    ([None, None, None, None], 90),
    (['x', 90, None, None], 90),
    (['x', 'hola', None, None], None)
])
def test_rot_type(_ax: any, input: list, expected: any):
    try:
        rotated_ax = rot_type(_ax, *input)
    except:
        with pytest.raises(Exception):
            rot_type(_ax, *input)
    else:
        for label in rotated_ax.get_xticklabels():
            assert label.get_rotation() == expected
    
