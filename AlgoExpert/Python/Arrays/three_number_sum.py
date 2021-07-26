# write a function that takes in a non-empty array of distinct integers and an integer representing a target sum
# the function should find all triplets in the array that sum up to the target sum and return a two-dimensional array
# of all these triplets
# the numbers in each triplet should be ordered in ascending order, and the triplets themselves should be ordered in
# ascending order with respect to the numbers they hold.

# INPUTS/OUTPUTS
#   array = [12, 3, 1, 2, -6, 5, -8, 6], targetSum = 0 => [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

# NOTES
#   we can create pointers for left and right, starting at beginning and end
#   do a while left < right loop OR a normal for loop
#       while loop might not work because it will remove numbers as we loop through that we need to consider
#   using the pointers, find the sum of the three numbers and check if it matches the target sum
#       ex: for num in range(len(array) - 2):
#               left =  num + 1
#               right = len(array) - 1
#               while left < right:
#                   possibleMatch = array[num] + array[left] + array[right]
#                   if possibleMatch == targetSum:
#                       res.append([array[num], array[left], array[right]])
#   then we can increment our left variable and decrement our right variable
#   if we dont have a match, then we just loop through again, BUT we need to see which pointer has to be changed
#   if our possibleMatch is less than our targetSum, we should increment our left pointer
#   if our possibleMatch is greater than our targetSum, we should decrement our right pointer

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
