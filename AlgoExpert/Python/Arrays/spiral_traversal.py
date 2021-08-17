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
    pass
