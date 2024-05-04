class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.endOfWord: bool = False
        self.value: str = ""


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
        cur.value = word
