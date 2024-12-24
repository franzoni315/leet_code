# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # the current tree is valid if it is greater than the left node and smaller than the right
        # recursively check if left and right subtrees are valid
        return self._isValidBSTHelper(root, float('-inf'), float('inf'))

    def _isValidBSTHelper(self, node: Optional[TreeNode], lower: float, upper: float):
        if not node:
            return True
        val = node.val

        if val <= lower or val >= upper:
            return False

        if not self._isValidBSTHelper(node.right, val, upper):
            return False
        if not self._isValidBSTHelper(node.left, lower, val):
            return False

        return True

if __name__ == '__main__':
    # n1 = TreeNode(2)
    # n2 = TreeNode(1)
    # n3 = TreeNode(3)
    # n1.left, n1.right = n2, n3

    # n1 = TreeNode(1)
    # n2 = TreeNode(1)
    # n1.left = n2

    n1 = TreeNode(5)
    n2 = TreeNode(4)
    n3 = TreeNode(6)
    n4 = TreeNode(3)
    n5 = TreeNode(7)
    n1.left, n2.right = n2, n3
    n3.left, n3.right = n4, n5

    print(Solution().isValidBST(n1))