from grplot.features.lim.lim_type import lim_type


def check_lim(ax, lim, xlim, ylim, xaxislabel, yaxislabel, axes):
    if xaxislabel is not None:
        if xlim is not None:
            lim_type(ax=ax, axis='x', lim=xlim, axislabel=xaxislabel, axes=axes)
        else:
            lim_type(ax=ax, axis='x', lim=lim, axislabel=xaxislabel, axes=axes)
    else:
        pass
    if yaxislabel is not None:
        if ylim is not None:
            lim_type(ax=ax, axis='y', lim=ylim, axislabel=yaxislabel, axes=axes)
        else:
            lim_type(ax=ax, axis='y', lim=lim, axislabel=yaxislabel, axes=axes)
    else:
        pass
    return ax