from grplot.features.sep.tick_sep.tick_sep_type import tick_sep_type


def check_tick_sep(df, ax, sep, xsep, ysep, xaxislabel, yaxislabel, axes):
    if xaxislabel is not None:
        if xsep is not None:
            tick_sep_type(df=df, ax=ax, axis='x', sep=xsep, axislabel=xaxislabel, axes=axes)
        else:
            tick_sep_type(df=df, ax=ax, axis='x', sep=sep, axislabel=xaxislabel, axes=axes)
    else:
        pass
    if yaxislabel is not None:
        if ysep is not None:
            tick_sep_type(df=df, ax=ax, axis='y', sep=ysep, axislabel=yaxislabel, axes=axes)
        else:
            tick_sep_type(df=df, ax=ax, axis='y', sep=sep, axislabel=yaxislabel, axes=axes)
    else:
        pass
    return ax