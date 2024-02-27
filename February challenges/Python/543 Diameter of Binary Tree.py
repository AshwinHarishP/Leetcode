# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    diameter = 0

    def height(self, node):
        if not node:
            return 0
        
        leftHeight = self.height(node.left)
        rightHeight = self.height(node.right)

        dia = leftHeight + rightHeight + 1
        self.diameter = max(self.diameter, dia)

        return max(leftHeight, rightHeight) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.height(root)
        return self.diameter-1
        
