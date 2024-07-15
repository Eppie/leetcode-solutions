class Solution:
    @staticmethod
    def removeElement(nums: list[int], val: int) -> int:
        """
        The `removeElement` method removes all instances of a specified value from a list
        in-place and returns the new length of the list after removal. The order of elements
        can be changed, and the elements beyond the new length are irrelevant.

        Algorithm:
        1. Initialize a variable `copy_to` to track the position where the next non-`val`
           element should be copied.
        2. Iterate over the list with index `i`:
           - Swap the current element `nums[i]` with the element at `nums[copy_to]`.
           - If `nums[copy_to]` is not equal to `val`, increment `copy_to`.
        3. Return the value of `copy_to` which represents the new length of the list
           after removing all instances of `val`.

        Example:
        Given the list [3, 2, 2, 3] and val = 3:
        1. Start with `copy_to = 0`.
        2. Swap `nums[0]` and `nums[0]`: [3, 2, 2, 3]
           - `nums[copy_to]` is 3, which is equal to `val`, so `copy_to` remains 0.
        3. Swap `nums[1]` and `nums[0]`: [2, 3, 2, 3]
           - `nums[copy_to]` is 2, which is not equal to `val`, so `copy_to` is incremented to 1.
        4. Swap `nums[2]` and `nums[1]`: [2, 2, 3, 3]
           - `nums[copy_to]` is 2, which is not equal to `val`, so `copy_to` is incremented to 2.
        5. Swap `nums[3]` and `nums[2]`: [2, 2, 3, 3]
           - `nums[copy_to]` is 3, which is equal to `val`, so `copy_to` remains 2.
        6. The final list is [2, 2, 3, 3] with `copy_to` being 2, indicating the new length.

        The function returns 2, and the modified list is [2, 2].
        """

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
