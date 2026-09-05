
"""
import math
array = [1, 2, 3, 4]
new = math.prod(array[:])
print(new)
"""


"""
import math

# if array contains any 0 then this solution fails totally
def ProductArray(array):
    new_arr=[]
    for i in range(len(array)):
        new_arr.append(math.prod(array[:])//array[i])
    return new_arr

array = [1, 2, 3, 4]
print(ProductArray(array))
"""


def ProductArray(array):
    result = [1]*len(array)
    prefix = 1
    for i in range(len(array)):
        result[i] = prefix
        prefix *= array[i]

    suffix = 1
    for i in range(len(array)-1, -1, -1):
        result[i] *= suffix
        suffix *= array[i]
    return result


array = [1, 2, 3, 4]
print(ProductArray(array))

# Time complexity: O(n)
# Space complexity: O(1)
