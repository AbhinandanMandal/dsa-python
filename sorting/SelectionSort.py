
""" 
Selection sort is `unstable`, `in-place` for sorting in computation.

Basic Idea: it chooses the smallest element first and put it in the first of an array.
            keep doing it, untill array become sorted.
"""


def SelectionSort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[min_index], array[i] = array[i], array[min_index]
    return array


array = [64, 25, 12, 22, 11]
print(SelectionSort(array))
# Time complexity: O(n^2), Space complexity: O(1)
