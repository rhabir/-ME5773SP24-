import numpy as np
import math
import numexpr as ne
import time

N = 10**9
deltax = 2 / N





F1 = 0
start_time = time.time()
for i in range(N):
    xi = 2 * i / N - 1
    fxi = math.sqrt(4 - (4 * xi**2))
    F1 = F1 + (fxi * deltax)
elapsed_time = time.time() - start_time

print(" for loop:")
print(f"Elapsed Time: {elapsed_time:.6f} seconds")
print(f"F1 Value: {F1:.16f}")



i_vec = np.arange(N)
x_vec = (2 * i_vec / N) - 1
F_vec = np.sqrt(4 - 4 * x_vec**2)
F2 = np.sum(F_vec)
start_time = time.time()
elapsed_time = time.time() - start_time


print("\nUsing numpy's vectorized functions:")
print(f"Elapsed Time: {elapsed_time:.6f} seconds")
print(f"F2 Value: {F2:.16f}")






i_vec = np.arange(N)
x_vec = numexpr.evaluate('(2 * i_vec / N) - 1')
F_vec = numexpr.evaluate('sqrt(4 - 4 * x_vec**2)')
F3 = numexpr.evaluate('sum(F_vec)')
start_time = time.time()
elapsed_time = time.time() - start_time

print("\nUsing numexpr evaluations:")
print(f"Elapsed Time: {elapsed_time:.6f} seconds")
print(f"F3 Value: {F3:.16f}")
