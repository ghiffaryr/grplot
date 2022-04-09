import numpy
from pandas.api.types import is_numeric_dtype
import matplotlib
from grplot.features.add.text_add.text_add_type import text_add_type
from grplot.features.sep.text_sep.text_sep_type import text_sep_type
from grplot.utils.arg_ax_type import arg_ax_type


def text_def(plot, df, ax, ci, cumulative, multiple, axis, text, sep, add, text_fontsize, naxislabel, axislabel, axes):
    ci, cumulative, multiple = map(arg_ax_type, (ci, cumulative, multiple), numpy.hstack([axes]*3))
    if plot is None:
        pass
    elif type(plot) == str:
        if ('histplot' in plot) or ('barplot' in plot) or ('countplot' in plot) or ('paretoplot' in plot):
            # check ci
            if (ci is not None) or (multiple in ['fill', 'stack']):
                if 'o' in text:
                    text = text.replace('o','i')
                elif 'h' in text:
                    text = 'h+i'
                elif 'v' in text:
                    text = 'v+i'
                else:
                    pass
            else:
                pass
            # get patches
            if cumulative is not None:
                if cumulative == True:
                    text_patches = ax.patches[len(ax.patches)//2:]
                else: # cumulative == False
                    text_patches = ax.patches
            else: 
                text_patches = ax.patches
            # get patches height and width data
            list_height = numpy.array([p.get_height() for p in ax.patches])
            list_width = numpy.array([p.get_width() for p in ax.patches])
            # get patches max height and width data
            if list_height.size != 0:
                max_height = max(list_height)
                # barplot calibration
                if ('barplot' in plot) or ('paretoplot' in plot):
                    max_height = max_height * 2
                else:
                    pass
            else:
                raise Exception('Patches height must not be an empty list!')
            if list_width.size != 0:
                max_width = max(list_width)
                # barplot calibration
                if ('barplot' in plot) or ('paretoplot' in plot):
                    max_width = max_width * 2
                else:
                    pass
            else:
                raise Exception('Patches width must not be an empty list!')
            # numerical check for main axis of histplot, barplot, countplot, barplot in paretoplot
            numeric = False
            if axislabel in df:
                if (is_numeric_dtype(df[axislabel]) == True) or (is_numeric_dtype(type(df[axislabel][0])) == True):
                    numeric = True
                else:
                    pass
            else: # axislabel not in df, special case as in histogram, barplot, etc.
                if axislabel in ['Probability', 'Proportion', 'Density', 'Count', 'Frequency', 'Percent']:
                    numeric = True
                else:
                    pass
            # annotate for histplot, barplot, countplot, barplot in paretoplot
            if numeric == True:
                if axis == 'x':
                    if text in ['h', 'h+o', 'o+h']:
                        for p in text_patches:
                            left, bottom, width, height = p.get_bbox().bounds
                            if width != 0:
                                width_sep = text_sep_type(num=width, df=df, sep=sep, axislabel=axislabel, axes=axes)
                                width_add = text_add_type(num=width_sep, add=add, axislabel=axislabel, axes=axes)
                                if text_fontsize is not None:
                                    try:
                                        ax.annotate((f'{width_add}'), xy=(width+max_width*0.0175*text_fontsize/10, bottom+height/2), ha='center', va='center', fontsize=text_fontsize, rotation=270)
                                    except:
                                        raise Exception('Unknown text fontsize argument!')
                                else:
                                    ax.annotate((f'{width_add}'), xy=(width+max_width*0.0175, bottom+height/2), ha='center', va='center', rotation=270)
                            else:
                                pass
                    elif text in ['v', 'v+o', 'o+v']:
                        for p in text_patches:
                            left, bottom, width, height = p.get_bbox().bounds
                            if width != 0:
                                width_sep = text_sep_type(num=width, df=df, sep=sep, axislabel=axislabel, axes=axes)
                                width_add = text_add_type(num=width_sep, add=add, axislabel=axislabel, axes=axes)
                                if text_fontsize is not None:
                                    try:
                                        ax.annotate((f'{width_add}'), xy=(width+max_width*0.0175*text_fontsize/10, bottom+height/2), ha='left', va='center', fontsize=text_fontsize)
                                    except:
                                        raise Exception('Unknown text fontsize argument!')
                                else:
                                    ax.annotate((f'{width_add}'), xy=(width+max_width*0.0175, bottom+height/2), ha='left', va='center')
                            else:
                                pass
                    elif text in ['i', 'i+v', 'v+i']:
                        for p in text_patches:
                            left, bottom, width, height = p.get_bbox().bounds
                            if width != 0:
                                width_sep = text_sep_type(num=width, df=df, sep=sep, axislabel=axislabel, axes=axes)
                                width_add = text_add_type(num=width_sep, add=add, axislabel=axislabel, axes=axes)
                                if text_fontsize is not None:
                                    try:
                                        ax.annotate((f'{width_add}'), xy=(left+width/2, bottom+height/2), ha='center', va='center', fontsize=text_fontsize)
                                    except:
                                        raise Exception('Unknown text fontsize argument!')
                                else:
                                    ax.annotate((f'{width_add}'), xy=(left+width/2, bottom+height/2), ha='center', va='center')
                            else:
                                pass
                    elif text in ['i+h', 'h+i']:
                        for p in text_patches:
                            left, bottom, width, height = p.get_bbox().bounds
                            if width != 0:
                                width_sep = text_sep_type(num=width, df=df, sep=sep, axislabel=axislabel, axes=axes)
                                width_add = text_add_type(num=width_sep, add=add, axislabel=axislabel, axes=axes)
                                if text_fontsize is not None:
                                    try:
                                        ax.annotate((f'{width_add}'), xy=(left+width/2, bottom+height/2), ha='center', va='center', fontsize=text_fontsize, rotation=270)
                                    except:
                                        raise Exception('Unknown text fontsize argument!')
                                else:
                                    ax.annotate((f'{width_add}'), xy=(left+width/2, bottom+height/2), ha='center', va='center', rotation=270)
                            else:
                                pass
                    else:
                        pass
                elif axis == 'y':
                    if text in ['h', 'h+o', 'o+h']:
                        for p in text_patches:
                            left, bottom, width, height = p.get_bbox().bounds
                            if height != 0:
                                height_sep = text_sep_type(num=height, df=df, sep=sep, axislabel=axislabel, axes=axes)
                                height_add = text_add_type(num=height_sep, add=add, axislabel=axislabel, axes=axes)
                                if text_fontsize is not None:
                                    try:
                                        ax.annotate((f'{height_add}'), xy=(left+width/2, height+max_height*0.0325*text_fontsize/10), ha='center', va='center', fontsize=text_fontsize)
                                    except:
                                        raise Exception('Unknown text fontsize argument!')
                                else:
                                    ax.annotate((f'{height_add}'), xy=(left+width/2, height+max_height*0.0325), ha='center', va='center')
                            else:
                                pass
                    elif text in ['v', 'v+o', 'o+v']:
                        for p in text_patches:
                            left, bottom, width, height = p.get_bbox().bounds
                            if height != 0:
                                height_sep = text_sep_type(num=height, df=df, sep=sep, axislabel=axislabel, axes=axes)
                                height_add = text_add_type(num=height_sep, add=add, axislabel=axislabel, axes=axes)
                                if text_fontsize is not None:
                                    try:
                                        ax.annotate((f'{height_add}'), xy=(left+width/2, height+max_height*0.0325*text_fontsize/10), ha='center', va='bottom', fontsize=text_fontsize, rotation=90)
                                    except:
                                        raise Exception('Unknown text fontsize argument!')
                                else:
                                    ax.annotate((f'{height_add}'), xy=(left+width/2, height+max_height*0.0325), ha='center', va='bottom', rotation=90)
                            else:
                                pass
                    elif text in ['i', 'i+v', 'v+i']:
                        for p in text_patches:
                            left, bottom, width, height = p.get_bbox().bounds
                            if height != 0:
                                height_sep = text_sep_type(num=height, df=df, sep=sep, axislabel=axislabel, axes=axes)
                                height_add = text_add_type(num=height_sep, add=add, axislabel=axislabel, axes=axes)
                                if text_fontsize is not None:
                                    try:
                                        ax.annotate((f'{height_add}'), xy=(left+width/2, bottom+height/2), ha='center', va='center', fontsize=text_fontsize, rotation=90)
                                    except:
                                        raise Exception('Unknown text fontsize argument!')
                                else:
                                    ax.annotate((f'{height_add}'), xy=(left+width/2, bottom+height/2), ha='center', va='center', rotation=90)
                            else:
                                pass
                    elif text in ['i+h', 'h+i']:
                        for p in text_patches:
                            left, bottom, width, height = p.get_bbox().bounds
                            if height != 0:
                                height_sep = text_sep_type(num=height, df=df, sep=sep, axislabel=axislabel, axes=axes)
                                height_add = text_add_type(num=height_sep, add=add, axislabel=axislabel, axes=axes)
                                if text_fontsize is not None:
                                    try:
                                        ax.annotate((f'{height_add}'), xy=(left+width/2, bottom+height/2), ha='center', va='center', fontsize=text_fontsize)
                                    except:
                                        raise Exception('Unknown text fontsize argument!')
                                else:
                                    ax.annotate((f'{height_add}'), xy=(left+width/2, bottom+height/2), ha='center', va='center')
                            else:
                                pass
                    else:
                        pass
                else:
                    raise Exception('Unsupported axis!')
            else:
                pass
            # annotate for lineplot in paretoplot
            if ('paretoplot' in plot) and (text in ['h', 'h+o', 'o+h', 'v', 'v+o', 'o+v', 'i', 'i+v', 'v+i', 'i+h', 'h+i']):
                if axis == 'x':
                    for data in ax.get_shared_y_axes().get_siblings(ax)[0].get_lines():
                        x_arr, y_arr = data.get_data()
                        # get max x data points
                        if x_arr.size != 0:
                            max_x = max(x_arr)
                        else:
                            raise Exception('x-axis data points must not be an empty list!')
                        for x, y in zip(x_arr, y_arr):
                            # annotate
                            x_sep = text_sep_type(num=x, df=df, sep=sep, axislabel='Cumulative Percentage', axes=axes)
                            x_add = text_add_type(num=x_sep, add='_%', axislabel='Cumulative Percentage', axes=axes)
                            if text_fontsize is not None:
                                try:
                                    ax.get_shared_y_axes().get_siblings(ax)[0].annotate(f'{x_add}', xy=(x+max_x*0.0175*text_fontsize/10, y), fontsize=text_fontsize, ha='left', va='center')
                                except:
                                    raise Exception('Unknown text fontsize argument!')
                            else:
                                ax.get_shared_y_axes().get_siblings(ax)[0].annotate(f'{x_add}', xy=(x+max_x*0.0175, y), ha='left', va='center')
                elif axis == 'y':
                    for data in ax.get_shared_x_axes().get_siblings(ax)[0].get_lines():
                        x_arr, y_arr = data.get_data()
                        # get max y data points
                        if y_arr.size != 0:
                            max_y = max(y_arr)
                        else:
                            raise Exception('y-axis data points must not be an empty list!')
                        for x, y in zip(x_arr, y_arr):
                            # annotate
                            y_sep = text_sep_type(num=y, df=df, sep=sep, axislabel='Cumulative Percentage', axes=axes)
                            y_add = text_add_type(num=y_sep, add='_%', axislabel='Cumulative Percentage', axes=axes)
                            if text_fontsize is not None:
                                try:
                                    ax.get_shared_x_axes().get_siblings(ax)[0].annotate(f'{y_add}', xy=(x, y+max_y*0.0325*text_fontsize/10), fontsize=text_fontsize, ha='center', va='center')
                                except:
                                    raise Exception('Unknown text fontsize argument!')
                            else:
                                ax.get_shared_x_axes().get_siblings(ax)[0].annotate(f'{y_add}', xy=(x, y+max_y*0.0325), ha='center', va='center')
                else:
                    raise Exception('Unsupported axis!')
            else:
                pass
        else:
            pass
        if ('scatterplot' in plot) and (text == True):
            # get y data points
            y_arr = numpy.array([y for _, y in ax.collections[0].get_offsets()])
            # get max y data points
            if y_arr.size != 0:
                max_y = max(y_arr)
            else:
                raise Exception('y-axis data points must not be an empty list!')
            for x, y in ax.collections[0].get_offsets():
                # annotate
                if axis == 'x':
                    x_sep = text_sep_type(num=x, df=df, sep=sep, axislabel=axislabel, axes=axes)
                    x_add = text_add_type(num=x_sep, add=add, axislabel=axislabel, axes=axes)
                    if text_fontsize is not None:
                        try:
                            ax.annotate(f'{x_add}', xy=(x, y-max_y*0.03*text_fontsize/10), fontsize=text_fontsize, ha='center', va='center')
                        except:
                            raise Exception('Unknown text fontsize argument!')
                    else:
                        ax.annotate(f'{x_add}', xy=(x, y-max_y*0.03), ha='center', va='center')
                elif axis == 'y':
                    y_sep = text_sep_type(num=y, df=df, sep=sep, axislabel=axislabel, axes=axes)
                    y_add = text_add_type(num=y_sep, add=add, axislabel=axislabel, axes=axes)
                    if text_fontsize is not None:
                        try:
                            ax.annotate(f'{y_add}', xy=(x, y+max_y*0.0325*text_fontsize/10), fontsize=text_fontsize, ha='center', va='center')
                        except:
                            raise Exception('Unknown text fontsize argument!')
                    else:
                        ax.annotate(f'{y_add}', xy=(x, y+max_y*0.0325), ha='center', va='center')
                else:
                    raise Exception('Unsupported axis!')
        else:
            pass
        if (('lineplot' in plot) or ('ecdfplot' in plot)) and (text == True):
            for data in ax.get_lines():
                x_arr, y_arr = data.get_data()
                # get max y data points
                if y_arr.size != 0:
                    max_y = max(y_arr)
                else:
                    raise Exception('y-axis data points must not be an empty list!')
                for x, y in zip(x_arr, y_arr):
                    # temporary bug fix for ecdfplot
                    if x == numpy.NINF:
                        x = 0
                    else:
                        pass
                    if y == numpy.NINF:
                        y = 0
                    else:
                        pass
                    # annotate
                    if axis == 'x':
                        x_sep = text_sep_type(num=x, df=df, sep=sep, axislabel=axislabel, axes=axes)
                        x_add = text_add_type(num=x_sep, add=add, axislabel=axislabel, axes=axes)
                        if text_fontsize is not None:
                            try:
                                ax.annotate(f'{x_add}', xy=(x, y-max_y*0.03*text_fontsize/10), fontsize=text_fontsize, ha='center', va='center')
                            except:
                                raise Exception('Unknown text fontsize argument!')
                        else:
                            ax.annotate(f'{x_add}', xy=(x, y-max_y*0.03), ha='center', va='center')
                    elif axis == 'y':
                        y_sep = text_sep_type(num=y, df=df, sep=sep, axislabel=axislabel, axes=axes)
                        y_add = text_add_type(num=y_sep, add=add, axislabel=axislabel, axes=axes)
                        if text_fontsize is not None:
                            try:
                                ax.annotate(f'{y_add}', xy=(x, y+max_y*0.0325*text_fontsize/10), fontsize=text_fontsize, ha='center', va='center')
                            except:
                                raise Exception('Unknown text fontsize argument!')
                        else:
                            ax.annotate(f'{y_add}', xy=(x, y+max_y*0.0325), ha='center', va='center')
                    else:
                        raise Exception('Unsupported axis!')
        else:
            pass
        if ('pieplot' in plot) and (text == True):
            for child in ax.get_children():
                if isinstance(child, matplotlib.text.Text) and ('%' in child.get_text()):
                    num = float(child.get_text()[:-1])
                    text_sep = text_sep_type(num=num, df=df, sep=sep, axislabel=naxislabel, axes=axes)
                    text_add = text_add_type(num=text_sep, add='_%', axislabel=naxislabel, axes=axes)
                    child.set_text(f'{text_add}')
                else:
                    pass
                if isinstance(child, matplotlib.text.Text) and (text_fontsize is not None):
                    try:
                        child.set_fontsize(text_fontsize)
                    except:
                        raise Exception('Unknown text fontsize argument!')
                else:
                    pass
        else:
            pass
        if (('treemapsplot' in plot) or ('packedbubblesplot' in plot)) and (text == True):
            for child in ax.get_children():
                if isinstance(child, matplotlib.text.Text) and (child.get_text().isdigit() == True):
                    num = int(child.get_text())
                    text_sep = text_sep_type(num=num, df=df, sep=sep, axislabel=naxislabel, axes=axes)
                    text_add = text_add_type(num=text_sep, add=add, axislabel=naxislabel, axes=axes)
                    child.set_text(f'{text_add}')
                else:
                    pass
                if isinstance(child, matplotlib.text.Text) and (text_fontsize is not None):
                    try:
                        child.set_fontsize(text_fontsize)
                    except:
                        raise Exception('Unknown text fontsize argument!')
                else:
                    pass
        else:
            pass
    else:
        raise Exception('Unknown plot argument!')
    return ax