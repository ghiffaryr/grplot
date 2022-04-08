from grplot.features.sep.tick_sep.tick_sep_data_def import tick_sep_data_def
from grplot.utils.arg_axis_ax_type import arg_axis_ax_type


def tick_sep_type(df, ax, axis, sep, axislabel, axes):
    sep = arg_axis_ax_type(arg=sep, axislabel=axislabel, axes=axes)
    if sep is None:
        pass
    elif type(sep) == str:
        tick_sep_data_def(df=df, ax=ax, axis=axis, axislabel=axislabel, sep=sep)
    else:
        raise Exception('Unknown sep argument!')
    return ax