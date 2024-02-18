import numpy as np
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




# 3.4 Numexpr 


start = time.time()
i_vec = np.arange(N)
x_vec = ne.evaluate('(2*i_vec/N)-1')
F_vec = ne.evaluate('sqrt(4 - 4*x_vec**2)')
F3 = ne.evaluate('sum(F_vec)')
end = time.time()

print("Value of F3:", F3)
print("Time taken to compute F3 with numexpr:", format(end - start, ".6f"), "seconds")
