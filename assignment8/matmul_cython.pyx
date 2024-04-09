# cython: language_level=3
import numpy as np
cimport numpy as cnp

def matmul_cython(cnp.ndarray[cnp.float64_t, ndim=2] A, cnp.ndarray[cnp.float64_t, ndim=2] B):
    assert A.shape[1] == B.shape[0], "Matrix shapes do not align"
    cdef int n = A.shape[0], m = A.shape[1], p = B.shape[1]
    cdef cnp.ndarray[cnp.float64_t, ndim=2] C = np.zeros((n, p), dtype=np.float64)
    
    cdef int i, j, k
    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i, j] += A[i, k] * B[k, j]
    
    return np.asarray(C)
