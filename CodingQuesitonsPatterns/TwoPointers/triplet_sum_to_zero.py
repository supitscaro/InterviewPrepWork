# Given an array of unsorted numbers, find all unique triplets in it that add up to zero

# INPUTS/OUTPUTS
# [-3, 0, 1, 2, -1, 1, -2] => [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
# explanation:
#   There are four unique triplets whose sum is equal to zero

# [-5, 2, -1, -2, 3] => [[-5, 2, 3], [-2, -1, 3]]
# explanation:
#   There are two unique triplets whose sum is equal to zero

# THOUGHTS
# I can create two pointers for the start and end
# loop through the array like normal
# use the pointers as indeces and add the 3 numbers (start, end, and current index)


def search_triplets(arr):
    triplets = []

    for idx in range(len(arr) - 2):
        start_pointer = idx + 1
        end_pointer = len(arr) - 1
        while start_pointer < end_pointer:
            possible_match = arr[idx] + arr[start_pointer] + arr[end_pointer]
            if possible_match == 0:
                triplets.append(
                    [arr[idx], arr[start_pointer], arr[end_pointer]])
                start_pointer += 1
                end_pointer -= 1
            elif possible_match < 0:
                start_pointer += 1
            elif possible_match > 0:
                end_pointer -= 1
    return triplets


search_triplets([-5, 2, -1, -2, 3])
