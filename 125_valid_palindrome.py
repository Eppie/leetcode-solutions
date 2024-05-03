import re


class Solution:
    pattern = re.compile(r"[\W_]+")

    def isPalindrome(self, s: str) -> bool:
        s = self.pattern.sub("", s.lower())
        return s == s[::-1]
