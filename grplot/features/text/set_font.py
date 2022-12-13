import matplotlib
from grplot.features.add.text_add.text_add_type import text_add_type
from grplot.features.sep.text_sep.text_sep_type import text_sep_type
from grplot.utils.decorator.check import check_text_fontsize_type
from grplot.utils.template.set_font_template import ISetFont
from grplot.utils.constant import constant
from abc import abstractmethod

class SetFontParams:
    def __init__(
        self,
        plot,
        df,
        add,
        sep,
        naxislabel,
        axes,
        text,
        text_fontsize
    ):
        self.add = add
        self.plot = plot
        self.df = df
        self.sep = sep
        self.naxislabel = naxislabel
        self.axes = axes
        self.text = text
        self.text_fontsize = text_fontsize

class SetFont(ISetFont):
    ax: any = None
    def __init__(self, params: SetFontParams):
        self.params = params

    @abstractmethod
    def set_font(self, ax) -> any:
        pass
    
    def get_ax(self) -> any:
        return self.ax

    def __set_child_font(self, add, num, is_set_text: bool, child) -> any:
        if isinstance(child, matplotlib.text.Text):
            return child

        if is_set_text:
            text_sep = text_sep_type(plot=self.params.plot, df=self.params.df, num=num, sep=self.params.sep, axislabel=self.params.naxislabel, axes=self.params.axes)
            text_add = text_add_type(plot=self.params.plot, num=text_sep, add=add, axislabel=self.params.naxislabel, axes=self.params.axes)
            child.set_text(f'{text_add}')

        if (self.params.text_fontsize is not None):
            child.set_fontsize(self.params.text_fontsize)
        
        return child

class SetFontPieplot(SetFont):
    def __init__(self, params: SetFontParams):
        super().__init__(params)
    
    @check_text_fontsize_type(constant.list_of_type)
    def set_font(self, ax):
        if self.params.text != True:
            return ax

        for child in ax.get_children():
            num = float(child.get_text()[:-1])
            is_set_text = ('%' in child.get_text())

            child = super().__set_child_font('_%', num, is_set_text, child)

        super().ax = ax
        return super().ax

class SetFontTreesAndPackedBubblePlot(SetFont):
    def __init__(self, params: SetFontParams):
        super().__init__(params)

    @check_text_fontsize_type(constant.list_of_type)
    def set_font(self, ax):
        if self.params.text != True:
            return ax
        
        for child in ax.get_children():
            num = int(child.get_text())
            is_set_text = (child.get_text().isdigit() == True)

            child = super().__set_child_font(self.params.add, num, is_set_text, child)            
        
        super().ax = ax
        return super().ax
