import numpy 


def strtoarray(x, y):
    if type(x) == str:
        x = numpy.hstack([x]*len(y)) # string x to array[len(y) x string]
    elif type(y) == str:
        y = numpy.hstack([y]*len(x)) # string y to array[len(x) y string]
    else:
        pass
    return x, y