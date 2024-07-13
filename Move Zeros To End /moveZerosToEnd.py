def moveZerosToEnd(arr):

    if arr is None:
        return []
    zero_index = -1

    for i in range(len(arr)):

        if arr[i] == 0 and zero_index == -1:
            zero_index = i

        elif zero_index != -1 and arr[i] != 0:
            arr[i], arr[zero_index] = arr[zero_index], arr[i]
            zero_index += 1

    return arr
