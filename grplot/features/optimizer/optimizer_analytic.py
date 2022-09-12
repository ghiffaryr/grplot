import numpy
import pandas
from grplot.features.optimizer.optimizer_key import optimizer_key


def optimizer_analytic(df, variables, mode):
    # key
    key = numpy.array([])
    if type(variables) == list:
        key = numpy.concatenate([key, optimizer_key(var_list=variables)])
    elif type(variables) == numpy.ndarray:
        key = numpy.concatenate([key, variables])
    else:
        raise Exception('Unsupported variables type!')
    # key length check
    if len(key) > 0:
        # filter data
        if type(df) == dict:
            df_ = {}
            for k in numpy.unique(key):
                if k in df.keys():
                    if type(df[k]) == list:
                        if mode in ['numpy','saver']:
                            df_[k] = numpy.array(df[k])
                        elif mode in ['pandas','perf']:
                            df_ = pandas.DataFrame.from_dict({k: df[k] for k in numpy.unique(key) if k in df.keys()})
                            break
                        else:
                            raise Exception('Unknown optimizer argument!')
                    elif type(df[k]) == numpy.ndarray:
                        if mode in ['numpy','saver']:
                            df_[k] = df[k]
                        elif mode in ['pandas','perf']:
                            df_ = pandas.DataFrame.from_dict({k: df[k] for k in numpy.unique(key) if k in df.keys()})
                            break
                        else:
                            raise Exception('Unknown optimizer argument!')
                    else:
                        raise Exception('Unsupported dictionary sub data structure!')
                else:
                    pass
        elif type(df) == pandas.core.frame.DataFrame:
            if mode in ['numpy','saver']:
                df_ = {k: df[[k]].to_records()[k] for k in numpy.unique(key) if k in df}
            elif mode in ['pandas','perf']:
                df_ = df[[k for k in numpy.unique(key) if k in df]]
                # if there is only one column
                if type(df_) == pandas.core.series.Series:
                    df_ = pandas.DataFrame(df_)
                else:
                    pass
            else:
                raise Exception('Unknown optimizer argument!')
        else:
            raise Exception('Unsupported data structure!')
    else:
        raise Exception('Wrong data type of axis!')
    return df_