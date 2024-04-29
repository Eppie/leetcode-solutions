from typing import Iterable


class Solution:
    @staticmethod
    def is_valid_segment(segment: Iterable[str]) -> bool:
        nums = list(filter(lambda x: x != ".", segment))
        return len(nums) == len(set(nums))

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for row in board:
            if not self.is_valid_segment(row):
                return False
        for col in zip(*board):
            if not self.is_valid_segment(col):
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                segment = []
                for k in range(3):
                    segment.extend(board[i + k][j : j + 3])
                if not self.is_valid_segment(segment):
                    return False
        return True
