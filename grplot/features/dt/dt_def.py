import matplotlib.dates as mdates


def dt_def(ax, axis, dt):
    if axis == 'x':
        if type(dt) == str:
            ax.xaxis.set_major_formatter(mdates.DateFormatter(dt))
        else:
            raise Exception('Unknown dt argument!')
    elif axis == 'y':
        if type(dt) == str:
            ax.yaxis.set_major_formatter(mdates.DateFormatter(dt))
        else:
            raise Exception('Unknown dt argument!')
    else:
        raise Exception('Unsupported axis!')
    return ax
