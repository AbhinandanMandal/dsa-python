
class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        m = len(nums)
        new_array = []*2*m
        i = 0
        while i < m:
            new_array.insert(i, nums[i])
            new_array.insert(m+i, nums[i])
            i += 1
        return new_array
