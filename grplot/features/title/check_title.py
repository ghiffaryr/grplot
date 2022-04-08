from grplot.features.title.title_def import title_def
from grplot.utils.arg_ax_type import arg_ax_type


def check_title(ax, title, title_fontsize, axes):
    title = arg_ax_type(arg=title, axes=axes)
    if title is None:
        pass
    elif type(title) == str:
        title_def(ax=ax, title=title, title_fontsize=title_fontsize)
    else:
        raise Exception('Unknown title argument!')
    return ax