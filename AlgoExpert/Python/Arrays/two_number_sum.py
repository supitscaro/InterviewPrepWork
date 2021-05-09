# write a function that takes in a non empty araay of distinct integers
# and an integer representing a target sum. If any two numbers in the
# input array sum up to the target sum, the function should return them
# in an array, in any order. If no two numbers sum up to the target sum,
# the function should return an empty array

def two_number_sum(arr, target_sum):
    # [1, 2, 3, 4] = 5
    arr.sort()
    left_pointer = 0
    right_pointer = len(arr) - 1
    while left_pointer < right_pointer:
        current_sum = arr[left_pointer] + arr[right_pointer]
        if current_sum == target_sum:
            return [arr[left_pointer], arr[right_pointer]]
        elif current_sum < target_sum:
            left_pointer += 1
        elif current_sum > target_sum:
            right_pointer -= 1
    return []
