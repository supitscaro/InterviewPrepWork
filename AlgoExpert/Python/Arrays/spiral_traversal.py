# write a function that takes in an n x m 2d array (that can be square-shaped when n == m) and returns a one-dimensional array of all the array's elements in spiral order

"""
    array = [
        [1,    2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10,  9,  8, 7],
    ]
"""

# NOTES
#	we need to find the length of each subarray and get the very last index
#		when we loop through row 1, we need to stop at 4
#		then we move to row 2 and START at row2[end_of_array]
#		then move again to row 3 and START at row3[end_of_array]
#		then do the same for row 4
#		once at row 4, we loop backwards in a decrementing order
#	because we need to check where we're starting and ending at each row and column
#		we should keep "pointers" for the row's start/end, and col's start/end


def spiralTraverse(array):
    res = []

    row_start, row_end = 0, len(array) - 1
    col_start, col_end = 0, len(array[0]) - 1

    while row_start <= row_end and col_start <= col_end:
        # [1, 2, 3, 4]
        for col in range(col_start, col_end + 1):
            res.append(array[row_start][col])

        # [5, 6, 7]
        for row in range(row_start + 1, row_end + 1):
            res.append(array[row][col_end])

        # [10, 9, 8]
        for col in reversed(range(col_start, col_end)):
            if row_start == row_end:
                break
            res.append(array[row_end][col])

        for row in reversed(range(row_start + 1, row_end)):
            if col_start == col_end:
                break
            res.append(array[row][col_start])

        row_start += 1
        row_end -= 1
        col_start += 1
        col_end -= 1

    return res
