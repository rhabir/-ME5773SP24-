import numpy as np
import math
import time


def funct1(x,y,z):
	return math.sin(x*y)+math.exp(z)*x*y
# end function

def funct2(X,Y,Z):
	
	res = np.zeros(X.shape)
	
	for i in range(X.shape[0]):
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