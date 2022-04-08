import numpy
from math import ceil


def check_axes(x, y, Nx, Ny):
    # check Nx
    if Nx is None:
        if type(x) in [list, numpy.ndarray]:
            max_Nx = len(x) 
        else:
            max_Nx = 1
    else: 
        pass
    # check Ny
    if Ny is None:
        if type(y) in [list, numpy.ndarray]:
            max_Ny = len(y) 
        else:
            max_Ny = 1
    else: 
        pass
    # determine Nx and Ny
    if Nx is None or Ny is None:
        max_N = max(max_Nx, max_Ny)
        if max_N <= 2:
            Nx = max_N
            Ny = 1
        elif max_N > 2:
            Nx = 2
            Ny = ceil(max_N/2)
    return Nx, Ny