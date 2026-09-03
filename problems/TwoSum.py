
"""def TwoSum(arr: list, target: int):
    num_hash = {}
    for i, num in enumerate(arr):
        complement = target-num
        if complement in num_hash:
            return [num_hash[complement], i]
        num_hash[num] = i
    return []


print(TwoSum([2, 7, 11, 15], 9))"""


def TwoSum(array: list, target: int):
    num_hash = {}
    for i, num in enumerate(array):
        complement = target-num
        if complement in num_hash:
            return [num_hash[complement], i]
        num_hash[num] = i  # creating the  hash
    return []


print(TwoSum([2, 7, 11, 15], 9))
# Time complexity: O(n), Space complexity: O(n)
