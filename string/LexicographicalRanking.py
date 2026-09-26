
"""
Need to rank based on lexicographical order (permutation order)

For example, 
ABC - 1 rank
ACB - 2 rank
BAC - 3 rank
BCA - 4 rank
CAB - 5 rank
CBA - 6 rank
"""


def Factorial(n):
    if n == 0:
        return 1
    return n*Factorial(n-1)


def LexicographicalRank(string):
    n = len(string)
    rank = 1
    for i in range(n):
        count = 0

        # Checking how many current digit smaller than prev digit
        for j in range(i+1, n):
            if string[j] < string[i]:
                count += 1
        rank += count*Factorial(n-i-1)
    return rank


print(LexicographicalRank('BCA'))

# Time complexity: O(n^2), Space complexity: O(1)
