
def maximumsubarray(array: list):
    current = array[0]
    maximum = array[0]

    for num in array[1:]:
        current = max(num, current+num)
        maximum = max(maximum, current)
    return maximum


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maximumsubarray(arr))

# Time complexity: O(n)
# Space complexity: O(1)
