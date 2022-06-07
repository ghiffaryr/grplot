import numpy
import pandas


def first_valid_index(df):
    if type(df) in [list, numpy.ndarray]:
        first_valid_index = 0
    elif type(df) == pandas.core.frame.DataFrame:
        first_valid_index = df.first_valid_index()
    else:
        raise Exception('Unsupported data structure!')
    return first_valid_index