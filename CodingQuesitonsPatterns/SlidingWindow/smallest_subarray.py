# Given an array of positive numbers and a positive number 'S', find the length of the smallest contigous subarray whose sum is greater than or equal to 'S'. Return 0 if no such subarray exists

# INPUTS/OUPUTS
# [2, 1, 5, 2, 3, 2], S = 7 => 2
# explanation:
#   the smallest subarray with a sum greater than or equal to '7' is [5, 2]

# [2, 1, 5, 2, 8], S = 7 => 1
# explanation:
#   the smallest subarray with a sum greater than or equal to '7' is [8]

# [3, 4, 1, 1, 6], S = 8 => 3
# explanation:
#   smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6]

# STEPS
#   add up elements from beginning of array until their sum becomes greater than or equal to S

#   these elements are our sliding window. we have to find the smallest window having a sum greater than or equal to S. the length of this window is the smallest window so far

#   we will add one element in the sliding window in a stepwise fashion

#   we will also try to shrink the window from the beginning. we will do this until the window's sum is smaller than S again. we need this to find the smallest window. the shrinking has to happen in multiple steps:
#       check if current window length is smallest so far, and if it is, remember its length
#       subtract first element of the window from the running sum to shrink the sliding window
import math


def smallest_subarray_with_given_sum(s, arr):
    min_length = float("inf")
    window_start, window_sum = 0, 0

    for window_end in range(0, len(arr)):
        window_sum += arr[window_end]

        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
    if min_length == float("inf"):
        return 0

    return min_length

# TIME COMPLEXITY
#   O(n)
#   the outer for loop runs for all elements, and inner while loop process each element only once

# SPACE COMPLEXITY
#   O(1)
