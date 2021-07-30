## Introduction

- In many problems with arrays, we need to find or calculate something among all the contiguous subarrays of a given size

```python
# find the average of all contiguous subarrays of size '5' in the given array
lst = [1, 3, 2, 6, -1, 4, 1, 8, 2], K = 5 => [2.2, 2.8, 2.4, 3.6, 2.8]
```
### Inefficient way of solving it
- If we calculate the sum of every 5 elements contiguous subarray and divide the sum by 5 to find the average, there will be an overlapping part of 4 elements for any two consecutive subarrays

### Efficient way of solving it
- We can visualize each contiguous subarray as a sliding window of 5 elements. We slide the window by one element when we move to the next subarray.
- We can reuse the sum from the previous subarray and subtract the element going out the window and add the element now being included in the sliding window

```python
def find_averages_of_subarray(K, arr):
    result = []
    window_sum, window_start = 0.0, 0
    for window_end_idx in range(len(arr)):
        window_sum += arr[window_end_idx]

        if window_end >= K - 1:
            result.append(window_sum / K)
            window_sum -= arr[window_start]
            window_start += 1

    return result

```
