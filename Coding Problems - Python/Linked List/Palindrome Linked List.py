# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        List = []
        if not head:
            return False

        temp = head
        while temp is not None:
            List.append(temp.val)
            temp = temp.next
        
        return List == List[::-1]
        
