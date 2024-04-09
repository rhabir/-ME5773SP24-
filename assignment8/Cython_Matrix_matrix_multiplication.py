import numpy as np
import time
from matmul_cython import matmul_cython

def measure_performance(func, sizes=[3, 10, 100, 1000], iterations=100):
    for size in sizes:
        A = np.random.rand(size, size)
        B = np.random.rand(size, size)
        
        start_time = time.time()
        for _ in range(iterations):
            C = func(A, B)
        end_time = time.time()
        
        avg_time = (end_time - start_time) / iterations
        print(f"Size: {size}x{size}, Avg Time: {avg_time:.6f} seconds")

print("Cython Implementation:")
measure_performance(matmul_cython)

print("\nNumPy dot Function:")
measure_performance(np.dot)
