from grplot.features.lim.lim_def import lim_def
from grplot.utils.arg_axis_ax_type import arg_axis_ax_type


def lim_type(ax, axis, lim, axislabel, axes):
    lim = arg_axis_ax_type(arg=lim, axislabel=axislabel, axes=axes)
    if lim is None:
        pass
    elif type(lim) == list:
        lim_def(ax=ax, axis=axis, lim=lim)
    else:
        raise Exception('Unknown lim argument!')
    return ax