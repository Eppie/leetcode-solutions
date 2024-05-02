class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        character_mapping = {"{": "}", "[": "]", "(": ")"}
        for c in s:
            if c in character_mapping:
                stack.append(character_mapping[c])
            elif len(stack) == 0 or stack.pop() != c:
                return False
        return len(stack) == 0
