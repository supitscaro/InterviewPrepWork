# write a function that takes in two non-empty arrays of integers, finds the pair of numbers (one from each array)
# whose absolute difference is closest to zero,
# and returns an array containing these two numbers, with the number from the first array in the first position

# INPUTS/OUPUTS
#   arrayOne = [-1, 5, 10, 20, 28, 3], arrayTwo = [26, 134, 135, 15, 17] => [28, 26]

# NOTES
#

def smallest_difference(array_one, array_two):
    array_one.sort()
    array_two.sort()

    idx_one = 0
    idx_two = 0

    smallest = float("inf")
    current = float("inf")

    smallest_pair = []

    while idx_one < len(array_one) and idx_two < len(array_two):
        first_num = array_one[idx_one]
        second_num = array_two[idx_two]

        if first_num < second_num:
            current = second_num - first_num
            idx_one += 1
        elif second_num < first_num:
            current = first_num - second_num
            idx_two += 1
        else:
            return [first_num, second_num]

        if smallest > current:
            smallest = current
            smallest_pair = [first_num, second_num]
    return smallest_pair
