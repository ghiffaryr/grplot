from grplot.features.text.text_type import text_type


def check_text(plot, df, x, y, ax, ci, cumulative, multiple, text, xtext, ytext, sep, xsep, ysep, add, xadd, yadd, text_fontsize, xaxislabel, yaxislabel, axes):
    if plot in ['pieplot', 'treemapsplot', 'packedbubblesplot']:
        if x is not None:
            if xtext is not None:
                if xsep is not None:
                    if xadd is not None:
                        text_type(plot=plot, df=df, ax=ax, ci=None, cumulative=None, multiple=None, axis=None, text=xtext, sep=xsep, add=xadd, text_fontsize=text_fontsize, naxislabel=x, axislabel=None, axes=axes)
                    else:
                        text_type(plot=plot, df=df, ax=ax, ci=None, cumulative=None, multiple=None, axis=None, text=xtext, sep=xsep, add=add, text_fontsize=text_fontsize, naxislabel=x, axislabel=None, axes=axes)
                else:
                    if xadd is not None:
                        text_type(plot=plot, df=df, ax=ax, ci=None, cumulative=None, multiple=None, axis=None, text=xtext, sep=sep, add=xadd, text_fontsize=text_fontsize, naxislabel=x, axislabel=None, axes=axes)
                    else:
                        text_type(plot=plot, df=df, ax=ax, ci=None, cumulative=None, multiple=None, axis=None, text=xtext, sep=sep, add=add, text_fontsize=text_fontsize, naxislabel=x, axislabel=None, axes=axes)
            else:
                if xsep is not None:
                    if xadd is not None:
                        text_type(plot=plot, df=df, ax=ax, ci=None, cumulative=None, multiple=None, axis=None, text=text, sep=xsep, add=xadd, text_fontsize=text_fontsize, naxislabel=x, axislabel=None, axes=axes)
                    else:
                        text_type(plot=plot, df=df, ax=ax, ci=None, cumulative=None, multiple=None, axis=None, text=text, sep=xsep, add=add, text_fontsize=text_fontsize, naxislabel=x, axislabel=None, axes=axes)
                else:
                    if xadd is not None:
                        text_type(plot=plot, df=df, ax=ax, ci=None, cumulative=None, multiple=None, axis=None, text=text, sep=sep, add=xadd, text_fontsize=text_fontsize, naxislabel=x, axislabel=None, axes=axes)
                    else:
                        text_type(plot=plot, df=df, ax=ax, ci=None, cumulative=None, multiple=None, axis=None, text=text, sep=sep, add=add, text_fontsize=text_fontsize, naxislabel=x, axislabel=None, axes=axes)
        else:
            pass
        if y is not None:
            if ytext is not None:
                if ysep is not None:
                    if yadd is not None:
                        text_type(plot=plot, df=df, ax=ax, ci=None, cumulative=None, multiple=None, axis=None, text=ytext, sep=ysep, add=yadd, text_fontsize=text_fontsize, naxislabel=y, axislabel=None, axes=axes)
                    else:
                        text_type(plot=plot, df=df, ax=ax, ci=None, cumulative=None, multiple=None, axis=None, text=ytext, sep=ysep, add=add, text_fontsize=text_fontsize, naxislabel=y, axislabel=None, axes=axes)
                else:
                    if yadd is not None:
                        text_type(plot=plot, df=df, ax=ax, ci=None, cumulative=None, multiple=None, axis=None, text=ytext, sep=sep, add=yadd, text_fontsize=text_fontsize, naxislabel=y, axislabel=None, axes=axes)
                    else:
                        text_type(plot=plot, df=df, ax=ax, ci=None, cumulative=None, multiple=None, axis=None, text=ytext, sep=sep, add=add, text_fontsize=text_fontsize, naxislabel=y, axislabel=None, axes=axes)
            else:
                if ysep is not None:
                    if yadd is not None:
                        text_type(plot=plot, df=df, ax=ax, ci=None, cumulative=None, multiple=None, axis=None, text=text, sep=ysep, add=yadd, text_fontsize=text_fontsize, naxislabel=y, axislabel=None, axes=axes)
                    else:
                        text_type(plot=plot, df=df, ax=ax, ci=None, cumulative=None, multiple=None, axis=None, text=text, sep=ysep, add=add, text_fontsize=text_fontsize, naxislabel=y, axislabel=None, axes=axes)
                else:
                    if yadd is not None:
                        text_type(plot=plot, df=df, ax=ax, ci=None, cumulative=None, multiple=None, axis=None, text=text, sep=sep, add=yadd, text_fontsize=text_fontsize, naxislabel=y, axislabel=None, axes=axes)
                    else:
                        text_type(plot=plot, df=df, ax=ax, ci=None, cumulative=None, multiple=None, axis=None, text=text, sep=sep, add=add, text_fontsize=text_fontsize, naxislabel=y, axislabel=None, axes=axes)
        else:
            pass
    else:
        if xaxislabel is not None:
            if xtext is not None:
                if xsep is not None:
                    if xadd is not None:
                        text_type(plot=plot, df=df, ax=ax, ci=ci, cumulative=cumulative, multiple=multiple, axis='x', text=xtext, sep=xsep, add=xadd, text_fontsize=text_fontsize, naxislabel=x, axislabel=xaxislabel, axes=axes)
                    else:
                        text_type(plot=plot, df=df, ax=ax, ci=ci, cumulative=cumulative, multiple=multiple, axis='x', text=xtext, sep=xsep, add=add, text_fontsize=text_fontsize, naxislabel=x, axislabel=xaxislabel, axes=axes)
                else:
                    if xadd is not None:
                        text_type(plot=plot, df=df, ax=ax, ci=ci, cumulative=cumulative, multiple=multiple, axis='x', text=xtext, sep=sep, add=xadd, text_fontsize=text_fontsize, naxislabel=x, axislabel=xaxislabel, axes=axes)
                    else:
                        text_type(plot=plot, df=df, ax=ax, ci=ci, cumulative=cumulative, multiple=multiple, axis='x', text=xtext, sep=sep, add=add, text_fontsize=text_fontsize, naxislabel=x, axislabel=xaxislabel, axes=axes)
            else:
                if xsep is not None:
                    if xadd is not None:
                        text_type(plot=plot, df=df, ax=ax, ci=ci, cumulative=cumulative, multiple=multiple, axis='x', text=text, sep=xsep, add=xadd, text_fontsize=text_fontsize, naxislabel=x, axislabel=xaxislabel, axes=axes)
                    else:
                        text_type(plot=plot, df=df, ax=ax, ci=ci, cumulative=cumulative, multiple=multiple, axis='x', text=text, sep=xsep, add=add, text_fontsize=text_fontsize, naxislabel=x, axislabel=xaxislabel, axes=axes)
                else:
                    if xadd is not None:
                        text_type(plot=plot, df=df, ax=ax, ci=ci, cumulative=cumulative, multiple=multiple, axis='x', text=text, sep=sep, add=xadd, text_fontsize=text_fontsize, naxislabel=x, axislabel=xaxislabel, axes=axes)
                    else:
                        text_type(plot=plot, df=df, ax=ax, ci=ci, cumulative=cumulative, multiple=multiple, axis='x', text=text, sep=sep, add=add, text_fontsize=text_fontsize, naxislabel=x, axislabel=xaxislabel, axes=axes)
        else:
            pass
        if yaxislabel is not None:
            if ytext is not None:
                if ysep is not None:
                    if yadd is not None:
                        text_type(plot=plot, df=df, ax=ax, ci=ci, cumulative=cumulative, multiple=multiple, axis='y', text=ytext, sep=ysep, add=yadd, text_fontsize=text_fontsize, naxislabel=y, axislabel=yaxislabel, axes=axes)
                    else:
                        text_type(plot=plot, df=df, ax=ax, ci=ci, cumulative=cumulative, multiple=multiple, axis='y', text=ytext, sep=ysep, add=add, text_fontsize=text_fontsize, naxislabel=y, axislabel=yaxislabel, axes=axes)
                else:
                    if yadd is not None:
                        text_type(plot=plot, df=df, ax=ax, ci=ci, cumulative=cumulative, multiple=multiple, axis='y', text=ytext, sep=sep, add=yadd, text_fontsize=text_fontsize, naxislabel=y, axislabel=yaxislabel, axes=axes)
                    else:
                        text_type(plot=plot, df=df, ax=ax, ci=ci, cumulative=cumulative, multiple=multiple, axis='y', text=ytext, sep=sep, add=add, text_fontsize=text_fontsize, naxislabel=y, axislabel=yaxislabel, axes=axes)
            else:
                if ysep is not None:
                    if yadd is not None:
                        text_type(plot=plot, df=df, ax=ax, ci=ci, cumulative=cumulative, multiple=multiple, axis='y', text=text, sep=ysep, add=yadd, text_fontsize=text_fontsize, naxislabel=y, axislabel=yaxislabel, axes=axes)
                    else:
                        text_type(plot=plot, df=df, ax=ax, ci=ci, cumulative=cumulative, multiple=multiple, axis='y', text=text, sep=ysep, add=add, text_fontsize=text_fontsize, naxislabel=y, axislabel=yaxislabel, axes=axes)
                else:
                    if yadd is not None:
                        text_type(plot=plot, df=df, ax=ax, ci=ci, cumulative=cumulative, multiple=multiple, axis='y', text=text, sep=sep, add=yadd, text_fontsize=text_fontsize, naxislabel=y, axislabel=yaxislabel, axes=axes)
                    else:
                        text_type(plot=plot, df=df, ax=ax, ci=ci, cumulative=cumulative, multiple=multiple, axis='y', text=text, sep=sep, add=add, text_fontsize=text_fontsize, naxislabel=y, axislabel=yaxislabel, axes=axes)
        else:
            pass
    return ax