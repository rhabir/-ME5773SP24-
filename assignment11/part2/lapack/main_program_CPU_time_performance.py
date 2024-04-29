import module as md
import numpy as np
import time


#Mainprogram(matrix as in assignment 4 and mkl solver symm)
N = 10000
A = np.zeros((N, N))

for i in range(N):
    A[i, i] = 2
    
    if i < N - 1:
        A[i, i + 1] = -1
    if i > 0:
        A[i, i - 1] = -1

A[N - 1, N - 1] = 1

b = np.zeros(N)
b[-1] = 1 / N
b = b.reshape((1, N)).T



print(A)
print(b)


t_start = time.time()
res = md.mkl_solver( A,b )
t_end = time.time()

#print(A)
#print(b)

print('Time spent for mkl_solver: {0:.6f} s'.format(t_end-t_start))


t_start = time.time()
res = md.mkl_solver_symm( A,b )
t_end = time.time()

#print(A)
#print(b)


print('Time spent for mkl_solver_symm: {0:.6f} s'.format(t_end-t_start))
