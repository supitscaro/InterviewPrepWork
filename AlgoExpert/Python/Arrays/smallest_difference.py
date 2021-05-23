# write a function that takes in two non-empty arrays of integers, finds the pair of numbers (one from each array) whose absolute difference is closest to zero,
# and returns an array containing these two numbers, with the number from the first array in the first position


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
