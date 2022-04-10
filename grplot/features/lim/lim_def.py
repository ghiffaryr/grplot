def lim_def(ax, axis, lim):
    if axis == 'x':
        try:
            ax.set_xlim(lim)
        except:
            raise Exception('Unknown lim argument!')
    elif axis == 'y':
        try:
            ax.set_ylim(lim)
        except:
            raise Exception('Unknown lim argument!')
    else:
        raise Exception('Unsupported axis!')
    return ax