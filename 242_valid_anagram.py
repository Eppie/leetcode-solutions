from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Minor optimization, doesn't impact correctness
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)
