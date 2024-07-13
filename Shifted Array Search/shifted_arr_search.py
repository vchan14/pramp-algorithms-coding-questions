def shifted_arr_search(A, n):
    lo = 0
    size = len(A)
    hi = size - 1
    s = smallestValue(A)
    while lo <= hi:
        mid = (lo + hi) // 2
        adjustMid = adjustIndex(mid, s, size)
        if A[adjustMid] == n:
            return adjustMid
        elif A[adjustMid] > n:
            hi = mid - 1
        else:
            lo = mid + 1

    return -1


def smallestValue(A):
    lo = 0
    hi = len(A) - 1

    while lo < hi:
        mid = (hi + lo) // 2
        if A[mid] < A[hi] and A[mid] < A[lo]:
            return mid
        elif A[hi] < A[lo]:
            lo = mid + 1
        else:
            hi = mid - 1

    return lo


def adjustIndex(x, s, size):
    return (x + s) % size
