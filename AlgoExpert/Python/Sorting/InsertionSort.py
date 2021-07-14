# INPUTS/OUTPUTS
#   array = [8, 5, 2, 9, 5, 6, 3] => [2, 3, 5, 5, 6, 8, 9]

# NOTES
#

def insertionSort(array):
    for i in range(1, len(array)):
        j = 1
        while j > 0 and array[j] < array[j - 1]:
            swap(j, j - 1, array)
            j -= 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[i], array[j]
