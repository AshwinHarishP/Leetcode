# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        global ans
        ans = 0
        freq = [0] * 10

        def palindrome(freq):
            count = 0
            for i in freq:
                if i % 2 == 1:
                    count += 1
            return count <= 1

        def helper(root, freq):
            if root.left == None and root.right == None:
                freq[root.val] += 1
                if palindrome(freq):
                    global ans
                    ans += 1

                freq[root.val] -= 1
                return
            
            freq[root.val] += 1
            if root.left:
                helper(root.left, freq)
            
            if root.right:
                helper(root.right, freq)

            freq[root.val] -= 1
            return
        helper(root, freq)

        return ans

            

            
