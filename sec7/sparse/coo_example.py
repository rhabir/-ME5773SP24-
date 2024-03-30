# Example for converting a lil matrix.
import numpy as np
import scipy as sp
import scipy.sparse as spr


Adense = np.array([[ 1, -1, 0, -3, 0],
	               [-1,  5, 0,  0, 0],
	               [ 0,  0, 4,  6, 4],
	               [-4,  0, 2,  7, 0],
	               [ 0,  8, 0,  0,-5]])


Acoo = spr.coo_matrix(Adense)
print('A.shape:', Acoo.shape)
print('A.nnz:  ', Acoo.nnz)
print()
print('A.data:')
print(Acoo.data)
print()
print('A.row:')
print(Acoo.row)
print()
print('A.col:')
print(Acoo.col)