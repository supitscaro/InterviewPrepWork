# Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket
# The only restriction is that each basket can have only one type of fruit

# Write a function to return the maxium number of fruits in both baskets

# INPUTS/OUTPUTS
#   ['A', 'B', 'C', 'A', 'C] => 3
#   explanation:
#       we can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

#   ['A', 'B', 'C', 'B', 'B', 'C'] => 5
#   explanation:
#       we can put 3 'B' in one basket and 2 'C' in the other basket. this can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

def fruits_into_baskets(fruits):
    fruits_frequency = {}
    max_length = 0
    window_start = 0

    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]
        if right_fruit not in fruits_frequency:
            fruits_frequency[right_fruit] = 0
        fruits_frequency[right_fruit] += 1

        while len(fruits_frequency) > 2:
            left_fruit = fruits[window_start]
            fruits_frequency[left_fruit] -= 1

            if fruits_frequency[left_fruit] == 0:
                del fruits_frequency[left_fruit]

            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length

