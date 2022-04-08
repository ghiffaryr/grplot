from grplot.features.dt.dt_def import dt_def
from grplot.utils.arg_axis_ax_type import arg_axis_ax_type


def dt_type(ax, axis, dt, axislabel, axes):
    dt = arg_axis_ax_type(arg=dt, axislabel=axislabel, axes=axes)
    if dt is None:
        pass
    elif type(dt) == str:
        dt_def(ax=ax, axis=axis, dt=dt)
    else:
        raise Exception('Unknown dt argument!')
    return ax