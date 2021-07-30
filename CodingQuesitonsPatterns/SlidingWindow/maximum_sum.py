# Given an array of positive numbers and a positive number of 'k', find the maximum sum of any contiguous subarray of size K

# INPUTS/OUTPUTS
# [2, 1, 5, 1, 3, 2], k = 3 => 9

# explanation:
#   subarray with maximum sum is [5, 1, 3]

# [2, 3, 4, 1, 5], k = 2 => 7

# explanation:
#   subarray with maximum sum is [3, 4]

def max_sub_array_of_size_k(k, arr):
    window_start = 0
    window_sum, max_sum = 0, 0

    for idx in range(len(arr)):
        window_sum += arr[idx]

        if idx >= k - 1:
            max_sum = max(window_sum, max_sum)
            window_sum -= arr[window_start]
            window_start += 1

    return max_sum
