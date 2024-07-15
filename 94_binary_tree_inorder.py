from common.tree_node import TreeNode


class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        if root:
            return (
                self.inorderTraversal(root.left)
                + [root.val]
                + self.inorderTraversal(root.right)
            )
        else:
            return []
