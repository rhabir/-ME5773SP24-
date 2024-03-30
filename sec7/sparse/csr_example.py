# Example for converting a lil matrix.
import numpy as np
import scipy as sp
import scipy.sparse as spr


Adense = np.array([[ 1, -1, 0, -3, 0],
	               [-1,  5, 0,  0, 0],
	               [ 0,  0, 4,  6, 4],
	               [-4,  0, 2,  7, 0],
	               [ 0,  8, 0,  0,-5]])


Acsr = spr.csr_array(Adense)

print('A.shape:', Acsr.shape)
print('A.nnz:  ', Acsr.nnz)
print()
print('A.data:')
print(Acsr.data)
print()
print('A.indices:')
print(Acsr.indices)
print()
print('A.indptr:')
print(Acsr.indptr)