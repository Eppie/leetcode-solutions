from common.tree_node import TreeNode


class Solution:
    def height(self, node: TreeNode | None) -> int:
        if node is None:
            return 0
        return max(self.height(node.left), self.height(node.right)) + 1

    def isBalanced(self, root: TreeNode | None) -> bool:
        if root is None:
            return True
        if abs(self.height(root.left) - self.height(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
