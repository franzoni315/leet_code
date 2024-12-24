# Definition for a binary tree node.


from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # the maximum depth of the current node is the max depth of the parent + 1
        # print(root.val)
        if root is None:
            return 0
        if root.right is None and root.left is None:
            return 1
        elif root.right is None:
            return self.maxDepth(root.left) + 1
        elif root.left is None:
            return self.maxDepth(root.right) + 1
        else:
            return max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1

if __name__ == '__main__':
    # n1 = TreeNode(3)
    # n2 = TreeNode(9)
    # n3 = TreeNode(20)
    # n4 = TreeNode(15)
    # n5 = TreeNode(7)
    # n1.left, n1.right = n2, n3
    # n3.left, n3.right = n4, n5

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n1.right = n2

    print(Solution().maxDepth(n1))