
""" 
We need to find maximum subarray that returns the maximum subarray sum
For the following array [-2, 1, -3, 4, -1, 2, 1, -5, 4], 
It's [4, -1, 2, 1] returns maximum sum of 6

"""


def MaximumSubarray(array):
    maximum_sum = float('-inf')
    maximum_subarray = []

    for i in range(len(array)):
        for j in range(len(array)):
            array_sum = sum(array[i:j+1])
            if array_sum > maximum_sum:
                maximum_sum = array_sum
                maximum_subarray = array[i:j+1]
            elif array_sum == maximum_sum:  # Checking if two are equal then
                maximum_subarray.append(array[i:j+1])
    return maximum_subarray


array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(MaximumSubarray(array))
