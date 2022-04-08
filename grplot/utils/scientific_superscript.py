def scientific_superscript(num, digits=1, exp=None):
    base, exponent = f'{num:.{digits}e}'.split('e')
    d = dict(zip('-+0123456789','⁻⁺⁰¹²³⁴⁵⁶⁷⁸⁹'))
    if exp == None: 
        exp = exponent
    else:
        n = int(exponent)-int(exp)
        if int(exponent) > 0 and n > int(exponent):
            digits = digits + n
        else:
            pass
        if int(exp) > int(exponent):
            base = float(base)*(10**n)
        else:
            base = float((f'{num:.{digits+n}e}'.split('e'))[0])*(10**n)
        base = f'{base:.{digits}f}'
    return f'{str(base)}$\cdot$10${"".join(d.get(x, x) for x in str(exp).lstrip("0+"))}$'