# write a function that takes in a non empty araay of distinct integers
# and an integer representing a target sum. If any two numbers in the
# input array sum up to the target sum, the function should return them
# in an array, in any order. If no two numbers sum up to the target sum,
# the function should return an empty array

def twoNumberSum(arr, targetSum):
    # [1, 2, 3, 4] = 5
    arr.sort()
    left_pointer = 0
    right_pointer = len(arr) - 1
    while left_pointer < right_pointer:
        current_sum = arr[left_pointer] + arr[right_pointer]
        if current_sum == targetSum:
            return [arr[left_pointer], arr[right_pointer]]
        elif current_sum < targetSum:
            left_pointer += 1
        elif current_sum > targetSum:
            right_pointer -= 1
    return []
