from grplot.features.statdesc.statdesc_type import statdesc_type


def check_statdesc(df, ax, statdesc, xstatdesc, ystatdesc, sep, xsep, ysep, add, xadd, yadd, xaxislabel, yaxislabel, axes):
    if xaxislabel is not None:
        if xstatdesc is not None:
            if xsep is not None:
                if xadd is not None:
                    statdesc_type(df=df, ax=ax, axis='x', statdesc=xstatdesc, sep=xsep, add=xadd, axislabel=xaxislabel, axes=axes)
                else:
                    statdesc_type(df=df, ax=ax, axis='x', statdesc=xstatdesc, sep=xsep, add=add, axislabel=xaxislabel, axes=axes)
            else:
                if xadd is not None:
                    statdesc_type(df=df, ax=ax, axis='x', statdesc=xstatdesc, sep=sep, add=xadd, axislabel=xaxislabel, axes=axes)
                else:
                    statdesc_type(df=df, ax=ax, axis='x', statdesc=xstatdesc, sep=sep, add=add, axislabel=xaxislabel, axes=axes)
        else:
            if xsep is not None:
                if xadd is not None:
                    statdesc_type(df=df, ax=ax, axis='x', statdesc=statdesc, sep=xsep, add=xadd, axislabel=xaxislabel, axes=axes)
                else:
                    statdesc_type(df=df, ax=ax, axis='x', statdesc=statdesc, sep=xsep, add=add, axislabel=xaxislabel, axes=axes)
            else:
                if xadd is not None:
                    statdesc_type(df=df, ax=ax, axis='x', statdesc=statdesc, sep=sep, add=xadd, axislabel=xaxislabel, axes=axes)
                else:
                    statdesc_type(df=df, ax=ax, axis='x', statdesc=statdesc, sep=sep, add=add, axislabel=xaxislabel, axes=axes)
    else:
        pass
    if yaxislabel is not None:
        if ystatdesc is not None:
            if ysep is not None:
                if yadd is not None:
                    statdesc_type(df=df, ax=ax, axis='y', statdesc=ystatdesc, sep=ysep, add=yadd, axislabel=yaxislabel, axes=axes)
                else:
                    statdesc_type(df=df, ax=ax, axis='y', statdesc=ystatdesc, sep=ysep, add=add, axislabel=yaxislabel, axes=axes)
            else:
                if yadd is not None:
                    statdesc_type(df=df, ax=ax, axis='y', statdesc=ystatdesc, sep=sep, add=yadd, axislabel=yaxislabel, axes=axes)
                else:
                    statdesc_type(df=df, ax=ax, axis='y', statdesc=ystatdesc, sep=sep, add=add, axislabel=yaxislabel, axes=axes)
        else:
            if ysep is not None:
                if yadd is not None:
                    statdesc_type(df=df, ax=ax, axis='y', statdesc=statdesc, sep=ysep, add=yadd, axislabel=yaxislabel, axes=axes)
                else:
                    statdesc_type(df=df, ax=ax, axis='y', statdesc=statdesc, sep=ysep, add=add, axislabel=yaxislabel, axes=axes)
            else:
                if yadd is not None:
                    statdesc_type(df=df, ax=ax, axis='y', statdesc=statdesc, sep=sep, add=yadd, axislabel=yaxislabel, axes=axes)
                else:
                    statdesc_type(df=df, ax=ax, axis='y', statdesc=statdesc, sep=sep, add=add, axislabel=yaxislabel, axes=axes)
    else:
        pass
    return ax