# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """

        res = []
        queue = []

        if not root:
            return res

        queue.append(root)

        while queue:
            temp = []
            level = len(queue)

            for i in range(level):
                curr_ele = queue.pop(0)
                temp.append(curr_ele.val)

                if curr_ele.left:
                    queue.append(curr_ele.left)

                if curr_ele.right:
                    queue.append(curr_ele.right)

            print(temp)

            avg = float(sum(temp))/len(temp)
            print(avg)
            res.append(avg)

        return res
