

def MergeSortedArray(array1: list, array2: list):
    i, j = 0, 0
    m, n = len(array1), len(array2)
    result = []
    while (i < m and j < n):
        if (array1[i] < array2[j]):
            result.append(array1[i])
            i += 1
        else:
            result.append(array2[j])
            j += 1
    while (i < m):
        result.append(array1[i])
        i += 1
    while (j < n):
        result.append(array2[j])
        j += 1
    return result


arr1 = [10, 15]
arr2 = [5, 6, 6, 30, 40]
print(MergeSortedArray(arr1, arr2))

# Time complexity: O(m+n)
# Space complexity: O(m+n)
