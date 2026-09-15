
""" 
Here we need to return minimum number of flips to make array same
Example, array=[1,1,0,0,1,1]
If we toss only two zeros to 1 then we get same array, so, minimum number of flips = 1 (for group)
Cause we're calculating the number of flips required for a group to flip to make array same

Again, for array=[1,1,0,0,1,1,0,0]
If we toss only 2 groups of both 0 and 1 then we'll have same array
"""


def MinimumConsecutiveFlips(array):
    flips_0 = 0
    flips_1 = 0
    for i in range(len(array)):
        if i == 0 or array[i] != array[i-1]:  # This making a grouping condition
            if array[i] == 0:
                flips_0 += 1
            else:
                flips_1 += 1
    return min(flips_0, flips_1)


array = [1, 1, 0, 0, 1, 1, 0, 0]
print(MinimumConsecutiveFlips(array))
# Time complexity: O(n)
# Space complexity: O(1)
