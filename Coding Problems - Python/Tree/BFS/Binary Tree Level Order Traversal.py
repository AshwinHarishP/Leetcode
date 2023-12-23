# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = []

        if not root:
            return res

        queue.append(root)
        while queue:
            level = len(queue)
            temp = []
            for i in range(level):
                curr_ele = queue.pop(0)
                temp.append(curr_ele.val)

                if curr_ele.left:
                    queue.append(curr_ele.left)
                if curr_ele.right:
                    queue.append(curr_ele.right)

            res.append(temp)

        return res
