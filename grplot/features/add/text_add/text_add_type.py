from grplot.features.add.text_add.text_add_def import text_add_def
from grplot.utils.arg_ax_type import arg_ax_type
from grplot.utils.arg_axis_ax_type import arg_axis_ax_type


def text_add_type(plot, num, add, axislabel, axes):
    if plot in ['pieplot', 'treemapsplot', 'packedbubblesplot']:
        add = arg_ax_type(arg=add, axes=axes)
    else:
        add = arg_axis_ax_type(arg=add, axislabel=axislabel, axes=axes)
    if add is None:
        pass
    elif type(add) == str:
        num = text_add_def(num=num, add=add)
    else:
        raise Exception('Unknown text add argument!')
    return num