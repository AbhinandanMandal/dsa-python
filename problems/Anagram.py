
# Anagram mean having similar count of characters in string

def Anagram(str1, str2):
    str1_hash = {}
    str2_hash = {}
    for char in str1:
        str1_hash[char] = str1_hash.get(char, 0)+1
    for char in str2:
        str2_hash[char] = str2_hash.get(char, 0)+1
    return str1_hash == str2_hash


print(Anagram('cat', 'tac'))
