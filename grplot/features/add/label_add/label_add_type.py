from grplot.features.add.label_add.label_add_def import label_add_def
from grplot.utils.arg_axis_ax_type import arg_axis_ax_type


def label_add_type(ax, axis, add, axislabel, axes):
    add = arg_axis_ax_type(arg=add, axislabel=axislabel, axes=axes)
    if add is None:
        pass
    elif type(add) == str:
        label_add_def(ax=ax, axis=axis, add=add)
    else:
        raise Exception('Unknown label add argument!')
    return ax