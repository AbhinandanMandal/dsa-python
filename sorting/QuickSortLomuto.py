
# We'll be applying same concept that of lomuto algorithm with zero based indexing
def LomutoPartition(array, low, high):
    pivot = array[high]  # n-1
    i = low-1  # -1
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return i+1


def QuickSort(array, low, high):
    if high > low:
        p = LomutoPartition(array, low, high)
        QuickSort(array, low, p-1)
        QuickSort(array, p+1, high)
    return array


array = [5, 13, 6, 9, 12, 8, 11]
print(QuickSort(array, 0, 6))
# best & avergae cases
# time complexity: O(nlogn)
# space complexity: O(logn) # quick sort is recursive
# wrost case
# time complexity: O(n^2)
# space complexity: O(n)
