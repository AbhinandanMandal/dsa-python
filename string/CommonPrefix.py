
"""
Longest Prefix
For example
str=["flower", "flow", "flowering"]
Hence, longest common prefix is "flow" which is same in all string's inside str.

We'll follow character by character comparison to find the longest common prefix
"""


def LongestCommonPrefix(strs: list):
    min_length = min(len(s) for s in strs)

    for i in range(min_length):
        for j in range(1, len(strs)):
            if strs[0][i] != strs[j][i]:
                return strs[0][:i]
    return strs[0][:min_length]


strs = ["flower", "flow", "flight"]
print(LongestCommonPrefix(strs))

# Time complexity: O(mxn)
# Space complexity: O(1)
