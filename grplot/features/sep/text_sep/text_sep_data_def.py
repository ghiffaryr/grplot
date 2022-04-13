from pandas.api.types import is_numeric_dtype
from grplot.features.sep.text_sep.text_sep_def import text_sep_def


def text_sep_data_def(df, num, axislabel, sep):
    if axislabel in df:
        if is_numeric_dtype(type(num)) == True: 
            num = text_sep_def(num=num, sep=sep)
        else:
            pass
    else: # axislabel not in df, special case as in histogram, barplot, etc.
        if axislabel in ['Probability', 'Proportion', 'Density', 'Count', 'Frequency', 'Percent', 'Cumulative Percentage']:
            if sep in [',c', ',cL']:
                num = text_sep_def(num=num, sep=',')
            elif sep in ['.c', '.cL']:
                num = text_sep_def(num=num, sep='.')
            else:
                num = text_sep_def(num=num, sep=sep)
        else:
            pass
    return num