import numpy as np
<<<<<<< HEAD
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
=======
from math import *
import time
import numexpr as ne

N = 10**9
deltax = 2/N


#3.2_For_loop

start = time.time()
F1 = 0
for i in range(N):
    xi = (2*i/N) - 1
    F1 += sqrt(4 - 4*xi**2) * deltax
end = time.time()

print("Value of F1:", format(F1, ".16f"))
print("Time taken to compute F1 with a for loop:", format(end - start, ".6f"), "seconds")




# 3.3 Vectorized

start = time.time()
i_vec = np.arange(N)
x_vec = (2 * i_vec / N) - 1
F_vec = np.sqrt(4 - 4*x_vec**2)
F2 = np.sum(F_vec)
end = time.time()

print("Value of F2:", F2)
print("Time taken to compute F2 with vectorization:", format(end - start, ".6f"), "seconds")
>>>>>>> 5869bc22836099f66ad2dc3131be58cdfd7b121a




<<<<<<< HEAD


i_vec = np.arange(N)
x_vec = numexpr.evaluate('(2 * i_vec / N) - 1')
F_vec = numexpr.evaluate('sqrt(4 - 4 * x_vec**2)')
F3 = numexpr.evaluate('sum(F_vec)')
start_time = time.time()
elapsed_time = time.time() - start_time

print("\nUsing numexpr evaluations:")
print(f"Elapsed Time: {elapsed_time:.6f} seconds")
print(f"F3 Value: {F3:.16f}")
=======
# 3.4 Numexpr 


start = time.time()
i_vec = np.arange(N)
x_vec = ne.evaluate('(2*i_vec/N)-1')
F_vec = ne.evaluate('sqrt(4 - 4*x_vec**2)')
F3 = ne.evaluate('sum(F_vec)')
end = time.time()

print("Value of F3:", F3)
print("Time taken to compute F3 with numexpr:", format(end - start, ".6f"), "seconds")
>>>>>>> 5869bc22836099f66ad2dc3131be58cdfd7b121a
