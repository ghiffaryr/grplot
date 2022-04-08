def log_label_add_def(ax, axis, add):
    if axis == 'x':
        ax.set_xlabel('{} ({})'.format(add, ax.get_xlabel()))
    elif axis == 'y':
        ax.set_ylabel('{} ({})'.format(add, ax.get_ylabel()))
    else:
        raise Exception('Unsupported axis!')
    return ax