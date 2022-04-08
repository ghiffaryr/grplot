from grplot.features.add.statdesc_add.statdesc_add_def import statdesc_add_def
from grplot.utils.arg_axis_ax_type import arg_axis_ax_type


def statdesc_add_type(num, add, axislabel, axes):
    add = arg_axis_ax_type(arg=add, axislabel=axislabel, axes=axes)
    if add is None:
        pass
    elif type(add) == str:
        num = statdesc_add_def(num=num, add=add)
    else:
        raise Exception('Unknown statdesc add argument!')
    return num