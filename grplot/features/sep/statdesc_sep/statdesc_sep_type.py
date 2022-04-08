from grplot.features.sep.statdesc_sep.statdesc_sep_data_def import statdesc_sep_data_def
from grplot.utils.arg_axis_ax_type import arg_axis_ax_type


def statdesc_sep_type(num, stat_label, sep, axislabel, axes):
    sep = arg_axis_ax_type(arg=sep, axislabel=axislabel, axes=axes)
    if sep is None:
        pass
    elif type(sep) == str:
        num = statdesc_sep_data_def(num=num, stat_label=stat_label, sep=sep)
    else:
        raise Exception('Unknown sep argument!')
    return num