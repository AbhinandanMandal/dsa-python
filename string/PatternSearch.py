
# In this approach, we need to find a string pattern within a string itself
"""
So, the given text can be written as, 

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
A A B A A C A A D A A  B  A  A  B  A

0 1 2 3
A A B A
"""

# Approach 1
"""txt = 'AABAACAADAABAABA'
pat = 'AABA'
pos = txt.find(pat)
while pos >= 0:
    print(pos)
    pos = txt.find(pat, pos+1)

# Time complexity: O(n^2.m)"""


"""# Approach 3
# For efficient pattern search, we can use KMP (Knuth-Morrish-Patt) algorithm
# At first, we need to maintain an LPS, 
# which is, longest proper prefix which is also a suffix


# A part of KMP
def LPS(pattern):
    lps=[0]*len(pattern)
    i=1
    length=0
    while i<len(pattern):
        if pattern[i]==pattern[length]:
            length+=1
            lps[i]=length
            i+=1

        else:
            if length!=0:
                length=lps[length-1]
            else:
                lps[i]=0
                i+=1
    return lps 

# KMP algorithm
"""

# Approach 2
# Naive approach


def PatternMatch(text, pattern):
    n = len(text)
    m = len(pattern)
    for i in range(n-m+1):
        j = 0
        while j < m:
            if pattern[j] != text[i+j]:
                break
            j += 1
        if j == m:
            print(i)


text = 'AABAACAADAABAABA'
pattern = 'AABA'
PatternMatch(text, pattern)
# Time complexity: O((n-m+1).m) or O(l.m)
# Space complexity: O(1)
