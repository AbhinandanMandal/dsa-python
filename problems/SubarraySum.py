

"""def SubarraySum(array, target):
    total = 0
    for i in range(len(array)):
        for j in range(i, len(array)):
            if sum(array[i:j+1]) == target:
                total += 1
    return total


print(SubarraySum([1, 1, 1], 2))
# But this approach is much expensive, taking O(n^3)
"""

# Similar can be done without using sum()


def SubarraySum(array, target):
    total = 0
    for i in range(len(array)):
        current_sum = 0
        for j in range(i, len(array)):
            current_sum += array[j]
            if current_sum == target:
                total += 1
    return total


print(SubarraySum([1, 1, 1], 2))
# Time complexity: O(n)
