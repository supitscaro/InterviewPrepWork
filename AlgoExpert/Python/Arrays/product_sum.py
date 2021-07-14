# write a function that takes in a "special" array and returns its product sum

# a "special" array is a non-empty array that contains either integers or other "special" arrays
# the product sum of a "special" array is the sum of its elements, where "special" arrays inside it are summed
# themselves and then multiplied by their level of depth

# the depth of a "special" array is how far nested it is. For instance, the depth of [] is 1; the depth of the inner array
# in [[]] is 2; the depth of the innermost array in [[[]]] is 3

# therefore, the product sum of [x, y] is x + y; the product sum of [x, [y, z]] is x + 2 * (y + z); the product sum of
# [x, [y, [z]]] is x + 2 * (y + 3z)
