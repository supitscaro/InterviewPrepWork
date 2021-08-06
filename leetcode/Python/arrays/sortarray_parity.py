# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers

# return any array that satisfies this condition

# IPUTS/OUPUTS
# nums = [3, 1, 2, 4] => [2, 4, 3, 1]

# nums = [0] => [0]

# NOTES
#   create two arrays to store odds and evens
#   create a pointer for the start and pointer for the end
#   loop through the array and check if the nums are odd or even and append them to their corresponding array

def sortArrayInPlace(nums):
    start_pointer, end_pointer = 0, len(nums) - 1

    while start_pointer <= end_pointer:
        if nums[start_pointer] % 2 == 0:
            # if the num is even, we can just skip it and move to the next num
            start_pointer += 1
        else:
            nums[start_pointer], nums[end_pointer] = nums[end_pointer], nums[start_pointer]
            # decrement end_pointer to avoid infinite loop
            end_pointer -= 1
    return nums


def sortArrayByParity(nums):
    odd = []
    even = []

    start_pointer = 0
    end_pointer = len(nums) - 1

    for idx in range(len(nums)):
        first_num = nums[start_pointer]
        last_num = nums[end_pointer]

        if first_num % 2 == 0:
            even.append(first_num)
            start_pointer += 1
        elif last_num % 2 == 0:
            even.append(last_num)
            end_pointer -= 1
        elif first_num % 2 != 0:
            odd.append(first_num)
            start_pointer += 1
        elif last_num % 2 != 0:
            odd.append(last_num)
            end_pointer -= 1

    return even + odd

# Time Complexity
# O(n)

# Space Complexity
# O(n^2) ?
#   created two new arrays, but they're only created once so is it still O(1)
