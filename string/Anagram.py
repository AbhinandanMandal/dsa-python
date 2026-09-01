

def ValidAnagram(str1: str, str2: str):
    hashA = {}
    hashB = {}

    for i in str1:
        hashA[i] = hashA.get(i, 0)+1
    for i in str2:
        hashB[i] = hashB.get(i, 0)+1

    # Complex approach
    """for k, v in hashA.items():
        if k in hashB and v != hashB.get(k):
            return False
    return True"""

    # Easiest approach
    return hashA == hashB


# print(ValidAnagram("listen", "silent"))
print(ValidAnagram("aab", "abb"))

# Time complexity: O(m+n), Space complexity: O(m+n)
