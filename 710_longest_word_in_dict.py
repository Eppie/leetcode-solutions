
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.value = ""


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
        cur.value = word


class Solution:
    def longestWord(self, words: list[str]) -> str:
        trie = Trie()
        for word in words:
            trie.addWord(word)

        queue = [trie.root]
        result = ""
        while queue:
            current = queue.pop(0)
            for child in current.children.values():
                if child.endOfWord:
                    queue.append(child)
                    if len(child.value) > len(result) or (
                        len(child.value) == len(result) and child.value < result
                    ):
                        result = child.value
        return result


if __name__ == "__main__":
    s = Solution()
    test_input = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    assert s.longestWord(test_input) == "apple"
