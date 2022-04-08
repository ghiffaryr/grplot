from grplot.features.add.label_add.label_add_type import label_add_type


def check_label_add(ax, add, xadd, yadd, xaxislabel, yaxislabel, axes):
    if xaxislabel is not None:
        if xadd is not None:
            label_add_type(ax=ax, axis='x', add=xadd, axislabel=xaxislabel, axes=axes)
        else:
            label_add_type(ax=ax, axis='x', add=add, axislabel=xaxislabel, axes=axes)
    else:
        pass
    if yaxislabel is not None:
        if yadd is not None:
            label_add_type(ax=ax, axis='y', add=yadd, axislabel=yaxislabel, axes=axes)
        else:
            label_add_type(ax=ax, axis='y', add=add, axislabel=yaxislabel, axes=axes)
    else:
        pass
    return ax