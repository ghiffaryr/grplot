import matplotlib as mpl
from pandas.api.types import is_float_dtype, is_integer_dtype
from grplot.utils.scientific_superscript import scientific_superscript


def text_sep_def(num, sep):
    lim = mpl.rcParams["axes.formatter.limits"] # default: lim = [-5,6]
    # comma
    if sep in [',', ',L']:
        if (abs(num) <= 10**lim[0] and abs(num) != 0) or abs(num) >= 10**lim[1]:
            num = scientific_superscript(num)
        elif abs(num) > 10**lim[0] and abs(num) < 1:
            num = round(num, abs(lim[0]))
            num = '{:,}'.format(num)
        else: # abs(num) >= 1 and abs(num) < 10**lim[1]
            if is_float_dtype(type(num)) == True:
                if num.is_integer() == True:
                    num = '{:,}'.format(int(num))
                else:
                    num = '{:,.1f}'.format(num)
            elif is_integer_dtype(type(num)) == True:
                num = '{:,}'.format(num)
            else:
                pass         
    elif sep in [',c', ',cL']:
        if abs(num) <= 10**lim[0] and abs(num) != 0:
            num = scientific_superscript(num)
        elif abs(num) > 10**lim[0] and abs(num) < 1:
            if abs(num) >= 0.01:
                num = '{:,.2f}'.format(num)
            else:
                num = round(num, abs(lim[0]))
                num = '{:,}'.format(num)
        else: # abs(num) >= 1
            num = '{:,.2f}'.format(num)
    # dot
    elif sep in ['.', '.L']:
        if (abs(num) <= 10**lim[0] and abs(num) != 0) or abs(num) >= 10**lim[1]:
            num = scientific_superscript(num).replace(',', '~').replace('.', ',').replace('~', '.')
        elif abs(num) > 10**lim[0] and abs(num) < 1:
            num = round(num, abs(lim[0]))
            num = '{:,}'.format(num).replace(',', '~').replace('.', ',').replace('~', '.')
        else: # abs(num) >= 1 and abs(num) < 10**lim[1]
            if is_float_dtype(type(num)) == True:
                if num.is_integer() == True:
                    num = '{:,}'.format(int(num)).replace(',', '~').replace('.', ',').replace('~', '.')
                else:
                    num = '{:,.1f}'.format(num).replace(',', '~').replace('.', ',').replace('~', '.')
            elif is_integer_dtype(type(num)) == True:
                num = '{:,}'.format(num).replace(',', '~').replace('.', ',').replace('~', '.')
            else:
                pass         
    elif sep in ['.c', '.cL']:
        if abs(num) <= 10**lim[0] and abs(num) != 0:
            num = scientific_superscript(num).replace(',', '~').replace('.', ',').replace('~', '.')
        elif abs(num) > 10**lim[0] and abs(num) < 1:
            if abs(num) >= 0.01:
                num = '{:,.2f}'.format(num).replace(',', '~').replace('.', ',').replace('~', '.')
            else:
                num = round(num, abs(lim[0]))
                num = '{:,}'.format(num).replace(',', '~').replace('.', ',').replace('~', '.')
        else: # abs(num) >= 1
            num = '{:,.2f}'.format(num).replace(',', '~').replace('.', ',').replace('~', '.')
    else:
        raise Exception('Unknown sep argument!')
    return num