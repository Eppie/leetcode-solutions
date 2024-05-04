from collections import defaultdict

from common.tree_node import TreeNode


class Solution:
    levels: dict[int, list[int]] = defaultdict(list)

    def build_levels(self, node: TreeNode | None, level: int = 0) -> None:
        if not node:
            return
        self.levels[level].append(node.val)
        self.build_levels(node.left, level + 1)
        self.build_levels(node.right, level + 1)

    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        self.levels.clear()
        if not root:
            return []
        self.build_levels(root)
        result = []
        level = 0
        while level in self.levels:
            result.append(sum(self.levels[level]) / len(self.levels[level]))
            level += 1
        return result
