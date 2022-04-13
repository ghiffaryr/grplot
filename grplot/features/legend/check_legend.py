def check_legend(plot, ax, legend_fontsize, legend_loc, hue, size, h, l):
    # legend font size
    if ax.get_legend_handles_labels() != ([], []):
        # temporary fix for histplot legend, waiting for seaborn to fix it's source code
        if hue is not None or size is not None:
            if plot == 'histplot':
                handles, labels = ax.get_legend_handles_labels()
                if legend_loc is None:
                    try:
                        ax.legend(handles+h, labels+l, fontsize=legend_fontsize)
                    except:
                        raise Exception('Unknown legend fontsize argument!')
                else:
                    try:
                        ax.legend(handles+h, labels+l, loc=legend_loc, fontsize=legend_fontsize)
                    except:
                        raise Exception('Unknown legend loc argument!')
            else:
                if plot in ['pieplot', 'treemapsplot', 'packedbubblesplot']:
                    pass
                else:
                    if legend_loc is None:
                        try:
                            ax.legend(fontsize=legend_fontsize)
                        except:
                            raise Exception('Unknown legend fontsize argument!')
                    else:
                        try:
                            ax.legend(loc=legend_loc, fontsize=legend_fontsize)
                        except:
                            raise Exception('Unknown legend loc argument!')
        else:
            if plot in ['pieplot', 'treemapsplot', 'packedbubblesplot']:
                pass
            else:
                if legend_loc is None:
                    try:
                        ax.legend(fontsize=legend_fontsize)
                    except:
                        raise Exception('Unknown legend fontsize argument!')
                else:
                    try:
                        ax.legend(loc=legend_loc, fontsize=legend_fontsize)
                    except:
                        raise Exception('Unknown legend loc argument!')
    else:
        pass
    return ax