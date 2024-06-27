class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        s1 = set()
        s2 = set()
        for i in range(len(nums)):
            if nums[i] in s1:
                s2.add(nums[i])
            else:
                s1.add(nums[i])
        k = s1.difference(s2)
        return list(k)[0]
