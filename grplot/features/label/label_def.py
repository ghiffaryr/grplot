def label_def(ax, axis, label):
    if axis == 'x':
        ax.set_xlabel(label)
    elif axis == 'y':
        ax.set_ylabel(label)
    else:
        raise Exception('Unsupported axis!')
    return ax