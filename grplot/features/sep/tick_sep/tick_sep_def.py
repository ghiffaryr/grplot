import matplotlib as mpl
from matplotlib import ticker
import locale
from pandas.api.types import is_float_dtype, is_integer_dtype


def tick_sep_def(ax, axis, sep):
    lim = mpl.rcParams["axes.formatter.limits"] # default: lim = [-5,6]
    if axis == 'x':
        # comma
        if sep == ',':
            xnum = []
            for x in ax.get_xticks():
                if (abs(x) <= 10**lim[0] and abs(x) != 0) or abs(x) >= 10**lim[1]:
                    ax.xaxis.set_major_formatter(ticker.ScalarFormatter(useLocale=False))
                    xnum = []
                    break
                elif abs(x) > 10**lim[0] and abs(x) < 1:
                    x = round(x, abs(lim[0]))
                    xnum.append('{:,}'.format(x))
                else: # abs(x) >= 1 and abs(x) < 10**lim[1]
                    if is_float_dtype(type(x)) == True:
                        if x.is_integer() == True:
                            xnum.append('{:,}'.format(int(x)))
                        else:
                            xnum.append('{:,.1f}'.format(x))
                    elif is_integer_dtype(type(x)) == True:
                        xnum.append('{:,}'.format(x))
                    else:
                        pass
            if xnum != []:
                ax.set_xticks(ax.get_xticks())
                ax.set_xticklabels(xnum)
            else:
                pass
        elif sep == ',c':
            xnum = []
            for x in ax.get_xticks():
                if abs(x) <= 10**lim[0] and abs(x) != 0:
                    ax.xaxis.set_major_formatter(ticker.ScalarFormatter(useLocale=False))
                    xnum = []
                    break
                elif abs(x) > 10**lim[0] and abs(x) < 1:
                    if (abs(x) == 0) or (abs(x) >= 0.01):
                        xnum.append('{:,.2f}'.format(x))
                    else:
                        x = round(x, abs(lim[0]))
                        xnum.append('{:,}'.format(x))
                else: # abs(x) >= 1
                    xnum.append('{:,.2f}'.format(x))
            if xnum != []:
                ax.set_xticks(ax.get_xticks())
                ax.set_xticklabels(xnum)
            else:
                pass
        elif sep in [',L', ',cL']:
            xnum = []
            for x in ax.get_xticks():
                if abs(x) <= 10**lim[0] and abs(x) != 0:
                    ax.xaxis.set_major_formatter(ticker.ScalarFormatter(useLocale=False))
                    xnum = []
                    break
                else: # abs(x) > 10**lim[0]
                    if abs(x) < 1:
                        if sep == ',cL' and ((abs(x) == 0) or (abs(x) >= 0.01)):
                            xnum.append('{:,.2f}'.format(x))
                        else:
                            x = round(x, abs(lim[0]))
                            xnum.append('{:,}'.format(x))
                    elif abs(x) < 1_000:
                        if sep == ',L':
                            if is_float_dtype(type(x)) == True:
                                if x.is_integer() == True:
                                    xnum.append('{:,}'.format(int(x)))
                                else:
                                    xnum.append('{:,.1f}'.format(x))
                            elif is_integer_dtype(type(x)) == True:
                                xnum.append('{:,}'.format(x))
                            else:
                                pass
                        else: # sep == ',cL'
                            xnum.append('{:,.2f}'.format(x))
                    elif abs(x) < 1_000_000:
                        num = x/1_000
                        if is_float_dtype(type(x)) == True:
                            if num.is_integer() == True:
                                xnum.append('{:,}K'.format(int(num)))
                            else:    
                                xnum.append('{:,.1f}K'.format(num))
                        elif is_integer_dtype(type(x)) == True:
                            xnum.append('{:,}K'.format(num))
                        else:
                            pass
                    elif abs(x) < 1_000_000_000:
                        num = x/1_000_000
                        if is_float_dtype(type(x)) == True:
                            if num.is_integer() == True:
                                xnum.append('{:,}M'.format(int(num)))
                            else:    
                                xnum.append('{:,.1f}M'.format(num))
                        elif is_integer_dtype(type(x)) == True:
                            xnum.append('{:,}M'.format(num))
                        else:
                            pass
                    elif abs(x) < 1_000_000_000_000:
                        num = x/1_000_000_000
                        if is_float_dtype(type(x)) == True:
                            if num.is_integer() == True:
                                xnum.append('{:,}B'.format(int(num)))
                            else:    
                                xnum.append('{:,.1f}B'.format(num))
                        elif is_integer_dtype(type(x)) == True:
                            xnum.append('{:,}B'.format(num))
                        else:
                            pass
                    elif abs(x) < 1_000_000_000_000_000:
                        num = x/1_000_000_000_000
                        if is_float_dtype(type(x)) == True:
                            if num.is_integer() == True:
                                xnum.append('{:,}T'.format(int(num)))
                            else:    
                                xnum.append('{:,.1f}T'.format(num))
                        elif is_integer_dtype(type(x)) == True:
                            xnum.append('{:,}T'.format(num))
                        else:
                            pass
                    else: # abs(x) >= 1_000_000_000_000_000:
                        num = x/1_000_000_000_000_000
                        if is_float_dtype(type(x)) == True:
                            if num.is_integer() == True:
                                xnum.append('{:,}Q'.format(int(num)))
                            else:    
                                xnum.append('{:,.1f}Q'.format(num))
                        elif is_integer_dtype(type(x)) == True:
                            xnum.append('{:,}Q'.format(num))
                        else:
                            pass
            if xnum != []:
                ax.set_xticks(ax.get_xticks())
                ax.set_xticklabels(xnum)
            else:
                pass
        # dot
        elif sep == '.':
            xnum = []
            for x in ax.get_xticks():
                if (abs(x) <= 10**lim[0] and abs(x) != 0) or abs(x) >= 10**lim[1]:
                    mpl.rcParams['axes.formatter.use_locale'] = True                    
                    try:
                        locale.setlocale(locale.LC_NUMERIC, "de")
                    except:
                        raise Exception("Your environment doesn't support \"de\" locale! Install it or set matplotlib.rcParams['axes.formatter.limits'] bigger than the dataframe.")
                    ax.xaxis.set_major_formatter(ticker.ScalarFormatter(useLocale=True))
                    xnum = []
                    break
                elif abs(x) > 10**lim[0] and abs(x) < 1:
                    x = round(x, abs(lim[0]))
                    xnum.append('{:,}'.format(x).replace(',', '~').replace('.', ',').replace('~', '.'))
                else: # abs(x) >= 1 and abs(x) < 10**lim[1]
                    if is_float_dtype(type(x)) == True:
                        if x.is_integer() == True:
                            xnum.append('{:,}'.format(int(x)).replace(',', '~').replace('.', ',').replace('~', '.'))
                        else:
                            xnum.append('{:,.1f}'.format(x).replace(',', '~').replace('.', ',').replace('~', '.'))
                    elif is_integer_dtype(type(x)) == True:
                        xnum.append('{:,}'.format(x).replace(',', '~').replace('.', ',').replace('~', '.'))
                    else:
                        pass
            if xnum != []:
                ax.set_xticks(ax.get_xticks())
                ax.set_xticklabels(xnum)
            else:
                pass
        elif sep == '.c':
            xnum = []
            for x in ax.get_xticks():
                if abs(x) <= 10**lim[0] and abs(x) != 0:
                    mpl.rcParams['axes.formatter.use_locale'] = True
                    try:
                        locale.setlocale(locale.LC_NUMERIC, "de")
                    except:
                        raise Exception("Your environment doesn't support \"de\" locale! Install it or set matplotlib.rcParams['axes.formatter.limits'] bigger than the dataframe.")
                    ax.xaxis.set_major_formatter(ticker.ScalarFormatter(useLocale=True))
                    xnum = []
                    break
                elif abs(x) > 10**lim[0] and abs(x) < 1:
                    if (abs(x) == 0) or (abs(x) >= 0.01):
                        xnum.append('{:,.2f}'.format(x).replace(',', '~').replace('.', ',').replace('~', '.'))
                    else:
                        x = round(x, abs(lim[0]))
                        xnum.append('{:,}'.format(x).replace(',', '~').replace('.', ',').replace('~', '.'))
                else: # abs(x) >= 1
                    xnum.append('{:,.2f}'.format(x).replace(',', '~').replace('.', ',').replace('~', '.'))
            if xnum != []:
                ax.set_xticks(ax.get_xticks())
                ax.set_xticklabels(xnum)
            else:
                pass
        elif sep in ['.L', '.cL']:
            xnum = []
            for x in ax.get_xticks():
                if abs(x) <= 10**lim[0] and abs(x) != 0:
                    mpl.rcParams['axes.formatter.use_locale'] = True
                    try:
                        locale.setlocale(locale.LC_NUMERIC, "de")
                    except:
                        raise Exception("Your environment doesn't support \"de\" locale! Install it or set matplotlib.rcParams['axes.formatter.limits'] bigger than the dataframe.")
                    ax.xaxis.set_major_formatter(ticker.ScalarFormatter(useLocale=True))
                    xnum = []
                    break
                else: # abs(x) > 10**lim[0]
                    if abs(x) < 1:
                        if sep == '.cL' and ((abs(x) == 0) or (abs(x) >= 0.01)):
                            xnum.append('{:,.2f}'.format(x).replace(',', '~').replace('.', ',').replace('~', '.'))
                        else:
                            x = round(x, abs(lim[0]))
                            xnum.append('{:,}'.format(x).replace(',', '~').replace('.', ',').replace('~', '.'))
                    elif abs(x) < 1_000:
                        if sep == '.L':
                            if is_float_dtype(type(x)) == True:
                                if x.is_integer() == True:
                                    xnum.append('{:,}'.format(int(x)).replace(',', '~').replace('.', ',').replace('~', '.'))
                                else:
                                    xnum.append('{:,.1f}'.format(x).replace(',', '~').replace('.', ',').replace('~', '.'))
                            elif is_integer_dtype(type(x)) == True:
                                xnum.append('{:,}'.format(x).replace(',', '~').replace('.', ',').replace('~', '.'))
                            else:
                                pass
                        else: # sep == '.cL'
                            xnum.append('{:,.2f}'.format(x).replace(',', '~').replace('.', ',').replace('~', '.'))
                    elif abs(x) < 1_000_000:
                        num = x/1_000
                        if is_float_dtype(type(x)) == True:
                            if num.is_integer() == True:
                                xnum.append('{:,}K'.format(int(num)).replace(',', '~').replace('.', ',').replace('~', '.'))
                            else:    
                                xnum.append('{:,.1f}K'.format(num).replace(',', '~').replace('.', ',').replace('~', '.'))
                        elif is_integer_dtype(type(x)) == True:
                            xnum.append('{:,}K'.format(num).replace(',', '~').replace('.', ',').replace('~', '.'))
                        else:
                            pass
                    elif abs(x) < 1_000_000_000:
                        num = x/1_000_000
                        if is_float_dtype(type(x)) == True:
                            if num.is_integer() == True:
                                xnum.append('{:,}M'.format(int(num)).replace(',', '~').replace('.', ',').replace('~', '.'))
                            else:    
                                xnum.append('{:,.1f}M'.format(num).replace(',', '~').replace('.', ',').replace('~', '.'))
                        elif is_integer_dtype(type(x)) == True:
                            xnum.append('{:,}M'.format(num).replace(',', '~').replace('.', ',').replace('~', '.'))
                        else:
                            pass
                    elif abs(x) < 1_000_000_000_000:
                        num = x/1_000_000_000
                        if is_float_dtype(type(x)) == True:
                            if num.is_integer() == True:
                                xnum.append('{:,}B'.format(int(num)).replace(',', '~').replace('.', ',').replace('~', '.'))
                            else:    
                                xnum.append('{:,.1f}B'.format(num).replace(',', '~').replace('.', ',').replace('~', '.'))
                        elif is_integer_dtype(type(x)) == True:
                            xnum.append('{:,}B'.format(num).replace(',', '~').replace('.', ',').replace('~', '.'))
                        else:
                            pass
                    elif abs(x) < 1_000_000_000_000_000:
                        num = x/1_000_000_000_000
                        if is_float_dtype(type(x)) == True:
                            if num.is_integer() == True:
                                xnum.append('{:,}T'.format(int(num)).replace(',', '~').replace('.', ',').replace('~', '.'))
                            else:    
                                xnum.append('{:,.1f}T'.format(num).replace(',', '~').replace('.', ',').replace('~', '.'))
                        elif is_integer_dtype(type(x)) == True:
                            xnum.append('{:,}T'.format(num).replace(',', '~').replace('.', ',').replace('~', '.'))
                        else:
                            pass
                    else: # abs(x) >= 1_000_000_000_000_000:
                        num = x/1_000_000_000_000_000
                        if is_float_dtype(type(x)) == True:
                            if num.is_integer() == True:
                                xnum.append('{:,}Q'.format(int(num)).replace(',', '~').replace('.', ',').replace('~', '.'))
                            else:    
                                xnum.append('{:,.1f}Q'.format(num).replace(',', '~').replace('.', ',').replace('~', '.'))
                        elif is_integer_dtype(type(x)) == True:
                            xnum.append('{:,}Q'.format(num).replace(',', '~').replace('.', ',').replace('~', '.'))
                        else:
                            pass
            if xnum != []:
                ax.set_xticks(ax.get_xticks())
                ax.set_xticklabels(xnum)
            else:
                pass
        else:
            raise Exception('Unknown sep argument!')
    elif axis == 'y':
        # comma
        if sep == ',':
            ynum = []
            for y in ax.get_yticks():
                if (abs(y) <= 10**lim[0] and abs(y) != 0) or abs(y) >= 10**lim[1]:
                    ax.yaxis.set_major_formatter(ticker.ScalarFormatter(useLocale=False))
                    ynum = []
                    break
                elif abs(y) > 10**lim[0] and abs(y) < 1:
                    y = round(y, abs(lim[0]))
                    ynum.append('{:,}'.format(y))
                else: # abs(y) >= 1 and abs(y) < 10**lim[1]
                    if is_float_dtype(type(y)) == True:
                        if y.is_integer() == True:
                            ynum.append('{:,}'.format(int(y)))
                        else:
                            ynum.append('{:,.1f}'.format(y))
                    elif is_integer_dtype(type(y)) == True:
                        ynum.append('{:,}'.format(y))
                    else:
                        pass
            if ynum != []:
                ax.set_yticks(ax.get_yticks())
                ax.set_yticklabels(ynum)
            else:
                pass
        elif sep == ',c':
            ynum = []
            for y in ax.get_yticks():
                if abs(y) <= 10**lim[0] and abs(y) != 0:
                    ax.yaxis.set_major_formatter(ticker.ScalarFormatter(useLocale=False))
                    ynum = []
                    break
                elif abs(y) > 10**lim[0] and abs(y) < 1:
                    if (abs(y) == 0) or (abs(y) >= 0.01):
                        ynum.append('{:,.2f}'.format(y))
                    else:
                        y = round(y, abs(lim[0]))
                        ynum.append('{:,}'.format(y))
                else: # abs(y) >= 1
                    ynum.append('{:,.2f}'.format(y))
            if ynum != []:
                ax.set_yticks(ax.get_yticks())
                ax.set_yticklabels(ynum)
            else:
                pass
        elif sep in [',L', ',cL']:
            ynum = []
            for y in ax.get_yticks():
                if abs(y) <= 10**lim[0] and abs(y) != 0:
                    ax.yaxis.set_major_formatter(ticker.ScalarFormatter(useLocale=False))
                    ynum = []
                    break
                else: # abs(y) > 10**lim[0]
                    if abs(y) < 1:
                        if sep == ',cL' and ((abs(y) == 0) or (abs(y) >= 0.01)):
                            ynum.append('{:,.2f}'.format(y))
                        else:
                            y = round(y, abs(lim[0]))
                            ynum.append('{:,}'.format(y))
                    elif abs(y) < 1_000:
                        if sep == ',L':
                            if is_float_dtype(type(y)) == True:
                                if y.is_integer() == True:
                                    ynum.append('{:,}'.format(int(y)))
                                else:
                                    ynum.append('{:,.1f}'.format(y))
                            elif is_integer_dtype(type(y)) == True:
                                ynum.append('{:,}'.format(y))
                            else:
                                pass
                        else: # sep == ',cL'
                            ynum.append('{:,.2f}'.format(y))
                    elif abs(y) < 1_000_000:
                        num = y/1_000
                        if is_float_dtype(type(y)) == True:
                            if num.is_integer() == True:
                                ynum.append('{:,}K'.format(int(num)))
                            else:    
                                ynum.append('{:,.1f}K'.format(num))
                        elif is_integer_dtype(type(y)) == True:
                            ynum.append('{:,}K'.format(num))
                        else:
                            pass
                    elif abs(y) < 1_000_000_000:
                        num = y/1_000_000
                        if is_float_dtype(type(y)) == True:
                            if num.is_integer() == True:
                                ynum.append('{:,}M'.format(int(num)))
                            else:    
                                ynum.append('{:,.1f}M'.format(num))
                        elif is_integer_dtype(type(y)) == True:
                            ynum.append('{:,}M'.format(num))
                        else:
                            pass
                    elif abs(y) < 1_000_000_000_000:
                        num = y/1_000_000_000
                        if is_float_dtype(type(y)) == True:
                            if num.is_integer() == True:
                                ynum.append('{:,}B'.format(int(num)))
                            else:    
                                ynum.append('{:,.1f}B'.format(num))
                        elif is_integer_dtype(type(y)) == True:
                            ynum.append('{:,}B'.format(num))
                        else:
                            pass
                    elif abs(y) < 1_000_000_000_000_000:
                        num = y/1_000_000_000_000
                        if is_float_dtype(type(y)) == True:
                            if num.is_integer() == True:
                                ynum.append('{:,}T'.format(int(num)))
                            else:    
                                ynum.append('{:,.1f}T'.format(num))
                        elif is_integer_dtype(type(y)) == True:
                            ynum.append('{:,}T'.format(num))
                        else:
                            pass
                    else: # abs(y) >= 1_000_000_000_000_000:
                        num = y/1_000_000_000_000_000
                        if is_float_dtype(type(y)) == True:
                            if num.is_integer() == True:
                                ynum.append('{:,}Q'.format(int(num)))
                            else:    
                                ynum.append('{:,.1f}Q'.format(num))
                        elif is_integer_dtype(type(y)) == True:
                            ynum.append('{:,}Q'.format(num))
                        else:
                            pass
            if ynum != []:
                ax.set_yticks(ax.get_yticks())
                ax.set_yticklabels(ynum)
            else:
                pass
        # dot
        elif sep == '.':
            ynum = []
            for y in ax.get_yticks():
                if (abs(y) <= 10**lim[0] and abs(y) != 0) or abs(y) >= 10**lim[1]:
                    mpl.rcParams['axes.formatter.use_locale'] = True
                    try:
                        locale.setlocale(locale.LC_NUMERIC, "de")
                    except:
                        raise Exception("Your environment doesn't support \"de\" locale! Install it or set matplotlib.rcParams['axes.formatter.limits'] bigger than the dataframe.")
                    ax.yaxis.set_major_formatter(ticker.ScalarFormatter(useLocale=True))
                    ynum = []
                    break
                elif abs(y) > 10**lim[0] and abs(y) < 1:
                    y = round(y, abs(lim[0]))
                    ynum.append('{:,}'.format(y).replace(',', '~').replace('.', ',').replace('~', '.'))
                else: # abs(y) >= 1 and abs(y) < 10**lim[1]
                    if is_float_dtype(type(y)) == True:
                        if y.is_integer():
                            ynum.append('{:,}'.format(int(y)).replace(',', '~').replace('.', ',').replace('~', '.'))
                        else:
                            ynum.append('{:,.1f}'.format(y).replace(',', '~').replace('.', ',').replace('~', '.'))
                    elif is_integer_dtype(type(y)) == True:
                        ynum.append('{:,}'.format(y).replace(',', '~').replace('.', ',').replace('~', '.'))
                    else:
                        pass
            if ynum != []:
                ax.set_yticks(ax.get_yticks())
                ax.set_yticklabels(ynum)
            else:
                pass
        elif sep == '.c':
            ynum = []
            for y in ax.get_yticks():
                if abs(y) <= 10**lim[0] and abs(y) != 0:
                    mpl.rcParams['axes.formatter.use_locale'] = True
                    try:
                        locale.setlocale(locale.LC_NUMERIC, "de")
                    except:
                        raise Exception("Your environment doesn't support \"de\" locale! Install it or set matplotlib.rcParams['axes.formatter.limits'] bigger than the dataframe.")
                    ax.yaxis.set_major_formatter(ticker.ScalarFormatter(useLocale=True))
                    ynum = []
                    break
                elif abs(y) > 10**lim[0] and abs(y) < 1:
                    if (abs(y) == 0) or (abs(y) >= 0.01):
                        ynum.append('{:,.2f}'.format(y).replace(',', '~').replace('.', ',').replace('~', '.'))
                    else:
                        y = round(y, abs(lim[0]))
                        ynum.append('{:,}'.format(y).replace(',', '~').replace('.', ',').replace('~', '.'))
                else: # abs(y) >= 1
                    ynum.append('{:,.2f}'.format(y).replace(',', '~').replace('.', ',').replace('~', '.'))
            if ynum != []:
                ax.set_yticks(ax.get_yticks())
                ax.set_yticklabels(ynum)
            else:
                pass
        elif sep in ['.L', '.cL']:
            ynum = []
            for y in ax.get_yticks():
                if abs(y) <= 10**lim[0] and abs(y) != 0:
                    mpl.rcParams['axes.formatter.use_locale'] = True
                    try:
                        locale.setlocale(locale.LC_NUMERIC, "de")
                    except:
                        raise Exception("Your environment doesn't support \"de\" locale! Install it or set matplotlib.rcParams['axes.formatter.limits'] bigger than the dataframe.")
                    ax.yaxis.set_major_formatter(ticker.ScalarFormatter(useLocale=True))
                    ynum = []
                    break
                else: # abs(y) > 10**lim[0]
                    if abs(y) < 1:
                        if sep == '.cL' and ((abs(y) == 0) or (abs(y) >= 0.01)):
                            ynum.append('{:,.2f}'.format(y).replace(',', '~').replace('.', ',').replace('~', '.'))
                        else:
                            y = round(y, abs(lim[0]))
                            ynum.append('{:,}'.format(y).replace(',', '~').replace('.', ',').replace('~', '.'))
                    elif abs(y) < 1_000:
                        if sep == '.L':
                            if is_float_dtype(type(y)) == True:
                                if y.is_integer() == True:
                                    ynum.append('{:,}'.format(int(y)).replace(',', '~').replace('.', ',').replace('~', '.'))
                                else:
                                    ynum.append('{:,.1f}'.format(y).replace(',', '~').replace('.', ',').replace('~', '.'))
                            elif is_integer_dtype(type(y)) == True:
                                ynum.append('{:,}'.format(y).replace(',', '~').replace('.', ',').replace('~', '.'))
                            else:
                                pass
                        else: # sep == '.cL'
                            ynum.append('{:,.2f}'.format(y).replace(',', '~').replace('.', ',').replace('~', '.'))
                    elif abs(y) < 1_000_000:
                        num = y/1_000
                        if is_float_dtype(type(y)) == True:
                            if num.is_integer() == True:
                                ynum.append('{:,}K'.format(int(num)).replace(',', '~').replace('.', ',').replace('~', '.'))
                            else:    
                                ynum.append('{:,.1f}K'.format(num).replace(',', '~').replace('.', ',').replace('~', '.'))
                        elif is_integer_dtype(type(y)) == True:
                            ynum.append('{:,}K'.format(num).replace(',', '~').replace('.', ',').replace('~', '.'))
                        else:
                            pass
                    elif abs(y) < 1_000_000_000:
                        num = y/1_000_000
                        if is_float_dtype(type(y)) == True:
                            if num.is_integer() == True:
                                ynum.append('{:,}M'.format(int(num)).replace(',', '~').replace('.', ',').replace('~', '.'))
                            else:    
                                ynum.append('{:,.1f}M'.format(num).replace(',', '~').replace('.', ',').replace('~', '.'))
                        elif is_integer_dtype(type(y)) == True:
                            ynum.append('{:,}M'.format(num).replace(',', '~').replace('.', ',').replace('~', '.'))
                        else:
                            pass
                    elif abs(y) < 1_000_000_000_000:
                        num = y/1_000_000_000
                        if is_float_dtype(type(y)) == True:
                            if num.is_integer() == True:
                                ynum.append('{:,}B'.format(int(num)).replace(',', '~').replace('.', ',').replace('~', '.'))
                            else:    
                                ynum.append('{:,.1f}B'.format(num).replace(',', '~').replace('.', ',').replace('~', '.'))
                        elif is_integer_dtype(type(y)) == True:
                            ynum.append('{:,}B'.format(num).replace(',', '~').replace('.', ',').replace('~', '.'))
                        else:
                            pass
                    elif abs(y) < 1_000_000_000_000_000:
                        num = y/1_000_000_000_000
                        if is_float_dtype(type(y)) == True:
                            if num.is_integer() == True:
                                ynum.append('{:,}T'.format(int(num)).replace(',', '~').replace('.', ',').replace('~', '.'))
                            else:    
                                ynum.append('{:,.1f}T'.format(num).replace(',', '~').replace('.', ',').replace('~', '.'))
                        elif is_integer_dtype(type(y)) == True:
                            ynum.append('{:,}T'.format(num).replace(',', '~').replace('.', ',').replace('~', '.'))
                        else:
                            pass
                    else: # abs(y) >= 1_000_000_000_000_000:
                        num = y/1_000_000_000_000_000
                        if is_float_dtype(type(y)) == True:
                            if num.is_integer() == True:
                                ynum.append('{:,}Q'.format(int(num)).replace(',', '~').replace('.', ',').replace('~', '.'))
                            else:    
                                ynum.append('{:,.1f}Q'.format(num).replace(',', '~').replace('.', ',').replace('~', '.'))
                        elif is_integer_dtype(type(y)) == True:
                            ynum.append('{:,}Q'.format(num).replace(',', '~').replace('.', ',').replace('~', '.'))
                        else:
                            pass
            if ynum != []:
                ax.set_yticks(ax.get_yticks())
                ax.set_yticklabels(ynum)
            else:
                pass
        else:
            raise Exception('Unknown sep argument!')
    else:
        raise Exception('Unsupported axis!')
    mpl.rcParams['axes.formatter.use_locale'] = False
    return ax
    