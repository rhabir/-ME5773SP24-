import numpy as np
import time

# Input the value of N
#N = int(input("Enter the value of N: "))
N = 10000
# Print the value of N
print("N =", N)

# Create the matrix K
K = np.zeros((N, N))
for i in range(N):
    K[i, i] = 2
    if i < N - 1:
        K[i, i + 1] = -1
    if i > 0:
        K[i, i - 1] = -1

K[N - 1, N - 1] = 1

print ( "\nMatrix K=",  "\n",K)

# Create the vector f
f = np.zeros(N)
f[-1] = 1 / N
f = f.reshape((1, N)).T

print("\nVector 𝐟=",  "\n",f)

timings_creation = []
timings_solution = []



# Measure the time taken to create K and f
start = time.time()
K = K
f = f
end = time.time()
timings_creation.append(end - start)
print("\nTime taken to create K and f:", end - start, "seconds")


# Solve for u
start = time.time()
u = np.linalg.solve(K, f)
end = time.time()
timings_solution.append(end - start)

print("\nTime taken to solve for u:", end - start, "seconds")

Total_CPU_time = sum(timings_creation) + sum(timings_solution)
print("\nTotal_CPU_time=", Total_CPU_time, "seconds")


print("\nu[N-1] =", u[-1])
