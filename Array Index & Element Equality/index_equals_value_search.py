def index_equals_value_search(arr):
    size = len(arr)
    result = -1
    result = helper(0, size - 1, arr)
    return result


def helper(lower, upper, arr):
    mid = (upper + lower) // 2
    val = arr[mid]

    if lower > upper:
        return -1
    if val > mid:
        return helper(lower, mid - 1, arr)

    elif val < mid:
        return helper(mid + 1, upper, arr)

    else:
        return val
