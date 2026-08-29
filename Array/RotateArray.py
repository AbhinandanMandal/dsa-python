
"""
One of the easiest way to remember, 
left rotate: putting the first d elements to the back
right rotate: putting the last d elements to the front
"""


def LeftRotate(array: list, d: int):
    d = d % len(array)
    return array[d:]+array[:d]


def RightRotate(array: list, d: int):
    d = d % len(array)
    return array[-d:]+array[:-d]


arr = [1, 2, 3, 4, 5]
print(LeftRotate(arr, 3))
print(RightRotate(arr, 3))

