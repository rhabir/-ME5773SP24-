
import numpy as np
import scipy.sparse        as spr
import scipy.sparse.linalg as spla




# Load sparse matrix:
A = spr.load_npz('Amat.npz')

# -- What is the format A is stored?
# Compute its sparsity and density.

# Load the vector b in the file 

# Profile your code from here.

# Perform the matrix-vector multiplication Ab.

# -- what happens if you use a dense version of A? How worse/better the performance is?

# Solve system of equations Ax = b

# Solve system of equations Ax = b, but use a dense matrix.

