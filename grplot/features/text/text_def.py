import numpy
from pandas.api.types import is_numeric_dtype
import matplotlib
from grplot.features.add.text_add.text_add_type import text_add_type
from grplot.features.sep.text_sep.text_sep_type import text_sep_type
from grplot.utils.first_valid_index import first_valid_index


def text_def(plot, df, ax, ci, hue, multiple, axis, text, sep, add, text_fontsize, naxislabel, axislabel, axes):
    if plot in ['histplot', 'barplot', 'countplot', 'paretoplot']:
        # check ci
        if (ci is not None) or (multiple == 'fill') or ((hue is not None) and (multiple == 'stack')):
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
        # get patches height and width data
        list_height = numpy.array([p.get_height() for p in ax.patches])
        list_width = numpy.array([p.get_width() for p in ax.patches])
        # get patches max and min height and width data
        if list_height.size != 0:
            max_height = max(list_height)
            min_height = min(list_height)
        else:
            pass
        if list_width.size != 0:
            max_width = max(list_width)
            min_width = min(list_width)
        else:
            pass
        # numerical check for main axis of histplot, barplot, countplot, barplot in paretoplot
        numeric = False
        if axislabel in df:
            if (is_numeric_dtype(df[axislabel]) == True) or (is_numeric_dtype(type(df[axislabel][first_valid_index(df[axislabel])])) == True):
                numeric = True
            else:
                pass
        else: # axislabel not in df, special case as in histogram, barplot, etc.
            if axislabel in ['Probability', 'Proportion', 'Density', 'Count', 'Frequency', 'Percent', 'count']:
                numeric = True
            else:
                pass
        # annotate for histplot, barplot, countplot, barplot in paretoplot
        if (list_height.size != 0) and (list_width.size != 0) and (numeric == True):
            if axis == 'x':
                if text in ['h', 'h+o', 'o+h']:
                    for p in ax.patches:
                        left, bottom, width, height = p.get_bbox().bounds
                        if width != 0:
                            width_sep = text_sep_type(plot=plot, df=df, num=width, sep=sep, axislabel=axislabel, axes=axes)
                            width_add = text_add_type(plot=plot, num=width_sep, add=add, axislabel=axislabel, axes=axes)
                            if width > 0:
                                if text_fontsize is not None:
                                    try:
                                        ax.annotate((f'{width_add}'), xy=(width+max_width*0.0175*text_fontsize/10, bottom+height/2), ha='center', va='center', fontsize=text_fontsize, rotation=270)
                                    except:
                                        raise Exception('Unknown text fontsize argument!')
                                else:
                                    ax.annotate((f'{width_add}'), xy=(width+max_width*0.0175, bottom+height/2), ha='center', va='center', rotation=270)
                            elif width < 0:
                                if text_fontsize is not None:
                                    try:
                                        ax.annotate((f'{width_add}'), xy=(width+min_width*0.0175*text_fontsize/10, bottom+height/2), ha='center', va='center', fontsize=text_fontsize, rotation=90)
                                    except:
                                        raise Exception('Unknown text fontsize argument!')
                                else:
                                    ax.annotate((f'{width_add}'), xy=(width+min_width*0.0175, bottom+height/2), ha='center', va='center', rotation=90)
                            else:
                                pass
                        else:
                            pass
                elif text in ['v', 'v+o', 'o+v']:
                    for p in ax.patches:
                        left, bottom, width, height = p.get_bbox().bounds
                        if width != 0:
                            width_sep = text_sep_type(plot=plot, df=df, num=width, sep=sep, axislabel=axislabel, axes=axes)
                            width_add = text_add_type(plot=plot, num=width_sep, add=add, axislabel=axislabel, axes=axes)
                            if width > 0:
                                if text_fontsize is not None:
                                    try:
                                        ax.annotate((f'{width_add}'), xy=(width+max_width*0.0175*text_fontsize/10, bottom+height/2), ha='left', va='center', fontsize=text_fontsize)
                                    except:
                                        raise Exception('Unknown text fontsize argument!')
                                else:
                                    ax.annotate((f'{width_add}'), xy=(width+max_width*0.0175, bottom+height/2), ha='left', va='center')
                            elif width < 0:
                                if text_fontsize is not None:
                                    try:
                                        ax.annotate((f'{width_add}'), xy=(width+min_width*0.0175*text_fontsize/10, bottom+height/2), ha='right', va='center', fontsize=text_fontsize)
                                    except:
                                        raise Exception('Unknown text fontsize argument!')
                                else:
                                    ax.annotate((f'{width_add}'), xy=(width+min_width*0.0175, bottom+height/2), ha='right', va='center')
                            else:
                                pass
                        else:
                            pass
                elif text in ['i', 'i+v', 'v+i']:
                    for p in ax.patches:
                        left, bottom, width, height = p.get_bbox().bounds
                        if width != 0:
                            width_sep = text_sep_type(plot=plot, df=df, num=width, sep=sep, axislabel=axislabel, axes=axes)
                            width_add = text_add_type(plot=plot, num=width_sep, add=add, axislabel=axislabel, axes=axes)
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
                    for p in ax.patches:
                        left, bottom, width, height = p.get_bbox().bounds
                        if width != 0:
                            width_sep = text_sep_type(plot=plot, df=df, num=width, sep=sep, axislabel=axislabel, axes=axes)
                            width_add = text_add_type(plot=plot, num=width_sep, add=add, axislabel=axislabel, axes=axes)
                            if width > 0:
                                if text_fontsize is not None:
                                    try:
                                        ax.annotate((f'{width_add}'), xy=(left+width/2, bottom+height/2), ha='center', va='center', fontsize=text_fontsize, rotation=270)
                                    except:
                                        raise Exception('Unknown text fontsize argument!')
                                else:
                                    ax.annotate((f'{width_add}'), xy=(left+width/2, bottom+height/2), ha='center', va='center', rotation=270)
                            elif width < 0:
                                if text_fontsize is not None:
                                    try:
                                        ax.annotate((f'{width_add}'), xy=(left+width/2, bottom+height/2), ha='center', va='center', fontsize=text_fontsize, rotation=90)
                                    except:
                                        raise Exception('Unknown text fontsize argument!')
                                else:
                                    ax.annotate((f'{width_add}'), xy=(left+width/2, bottom+height/2), ha='center', va='center', rotation=90)
                            else:
                                pass
                        else:
                            pass
                else:
                    pass
            elif axis == 'y':
                if text in ['h', 'h+o', 'o+h']:
                    for p in ax.patches:
                        left, bottom, width, height = p.get_bbox().bounds
                        if height != 0:
                            height_sep = text_sep_type(plot=plot, df=df, num=height, sep=sep, axislabel=axislabel, axes=axes)
                            height_add = text_add_type(plot=plot, num=height_sep, add=add, axislabel=axislabel, axes=axes)
                            if height > 0:
                                if text_fontsize is not None:
                                    try:
                                        ax.annotate((f'{height_add}'), xy=(left+width/2, height+max_height*0.0325*text_fontsize/10), ha='center', va='center', fontsize=text_fontsize)
                                    except:
                                        raise Exception('Unknown text fontsize argument!')
                                else:
                                    ax.annotate((f'{height_add}'), xy=(left+width/2, height+max_height*0.0325), ha='center', va='center')
                            elif height < 0:
                                if text_fontsize is not None:
                                    try:
                                        ax.annotate((f'{height_add}'), xy=(left+width/2, height+min_height*0.0325*text_fontsize/10), ha='center', va='center', fontsize=text_fontsize)
                                    except:
                                        raise Exception('Unknown text fontsize argument!')
                                else:
                                    ax.annotate((f'{height_add}'), xy=(left+width/2, height+min_height*0.0325), ha='center', va='center')
                            else:
                                pass
                        else:
                            pass
                elif text in ['v', 'v+o', 'o+v']:
                    for p in ax.patches:
                        left, bottom, width, height = p.get_bbox().bounds
                        if height != 0:
                            height_sep = text_sep_type(plot=plot, df=df, num=height, sep=sep, axislabel=axislabel, axes=axes)
                            height_add = text_add_type(plot=plot, num=height_sep, add=add, axislabel=axislabel, axes=axes)
                            if height > 0:
                                if text_fontsize is not None:
                                    try:
                                        ax.annotate((f'{height_add}'), xy=(left+width/2, height+max_height*0.0325*text_fontsize/10), ha='center', va='bottom', fontsize=text_fontsize, rotation=90)
                                    except:
                                        raise Exception('Unknown text fontsize argument!')
                                else:
                                    ax.annotate((f'{height_add}'), xy=(left+width/2, height+max_height*0.0325), ha='center', va='bottom', rotation=90)
                            elif height < 0:
                                if text_fontsize is not None:
                                    try:
                                        ax.annotate((f'{height_add}'), xy=(left+width/2, height+min_height*0.0325*text_fontsize/10), ha='center', va='top', fontsize=text_fontsize, rotation=90)
                                    except:
                                        raise Exception('Unknown text fontsize argument!')
                                else:
                                    ax.annotate((f'{height_add}'), xy=(left+width/2, height+min_height*0.0325), ha='center', va='top', rotation=90)
                            else:
                                pass
                        else:
                            pass
                elif text in ['i', 'i+v', 'v+i']:
                    for p in ax.patches:
                        left, bottom, width, height = p.get_bbox().bounds
                        if height != 0:
                            height_sep = text_sep_type(plot=plot, df=df, num=height, sep=sep, axislabel=axislabel, axes=axes)
                            height_add = text_add_type(plot=plot, num=height_sep, add=add, axislabel=axislabel, axes=axes)
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
                    for p in ax.patches:
                        left, bottom, width, height = p.get_bbox().bounds
                        if height != 0:
                            height_sep = text_sep_type(plot=plot, df=df, num=height, sep=sep, axislabel=axislabel, axes=axes)
                            height_add = text_add_type(plot=plot, num=height_sep, add=add, axislabel=axislabel, axes=axes)
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
        if (plot == 'paretoplot') and (text in ['h', 'h+o', 'o+h', 'v', 'v+o', 'o+v', 'i', 'i+v', 'v+i', 'i+h', 'h+i']):
            if axis == 'x':
                for data in ax.get_shared_y_axes().get_siblings(ax)[0].get_lines():
                    x_arr, y_arr = data.get_data()
                    # check x_arr data type
                    if (type(x_arr) == list) or (numpy.issubdtype(type(x_arr), numpy.ndarray) == False):
                        x_arr = numpy.array(x_arr)
                    else:
                        pass
                    # check y_arr data type
                    if (type(y_arr) == list) or (numpy.issubdtype(type(y_arr), numpy.ndarray) == False):
                        y_arr = numpy.array(y_arr)
                    else:
                        pass
                    # get max x data points
                    if x_arr.size != 0:
                        max_x = max(x_arr)
                    else:
                        pass
                    if (x_arr.size != 0) and (y_arr.size != 0):
                        for x, y in zip(x_arr, y_arr):
                            # annotate
                            x_sep = text_sep_type(plot=plot, df=df, num=x, sep=sep, axislabel='Cumulative Percentage', axes=axes)
                            x_add = text_add_type(plot=plot, num=x_sep, add='_%', axislabel='Cumulative Percentage', axes=axes)
                            if text_fontsize is not None:
                                try:
                                    ax.get_shared_y_axes().get_siblings(ax)[0].annotate(f'{x_add}', xy=(x-max_x*0.0325*text_fontsize/10, y), fontsize=text_fontsize, ha='right', va='center')
                                except:
                                    raise Exception('Unknown text fontsize argument!')
                            else:
                                ax.get_shared_y_axes().get_siblings(ax)[0].annotate(f'{x_add}', xy=(x-max_x*0.0325, y), ha='right', va='center')
                    else:
                        pass
            elif axis == 'y':
                for data in ax.get_shared_x_axes().get_siblings(ax)[0].get_lines():
                    x_arr, y_arr = data.get_data()
                    # check x_arr data type
                    if (type(x_arr) == list) or (numpy.issubdtype(type(x_arr), numpy.ndarray) == False):
                        x_arr = numpy.array(x_arr)
                    else:
                        pass
                    # check y_arr data type
                    if (type(y_arr) == list) or (numpy.issubdtype(type(y_arr), numpy.ndarray) == False):
                        y_arr = numpy.array(y_arr)
                    else:
                        pass
                    # get max y data points
                    if y_arr.size != 0:
                        max_y = max(y_arr)
                    else:
                        pass
                    if (x_arr.size != 0) and (y_arr.size != 0):
                        for x, y in zip(x_arr, y_arr):
                            # annotate
                            y_sep = text_sep_type(plot=plot, df=df, num=y, sep=sep, axislabel='Cumulative Percentage', axes=axes)
                            y_add = text_add_type(plot=plot, num=y_sep, add='_%', axislabel='Cumulative Percentage', axes=axes)
                            if text_fontsize is not None:
                                try:
                                    ax.get_shared_x_axes().get_siblings(ax)[0].annotate(f'{y_add}', xy=(x, y+max_y*0.0325*text_fontsize/10), fontsize=text_fontsize, ha='center', va='bottom')
                                except:
                                    raise Exception('Unknown text fontsize argument!')
                            else:
                                ax.get_shared_x_axes().get_siblings(ax)[0].annotate(f'{y_add}', xy=(x, y+max_y*0.0325), ha='center', va='bottom')
                    else:
                        pass
            else:
                raise Exception('Unsupported axis!')
        else:
            pass
    else:
        pass
    if (plot in ['scatterplot', 'residplot']) and (text == True):
        x_arr, y_arr = numpy.array([x for x, _ in ax.collections[0].get_offsets()]), numpy.array([y for _, y in ax.collections[0].get_offsets()])
        # get max and min y data points
        if y_arr.size != 0:
            max_y = max(y_arr)
            min_y = min(y_arr)
        else:
            pass
        # position calibrator
        if plot == 'residplot':
            weight = 5
        else:
            weight = 1
        if (x_arr.size != 0) and (y_arr.size != 0):
            for x, y in ax.collections[0].get_offsets():
                # annotate
                if axis == 'x':
                    x_sep = text_sep_type(plot=plot, df=df, num=x, sep=sep, axislabel=axislabel, axes=axes)
                    x_add = text_add_type(plot=plot, num=x_sep, add=add, axislabel=axislabel, axes=axes)
                    if y > 0:
                        if text_fontsize is not None:
                            try:
                                ax.annotate(f'{x_add}', xy=(x, y-max_y*0.0325*weight*text_fontsize/10), fontsize=text_fontsize, ha='center', va='center')
                            except:
                                raise Exception('Unknown text fontsize argument!')
                        else:
                            ax.annotate(f'{x_add}', xy=(x, y-max_y*0.0325*weight), ha='center', va='center')
                    elif y < 0:
                        if text_fontsize is not None:
                            try:
                                ax.annotate(f'{x_add}', xy=(x, y+min_y*0.0325*weight*text_fontsize/10), fontsize=text_fontsize, ha='center', va='center')
                            except:
                                raise Exception('Unknown text fontsize argument!')
                        else:
                            ax.annotate(f'{x_add}', xy=(x, y+min_y*0.0325*weight), ha='center', va='center')
                    else:
                        pass
                elif axis == 'y':
                    y_sep = text_sep_type(plot=plot, df=df, num=y, sep=sep, axislabel=axislabel, axes=axes)
                    y_add = text_add_type(plot=plot, num=y_sep, add=add, axislabel=axislabel, axes=axes)
                    if y > 0:
                        if text_fontsize is not None:
                            try:
                                ax.annotate(f'{y_add}', xy=(x, y+max_y*0.03*weight*text_fontsize/10), fontsize=text_fontsize, ha='center', va='center')
                            except:
                                raise Exception('Unknown text fontsize argument!')
                        else:
                            ax.annotate(f'{y_add}', xy=(x, y+max_y*0.03*weight), ha='center', va='center')
                    elif y < 0:
                        if text_fontsize is not None:
                            try:
                                ax.annotate(f'{y_add}', xy=(x, y-min_y*0.03*weight*text_fontsize/10), fontsize=text_fontsize, ha='center', va='center')
                            except:
                                raise Exception('Unknown text fontsize argument!')
                        else:
                            ax.annotate(f'{y_add}', xy=(x, y-min_y*0.03*weight), ha='center', va='center')
                    else:
                        pass
                else:
                    raise Exception('Unsupported axis!')
        else:
            pass
    else:
        pass
    if (plot in ['lineplot', 'ecdfplot']) and (text == True):
        for data in ax.get_lines():
            x_arr, y_arr = data.get_data()
            # check x_arr data type
            if (type(x_arr) == list) or (numpy.issubdtype(type(x_arr), numpy.ndarray) == False):
                x_arr = numpy.array(x_arr)
            else:
                pass
            # check y_arr data type
            if (type(y_arr) == list) or (numpy.issubdtype(type(y_arr), numpy.ndarray) == False):
                y_arr = numpy.array(y_arr)
            else:
                pass
            # get max and min y data points
            if y_arr.size != 0:
                max_y = max(y_arr)
                min_y = min(y_arr)
            else:
                pass
            if (x_arr.size != 0) and (y_arr.size != 0):
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
                        x_sep = text_sep_type(plot=plot, df=df, num=x, sep=sep, axislabel=axislabel, axes=axes)
                        x_add = text_add_type(plot=plot, num=x_sep, add=add, axislabel=axislabel, axes=axes)
                        if y > 0:
                            if text_fontsize is not None:
                                try:
                                    ax.annotate(f'{x_add}', xy=(x, y-max_y*0.0325*text_fontsize/10), fontsize=text_fontsize, ha='center', va='center')
                                except:
                                    raise Exception('Unknown text fontsize argument!')
                            else:
                                ax.annotate(f'{x_add}', xy=(x, y-max_y*0.0325), ha='center', va='center')
                        elif y < 0:
                            if text_fontsize is not None:
                                try:
                                    ax.annotate(f'{x_add}', xy=(x, y+min_y*0.0325*text_fontsize/10), fontsize=text_fontsize, ha='center', va='center')
                                except:
                                    raise Exception('Unknown text fontsize argument!')
                            else:
                                ax.annotate(f'{x_add}', xy=(x, y+min_y*0.0325), ha='center', va='center')
                        else:
                            pass
                    elif axis == 'y':
                        y_sep = text_sep_type(plot=plot, df=df, num=y, sep=sep, axislabel=axislabel, axes=axes)
                        y_add = text_add_type(plot=plot, num=y_sep, add=add, axislabel=axislabel, axes=axes)
                        if y > 0:
                            if text_fontsize is not None:
                                try:
                                    ax.annotate(f'{y_add}', xy=(x, y+max_y*0.03*text_fontsize/10), fontsize=text_fontsize, ha='center', va='center')
                                except:
                                    raise Exception('Unknown text fontsize argument!')
                            else:
                                ax.annotate(f'{y_add}', xy=(x, y+max_y*0.03), ha='center', va='center')
                        elif y < 0:
                            if text_fontsize is not None:
                                try:
                                    ax.annotate(f'{y_add}', xy=(x, y-min_y*0.03*text_fontsize/10), fontsize=text_fontsize, ha='center', va='center')
                                except:
                                    raise Exception('Unknown text fontsize argument!')
                            else:
                                ax.annotate(f'{y_add}', xy=(x, y-min_y*0.03), ha='center', va='center')
                        else:
                            pass
                    else:
                        raise Exception('Unsupported axis!')
            else:
                pass
    else:
        pass
    if (plot == 'pieplot') and (text == True):
        for child in ax.get_children():
            if isinstance(child, matplotlib.text.Text) and ('%' in child.get_text()):
                num = float(child.get_text()[:-1])
                text_sep = text_sep_type(plot=plot, df=df, num=num, sep=sep, axislabel=naxislabel, axes=axes)
                text_add = text_add_type(plot=plot, num=text_sep, add='_%', axislabel=naxislabel, axes=axes)
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
    if (plot in ['treemapsplot', 'packedbubblesplot']) and (text == True):
        for child in ax.get_children():
            if isinstance(child, matplotlib.text.Text) and (child.get_text().isdigit() == True):
                num = int(child.get_text())
                text_sep = text_sep_type(plot=plot, df=df, num=num, sep=sep, axislabel=naxislabel, axes=axes)
                text_add = text_add_type(plot=plot, num=text_sep, add=add, axislabel=naxislabel, axes=axes)
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
    return ax