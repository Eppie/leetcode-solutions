class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            index = (left + right) // 2
            value = nums[index]
            if value == target:
                return index
            elif value < target:
                left = index + 1
            else:
                right = index - 1
        return -1


if __name__ == "__main__":
    s = Solution()
    assert s.search([-1, 0, 3, 5, 9, 12], 2) == -1
