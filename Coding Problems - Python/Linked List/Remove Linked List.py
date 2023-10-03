# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # 0 Node
        if not head:
            return None
        
        # 1 Node
        if not head.next:

            if head.val == val:
                return None
            else:
                return head

        # >=2 Nodes
        while head.val == val:
            head = head.next
            if not head:
                return None
        
        temp = head
        while temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next

        return head
            
