import numpy


def optimizer_key(var_list):
    key = numpy.array([])
    if type(var_list) not in [list, numpy.ndarray]:
        return key

    for var in var_list:
        if type(var) == str:
            key = numpy.concatenate([key, numpy.array([var])])
        
        if type(var) == list:
            key = numpy.concatenate([key, numpy.array(var)])
        
        if type(var) == numpy.ndarray:
            key = numpy.concatenate([key, var])
    
    return key