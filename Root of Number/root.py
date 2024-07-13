import math


def root(x, n):

    if x == 0:
        return 0

    left = 0
    right = max(1, x)
    mid = (right + left) / 2

    while mid - left >= 0.001:

        if math.pow(mid, n) > x:
            right = mid
        elif math.pow(mid, n) < x:
            left = mid
        else:
            break

        mid = (left + right) / 2

    return mid
