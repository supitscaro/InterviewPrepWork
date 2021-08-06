# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers

# return any array that satisfies this condition

# IPUTS/OUPUTS
# nums = [3, 1, 2, 4] => [2, 4, 3, 1]

# nums = [0] => [0]

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

        if first_num % 2 != 0:
            odd.append(first_num)
            start_pointer += 1
        elif last_num % 2 != 0:
            odd.append(last_num)
            end_pointer -= 1

    return even + odd
