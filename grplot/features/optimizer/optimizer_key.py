import numpy


def optimizer_key(var_list):
    key = numpy.array([])
    if type(var_list) in [list, numpy.ndarray]:
        for var in var_list:
            if type(var) in [str, numpy.str_]:
                key = numpy.concatenate([key, numpy.array([var])])
            elif type(var) == list:
                key = numpy.concatenate([key, numpy.array(var)])
            elif type(var) == numpy.ndarray:
                key = numpy.concatenate([key, var])
            else:
                pass
    else:
        pass
    return key