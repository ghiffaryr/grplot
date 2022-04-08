from grplot.utils.arg_ax_type import arg_ax_type


def check_fontsize(fontsize, tick_fontsize, legend_fontsize, text_fontsize, label_fontsize, title_fontsize, axes):
    tick_fontsize = arg_ax_type(arg=tick_fontsize, axes=axes)
    legend_fontsize = arg_ax_type(arg=legend_fontsize, axes=axes)
    text_fontsize = arg_ax_type(arg=text_fontsize, axes=axes)
    label_fontsize = arg_ax_type(arg=label_fontsize, axes=axes)
    title_fontsize = arg_ax_type(arg=title_fontsize, axes=axes)
    # check fontsize
    if tick_fontsize is None:
        tick_fontsize = fontsize
    else:
        pass
    if legend_fontsize is None:
        legend_fontsize = fontsize
    else:
        pass
    if text_fontsize is None:
        text_fontsize = fontsize
    else:
        pass
    if label_fontsize is None:
        label_fontsize = fontsize
    else:
        pass
    if title_fontsize is None:
        title_fontsize = fontsize
    else:
        pass
    return tick_fontsize, legend_fontsize, text_fontsize, label_fontsize, title_fontsize