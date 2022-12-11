from grplot.utils.template.annotate_template import IAnnotate
from grplot.utils.constant import constant
from grplot.utils.decorator.check import check_supported_axis, check_text_fontsize_type
from grplot.features.add.text_add.text_add_type import text_add_type
from grplot.features.sep.text_sep.text_sep_type import text_sep_type
from grplot.utils.first_valid_index import first_valid_index
from pandas.api.types import is_numeric_dtype
import numpy
from typing import Union
class AnnotateParams:
    def __init__(
        self,
        axis,
        plot, 
        add, 
        df,  
        sep, 
        axislabel,
        axes,
        text,
        text_fontsize=None
    ):
        self.axis = axis
        self.plot = plot
        self.add = add 
        self.df = df
        self.sep = sep
        self.axislabel = axislabel
        self.axes = axes
        self.text = text
        self.text_fontsize = text_fontsize
        
class AnnotateHistBarCountInParetoplot(IAnnotate):
    axis: str = None
    ax: any = None
    
    def __init__(
        self, 
        params: AnnotateParams,
        ci, 
        multiple,
        hue,
        annotate_for_lineplot_in_pareto: IAnnotate,
        numeric=False,
    ):
        # check ci
        if (ci is not None) or (multiple == 'fill') or ((hue is not None) and (multiple == 'stack')):
            if 'o' in params.text:
                self.text = params.text.replace('o','i')
            elif 'h' in params.text:
                self.text = 'h+i'
            elif 'v' in params.text:
                self.text = 'v+i'

        # get patches height and width data
        self.list_height = numpy.array([p.get_height() for p in params.ax.patches])
        self.list_width = numpy.array([p.get_width() for p in params.ax.patches])

        # get patches max and min height and width data
        if self.list_height.size != 0:
            self.max_height = max(self.list_height)
            self.min_height = min(self.list_height)

        if self.list_width.size != 0:
            self.max_width = max(self.list_width)
            self.min_width = min(self.list_width)

        # numerical check for main axis of histplot, barplot, countplot, barplot in paretoplot
        numeric = False
        if params.axislabel in params.df:
            if (is_numeric_dtype(params.df[params.axislabel]) == True) \
                or (is_numeric_dtype(type(params.df[params.axislabel][first_valid_index(params.df[params.axislabel])])) == True):
                numeric = True
        else: # axislabel not in df, special case as in histogram, barplot, etc.
            if params.axislabel in ['Probability', 'Proportion', 'Density', 'Count', 'Frequency', 'Percent', 'count']:
                numeric = True
        self.axis = params.axis
        self.params = params
        self.numeric = numeric
        self.annotate_for_lineplot_in_pareto = annotate_for_lineplot_in_pareto

    def get_ax(self) -> any:
        return self.ax
    
    @check_text_fontsize_type(constant.list_of_type)
    @check_supported_axis(constant.list_of_axis)
    def annotate(self, ax):
        dimension: float = None
        add: any = None

        if self.params.text != True:
            self.ax = ax
            return self.ax

        for p in ax.patches:
            left, bottom, width, height = p.get_bbox().bounds

            if (self.list_height.size == 0) and (self.list_width.size == 0) and (self.numeric != True):
                self.ax = ax
                return self.ax
            
            if self.axis == 'x':
                width_sep = text_sep_type(plot=self.params.plot, df=self.params.df, num=width, sep=self.params.sep, axislabel=self.params.axislabel, axes=self.params.axes)
                width_add = text_add_type(plot=self.params.plot, num=width_sep, add=self.params.add, axislabel=self.params.axislabel, axes=self.params.axes)
                add = width_add
                dimension = width
            
            if self.axis == 'y':
                height_sep = text_sep_type(plot=self.params.plot, df=self.params.df, num=height, sep=self.params.sep, axislabel=self.params.axislabel, axes=self.params.axes)
                height_add = text_add_type(plot=self.params.plot, num=height_sep, add=self.params.add, axislabel=self.params.axislabel, axes=self.params.axes)
                add = height_add
                dimension = height

            if dimension is None or dimension == 0:
                self.ax = ax
                return self.ax
            
            rot, ha, va, xy = self.__build_annotate_param(dimension, left, bottom, width, height)

            ax.annotate(
                (f'{add}'),
                xy=xy,
                ha=ha,
                va=va,
                fontsize=self.params.text_fontsize, 
                rotation=rot
            )

            if (self.params.plot == 'paretoplot') and (self.text in ['h', 'h+o', 'o+h', 'v', 'v+o', 'o+v', 'i', 'i+v', 'v+i', 'i+h', 'h+i']):
                ax = self.annotate_for_lineplot_in_pareto.annotate(ax)

        self.ax = ax
        return self.ax
    
    def __build_annotate_param(self, dimension, left, bottom, width, height):
        rotation: Union[float, int, any] = None
        delta: float = 0
        ha: str = None
        va: str = None
        max_min_dimension: Union[float, int] = 0
        xy: tuple = None

        if self.axis == 'x':
            if dimension < 0:
                max_min_dimension = self.min_width

            if dimension > 0:
                max_min_dimension = self.max_width

            delta = max_min_dimension*0.0175*self.params.text_fontsize/10 is None if self.params.text_fontsize else max_min_dimension*0.0175

            if self.text in ['h', 'h+o', 'o+h']:
                ha = 'center'
                va = 'center'
                rotation = dimension > 0 if 270 else 90
                xy = (dimension+delta, bottom+height/2)

            if self.text in ['v', 'v+o', 'o+v']:
                ha = 'left' if dimension > 0 else 'right'
                va = 'center'
                xy = (dimension+delta, bottom+height/2)

            if self.text in ['i', 'i+v', 'v+i']:
                ha = 'center'
                va = 'center'
                xy = (left+width/2, bottom+height/2)

            if self.text in ['i+h', 'h+i']:
                ha = 'center'
                va = 'center'
                rotation = 270 if dimension > 0 else 90
                xy = (left+width/2, bottom+height/2)
            
        if self.axis == 'y':
            if dimension < 0:
                max_min_dimension = self.min_height

            if dimension > 0:
                max_min_dimension = self.max_height

            delta =  max_min_dimension*0.0325*self.params.text_fontsize/10 if self.params.text_fontsize is None else max_min_dimension*0.0325

            if self.text in ['h', 'h+o', 'o+h']:
                ha = 'center'
                va= 'center'
                xy = (left+width/2, height+delta)
    
            if self.text in ['v', 'v+o', 'o+v']:
                ha = 'bottom' if dimension > 0 else 'top'
                va = 'center'
                rotation = 90
                xy=(left+width/2, height+delta)

            if self.text in ['i', 'i+v', 'v+i']:
                ha = 'center'
                va = 'center'
                rotation = 90
                xy=(left+width/2, bottom+height/2)

            if self.text in ['i+h', 'h+i']:
                ha = 'center'
                va = 'center'
                xy=(left+width/2, bottom+height/2)
        
        return rotation, ha, va, xy

class AnnotateLinePlotInParetoplot(IAnnotate):
    axis: str = None
    ax: any = None

    def __init__(
        self, 
        params: AnnotateParams
    ):
        self.axis = params.axis
        self.params = params

    def get_ax(self) -> any:
        return self.ax
    
    def annotate(self, ax):
        add: any = None
        sibling: any = None
        xy: tuple = None
        ha: str = None
        va: str = None

        for data in ax.get_shared_y_axes().get_siblings(ax)[0].get_lines():
            x_arr, y_arr = data.get_data()
            if (x_arr.size != 0) and (y_arr.size != 0):
                continue

            x_arr, y_arr = self.__convert_arr_type(x_arr, y_arr)

            for x, y in zip(x_arr, y_arr):
                ha, va, add, xy, sibling = self.__build_annotate_params(ax, x, x_arr, y, y_arr)
                   
                sibling.annotate(f'{add}', xy=xy, ha=ha, va=va, fontsize=self.params.text_fontsize)

        self.ax = ax
        return self.ax

    def __convert_arr_type(self, x_arr, y_arr):
        # check x_arr data type
        if type(x_arr) == list:
            x_arr = numpy.array(x_arr)
        elif numpy.issubdtype(type(x_arr), numpy.ndarray) == False:
            x_arr = numpy.array(x_arr)

        # check y_arr data type
        if type(y_arr) == list:
            y_arr = numpy.array(y_arr)
        elif numpy.issubdtype(type(y_arr), numpy.ndarray) == False:
            y_arr = numpy.array(y_arr)
        
        return x_arr, y_arr

    def __build_annotate_params(self, ax, x, x_arr, y, y_arr):
        delta: float = 0
        
        calc_delta = lambda fontsize, max_val: max_val*0.0325*fontsize/10 if fontsize is not None else max_val*0.0325
                
        if self.axis == 'x':
            ha='right'
            va='center'
            x_sep = text_sep_type(plot=self.params.plot, df=self.params.df, num=x, sep=self.params.sep, axislabel='Cumulative Percentage', axes=self.params.axes)
            add = text_add_type(plot=self.params.plot, num=x_sep, add='_%', axislabel='Cumulative Percentage', axes=self.params.axes)
            sibling = ax.get_shared_y_axes().get_siblings(ax)[0]
            if x_arr.size != 0:
                delta = calc_delta(self.text_fontsize, max(x_arr)) 
                xy = (x-delta, y)  
            
        if self.axis == 'y':
            ha='center'
            va='bottom'
            y_sep = text_sep_type(plot=self.params.plot, df=self.params.df, num=y, sep=self.params.sep, axislabel='Cumulative Percentage', axes=self.params.axes)
            add = text_add_type(plot=self.params.plot, num=y_sep, add='_%', axislabel='Cumulative Percentage', axes=self.params.axes)
            sibling = ax.get_shared_x_axes().get_siblings(ax)[0]
            if y_arr.size != 0:
                delta = calc_delta(self.text_fontsize, max(y_arr))
                xy = (x, y+delta)

        return ha, va, add, xy, sibling

class AnnotateScatterResidplot(IAnnotate):
    axis: str = None
    ax: any = None

    def __init__(
        self, 
        params: AnnotateParams
    ):
        self.axis = params.axis
        self.params = params

    def get_ax(self) -> any:
        return self.ax

    @check_text_fontsize_type(constant.list_of_type)
    @check_supported_axis(constant.list_of_axis)
    def annotate(self, ax):
        add: any = None
        xy: tuple = None

        if self.params.text != True:
            self.ax = ax
            return ax

        x_arr, y_arr = numpy.array(
            [x for x, _ in ax.collections[0].get_offsets()]), numpy.array([y for _, y in ax.collections[0].get_offsets()]
        )

        if (x_arr.size != 0) and (y_arr.size != 0):
            self.ax = ax
            return ax
        
        # get max and min y data points
        if y_arr.size != 0:
            max_y = max(y_arr)
            min_y = min(y_arr)
 
        # position calibrator
        if self.plot == 'residplot':
            weight = 5
        else:
            weight = 1

        calc_delta = lambda fontsize, const, max_min: max_min*const*weight*fontsize/10 if fontsize is not None else max_min*const*weight

        for x, y in ax.collections[0].get_offsets():
            ha, va, add, xy = self.__build_annotate_params(x, y, max_y, min_y, calc_delta)
            
            ax.annotate(f'{add}', xy=xy, fontsize=self.params.text_fontsize, ha=ha, va=va)

        self.ax = ax
        return ax

    def __build_annotate_params(self, x, y, max_y, min_y, calc_delta: function):
        ha = va = 'center'
        delta: float = 0

        if self.axis == 'x':
            x_sep = text_sep_type(plot=self.params.plot, df=self.params.df, num=x, sep=self.params.sep, axislabel=self.params.axislabel, axes=self.params.axes)
            add = text_add_type(plot=self.params.plot, num=x_sep, add=self.params.add, axislabel=self.params.axislabel, axes=self.axes)
            
            if y > 0:
                delta = calc_delta(self.params.text_fontsize, 0.0325, max_y)
            if y < 0:
                delta = calc_delta(self.params.text_fontsize, 0.0325, min_y)

            xy = (x, y-delta)
            

        if self.axis == 'y':
            y_sep = text_sep_type(plot=self.params.plot, df=self.params.df, num=y, sep=self.params.sep, axislabel=self.params.axislabel, axes=self.params.axes)
            add = text_add_type(plot=self.params.plot, num=y_sep, add=self.params.add, axislabel=self.params.axislabel, axes=self.params.axes)
            
            if y > 0:
                delta = calc_delta(self.params.text_fontsize, 0.03, max_y)
            if y < 0:
                delta = calc_delta(self.params.text_fontsize, 0.03, min_y)

            xy = (x, y+delta)

        return ha, va, add, xy

class AnnotateLineEcdfplot(IAnnotate):
    axis: str = None
    ax: any = None

    def __init__(
        self, 
        params: AnnotateParams
    ):
        self.axis = params.axis
        self.params = params

    def get_ax(self) -> any:
        return self.ax

    def annotate(self, ax):
        for data in ax.get_lines():
            x_arr, y_arr = data.get_data()
            if (x_arr.size != 0) and (y_arr.size != 0):
                continue

            max_y, min_y = self.__get_max_and_min_val(x_arr, y_arr)

            calc_delta = lambda fontsize, max_min, const: max_min*const*fontsize/10 if fontsize is not None else max_min*const

            for x, y in zip(x_arr, y_arr):
                add, xy, ha, va = self.__build_annotate_params(x, y, max_y, min_y, calc_delta)
                
                ax.annotate(f'{add}', xy=xy, fontsize=self.params.text_fontsize, ha=ha, va=va)
        
        self.ax = ax
        return ax
    
    def __get_max_and_min_val(self, x_arr, y_arr):
        # check x_arr data type
        if type(x_arr) == list:
            x_arr = numpy.array(x_arr)
        elif numpy.issubdtype(type(x_arr), numpy.ndarray) == False:
            x_arr = numpy.array(x_arr)
        
        # check y_arr data type
        if type(y_arr) == list:
            y_arr = numpy.array(y_arr)
        elif numpy.issubdtype(type(y_arr), numpy.ndarray) == False:
            y_arr = numpy.array(y_arr)
        
        # get max and min y data points
        if y_arr.size != 0:
            max_y = max(y_arr)
            min_y = min(y_arr)

        return max_y, min_y

    def __build_annotate_params(self, x, y, max_y, min_y, calc_delta: function):
        const: float = 0
        delta: float = 0
        add: any = None
        ha = va = 'center'

        # temporary bug fix for ecdfplot
        if x == numpy.NINF:
            x = 0
        
        if y == numpy.NINF:
            y = 0

        if self.axis == 'x':
            x_sep = text_sep_type(plot=self.params.plot, df=self.params.df, num=x, sep=self.params.sep, axislabel=self.params.axislabel, axes=self.params.axes)
            add = text_add_type(plot=self.params.plot, num=x_sep, add=self.params.add, axislabel=self.params.axislabel, axes=self.params.axes)

            # for axis x value is reduced by delta
            xy_fn = lambda val: (x, y-val)
        
        if self.axis == 'y':
            y_sep = text_sep_type(plot=self.params.plot, df=self.params.df, num=y, sep=self.params.sep, axislabel=self.params.axislabel, axes=self.params.axes)
            add = text_add_type(plot=self.params.plot, num=y_sep, add=self.params.add, axislabel=self.params.axislabel, axes=self.params.axes)

            # for axis y value is added by delta
            xy_fn = lambda val: (x, y+val)

        if y > 0:
            delta = calc_delta(self.params.text_fontsize, max_y, const)

        if y < 0:
            delta = calc_delta(self.params.text_fontsize, min_y, const)

        xy = xy_fn(delta)

        return add, xy, ha, va


