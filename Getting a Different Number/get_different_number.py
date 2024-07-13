def get_different_number(arr):
    mySet = set(arr)
    for i in range(len(arr)):
        if not (i in mySet):
            return i

    return i + 1


arr = [0, 2, 3, 4, 6, 5]
print(get_different_number(arr))
