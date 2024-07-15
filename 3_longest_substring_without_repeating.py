class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Find the length of the longest substring without repeating characters in a given string.

        The function uses a sliding window approach with two pointers (left and right) and a set
        to keep track of characters in the current window. It iterates through the string, expanding
        the window by moving the right pointer and checking for duplicates. If a duplicate is found,
        the left pointer moves to the right until the duplicate is removed from the set.

        Examples:
        For the string "abcabcbb":
        1. Initialize `best` to 1, `current_chars` to an empty set, `left` to 0, and `right` to 0.
        2. Add 'a' to `current_chars`, increment `right` to 1, `best` is updated to 1.
        3. Add 'b' to `current_chars`, increment `right` to 2, `best` is updated to 2.
        4. Add 'c' to `current_chars`, increment `right` to 3, `best` is updated to 3.
        5. 'a' is already in `current_chars`, remove 'a' from `current_chars`, increment `left` to 1.
        6. Add 'a' to `current_chars`, increment `right` to 4.
        7. Continue this process until the end of the string.
        8. The longest substring without repeating characters is "abc" with a length of 3.

        For the string "bbbbb":
        1. Initialize `best` to 1, `current_chars` to an empty set, `left` to 0, and `right` to 0.
        2. Add 'b' to `current_chars`, increment `right` to 1, `best` is updated to 1.
        3. 'b' is already in `current_chars`, remove 'b' from `current_chars`, increment `left` to 1.
        4. Add 'b' to `current_chars`, increment `right` to 2.
        5. Continue this process until the end of the string.
        6. The longest substring without repeating characters is "b" with a length of 1.
        """

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
