class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for e in nums:
            result ^= e
        return result
