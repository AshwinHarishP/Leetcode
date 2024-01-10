# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        Q = []
        def helper(root):
            if not root:
                return None

            helper(root.left)
            Q.append(root.val)
            helper(root.right)
            return Q

        helper(root)
        return Q[k-1]
            
