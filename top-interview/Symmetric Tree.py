from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is not None:
            return True
        
        return self.checkSymmetry(root.left, root.right)
    
    def checkSymmetry(self, leftNode, rightNode):
        if leftNode is None and rightNode is None:
            return True
        if leftNode is None and rightNode is not None:
            return False
        if leftNode is not None and rightNode is None:
            return False
        print(leftNode.val, rightNode.val)
        
        if (leftNode.val != rightNode.val):
            return False
        
        return (self.checkSymmetry(leftNode.left, rightNode.right) 
                and self.checkSymmetry(leftNode.right, rightNode.left))




if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(2)
    n4 = TreeNode(3)
    n5 = TreeNode(4)
    n6 = TreeNode(4)
    n7 = TreeNode(3)
    n1.left, n1.right = n2, n3
    n2.left, n2.right = n4, n5
    n3.left, n3.right = n6

    print(Solution().isSymmetric(n1))