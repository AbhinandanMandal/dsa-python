
"""
# Solution with O(n^2) time complexity

def MissingNumber(array: list):
    for i in range(len(array)+1):
        if i not in array:
            return i
    return -1


arr = [3, 0, 1]
print(MissingNumber(arr))"""

# Similary can be done with O(n) approach


def MissingNumber(array: list):
    n = len(array)
    expected = n*(n+1)//2
    actual = sum(array)
    return expected - actual


arr = [3, 0, 1]
print(MissingNumber(arr))
