import module as md
import numpy as np
import math
import time
import numba


# Pure python function
def func_eval(x_arr):
    """
    DESCRIPTION:
        This function evaluates the sin(x)*cos(x) for an array of values.

    INPUTS:
        - x_arr: (Array), input values to evaluate the function.
    """

    res = np.empty_like(x_arr)

    for i in range( x_arr.shape[0] ):
        res[i] = math.sin(x_arr[i])*math.cos(x_arr[i])+3
    # end for

    return res

# end function

npoints = 100_000

x   = np.linspace( 0, np.pi, npoints )




t_start = time.time()

res = md.func_eval_cy( x )

t_end = time.time()

print('Time spent: {0:.6f} s -- Cython'.format(t_end-t_start))



t_start = time.time()

res = md.func_eval_cy_mem( x )

t_end = time.time()

print('Time spent: {0:.6f} s -- Cython (memory view)'.format(t_end-t_start))




t_start = time.time()

res = md.func_eval_py( x )

t_end = time.time()

print('Time spent: {0:.6f} s -- Python function compiled with cython.'.format(t_end-t_start))




t_start = time.time()

res = func_eval( x )

t_end = time.time()

print('Time spent: {0:.6f} s -- Pure Python function.'.format(t_end-t_start))

