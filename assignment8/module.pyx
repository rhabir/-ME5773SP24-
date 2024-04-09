# cython: wraparound=False
# cython: boundscheck=False
# cython: profile=True
# cython: initializedcheck=False
import cython
cimport cython

import  numpy as np
cimport numpy as np

cimport libc.math as cmath # Import c- math libraries.

import math # Math function in python

def func_eval_cy(np.ndarray[double] x_arr):
    """
    DESCRIPTION:
        This function evaluates the sin(x)*cos(x) for an array of values.

    INPUTS:
        - x_arr: (Array), input values to evaluate the function.
    """

    cdef int i
    
    cdef np.ndarray[double] res = np.empty_like(x_arr)

    for i in range( x_arr.shape[0] ):
        res[i] = cmath.sin(x_arr[i])*cmath.cos(x_arr[i])
    # end for

    return res

# end function

def func_eval_cy_mem(double[::1] x_arr):
    """
    DESCRIPTION:
        This function evaluates the sin(x)*cos(x) for an array of values.

    INPUTS:
        - x_arr: (Array), input values to evaluate the function.
    """

    cdef int i
    cdef double[:] res = np.empty_like(x_arr)

    for i in range( x_arr.shape[0] ):
        res[i] = cmath.sin(x_arr[i])*cmath.cos(x_arr[i])
    # end for

    return res

# end function

def func_eval_py(x_arr):
    """
    DESCRIPTION:
        This function evaluates the sin(x)*cos(x) for an array of values.

    INPUTS:
        - x_arr: (Array), input values to evaluate the function.
    """
    cdef int i
    res = np.empty_like(x_arr)
    
    for i in range( x_arr.shape[0] ):
        res[i] = math.sin(x_arr[i])*math.cos(x_arr[i])
    # end for
    
    return res

# end function