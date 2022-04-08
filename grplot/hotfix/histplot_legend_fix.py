import numpy
from grplot.utils.arg_ax_type import arg_ax_type


def histplot_legend_fix(plot, ax, hue, size, legend_fontsize, axes):
    plot, hue, size = map(arg_ax_type, (plot, hue, size), numpy.hstack([axes]*3))
    # temporary fix for histplot legend, waiting for seaborn to fix it's source code
    if hue is not None or size is not None:
        if plot is None:
            pass
        elif type(plot) == str:
            if 'histplot' in plot:
                h = ax.legend_.legendHandles
                l = [t.get_text() for t in ax.legend_.texts]
                ax.legend(h, l, fontsize=legend_fontsize)
            else:
                h = []
                l = [] 
        else:
            raise Exception('Unknown plot argument!')
    else:
        h = []
        l = []
    return h, l