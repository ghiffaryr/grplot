from pandas.api.types import is_numeric_dtype
from grplot.features.sep.statdesc_sep.statdesc_sep_def import statdesc_sep_def


def statdesc_sep_data_def(num, stat_label, sep):
    if is_numeric_dtype(type(num)) == True:
        if stat_label in ['count', 'non zero count', 'unique count']:
            if sep in [',c', ',cL']:
                num = statdesc_sep_def(num=num, sep=',')
            elif sep in ['.c', '.cL']:
                num = statdesc_sep_def(num=num, sep='.')
            else:
                num = statdesc_sep_def(num=num, sep=sep)
        else:
            num = statdesc_sep_def(num=num, sep=sep)
    else:
        raise Exception('Unsupported data type!')
    return num