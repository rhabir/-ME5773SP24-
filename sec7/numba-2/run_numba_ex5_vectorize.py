import numpy as np
from numba import vectorize
import time


@vectorize('f8(f8,f8,f8)',nopython=True, fastmath=True)
def funct2(x,y,z):
	return np.sin(x*y)+np.exp(z)*x*y
# end function

if __name__=='__main__':

	# First run, small size
	# Dummy call to compil

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