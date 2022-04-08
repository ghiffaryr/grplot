def title_def(ax, title, title_fontsize):
    if title_fontsize is None:
        ax.set_title(label=title)
    else: # title_fontsize is not None
        try:
            ax.set_title(label=title, fontsize=title_fontsize)
        except:
            raise Exception('Unknown title fontsize argument!')
    return ax