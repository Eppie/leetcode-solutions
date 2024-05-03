class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        sum_of_all = n * (n + 1) // 2
        return sum_of_all - sum(nums)
