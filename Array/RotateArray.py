
"""
One of the easiest way to remember, 
left rotate: putting the first d elements to the back
right rotate: putting the last d elements to the front
"""


"""def LeftRotate(array: list, d: int):
    d = d % len(array)
    return array[d:]+array[:d]


def RightRotate(array: list, d: int):
    d = d % len(array)
    return array[-d:]+array[:-d]


arr = [1, 2, 3, 4, 5]
print(LeftRotate(arr, 3))
print(RightRotate(arr, 3))"""

# Left Rotate: putting first d element to the back of the array
# That means last n-d element came to first


def LeftRotate(array, d):
    d = d % len(array)
    return array[d:]+array[:d]


def RightRotate(array, d):
    d = d % len(array)
    return array[-d:]+array[:-d]


array = [1, 2, 3, 4, 5]
print(LeftRotate(array, 3))
print(RightRotate(array, 3))

# Time complexity: O(n)
# Space Complexity: O(n)
