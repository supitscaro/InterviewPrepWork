def bubbleSort(array):
    isSorted = False
    counter = 0

    while not isSorted:
        for idx in range(len(array) - 1 - counter):
            if array[idx] > array[idx + 1]:
                swap(idx, idx + 1, array)
                isSorted = False
        counter += 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
