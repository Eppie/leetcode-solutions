class Solution:
    def longestCommonSubsequence(self, str1: str, str2: str) -> int:
        """
        The `table` keeps track of the longest common subsequence we can make with the given prefixes of `str1` and `str2`.
        For example, if `str1` is "ABB" and `str2` is "BBD", `table` will contain the following:
        [0, 0, 0, 0]: length 0 prefix of `str1` ("") has no common subsequences
        [0, 0, 0, 0]: length 1 prefix of `str1` ("A") has no common subsequences because `str2` does not contain an "A".
        [0, 1, 1, 1]: length 2 prefix of `str1` ("AB") has a length 1 common subsequence
        [0, 1, 2, 2]: length 3 prefix of `str1` ("ABB") has a length 2 common subsequence, but only once we've extended
            the length of the `str2` prefix to include both "B" characters.
        """
        if not str1 or not str2:
            return 0
        table = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
        for i in range(len(str1)):
            for j in range(len(str2)):
                if str1[i] == str2[j]:
                    table[i + 1][j + 1] = table[i][j] + 1
                else:
                    table[i + 1][j + 1] = max(table[i][j + 1], table[i + 1][j])
        return table[len(str1)][len(str2)]
