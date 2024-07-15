class Solution:
    def countBits(self, n: int) -> list[int]:
        """
        The `countBits` method calculates the number of 1-bits for all numbers from 0 to `n`.

        The function initializes the `result` list with the base cases for the first four numbers:
        - `0` has 0 bits.
        - `1` has 1 bit.
        - `2` has 1 bit.
        - `3` has 2 bits.

        It then iteratively expands the list by appending a modified version of itself where each
        element is incremented by 1. This leverages the property that the number of 1-bits in
        a number `i` is the number of 1-bits in `i - 2^m` plus 1, where `2^m` is the highest power
        of 2 less than or equal to `i`.

        Example:
        For `n = 5`:
        1. Initialize `result = [0, 1, 1, 2]`.
        2. Since `len(result) < 6`, extend `result`:
           - New elements: `map(lambda i: i + 1, [0, 1, 1, 2])` results in `[1, 2, 2, 3]`.
           - `result` becomes `[0, 1, 1, 2, 1, 2, 2, 3]`.
        3. Trim to the first `n + 1` elements: `[0, 1, 1, 2, 1, 2]`.

        Example:
        For `n = 2`:
        1. Initialize `result = [0, 1, 1, 2]`.
        2. Since `len(result) >= 3`, return the first `n + 1` elements: `[0, 1, 1]`.
        """

        result = [0, 1, 1, 2]
        while len(result) < n + 1:
            result = result + list(map(lambda i: i + 1, result))
        return result[: n + 1]


if __name__ == "__main__":
    print(Solution().countBits(2))  # [0,1,1]
    print(Solution().countBits(5))  # [0,1,1,2,1,2]

# 1-bit: (0-1) 0,1
# 2-bit: (2-3) 1,2
# 3-bit: (4-7) 1,2,2,3
# 4-bit: (8-15) 1,2,2,3,2,3,3,4
# 5-bit: (15-31) 1,2,2,3,2,3,3,4, 2,3,3,4,3,4,4,5,
# so,
