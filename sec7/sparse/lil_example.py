# Example for converting a lil matrix.
import numpy as np
import scipy as sp
import scipy.sparse as spr


Adense = np.array([[ 1, -1, 0, -3, 0],
	               [-1,  5, 0,  0, 0],
	               [ 0,  0, 4,  6, 4],
	               [-4,  0, 2,  7, 0],
	               [ 0,  8, 0,  0,-5]])


Alil = spr.lil_array(Adense)

print('A.shape:', Alil.shape)
print('A.nnz:  ', Alil.nnz)
print()
print('A.data:')
print(Alil.data)
print()
print('A.rows:')
print(Alil.rows)