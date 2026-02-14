from grplot.features.label.label_type import label_type


def check_label(ax, xlabel, ylabel, axes):
    if xlabel is not None:
        label_type(ax=ax, axis='x', label=xlabel, axes=axes)
    else:
        pass
    if ylabel is not None:
        label_type(ax=ax, axis='y', label=ylabel, axes=axes)
    else:
        pass
    return ax