PROGRAM main_program
USE searchutils
USE omp_lib  ! Include the OpenMP library for timing functions

IMPLICIT NONE

INTEGER, PARAMETER :: N2 = 10000000
REAL(8), dimension(10) :: arr_test = [1.d0, 2.d0, 4.d0, 5.d0, 6.d0, 7.d0, 9.d0, 10.d0, 11.d0, 15.d0]
REAL(8) :: arr2(N2)
REAL(8) :: x, t_start, t_end
INTEGER :: idx, n

! Declare the variables used for timing and calculating speedup
REAL(8) :: linear_search_time, binary_search_time
REAL(8) :: time_difference, speedup_factor


n = size(arr_test,1)  ! Number of elements in the array.
x = 7.d0  ! Search for value 7.0 in the array.

idx = linearSearch(arr_test, n, x)
print*, "Index computed with linear search: ", idx



! Fill an array with sorted values and execute timing tests
CALL fillSortedArray(arr2)
x = arr2(N2-1)  ! Value of interest: Second to last element.
n = SIZE(arr2, 1)

t_start = omp_get_wtime()  ! Start measuring time here
idx = linearSearch(arr2, n, x)
t_end = omp_get_wtime()  ! End measuring time here
linear_search_time = t_end - t_start

print*, "CPU time for linear search: ", linear_search_time
print*, "Index computed with linear search: ", idx
print*, "was the value found?: ", arr2(idx) == x

CONTAINS

SUBROUTINE fillSortedArray(array)
    IMPLICIT NONE
    REAL(8), INTENT(INOUT) :: array(:)
    INTEGER :: i
    DO i = 1, SIZE(array, 1)
        array(i) = (i * 3.d0)
    END DO
END SUBROUTINE fillSortedArray

END PROGRAM main_program