MODULE searchutils
  USE omp_lib  ! Include OpenMP library functions
  IMPLICIT NONE
CONTAINS

  FUNCTION linearSearch(arr, n, x) RESULT(idx)
    REAL(8), INTENT(IN) :: arr(n)
    INTEGER, INTENT(IN) :: n
    REAL(8), INTENT(IN) :: x
    INTEGER :: idx
    INTEGER :: i   ! Declaration of the loop variable
    LOGICAL :: found

    idx = -1
    found = .FALSE.
    !$omp parallel do private(i) shared(arr, n, x, idx, found)
    DO i = 1, n
      IF (arr(i) == x .AND. .NOT. found) THEN
        !$omp critical
        IF (.NOT. found) THEN
          idx = i
          found = .TRUE.
        END IF
        !$omp end critical
      END IF
    END DO
    !$omp end parallel do
  END FUNCTION linearSearch

  ! Rest of the module remains unchanged.
END MODULE searchutils
