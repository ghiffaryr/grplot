import pandas
import numpy


def check_pandas_index(x, y):
    if type(x) == pandas.core.indexes.base.Index: 
        x = numpy.array(x.to_list())
    else:
        pass
    if type(y) == pandas.core.indexes.base.Index: 
        y = numpy.array(y.to_list())
    else:
        pass
    return x, y