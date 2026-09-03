"""
def GroundAnagrams(strs):
    groups = {}
    for word in strs:
        key = ''.join(sorted(word))

        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())


print(GroundAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
"""


def GroupAnagrams(strs):
    groups = {}

    for word in strs:
        key = ''.join(sorted(word))

        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())


print(GroupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# Time complexity: O(n.klogk)
# Space complexity: O(n.k)

# klogk coming for sorting
# Python internally use combination of merge sort and insertion sort, having time complexity: O(nlogn)
# In best case, O(n)
