# given two non-empty arrays of integers, write a function that
# determines whether the second array is a subsequence of the first one

# a subsequence of an array is a set of numbers that aren't necessarily
# adjacent in the array but that are in the same order as they appear
# in the array.

def is_valid_subsequence(array, sequence):
    seq_idx = 0
    for val in array:
        if seq_idx == len(sequence):
            break
        if sequence[seq_idx] == val:
            seq_idx += 1
    return seq_idx == len(sequence)
