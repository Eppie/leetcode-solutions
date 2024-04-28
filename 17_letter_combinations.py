class Solution:
    num_to_letter: dict[int, str] = {
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz",
    }

    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        if len(digits) == 1:
            return list(self.num_to_letter[int(digits[0])])
        return [
            first_letter + the_rest for first_letter in self.num_to_letter[int(digits[0])] for the_rest in
            self.letterCombinations(digits[1:])]
