def statdesc_plot_def(ax, axis, stat, color, stat_label, stat_fmt):
    if color is None:
        ax.plot([], [], alpha=0, color='white', label='{}: {}'.format(stat_label, stat_fmt))
    else:
        if axis == 'x':
            ax.axvline(stat, color=color, linestyle=':', label='{}: {}'.format(stat_label, stat_fmt))
        elif axis == 'y':
            ax.axhline(stat, color=color, linestyle=':', label='{}: {}'.format(stat_label, stat_fmt))
        else:
            raise Exception('Unsupported axis!')
    return ax