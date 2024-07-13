def dfs(i, j, grid, column, row, tr, tc, distance, output):
    # go right
    if (i < row) and ((j + 1) < column) and (grid[i][j + 1] == 1):
        if (i == tr) and ((j + 1) == tc):
            output.append(distance + 1)
        else:
            grid[i][j + 1] = 0
            dfs(i, j + 1, grid, column, row, tr, tc, distance + 1, output)
            grid[i][j + 1] = 1

    # go down
    if (i + 1) < row and (j) < column and grid[i + 1][j] == 1:
        grid[i + 1][j] = 0
        if (i + 1) == tr and (j) == tc:
            output.append(distance + 1)
        else:
            grid[i + 1][j] = 0
            dfs(i + 1, j, grid, column, row, tr, tc, distance + 1, output)
            grid[i + 1][j] = 1

    # go left
    if i < row and (j - 1) >= 0 and grid[i][j - 1] == 1:
        if i == tr and (j - 1) == tc:
            output.append(distance + 1)
        else:
            grid[i][j - 1] = 0
            dfs(i, j - 1, grid, column, row, tr, tc, distance + 1, output)
            grid[i][j - 1] = 1

    # go up
    if (i - 1) >= 0 and (j) < column and grid[i - 1][j] == 1:
        if (i - 1) == tr and j == tc:
            output.append(distance + 1)
        else:
            grid[i - 1][j] = 0
            dfs(i - 1, j, grid, column, row, tr, tc, distance + 1, output)
            grid[i - 1][j] = 1


def shortestCellPath(grid, sr, sc, tr, tc):

    column = len(grid[0])
    row = len(grid)
    distance = 0
    output = []
    grid[sr][sc] = 0
    dfs(sr, sc, grid, column, row, tr, tc, distance, output)
    print(output)
    if len(output) == 0:
        return -1
    else:
        return min(output)
