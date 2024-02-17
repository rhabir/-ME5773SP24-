import numpy as np
import time

# Input the value of N
N = int(input("Enter the value of N: "))

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

# Measure the time taken to create K and f
start = time.time()
K = K
f = f
end = time.time()
print("\nTime taken to create K and f:", end - start, "seconds")

# Solve for u
start = time.time()
u = np.linalg.solve(K, f)
end = time.time()
print("\nTime taken to solve for u:", end - start, "seconds")

print("\nu[N-1] =", u[-1])
