from grplot.features.log.log_type import log_type


def check_log(ax, log, xlog, ylog, xaxislabel, yaxislabel, axes):
    if xaxislabel is not None:
        if xlog is not None:
            log_type(ax=ax, axis='x', log=xlog, axislabel=xaxislabel, axes=axes)
        else:
            log_type(ax=ax, axis='x', log=log, axislabel=xaxislabel, axes=axes)
    else:
        pass
    if yaxislabel is not None:
        if ylog is not None:
            log_type(ax=ax, axis='y', log=ylog, axislabel=yaxislabel, axes=axes)
        else:
            log_type(ax=ax, axis='y', log=log, axislabel=yaxislabel, axes=axes)
    else:
        pass
    return ax