from grplot.features.add.log_label_add.log_label_add_type import log_label_add_type


def check_log_label_add(ax, add, xadd, yadd, xaxislabel, yaxislabel, axes):
    if xaxislabel is not None:
        if xadd is not None:
            log_label_add_type(ax=ax, axis='x', add=xadd, axislabel=xaxislabel, axes=axes)
        else:
            log_label_add_type(ax=ax, axis='x', add=add, axislabel=xaxislabel, axes=axes)
    else:
        pass
    if yaxislabel is not None:
        if yadd is not None:
            log_label_add_type(ax=ax, axis='y', add=yadd, axislabel=yaxislabel, axes=axes)
        else:
            log_label_add_type(ax=ax, axis='y', add=add, axislabel=yaxislabel, axes=axes)
    else:
        pass
    return ax