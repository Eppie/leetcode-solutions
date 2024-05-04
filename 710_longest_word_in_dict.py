from common.trie import Trie


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
