from pandas.api.types import is_numeric_dtype
from grplot.features.sep.tick_sep.tick_sep_def import tick_sep_def


def tick_sep_data_def(df, ax, axis, axislabel, sep):
    if axislabel in df:
        if (is_numeric_dtype(df[axislabel]) == True) or (is_numeric_dtype(type(df[axislabel][df.first_valid_index()])) == True):
            tick_sep_def(ax=ax, axis=axis, sep=sep)
        else:
            pass
    else: # axislabel not in df, special case as in histogram, barplot, etc.
        if axislabel in ['Probability', 'Proportion', 'Density', 'Count', 'Frequency', 'Percent', 'count', 'Cumulative Percentage']:
            if sep in [',c', ',cL']:
                tick_sep_def(ax=ax, axis=axis, sep=',')
            elif sep in ['.c', '.cL']:
                tick_sep_def(ax=ax, axis=axis, sep='.')
            else:
                tick_sep_def(ax=ax, axis=axis, sep=sep)
        else:
            pass
    return ax