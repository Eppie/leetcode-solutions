class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        """
        The `findTargetSumWays` method calculates the number of ways to assign symbols
        "+" and "-" to make the sum of `nums` equal to the `target`.

        Algorithm:
        1. Calculate the total sum of `nums`.
        2. If `abs(target)` is greater than `total` or if `(target + total) % 2 == 1`, return 0.
        3. Initialize a list of dictionaries `table` to store intermediate results.
        4. Define a recursive function `backtrack` to explore all possible sums:
            - If `current_sum` is already computed for the current index, return its value.
            - If `index` is -1, check if `current_sum` equals the target and return 1 if true, otherwise 0.
            - Calculate the number of ways to achieve `current_sum` by adding or subtracting the current element.
            - Store the result in `table` and return it.
        5. Start the backtracking process from the last index with an initial `current_sum` of 0.

        Example:
        For `nums = [1, 1, 1, 1, 1]` and `target = 3`:
        1. Total sum is 5.
        2. Initialize `table` as `[{}, {}, {}, {}, {}]`.
        3. Backtrack:
            - Start from index 4 with `current_sum = 0`.
            - Recursively explore sums by adding/subtracting elements:
                - At index 4 with `current_sum = 0`, explore index 3 with `current_sum + 1` and `current_sum - 1`.
                - Continue this process until index -1 is reached.
            - Count the number of valid ways to achieve `target = 3`.
        4. The result is 5.
        """

        total = sum(nums)
        if abs(target) > total or (target + total) % 2 == 1:
            return 0
        table: list[dict[int, int]] = [{} for _ in range(len(nums))]

        def backtrack(index: int, current_sum: int) -> int:
            if current_sum in table[index]:
                return table[index][current_sum]

            if index == -1:
                return 1 if current_sum == target else 0

            add = backtrack(index - 1, current_sum + nums[index])
            sub = backtrack(index - 1, current_sum - nums[index])
            table[index][current_sum] = add + sub
            return table[index][current_sum]

        return backtrack(len(nums) - 1, 0)


if __name__ == "__main__":
    print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))
    print(
        Solution().findTargetSumWays(
            [10, 9, 6, 4, 19, 0, 41, 30, 27, 15, 14, 39, 33, 7, 34, 17, 24, 46, 2, 46],
            45,
        )
    )
