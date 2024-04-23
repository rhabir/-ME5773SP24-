PROGRAM main_program
USE searchutils


  IMPLICIT NONE


  INTEGER, PARAMETER :: N2 = 10000000
  REAL(8), dimension(10) :: arr_test=[1.d0,2.d0,4.d0,5.d0,6.d0,7.d0,9.d0,10.d0,11.d0,15.d0]
  REAL(8) :: arr2(N2)
  REAL(8) :: x, t_start, t_end
  INTEGER :: idx, n
  
  
  
  
  
  ! Declare the variables used for timing and calculating speedup
  REAL(8) :: linear_search_time, binary_search_time
  REAL(8) :: time_difference, speedup_factor
  
  
  
  
  
  
  

  n = size(arr_test,1) ! Number of elements in the array.
  x = 10.d0        ! Search for value 10.0 in the array.
  idx = linearsearch(arr_test,n,x)
  print*, "Index computed with linear search: ", idx

  idx = binarySearch(arr_test,n,x)
  print*, "Index computed with binary search: ", idx



  ! Uncomment lines 27-54 to check the behavior with sorted arrays.

  ! Use here these two cases to evaluate performance.
  print*, " -------------------------- "
  print*, "Testing on a sorted array"

  ! Call the fillSortedArray subroutine to fill arr2 with sorted values.

   CALL fillSortedArray(arr2)
   x = arr2(N2-1)   ! Value of interest: Second to last element.
   n = SIZE(arr2,1)

   ! Measure the CPU time of this linearsearch function.
   CALL CPU_TIME(t_start) ! Start measuring time here
   idx = linearsearch(arr2,n,x)
   ! Complete the CPU TIME measrurement 
  
   ! Idx must be the second to last elemetn.
   print*, "Index computed with linear search: ", idx , N2-1
   print*, "was the value found?: ", arr2(idx)==x

   ! Measure the CPU time of this binarysearch function.
   CALL CPU_TIME(t_start) ! Start measuring time here
   idx = binarysearch(arr2,n,x)
   ! Complete the CPU TIME measrurement 

   print*, "Index computed with binary search: ", idx, N2-1
   print*, "was the value found?: ", arr2(idx)==x
  


   ! Uncomment lines 56-71 to the behavior with unsorted arrays.

   print*, " -------------------------- "
   print*, "Testing on an unsorted array"

  
  ! Call the fillUnsortedArray subroutine to fill arr2 with unsorted values.
  CALL fillSortedArray(arr2)

   x = arr2(N2/2-1) ! Value of interest: midle element -1.
   n = SIZE(arr2,1)

   idx = linearsearch(arr2,n,x)

   print*, "Index computed with linear search: ", idx
   print*, "was the value found?: ", arr2(idx)==x
   

   
   
   
   
   
   ! Measure the CPU time of this linearsearch function.
  CALL CPU_TIME(t_start) ! Start measuring time here
  idx = linearsearch(arr2, n, x)
  CALL CPU_TIME(t_end) ! End measuring time here
  linear_search_time = t_end - t_start
  print*, "CPU time for linear search: ", linear_search_time
  print*, "Index computed with linear search: ", idx
  print*, "was the value found?: ", arr2(idx) == x

  ! Measure the CPU time of this binarysearch function.
  CALL CPU_TIME(t_start) ! Start measuring time here
  idx = binarysearch(arr2, n, x)
  CALL CPU_TIME(t_end) ! End measuring time here
  binary_search_time = t_end - t_start
  print*, "CPU time for binary search: ", binary_search_time
  print*, "Index computed with binary search: ", idx
  print*, "was the value found?: ", arr2(idx) == x

  ! Calculate the performance difference
  time_difference = ABS(linear_search_time - binary_search_time)
  speedup_factor = MAX(linear_search_time, binary_search_time) / MIN(linear_search_time, binary_search_time)
  print*, "Time difference between linear and binary search: ", time_difference
  print*, "Speedup factor: ", speedup_factor, " times faster"
   
   
   
   
   
   
   
   
   

CONTAINS
  
  ! Fill an array with sorted values.
  SUBROUTINE fillSortedArray(array)
    
    IMPLICIT NONE

    REAL(8):: array(:)

    INTEGER :: i

    DO i=1,SIZE(array,1)
      array(i) = (i*3.d0)
    END DO

  END SUBROUTINE fillSortedArray

  ! Fill an array with unsorted values.
  SUBROUTINE fillUnsortedArray(array)
    
    IMPLICIT NONE

    REAL(8):: array(:)

    INTEGER :: i

    DO i=1,SIZE(array,1)
      array(i) = (-1.d0)**(i) * i*2.d0
    END DO

  END SUBROUTINE fillUnsortedArray


END PROGRAM main_program
