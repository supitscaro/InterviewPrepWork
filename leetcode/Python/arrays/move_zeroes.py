# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements
# note that you must do this in-place without making a copy of the array

# INPUTS/OUTPUTS
#   nums = [0, 1, 0, 3, 12] => [1, 3, 12, 0, 0]

#   nums = [0] => [0]


def moveZeroes(nums):
    current_pointer = 0
    compare_pointer = 0

    while compare_pointer < len(nums):
        if nums[compare_pointer] != 0:
            nums[compare_pointer], nums[current_pointer] = nums[current_pointer], nums[compare_pointer]
            current_pointer += 1
        compare_pointer += 1
