import numpy
import pandas

def check_data_structure(df):
    if type(df) == dict:
        if any(isinstance(df[key], list) for key in df.keys()) == True:
            out = 'dictionary-list'
        elif any(isinstance(df[i], numpy.ndarray) for i in df.keys()):
            out = 'dictionary-numpy.array'
        else:
            raise Exception('Unsupported dictionary sub data structure!')
    elif type(df) == pandas.core.frame.DataFrame:
        out = 'pandas dataframe'
    else:
        raise Exception('Unsupported data structure!')
    return out

