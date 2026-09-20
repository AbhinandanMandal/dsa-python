
def LomutoPartition(array, p):
    pivot = array[p]
    n = len(array)
    array[p], array[n-1] = array[n-1], array[p]
    i = -1
    for j in range(n-1):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[n-1] = array[n-1], array[i+1]
    return array


arr = [5, 13, 6, 9, 12, 8, 11]
print(LomutoPartition(arr, 3))
# Time complexity: O(n), Space complexity: O(1)
