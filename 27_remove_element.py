class Solution:
    @staticmethod
    def removeElement(nums: list[int], val: int) -> int:
        copy_to = 0
        for i in range(len(nums)):
            nums[i], nums[copy_to] = nums[copy_to], nums[i]
            if nums[copy_to] != val:
                copy_to += 1

        return copy_to


if __name__ == "__main__":
    test_input = [3, 2, 2, 3]
    test_output = Solution.removeElement(test_input, 3)
    assert test_output == 2, f"{test_output}"
    assert test_input[:2] == [2, 2], f"{test_input}"
