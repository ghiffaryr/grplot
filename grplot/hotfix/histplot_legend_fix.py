def histplot_legend_fix(plot, ax, hue, size, legend_fontsize):
    # temporary fix for histplot legend, waiting for seaborn to fix it's source code
    if hue is not None or size is not None:
        if plot == 'histplot':
            h = ax.legend_.legendHandles
            l = [t.get_text() for t in ax.legend_.texts]
            ax.legend(h, l, fontsize=legend_fontsize)
        else:
            h = []
            l = [] 
    else:
        h = []
        l = []
    return h, l