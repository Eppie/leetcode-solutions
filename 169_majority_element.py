from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        c = Counter(nums)
        return c.most_common()[0][0]


if __name__ == "__main__":
    s = Solution()
    assert s.majorityElement([1, 2, 3, 3]) == 3


