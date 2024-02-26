# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions):
        root = TreeNode()
        
        def helper(i, root):
            if i == len(descriptions):
                return root
            
            parent, child, isLeft = descriptions[i]
            
            if not root:
                return None

            root.val = parent

            if isLeft == 1:
                root.left = TreeNode(child) 
                helper(i+1, root.left)
            else:
                helper(i+1, root.right)
            
            return root
            
            
        return helper(0, root)
