from decimal import Decimal


def trim_to_3_nonzero_after_decimal(num, dec_point='.'):
    """
    For |num| < 1: return a string truncated at the digit that contains the 3rd
    non-zero digit after the decimal point. Zeros between non-zero digits are kept.
    Examples:
      0.000123456 -> '0.000123'
      0.004560078 -> '0.00456'
      0.12        -> '0.12'
    """
    sign = '-' if num < 0 else ''
    n = abs(num)
    d = Decimal(str(n))
    s = format(d, 'f')  # full decimal expansion, no exponent
    if '.' not in s:
        return sign + s.replace('.', dec_point)
    int_part, frac = s.split('.')

    nonzero = 0
    cut = None
    for i, ch in enumerate(frac):
        if ch != '0':
            nonzero += 1
            if nonzero == 3:
                cut = i
                break

    if cut is None:
        # fewer than 3 non-zero digits -> strip trailing zeros
        frac = frac.rstrip('0')
        if not frac:
            return sign + int_part.replace('.', dec_point)
        return sign + int_part + dec_point + frac
    else:
        return sign + int_part + dec_point + frac[: cut + 1]