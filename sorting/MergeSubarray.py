
""" 
Merge subarray can be done by bifurcating array into two, then apply merge two sorted array concept
Always will be using 0 based indexing
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


array = [5, 8, 11, 14, 7]
print(MergeSubarray(array, 0, 4, 2))
# Time complexity: O(m+n)
# Space complexity: O(m+n)
