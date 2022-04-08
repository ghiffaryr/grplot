import numpy
from pandas.api.types import is_numeric_dtype, is_object_dtype, is_categorical_dtype
from grplot.utils.arg_ax_type import arg_ax_type


def font_def(plot, df, x, y, ax, axes, tick_fontsize, legend_fontsize, label_fontsize, hue, size, h, l):
    plot, hue, size = map(arg_ax_type, (plot, hue, size), numpy.hstack([axes]*3))
    if plot is None:
        pass
    elif type(plot) == str:
        # axis tick font size
        if tick_fontsize is not None:
            ax.tick_params(axis='both', labelsize=tick_fontsize)
            if 'paretoplot' in plot:
                if ((is_object_dtype(df[x]) == True) or (is_object_dtype(type(df[x][0])) == True) or (is_categorical_dtype(df[x]) == True) or (is_categorical_dtype(type(df[x][0])) == True)) and ((is_numeric_dtype(df[y]) == True) or (is_numeric_dtype(type(df[y][0])) == True)):
                    try:
                        ax.get_shared_x_axes().get_siblings(ax)[0].tick_params(axis='both', labelsize=tick_fontsize)
                    except:
                        raise Exception('Unknown tick fontsize argument!')
                elif ((is_numeric_dtype(df[x]) == True) or (is_numeric_dtype(type(df[x][0])) == True)) and ((is_object_dtype(df[y]) == True) or (is_object_dtype(type(df[y][0])) == True) or (is_categorical_dtype(df[y]) == True) or (is_categorical_dtype(type(df[y][0])) == True)):
                    try:
                        ax.get_shared_y_axes().get_siblings(ax)[0].tick_params(axis='both', labelsize=tick_fontsize)
                    except:
                        raise Exception('Unknown tick fontsize argument!')
                else:
                    raise Exception('Either x or y must be numerical or object data type!')
            else:
                pass
        else:
            pass
        # legend font size
        if ax.get_legend_handles_labels() != ([], []):
            # temporary fix for histplot legend, waiting for seaborn to fix it's source code
            if hue is not None or size is not None:
                if 'histplot' in plot:
                    handles, labels = ax.get_legend_handles_labels()
                    try:
                        ax.legend(handles+h, labels+l, fontsize=legend_fontsize)
                    except:
                        raise Exception('Unknown legend fontsize argument!')
                else:
                    if plot in ['pieplot', 'treemapsplot']:
                        pass
                    else:
                        try:
                            ax.legend(fontsize=legend_fontsize)
                        except:
                            raise Exception('Unknown legend fontsize argument!')
            else:
                if plot in ['pieplot', 'treemapsplot']:
                    pass
                else:
                    try:
                        ax.legend(fontsize=legend_fontsize)
                    except:
                        raise Exception('Unknown legend fontsize argument!')
        else:
            pass
        # axis label font size
        if label_fontsize is not None:
            try:
                ax.xaxis.get_label().set_fontsize(label_fontsize)
                ax.yaxis.get_label().set_fontsize(label_fontsize)
            except:
                raise Exception('Unknown label fontsize argument!')
            if 'paretoplot' in plot:
                if ((is_object_dtype(df[x]) == True) or (is_object_dtype(type(df[x][0])) == True) or (is_categorical_dtype(df[x]) == True) or (is_categorical_dtype(type(df[x][0])) == True)) and ((is_numeric_dtype(df[y]) == True) or (is_numeric_dtype(type(df[y][0])) == True)):
                    try:
                        ax.get_shared_x_axes().get_siblings(ax)[0].yaxis.get_label().set_fontsize(label_fontsize)
                    except:
                        raise Exception('Unknown label fontsize argument!')
                elif ((is_numeric_dtype(df[x]) == True) or (is_numeric_dtype(type(df[x][0])) == True)) and ((is_object_dtype(df[y]) == True) or (is_object_dtype(type(df[y][0])) == True) or (is_categorical_dtype(df[y]) == True) or (is_categorical_dtype(type(df[y][0])) == True)):
                    try:
                        ax.get_shared_y_axes().get_siblings(ax)[0].xaxis.get_label().set_fontsize(label_fontsize)
                    except:
                        raise Exception('Unknown label fontsize argument!')
                else:
                    raise Exception('Either x or y must be numerical or object data type!')
            else:
                pass
        else:
            pass
    else:
        raise Exception('Unknown plot argument!')
    return ax