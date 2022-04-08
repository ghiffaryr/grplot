import matplotlib.dates as mdates


def dt_def(ax, axis, dt):
    if axis == 'x':
        try:
            ax.xaxis.set_major_formatter(mdates.DateFormatter(dt))
        except:
            raise Exception('Unknown dt argument!')
    elif axis == 'y':
        try:
            ax.yaxis.set_major_formatter(mdates.DateFormatter(dt))
        except:
            raise Exception('Unknown dt argument!')
    else:
        raise Exception('Unsupported axis!')
    return ax