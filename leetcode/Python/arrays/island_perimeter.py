def islandPerimeter(grid):
    """
        grid = [
                    [0,1,0,0],
                    [1,1,1,0],
                    [0,1,0,0],
                    [1,1,0,0]
                ]
    """
    perimeter = 0

    if (len(grid) == 0):
        return 0

    for row_idx in range(len(grid)):
        for col_idx in range(len(grid[0])):

            if grid[row_idx][col_idx] == 1:
                perimeter += 4

                # check if there's a 1 in the previous row or previous column to then subtract 2

                # row_idx = 1      grid at the second row at first index
                if row_idx > 0 and grid[row_idx - 1][col_idx] == 1:
                    perimeter -= 2

                # assuming col_idx is 2 and row_idx is still 1
                # row_idx = 1      gird at second row, col index 2
                if row_idx > 0 and grid[row_idx][col_idx - 1] == 1:
                    perimeter -= 2

    # print(perimeter)
    return perimeter


islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]])
