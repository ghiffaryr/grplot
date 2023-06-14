from pandas.api.types import is_float_dtype, is_integer_dtype


def statdesc_sep_def(num, sep):
    # comma
    if sep in [',', ',c', ',L', ',cL']:
        if abs(num) < 1:
            if (sep in [',c', ',cL']) and (abs(num) >= 0.01):
                num = '{:,.2f}'.format(num)
            else:
                num = '{:,}'.format(num)
        else: # abs(num) >= 1
            if sep in [',c', ',cL']:
                num = '{:,.2f}'.format(num)
            else:
                if is_float_dtype(type(num)) == True:
                    if num.is_integer() == True:
                        num = '{:,}'.format(int(num))
                    else:
                        num = '{:,.1f}'.format(num)
                elif is_integer_dtype(type(num)) == True:
                    num = '{:,}'.format(num)
                else:
                    pass
    # dot
    elif sep in ['.', '.c', '.L', '.cL']:
        if abs(num) < 1:
            if (sep in ['.c', '.cL']) and (abs(num) >= 0.01):
                num = '{:,.2f}'.format(num).replace(',', '~').replace('.', ',').replace('~', '.')
            else:
                num = '{:,}'.format(num).replace(',', '~').replace('.', ',').replace('~', '.')
        else: # abs(num) >= 1
            if sep in ['.c', '.cL']:
                num = '{:,.2f}'.format(num).replace(',', '~').replace('.', ',').replace('~', '.')
            else:
                if is_float_dtype(type(num)) == True:
                    if num.is_integer() == True:
                        num = '{:,}'.format(int(num)).replace(',', '~').replace('.', ',').replace('~', '.')
                    else:
                        num = '{:,.1f}'.format(num).replace(',', '~').replace('.', ',').replace('~', '.')
                elif is_integer_dtype(type(num)) == True:
                    num = '{:,}'.format(num).replace(',', '~').replace('.', ',').replace('~', '.')
                else:
                    pass
    else:
        raise Exception('Unknown sep argument!')
    return num