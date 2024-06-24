class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        sub_solutions = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    sub_solutions[i][j] = sub_solutions[i - 1][j - 1] + 1
                else:
                    sub_solutions[i][j] = max(
                        sub_solutions[i - 1][j], sub_solutions[i][j - 1]
                    )
        return sub_solutions[len(text1)][len(text2)]
