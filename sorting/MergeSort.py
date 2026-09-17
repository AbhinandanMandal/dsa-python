
""" 
Merge sort is stable, not in-place algorithm
"""


def MergeSubarray(array, low, high, mid):
    array1 = array[low:mid+1]
    array2 = array[mid+1:high+1]
    m = len(array1)
    n = len(array2)
    i = 0
    j = 0
    k = low
    while (i < m and j < n):
        if array1[i] < array2[j]:
            array[k] = array1[i]
            i += 1
            k += 1
        else:
            array[k] = array2[j]
            j += 1
            k += 1
    while (i < m):
        array[k] = array1[i]
        i += 1
        k += 1
    while (j < n):
        array[k] = array2[j]
        j += 1
        k += 1
    return array


def MergeSort(array, low, high):
    if high > low:
        mid = (low+high)//2
        MergeSort(array, low, mid)
        MergeSort(array, mid+1, high)
        MergeSubarray(array, low, high, mid)
    return array


array = [10, 5, 30, 15, 7]
print(MergeSort(array, 0, 4))
# Time complexity: O(nlogn)
# Space complexity: o(n)
