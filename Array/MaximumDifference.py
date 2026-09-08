
"""
For example,
array=[2,1,5,3]
maximum difference = 4 (|5-1|)

array=[-10, 4, -9, -5]
maximum difference = 14 (|-10-4|)

"""

"""
def MaximumDifference(array):
    maximum_difference = 0
    prev = array[0]
    for n in range(1, len(array)):
        diff = abs(prev-array[n])
        prev = array[n]
        maximum_difference = max(diff, maximum_difference)
    return maximum_difference


array = [2, 1, 5, 3]
print(MaximumDifference(array))

# Time complexity: O(n), Space complexity: O(1)"""

# Another optimal solution


def MaximumDifference(array):
    maximum = array[0]
    minimum = array[0]
    for n in array:
        maximum = max(maximum, n)
        minimum = min(minimum, n)
    return abs(maximum-minimum)


array = [2, 1, 5, 3]
print(MaximumDifference(array))
