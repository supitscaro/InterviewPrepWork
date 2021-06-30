# write a function that takes in a non-empty array of integers and returns an array of the same length, where each element in the output array is equal to the product of every other number in the input array.

def array_of_products(array):
    products = [1 for x in range(len(array))]

    left_product = 1
    for i in range(len(array)):
        products[i] = left_product
        left_product *= array[i]

    right_product = 1
    for i in range(len(array)):
        products[i] *= right_product
        right_product *= array[i]

    return products
