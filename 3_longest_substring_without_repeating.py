class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        best = 1
        current_chars = set()
        left = 0
        right = 0
        while right < len(s):
            if s[right] not in current_chars:
                current_chars.add(s[right])
                right += 1
                if right - left > best:
                    best = right - left
            else:
                while s[right] in current_chars:
                    current_chars.remove(s[left])
                    left += 1
        return best
