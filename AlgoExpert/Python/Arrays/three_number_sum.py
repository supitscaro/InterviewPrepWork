# write a function that takes in a non-empty array of distinct integers and an integer representing a target sum
# the function should find all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplets
# the numbers in each triplet should be ordered in ascending order, and the triplets themselves should be ordered in ascending order with respect to the numbers they hold.

def three_number_sum(array, target_sum):
    array.sort()

    triplets = []

    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            current_sum = array[i] + array[left] + array[right]
            if current_sum == target_sum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif current_sum < target_sum:
                left += 1
            elif current_sum > target_sum:
                right -= 1
    return triplets
