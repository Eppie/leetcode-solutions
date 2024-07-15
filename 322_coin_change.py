class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        The `coinChange` function determines the minimum number of coins required to make
        up a given amount using a dynamic programming approach.

        Algorithm:
        1. Initialize a `table` list where `table[i]` represents the minimum number of
           coins required to make the amount `i`.
        2. The `table` is initialized with a large number (`10**5`) except for `table[0]`,
           which is 0 (no coins needed for amount 0).
        3. For each amount `i` from 1 to `amount`, check each coin. If the coin can be
           used (i.e., `i - coin >= 0`), update `table[i]` to the minimum of its current
           value and `table[i - coin] + 1`.
        4. If `table[amount]` is still `10**5`, return -1 indicating it's not possible
           to make that amount. Otherwise, return `table[amount]`.

        Example:
        Using `coins = [1, 2, 5]` and `amount = 11`:

        1. Initialize `table` as [0, 100000, 100000, ..., 100000] (length 12).
        2. For `i = 1`:
           - Using coin 1: `table[1] = min(table[1], table[0] + 1) = 1`.
           - Using coins 2 and 5 are not possible for amount 1.
        3. For `i = 2`:
           - Using coin 1: `table[2] = min(table[2], table[1] + 1) = 2`.
           - Using coin 2: `table[2] = min(table[2], table[0] + 1) = 1`.
           - Using coin 5 is not possible for amount 2.
        4. Continue this process up to `i = 11`:
           - Using coin 1: `table[11] = min(table[11], table[10] + 1)`.
           - Using coin 2: `table[11] = min(table[11], table[9] + 1)`.
           - Using coin 5: `table[11] = min(table[11], table[6] + 1)`.
        5. After processing, `table` will have `table[11] = 3`, indicating the minimum
           number of coins needed is 3 (5 + 5 + 1).
        """

        if amount == 0:
            return 0
        table: list[int] = [0] + [10**5 for _ in range(amount)]
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    table[i] = min(table[i], table[i - coin] + 1)
        if table[amount] != 10**5:
            return table[amount]
        else:
            return -1


if __name__ == "__main__":
    print(Solution().coinChange([1, 2, 5], 11))  # 3
