def spiral_copy(inputMatrix):
    if (inputMatrix == None) or len(inputMatrix) < 1:
        return []

    row_i = 0
    row_f = len(inputMatrix)

    col_i = 0
    col_f = len(inputMatrix[0])

    output = []

    while True:
        # go right
        for i in range(col_i, col_f):
            output.append(inputMatrix[row_i][i])
        row_i += 1
        if row_i >= row_f:
            break
        # go down
        for i in range(row_i, row_f):
            output.append(inputMatrix[i][col_f - 1])
        col_f -= 1

        if col_i >= col_f:
            break
        # go left
        for i in range(col_f - 1, col_i - 1, -1):
            output.append(inputMatrix[row_f - 1][i])
        row_f -= 1

        if row_i >= row_f:
            break
        # go up
        for i in range(row_f - 1, row_i - 1, -1):
            output.append(inputMatrix[i][col_i])
        col_i += 1

        if col_i > col_f:
            break
    return output
