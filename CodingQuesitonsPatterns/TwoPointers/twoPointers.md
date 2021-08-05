# Pointers
- dealing with sorted arrays or linked lists and we need to find a set of elements that fulfill certain constraints
- the set of elements can be a pair, a triplet, or even a subarray

##### Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target

- since the array is sorted, we could start with one pointer in the beginning and another pointer in the end
- at every step, we see if the numbers pointed by the two pointers add up to the target sum.
- if they don't:
    - if the sum of the two pointers is greater than the target sum, we need a pair with smaller sum so we need to decrement the end pointer
    - if the sum of the two pointers is less than the target sum, we need a pair with a larger sum so we need to increment the start pointer
