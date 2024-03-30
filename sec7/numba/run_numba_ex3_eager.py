import numpy as np
from numba import jit, prange, float64
import time


@jit(float64(float64,float64,float64),nopython=True, nogil=True)
def funct1(x,y,z):
	return np.sin(x*y)+np.exp(z)*x*y
# end function

@jit(float64[:](float64[:],float64[:],float64[:]),nopython=True, parallel=True, nogil=True)
def funct2(X,Y,Z):
	
	res = np.zeros(X.shape)
	
	for i in prange(X.shape[0]):
		res[i] = funct1(X[i],Y[i],Z[i])
	# end for 

	return res

# end function



if __name__=='__main__':

	# First run, small size
	# Dummy call to compile

	t_start = time.time()

	size = int(10)
	X = np.ones(size)
	Y = np.ones(size)
	Z = np.ones(size)
	res = funct2(X,Y,Z)

	t_end = time.time()

	print("Execution time small= {0}s".format(t_end-t_start))



	t_start = time.time()
	size = int(10**8)
	X = np.ones(size)
	Y = np.ones(size)
	Z = np.ones(size)

	res = funct2(X,Y,Z)

	t_end = time.time()

	print("Execution time large = {0}s".format(t_end-t_start))