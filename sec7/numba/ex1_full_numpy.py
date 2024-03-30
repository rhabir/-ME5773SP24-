import numpy as np

import time



def funct2(X,Y,Z):
	
	return np.sin(X*Y)+np.exp(Z)*X*Y

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
	print(res)
	t_end = time.time()

	print("Execution time large = {0}s".format(t_end-t_start))