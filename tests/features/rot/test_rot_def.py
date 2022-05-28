from grplot.features.rot.rot_def import rot_def
import matplotlib as mpl
import pytest

@pytest.mark.parametrize('input', [
    ({ 'axis': 'x', 'rot': 90}),
    ({ 'axis': 'y', 'rot': 90}),
    ({ 'axis': None, 'rot': 90}),
])
def test_rot_def(_ax: any, input: dict):
    try:
        rotated_tick_ax = rot_def(_ax, **input)
    except:
        with pytest.raises(Exception):
            rot_def(_ax, *input)
    else:
        if input['axis'] == 'x':
            for label in rotated_tick_ax.get_xticklabels():
                assert label.get_rotation() == input['rot']
        else:
            for label in rotated_tick_ax.get_yticklabels():
                assert label.get_rotation() == input['rot']
