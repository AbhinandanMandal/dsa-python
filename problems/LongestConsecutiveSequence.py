
""" 
consecutive numbers means that each number differs from the next number by exactly 1.
"""
"""def LongestConsecutiveSequence(array):
    num_set = set(array)
    longest = 0

    for num in num_set:
        if num-1 not in num_set: # It has to be true for finding longest consecutive sequence
            length = 1
            if num+length in num_set:
                length += 1
            longest = max(longest, length)
    return longest"""


def LongestConsecutiveSequence(array):
    num_set = set(array)
    longest = 0

    for num in num_set:
        if num-1 not in num_set:
            length = 1
            while num+length in num_set:
                length += 1
            longest = max(longest, length)
    return longest


print(LongestConsecutiveSequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))

# Time complexity: O(n), Space complexity: O(n)
