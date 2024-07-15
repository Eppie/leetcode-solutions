class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int] | None:
        """
        Find two distinct indices in `nums` that sum up to `target`.

        Example:
            Given `nums = [2, 7, 11, 15]` and `target = 9`, the function will:
            1. Create a dictionary `num_by_index` to map each number to its index:
               {2: 0, 7: 1, 11: 2, 15: 3}
            2. Iterate through `nums`:
               - For `i = 0`, `nums[i] = 2`, compute `target - nums[i] = 7`
                 - 7 is in `num_by_index` and its index is not 0, so return [0, 1]
               - No need to continue as the solution is found.

            Given `nums = [1, 2, 3, 4]` and `target = 8`, the function will:
            1. Create `num_by_index`: {1: 0, 2: 1, 3: 2, 4: 3}
            2. Iterate through `nums`:
               - For `i = 0`, `nums[i] = 1`, compute `target - nums[i] = 7`
                 - 7 is not in `num_by_index`
               - For `i = 1`, `nums[i] = 2`, compute `target - nums[i] = 6`
                 - 6 is not in `num_by_index`
               - For `i = 2`, `nums[i] = 3`, compute `target - nums[i] = 5`
                 - 5 is not in `num_by_index`
               - For `i = 3`, `nums[i] = 4`, compute `target - nums[i] = 4`
                 - 4 is in `num_by_index` but its index is the same (3), so not valid
               - No solution found, return None.
        """
        num_by_index = {nums[i]: i for i in range(len(nums))}
        for i in range(len(nums)):
            if (
                target - nums[i] in num_by_index.keys()
                and num_by_index[target - nums[i]] != i
            ):
                return [i, num_by_index[target - nums[i]]]
        return None
