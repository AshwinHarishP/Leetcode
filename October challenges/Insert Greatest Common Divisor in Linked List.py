# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        if not head.next:
            return head

        temp = head
        while temp and temp.next:
            gcd_value = math.gcd(temp.val, temp.next.val)
            new_node = ListNode(gcd_value)
            new_node.next = temp.next
            temp.next = new_node
            temp = temp.next.next

        return head
