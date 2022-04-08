from grplot.features.statdesc.statdesc_multi_def import statdesc_multi_def
from grplot.utils.arg_axis_ax_type import arg_axis_ax_type


def statdesc_type(df, ax, axis, statdesc, sep, add, axislabel, axes):
    statdesc = arg_axis_ax_type(arg=statdesc, axislabel=axislabel, axes=axes)
    if statdesc is None:
        pass
    elif type(statdesc) == str:
        statdesc_multi_def(df=df, ax=ax, axis=axis, statdesc=statdesc, sep=sep, add=add, axislabel=axislabel, axes=axes)
    else:
        raise Exception('Unknown statdesc argument!')
    return ax