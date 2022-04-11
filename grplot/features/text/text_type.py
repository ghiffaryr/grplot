from grplot.features.text.text_def import text_def
from grplot.utils.arg_ax_type import arg_ax_type
from grplot.utils.arg_axis_ax_type import arg_axis_ax_type


def text_type(plot, df, ax, ci, cumulative, multiple, axis, text, sep, add, text_fontsize, naxislabel, axislabel, axes):
    if plot in ['pieplot', 'treemapsplot', 'packedbubblesplot']:
        text = arg_ax_type(arg=text, axes=axes)
    else:
        text = arg_axis_ax_type(arg=text, axislabel=axislabel, axes=axes)
    if text is None:
        pass
    elif type(text) in [str, bool]:
        text_def(plot=plot, df=df, ax=ax, ci=ci, cumulative=cumulative, multiple=multiple, axis=axis, text=text, sep=sep, add=add, text_fontsize=text_fontsize, naxislabel=naxislabel, axislabel=axislabel, axes=axes)
    else:
        raise Exception('Unknown text argument!')
    return ax