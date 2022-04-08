from pandas.api.types import is_numeric_dtype


def check_alpha(alpha, count):
    if (alpha is None) or (is_numeric_dtype(type(alpha))):
        pass
    elif type(alpha) == list:
        alpha = alpha[count]
    else:
        raise Exception('Unsupported alpha argument!')
    return alpha