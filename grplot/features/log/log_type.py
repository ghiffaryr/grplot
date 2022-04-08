from grplot.features.log.log_def import log_def
from grplot.utils.arg_axis_ax_type import arg_axis_ax_type


def log_type(ax, axis, log, axislabel, axes):
    log = arg_axis_ax_type(arg=log, axislabel=axislabel, axes=axes)
    if log is None:
        pass
    elif type(log) == str:
        log_def(ax=ax, axis=axis, log=log)
    else:
        raise Exception('Unknown log argument!')
    return ax