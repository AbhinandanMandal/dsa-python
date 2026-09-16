
""" 
In the following we need to return maximum sum of array
For the following array [-2, 1, -3, 4, -1, 2, 1, -5, 4], 
It's [4, -1, 2, 1] returns maximum sum of 6
"""


def MaximumSubarraySum(array):
    current = array[0]
    maximum = array[0]

    for num in array[1:]:
        current = max(num, current+num)
        maximum = max(maximum, current)
    return maximum


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(MaximumSubarraySum(arr))

# Time complexity: O(n)
# Space complexity: O(1)
