"""
# Brute force approach
# Time complexity: O(n^2)

def twosum(array: list, target: int):
    index = []
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i]+array[j] == target:
                return [i, j]
    return []


print(twosum([2, 7, 11, 15], 9))

"""

"""
def twosum(array: list, target: int):
    for x in array:
        if target-x in array:
            return [array.index(x), array.index(target-x)]
    return []


print(twosum([2, 7, 11, 15], 9))

# Time complexity and space complexity: O(n^2)
"""


def twosum(array: list, target: int):
    seen = {}  # creating a set for this

    for i, num in enumerate(array):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


print(twosum([2, 7, 11, 15], 9))

# Time complexity: O(n)
# Space complexity: O(n)
