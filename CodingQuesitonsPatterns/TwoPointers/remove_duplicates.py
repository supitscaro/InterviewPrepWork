# Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in place return the length of the subarray that has no duplicate in it

# INPUTS/OUPUTS
# [2, 3, 3, 3, 6, 9, 9] => 4
#   explanation:
#       the first four elements after removing the duplicates will be [2, 3, 6, 9]

# [2, 2, 2, 11] => 2
#   explanation:
#       the first two elements after removing the duplicates will be [2, 11]

# SOLUTION EXPLANATION

# since the input array is sorted, one way to remove duplicates in place is to shift the elements left whenever we encounter duplicates

# we will keep one pointer for iterating the array and one pointer for placing the next non duplicate number

def remove_duplicates(arr):
    # pointer we use to place the next non duplicate number
    next_non_duplicate_idx = 1

    # pointer we use to iterate
    i = 1
    while (i < len(arr)):
        if arr[next_non_duplicate_idx - 1] != arr[i]:
            arr[next_non_duplicate_idx] = arr[i]
            next_non_duplicate_idx += 1
        i += 1

    return next_non_duplicate_idx
