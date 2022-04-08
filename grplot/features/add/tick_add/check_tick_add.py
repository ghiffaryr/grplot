from grplot.features.add.tick_add.tick_add_type import tick_add_type


def check_tick_add(ax, add, xadd, yadd, xaxislabel, yaxislabel, axes):
    if xaxislabel is not None:
        if xadd is not None:
            tick_add_type(ax=ax, axis='x', add=xadd, axislabel=xaxislabel, axes=axes)
        else:
            tick_add_type(ax=ax, axis='x', add=add, axislabel=xaxislabel, axes=axes)
    else:
        pass
    if yaxislabel is not None:
        if yadd is not None:
            tick_add_type(ax=ax, axis='y', add=yadd, axislabel=yaxislabel, axes=axes)
        else:
            tick_add_type(ax=ax, axis='y', add=add, axislabel=yaxislabel, axes=axes)
    else:
        pass
    return ax