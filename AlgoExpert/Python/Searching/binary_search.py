# write a function that takes in a sorted array of integers as well as a target integer
# the function should use the binary search algorithm to determine if the target integer is contained in the array
# and should return its index if it is, otherwise -1

# INPUTS/OUTPUTS
#   array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], target = 33 => 3

# NOTES/PSEUDOCODE
#   we can do binary search by splitting the array in half
#   we can create pointers to help us figure out the middle point
#   we're gonna want to solve this recursively, so we can create a helper function
#   we can do a loop while left <= right
#       create a variable for our possible match and use the middle variable to get the num in that index
#       if possible match == target
#           return middle
#       elif possible_match > target
#           left = middle - 1
#       elif possible_match < target
#           right = middle + 1

def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)


def binarySearchHelper(array, target, left, right):
    while left <= right:
        middle = (left + right) // 2
        possible_match = array[middle]

        if possible_match == target:
            return middle
        elif possible_match > target:
            left = middle - 1
        elif possible_match < target:
            right = middle + 1
