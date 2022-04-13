from grplot.features.sep.text_sep.text_sep_data_def import text_sep_data_def
from grplot.utils.arg_ax_type import arg_ax_type
from grplot.utils.arg_axis_ax_type import arg_axis_ax_type


def text_sep_type(plot, df, num, sep, axislabel, axes):
    if plot in ['pieplot', 'treemapsplot', 'packedbubblesplot']:
        sep = arg_ax_type(arg=sep, axes=axes)
    else:
        sep = arg_axis_ax_type(arg=sep, axislabel=axislabel, axes=axes)
    if sep is None:
        pass
    elif type(sep) == str:
        num = text_sep_data_def(df=df, num=num, axislabel=axislabel, sep=sep)
    else:
        raise Exception('Unknown sep argument!')
    return num