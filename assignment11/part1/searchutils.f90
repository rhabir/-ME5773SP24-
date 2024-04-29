MODULE searchutils
  IMPLICIT NONE
CONTAINS

  FUNCTION linearsearch(arr, n, x) RESULT(idx)
    REAL(8), INTENT(IN) :: arr(n)
    INTEGER, INTENT(IN) :: n
    REAL(8), INTENT(IN) :: x
    INTEGER :: idx
    INTEGER :: i   ! Declaration of the loop variable

    idx = -1
    DO i = 1, n
      IF (arr(i) == x) THEN
        idx = i
        EXIT
      END IF
    END DO
  END FUNCTION linearsearch

  FUNCTION binarysearch(arr, n, x) RESULT(idx)
    REAL(8), INTENT(IN) :: arr(n)
    INTEGER, INTENT(IN) :: n
    REAL(8), INTENT(IN) :: x
    INTEGER :: idx
    INTEGER :: low, high, mid

    low = 1
    high = n
    idx = -1

    DO WHILE (low <= high)
      mid = (low + high) / 2
      IF (arr(mid) == x) THEN
        idx = mid
        EXIT
      ELSEIF (x < arr(mid)) THEN
        high = mid - 1
      ELSE
        low = mid + 1
      END IF
    END DO
  END FUNCTION binarysearch

END MODULE searchutils
