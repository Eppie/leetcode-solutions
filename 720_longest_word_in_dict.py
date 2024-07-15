from common.trie import Trie


class Solution:
    def longestWord(self, words: list[str]) -> str:
        """
         Finds the longest word in the given list that can be built one character
        at a time by other words in the list.

        Args:
            words (list[str]): The list of words to be processed.

        Returns:
            str: The longest word satisfying the condition.

        Example:
            Given the input list ["a", "banana", "app", "appl", "ap", "apply", "apple"],
            the function processes the words and builds a Trie structure to facilitate
            the search. It uses a breadth-first search (BFS) approach to traverse
            the Trie, ensuring that it explores all possible words in increasing order
            of length. The result "apple" is found as it is the longest word that can
            be constructed from other words in the list.

        Process:
            1. Initialize the Trie and add all words to it.
            2. Use a queue to perform BFS starting from the root node.
            3. For each node, check its children. If a child node represents the end
               of a word, add it to the queue for further exploration.
            4. Update the result with the longest valid word found during the traversal.

        Example:
            1. Add words to the Trie:
               - "a" -> Trie structure: root -> 'a'
               - "banana" -> Trie structure: root -> 'b' -> 'a' -> 'n' -> 'a' -> 'n' -> 'a'
               - The final Trie structure will be:
               root
                ├── a (endOfWord=True, value='a')
                │   ├── p (endOfWord=True, value='ap')
                │   │   ├── p (endOfWord=True, value='app')
                │   │   │   ├── l (endOfWord=True, value='appl')
                │   │   │   │   ├── e (endOfWord=True, value='apple')
                │   │   │   │   └── y (endOfWord=True, value='apply')
                └── b
                    └── a
                        └── n
                            └── a
                                └── n
                                    └── a (endOfWord=True, value='banana')
            2. Traverse the Trie using BFS:
               - Start with the root node, explore its children.
               - For each child node that is the end of a word, add it to the queue.
               - Continue until all nodes are processed.
        """
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
