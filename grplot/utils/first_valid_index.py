import numpy
import pandas


def first_valid_index(series):
    if type(series) in [list, numpy.ndarray]:
        first_valid_index = (~numpy.isnan(series)).argmax()
    elif type(series) == pandas.core.series.Series:
        first_valid_index = series.first_valid_index()
    else:
        raise Exception('Unsupported data structure!')
    return first_valid_index