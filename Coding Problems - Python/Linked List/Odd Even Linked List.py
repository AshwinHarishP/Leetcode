# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head:
            return None

        temp = head
        odd_head = ListNode(-1)
        even_head = ListNode(-1)

        odd_temp = odd_head
        even_temp = even_head

        odd = True
        while temp:
            if odd:
                odd_temp.next = ListNode(temp.val)
                odd_temp = odd_temp.next
            else:
                even_temp.next = ListNode(temp.val)
                even_temp = even_temp.next

            odd = not odd
            temp = temp.next

        odd_temp.next = even_head.next
        return odd_head.next
