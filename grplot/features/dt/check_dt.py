from grplot.features.dt.dt_type import dt_type


def check_dt(ax, dt, xdt, ydt, xaxislabel, yaxislabel, axes):
    if xaxislabel is not None:
        if xdt is not None:
            dt_type(ax=ax, axis='x', dt=xdt, axislabel=xaxislabel, axes=axes)
        else:
            dt_type(ax=ax, axis='x', dt=dt, axislabel=xaxislabel, axes=axes)
    else:
        pass
    if yaxislabel is not None:
        if ydt is not None:
            dt_type(ax=ax, axis='y', dt=ydt, axislabel=yaxislabel, axes=axes)
        else:
            dt_type(ax=ax, axis='y', dt=dt, axislabel=yaxislabel, axes=axes)
    else:
        pass
    return ax