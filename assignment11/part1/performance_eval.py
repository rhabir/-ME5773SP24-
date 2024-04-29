import numpy as np
import searchUtilsTeam04 as search
import time

# Create a large array with unique elements
array_size = 10**7
array = np.linspace(-10, 10, array_size)

# Find the index of the second to last element using numpy's searchsorted
start_time = time.time()
numpy_index = np.searchsorted(array, array[-2])
numpy_time = time.time() - start_time

# Ensure to access the linear search function from the Fortran module correctly
# Assume the function is accessed as search.searchutils.linearsearch based on your Fortran module structure
start_time = time.time()
fortran_index = search.searchutils.linearsearch(array, array[-2], array_size)  # Assuming the linear search function requires the size
fortran_time = time.time() - start_time

# Display performance results
print("Numpy searchsorted time:", numpy_time)
print("Fortran linear search time:", fortran_time)
print("Numpy index:", numpy_index)
print("Fortran index:", fortran_index)

# Additional testing for Fortran binary search for comparison (only valid for sorted arrays)
start_time = time.time()
fortran_binary_index = search.searchutils.binarysearch(array, array[-2], array_size)
fortran_binary_time = time.time() - start_time

# Display results for binary search
print("Fortran binary search time:", fortran_binary_time)
print("Fortran binary search index:", fortran_binary_index)

