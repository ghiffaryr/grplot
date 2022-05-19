from grplot.features.rot.check_rot import check_rot
import pytest

@pytest.mark.parametrize('input, expected', [
    (
        {
            'rot': 90,
            'xrot': None,
            'yrot': None,
            'xaxislabel': None,
            'yaxislabel': None,
            'axes' : None
        }, [0, 0]
    ), (
        {
            'rot': 90,
            'xrot': None,
            'yrot': None,
            'xaxislabel': 'hola',
            'yaxislabel': 'amigos',
            'axes' : None
        }, [90, 90]
    ), (
        {
            'rot': 90,
            'xrot': 17,
            'yrot': 71,
            'xaxislabel': 'hola',
            'yaxislabel': 'amigos',
            'axes' : None
        }, [17, 71]
    )
])
def test_check_rot(_ax, input, expected):
    rotated_ax = check_rot(_ax, **input)
    [x_rot_val, y_rot_val] = expected
    for label in rotated_ax.get_xticklabels():
            assert label.get_rotation() == x_rot_val
    for label in rotated_ax.get_yticklabels():
            assert label.get_rotation() == y_rot_val
