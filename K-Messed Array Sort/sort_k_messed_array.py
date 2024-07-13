def sort_k_messed_array(arr, k):
    output = [0] * len(arr)

    mySet = set()

    for i in range(len(arr)):
        start = i - k
        end = i + k + 1
        current_min = float("inf")
        current_index = -1
        for j in range(start, end):
            if ((j % len(arr)) not in mySet) and (current_min > arr[j % len(arr)]):
                current_min = arr[j % len(arr)]
                current_index = j % len(arr)

        output[i] = current_min
        mySet.add(current_index)

    return output
