# write a function that takes in a "special" array and returns its product sum

# a "special" array is a non-empty array that contains either integers or other "special" arrays
# the product sum of a "special" array is the sum of its elements, where "special" arrays inside it are summed
# themselves and then multiplied by their level of depth

# the depth of a "special" array is how far nested it is. For instance, the depth of [] is 1; the depth of the inner array
# in [[]] is 2; the depth of the innermost array in [[[]]] is 3

# therefore, the product sum of [x, y] is x + y; the product sum of [x, [y, z]] is x + 2 * (y + z); the product sum of
# [x, [y, [z]]] is x + 2 * (y + 3z)

# NOTES
#    we have to check somehow if the current element we're on is an integer or an array
#    if the element is a "special" array, then the product is the sum of all its elements
#       if the special arrays have special arrays inside of them, they are summed and
#       then multiplied by their level of depth
#       keep in mind: the outer array is the first level, anything inside that is +1 level
#    since we have nested arrays, we could solve this recursively

def productSum(array, multiplier=1):
    sum = 0
    for element in array:
        if type(element) is list:
            sum += productSum(element, multiplier + 1)
        else:
            sum += element
    return sum * multiplier
