class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        The `table` keeps track of whether the string from `start` to `end + 1` is a palindrome.
        The diagonal of the table is initialized with all `True` values, because every single-character
        substring is trivially a palindrome.
        For each ending point `end` in the string, iterate over all `start` positions before it.
        Using the example string "babadb":
        1. Check "ba": This IS NOT a palindrome because the first and last characters are not the same.
        2. Check "bab": This IS a palindrome because the first and last characters are the same,
            and the substring ("a") between the first and last characters is also a palindrome
        ... some checks omitted for brevity ...
        3. Check "aba": This IS a palindrome as per reasoning in step 2, but it isn't longer than previous best, so we
            don't update our return value
        ... some checks omitted for brevity ...
        4. Check "badb": This IS NOT a palindrome. The first and last characters are equal, but the substring
            in the middle ("ad") is NOT, as per our table lookup.
        """
        if len(s) <= 1:
            return s

        best_len = 1
        longest_palindrome = s[0]
        table = [[False for _ in range(len(s))] for _ in range(len(s))]
        for end in range(1, len(s)):
            table[end][end] = True
            for start in range(end):
                if s[start] == s[end] and (
                    end - start < 2 or table[start + 1][end - 1]
                ):
                    table[start][end] = True
                    if end - start + 1 > best_len:
                        best_len = end - start + 1
                        longest_palindrome = s[start : end + 1]
        return longest_palindrome


if __name__ == "__main__":
    result = Solution().longestPalindrome("babadb")
    print(f"Longest palindromic substring: {result}")
