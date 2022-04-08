from grplot.features.add.tick_add.tick_add_def import tick_add_def
from grplot.utils.arg_axis_ax_type import arg_axis_ax_type


def tick_add_type(ax, axis, add, axislabel, axes):
    add = arg_axis_ax_type(arg=add, axislabel=axislabel, axes=axes)
    if add is None:
        pass
    elif type(add) == str:
        tick_add_def(ax=ax, axis=axis, add=add)
    else:
        raise Exception('Unknown tick add argument!')
    return ax