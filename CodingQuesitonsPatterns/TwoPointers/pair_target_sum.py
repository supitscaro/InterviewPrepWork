# Given an array of sorted numbers and a target sum, find a pari in the array whose sum is equal to the given target

# Write a function to return the indices of the two numbers such that they add up to the given target

# INPUTS/OUPUTS
# [1, 2, 3, 4, 6], target = 6 => [1, 3]
#   explanation:
#       the numbers at index 1 and 3 add up to 6

# [2, 5, 9, 11], target = 11 => [0, 2]
#   explanation:
#       the numbers at index 0 and 2 add up to 11

def pair_with_targetsum(arr, target_sum):
    start_pointer = 0
    end_pointer = len(arr) - 1

    while start_pointer < end_pointer:
        possible_match = arr[start_pointer] + arr[end_pointer]
        if possible_match < target_sum:
            start_pointer += 1
        elif possible_match > target_sum:
            end_pointer -= 1
        else:
            return [start_pointer, end_pointer]
