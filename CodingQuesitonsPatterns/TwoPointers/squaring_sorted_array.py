# Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order

# INPUTS/OUPUTS
# [-2, -1, 0, 2, 3] => [0, 1, 4, 4, 9]

# [-3, -1, 0, 1, 2] => [0, 1, 1, 4, 9]

# THOUGHTS
#   if i iterate through the array and just square each of the elements, will they be placed in order in the new array?
# how should i handle the negative numbers?
# i could have a pointer in the start and end of the array, square the two numbers and then compare them
#   if the num[start] is > than the num[end], then that should be the biggest number in the entire array (?)
#

def make_squares(array):
    # squares = []

    # pointer_start = 0
    # pointer_end = len(arr) - 1

    # for idx in reversed(range(len(arr))):
    #     small_value = arr[pointer_start]
    #     large_value = arr[pointer_end]

    #     if abs(small_value) > abs(large_value):
    #         squares.append(small_value * small_value)
    #         pointer_start += 1
    #         # print('squares', squares)
    #     else:
    #         squares.append(large_value * large_value)
    #         print('squares', squares)
    #         pointer_end -= 1

    # print(squares)
    # return squares

    squares = [0 for _ in array]
    pointer_start = 0
    pointer_end = len(array) - 1

    for idx in reversed(range(len(array))):
        small_val = array[pointer_start]
        large_val = array[pointer_end]

        if abs(small_val) > abs(large_val):
            squares[idx] = (small_val * small_val)
            pointer_start += 1
        else:
            squares[idx] = (large_val * large_val)
            print('index', idx)
            print('squares', squares)
            pointer_end -= 1
    print(squares)
    return squares


make_squares([-2, -1, 0, 2, 3])
