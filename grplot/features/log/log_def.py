from matplotlib import ticker


def log_def(ax, axis, log):
    if axis == 'x':
        try:
            ax.set_xscale(log)
            ax.xaxis.set_major_formatter(ticker.ScalarFormatter(useLocale=False))
        except:
            raise Exception('Unknown log argument!')
    elif axis == 'y':
        try:
            ax.set_yscale(log)
            ax.yaxis.set_major_formatter(ticker.ScalarFormatter(useLocale=False))
        except:
            raise Exception('Unknown log argument!')
    else:
        raise Exception('Unsupported axis!')
    return ax