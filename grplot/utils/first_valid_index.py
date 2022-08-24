import numpy
import pandas


def first_valid_index(series):
    if type(series) in [list, numpy.ndarray]:
        try:
            first_valid_index = (~numpy.isnan(series)).argmax()
        except:
            first_valid_index = numpy.where(series==numpy.array([value for value in series if str(value) != 'nan'])[0])[0][0]
    elif type(series) == pandas.core.series.Series:
        first_valid_index = series.first_valid_index()
    else:
        raise Exception('Unsupported data structure!')
    return first_valid_index