
def FirstUnique(string: str):
    characters = {}
    for c in string:
        characters[c] = characters.get(c, 0)+1
    for k, v in characters.items():
        if v == 1:
            return k
    return -1  # In case of not presence of any unique characters


# print(FirstUnique("leetcode"))
print(FirstUnique("loveleetcode"))

# Time complexity: O(n), Space complexity: O(n)
