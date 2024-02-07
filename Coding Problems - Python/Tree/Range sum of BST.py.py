# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root: return 0

        Range = list(range(low, high+1))
        Sum = 0
        
        queue = [root]
        while queue:
            curr = queue.pop(0)
            if curr.val in Range:
                Sum += curr.val

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)
        return Sum
        

