import cupy as cp
import time as time
import numpy as np


defK_kernel = cp.RawKernel(r'''
extern "C" __global__
void defK(double* K, int ncols, int nrows) {

/*
This function defines a square matrix K (row-major format)
with all elements in the diagonal as 4 and all elements
next to the diagonal as -2. The last element of the diagonal
set to 2. All other elements are set to zero.
INPUTS:
- K: Pointer to the memory in K.
- nrows: Number of rows of the matrix
- ncols: Number of columns of the matrix
*/

    int i = blockDim.x * blockIdx.x + threadIdx.x;
    int j = blockDim.y * blockIdx.y + threadIdx.y;

    if (i < nrows && j < ncols) {
        if (i == j) {
            if (i == ncols - 1) {
                K[i * ncols + j] = 2.0; // Last diagonal element
            } else {
                K[i * ncols + j] = 4.0; // Diagonal element
            }
        } else if (i == j + 1 || i == j - 1) {
            K[i * ncols + j] = -2.0; // Elements next to diagonal
        } else {
            K[i * ncols + j] = 0.0; // Other elements
        }
    }
}
''', 'defK')

# Create the inputs. Must be defined with corresponding 
# types as in the raw kernel.

start_time = time.time()

N = 30000
K = cp.empty((N, N), dtype=cp.float64)
f = cp.zeros(N, dtype=cp.float64)
f[-1] = 1/N  # Set the last element of f to 1/N

block_dim = 16
grid_dim = (N + block_dim - 1) // block_dim

defK_kernel((grid_dim, grid_dim, 1), (16, 16, 1), (K, K.shape[0], K.shape[1]))

print("Matrix K:", K)
print("Matrix f:", f)

#print(K)
#print (f)



# Solve the system of equations
u = cp.linalg.solve(K, f)

print("\nSolution vector u:")
print(u)

end_time = time.time()

print(f"Value of u[N-1]: {u[-1]}")  # Verify the last element of the solution

cpu_time = end_time - start_time

print("CPU time:", cpu_time, "seconds")