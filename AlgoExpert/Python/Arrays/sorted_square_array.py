# write a function that takes in a non-empty array of integers that
# are sorted in ascending order and returns a new array of the
# same length with the squares of the original integers also sorted
# in ascending order

# INPUTS/OUTPUTS
# [1, 2, 3, 5, 6, 8, 9] => [1, 4, 9, 25, 36, 64, 81]

# NOTES
# we could just iterate through the array, square each element,
# and then .sort() it.
# this might not be the most optimal solution

# we can use pointers
# iterate through the array
# create pointer for start and end
# check which of the two is bigger
# append that number to the array

def sortedSquareArray(array):
    sorted = []
    small_pointer = 0
    large_pointer = len(array) - 1

    for idx in reversed(range(len(array))):
        small_num = array[small_pointer]
        large_num = array[large_pointer]

        if abs(small_num) > abs(large_num):
            sorted.append(small_num * small_num)
            small_pointer += 1
        else:
            sorted.append(large_num * large_num)
            large_pointer -= 1
    return sorted
