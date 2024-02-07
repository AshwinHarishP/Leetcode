# Definition for a binary tree root.
class Treeroot(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def flatten(self, root):
        """
        :type root: Treeroot
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def helper(root):
            if not root:
                return None
            if not root.left and not root.right:
                return root
            
            left_tail = helper(root.left)
            right_tail = helper(root.right)
            
            if root.left:
                left_tail.right = root.right
                root.right = root.left
                root.left = None
            
            return right_tail if right_tail else left_tail
        
        helper(root)
