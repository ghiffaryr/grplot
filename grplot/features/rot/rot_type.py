from grplot.features.rot.rot_def import rot_def
from grplot.utils.arg_axis_ax_type import arg_axis_ax_type


def rot_type(ax, axis, rot, axislabel, axes):
    rot = arg_axis_ax_type(arg=rot, axislabel=axislabel, axes=axes)
    if rot is None:
        pass
    elif type(rot) in [int, float]:
        rot_def(ax=ax, axis=axis, rot=rot)
    else:
        raise Exception('Unknown rot argument!')
    return ax