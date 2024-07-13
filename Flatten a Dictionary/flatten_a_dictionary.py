def newKey(str1, str2):
    if len(str1) == 0:
        return str2

    if len(str2) == 0:
        return str1

    return str1 + "." + str2


def helper(initial_key, obj, output):
    if type(obj) is dict:
        for key, value in obj.items():
            helper(newKey(initial_key, key), value, output)
    else:
        output[initial_key] = obj


def flatten_dicionary(dictionary):
    output = {}
    helper("", dictionary, output)

    return output


if __name__ == "__main__":
    main()
