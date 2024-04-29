import numpy as np
import searchUtilsTeam04 as search  # This imports the compiled module

sorted_array = np.array([1.0, 2.0, 3.0, 4.0, 5.0], dtype=np.float64)
unsorted_array = np.array([2.0, 1.0, 5.0, 3.0, 6.0], dtype=np.float64)

def test_search_function(search_function, array, value, function_name):
    # Execute search function and print results
    idx = search_function(array, value, len(array))
    if idx != -1:
        print(f"{function_name} found {value} at index: {idx}")
    else:
        print(f"{function_name} didn't find {value}")

def main():
    # Accessing Fortran functions from the module 'searchutils'
    linear_search_func = search.searchutils.linearsearch
    binary_search_func = search.searchutils.binarysearch

    print("Testing on sorted array:")
    test_search_function(linear_search_func, sorted_array, 3.0, "Linear search")
    test_search_function(binary_search_func, sorted_array, 3.0, "Binary search")

    print("\nTesting on unsorted array:")
    test_search_function(linear_search_func, unsorted_array, 3.0, "Linear search")
    # Note: Binary search should not be conducted on an unsorted array

if __name__ == "__main__":
    main()
