import numpy as np
import time

# Start time for NumPy operations
start_cpu_time = time.time()

N= 30000
# Matrix and vector initialization
K_cpu = np.zeros((N, N), dtype=np.float64)
np.fill_diagonal(K_cpu, 4)
np.fill_diagonal(K_cpu[:-1, 1:], -2)
np.fill_diagonal(K_cpu[1:, :-1], -2)
K_cpu[-1, -1] = 2  # Set the last diagonal element

f_cpu = np.zeros(N, dtype=np.float64)
f_cpu[-1] = 1/N  # Set the last element of f to 1/N

# Solve the system of equations using NumPy
u_cpu = np.linalg.solve(K_cpu, f_cpu)

# End time for NumPy operations
end_cpu_time = time.time()
cpu_execution_time = end_cpu_time - start_cpu_time


print("Matrix K:", K_cpu)
print("Matrix f:", f_cpu)

print("\nSolution vector u (CPU):")
print(u_cpu)
print(f"Value of u[N-1] on CPU: {u_cpu[-1]}")

print("CPU execution time (NumPy):", cpu_execution_time, "seconds")
