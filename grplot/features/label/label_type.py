from grplot.features.label.label_def import label_def
from grplot.utils.arg_ax_type import arg_ax_type


def label_type(ax, axis, label, axes):
    label = arg_ax_type(arg=label, axes=axes)
    if label is None:
        pass
    elif type(label) == str:
        label_def(ax=ax, axis=axis, label=label)
    else:
        raise Exception('Unknown label argument!')
    return ax