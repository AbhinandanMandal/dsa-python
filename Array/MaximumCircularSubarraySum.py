
""" 
Approach for this is, 
maximum_normal = kadane's algorithm
maximum_circular = total - minimum_sum
return max(maximum_normal, maximum_circular)

"""


def MaximumCircularSubarraySum(array):
    maximum_sum = array[0]
    minimum_sum = array[0]
    current_max = array[0]
    current_min = array[0]

    for num in array:
        current_max = max(num, current_max+num)
        current_min = min(num, current_min+num)
        # Maximum normal (kadane's algorithm)
        maximum_sum = max(maximum_sum, current_max)
        minimum_sum = min(minimum_sum, current_min)

    total_sum = sum(array)
    maximum_circular = total_sum-minimum_sum
    return max(maximum_sum, maximum_circular)


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(MaximumCircularSubarraySum(arr))
# Time complexity: O(n)
# Space complexity: O(1)
