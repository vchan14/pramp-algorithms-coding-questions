def decrypt(word):

    if word == None or len(word) == 0:
        return ""
    table = []
    for i in range(len(word)):
        if i == 0:
            table.append(ord(word[i]) - 1)
        else:
            temp = ord(word[i]) - ord(word[i - 1])
            while not (temp >= ord("a")):
                temp += 26

            table.append(temp)

    for i in range(len(table)):
        table[i] = chr(table[i])

    return "".join(table)
