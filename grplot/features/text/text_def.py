import numpy
from pandas.api.types import is_numeric_dtype
import matplotlib
from grplot.features.add.text_add.text_add_type import text_add_type
from grplot.features.sep.text_sep.text_sep_type import text_sep_type
from grplot.utils.first_valid_index import first_valid_index
from grplot.features.text import annotate, set_font
from grplot.utils.template.set_font_template import ISetFont
from grplot.utils.template.annotate_template import IAnnotate
from typing import Dict

class IHandler(IAnnotate, ISetFont):
    pass

class TextDefHandler:
    handler_map: Dict[str, IHandler] = dict()

    def register_handler(self, obj: IHandler, *conditions):
        for condition in conditions:
            self.handler_map.update(condition, obj)

    def get_instance(self, plot: str):
        p = self.handler_map[plot]
        if isinstance(p, IAnnotate):
            p.annotate()

        if isinstance(p, ISetFont):
            p.set_font()
        
        return p
        


def text_def(plot, df, ax, ci, hue, multiple, axis, text, sep, add, text_fontsize, naxislabel, axislabel, axes):
    text_def_handler = TextDefHandler()

    # instantiate object responsible for annotation
    annotate_params = annotate.AnnotateParams(
        add=add,
        axes=axes,
        axis=axis,
        axislabel=axislabel,
        df=df, 
        plot=plot,
        sep=sep,
        text_fontsize=text_fontsize
    )
    annotate_line_pareto = annotate.AnnotateLinePlotInParetoplot(annotate_params)
    annotate_hist_bar_count_in_pareto = annotate.AnnotateHistBarCountInParetoplot(
        annotate_params, text, ci, multiple, hue, annotate_line_pareto
    )
    annotate_scatter_resid =  annotate.AnnotateScatterResidplot(annotate_params)
    annotate_line_ecdf =  annotate.AnnotateLineEcdfplot(annotate_params)
    
    # instantiate object responsible for set font
    set_font_params = set_font.SetFontParams(
        plot=plot,
        add=add,
        axes=axes, 
        df=df,
        naxislabel=naxislabel,
        sep=sep,
        text_fontsize=text_fontsize,
    )
    set_font_pie = set_font.SetFontPieplot(set_font_params)
    set_font_trees_bubble = set_font.SetFontTreesAndPackedBubblePlot(set_font_params)


    text_def_handler.register_handler(annotate_hist_bar_count_in_pareto, *['histplot', 'barplot', 'countplot', 'paretoplot'])
    text_def_handler.register_handler(annotate_scatter_resid, *['scatterplot', 'residplot'])
    text_def_handler.register_handler(annotate_line_ecdf ,*['lineplot', 'ecdfplot'])
    text_def_handler.register_handler(set_font_pie, 'pieplot')
    text_def_handler.register_handler(set_font_trees_bubble, ['treemapsplot', 'packedbubblesplot'])

    return text_def_handler.get_instance(plot).get_ax()
