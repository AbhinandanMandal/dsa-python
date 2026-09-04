
"""def TwoSumII(array, target):
    num_hash = {}

    for i, num in enumerate(array):
        complement = target-num
        if complement in num_hash:
            return [num_hash[complement]+1, i+1]
        num_hash[num] = i  # Constructing the dictionary
    return []


print(TwoSumII([2, 7, 11, 15], 9))
# Time complexity: O(n)
# Space complexity: O(n)

"""

"""
Though previous hash map approach can be done, but
in TwoSumII problem, the array is already sorted, so 
we don't need to use hash map for that. 

we can use simply array with two pointer approach

"""


def TwoSum2(array, target):
    left = 0
    right = len(array)-1

    while left < right:
        total = array[left]+array[right]
        if total == target:
            return [left+1, right+1]
        elif total < target:
            left += 1
        else:
            right -= 1
    return []  # If no pair exists


print(TwoSum2([2, 7, 11, 15], 9))
# Time complexity: O(n), Space complexity: O(1)