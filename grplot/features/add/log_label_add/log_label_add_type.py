from grplot.features.add.log_label_add.log_label_add_def import log_label_add_def
from grplot.utils.arg_axis_ax_type import arg_axis_ax_type


def log_label_add_type(ax, axis, add, axislabel, axes):
    add = arg_axis_ax_type(arg=add, axislabel=axislabel, axes=axes)
    if add is None:
        pass
    elif type(add) == str:
        log_label_add_def(ax=ax, axis=axis, add=add)
    else:
        raise Exception('Unknown log label add argument!')
    return ax