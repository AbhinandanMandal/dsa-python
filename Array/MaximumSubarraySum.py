
"""# Maximum subarray sum
# This is also known as kadane's algorithm
def MaximumSubarraySum(array):
    max_sum = array[0]
    current = array[0]
    for num in array:
        current = max(num, current+num)
        max_sum = max(max_sum, current)
    return max_sum


array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(MaximumSubarraySum(array))

# Time complexity: O(n)
# Space complexity: O(1)
"""

# Printing the maximum subarray


def MaximumSubarray(array):
    max_sum = float('-inf')
    maximum_subarray = []

    for i in range(len(array)):
        for j in range(len(array)):
            array_sum = sum(array[i:j+1])
            if array_sum > max_sum:
                max_sum = array_sum
                maximum_subarray = [array[i:j+1]]
            elif array_sum == max_sum:
                maximum_subarray.append(array[i:j+1])
    return maximum_subarray


array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(MaximumSubarray(array))

# Time complexity is O(n^3)
