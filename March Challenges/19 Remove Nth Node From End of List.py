class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or n <= 0:
            return head

        dummy = ListNode()
        dummy.next = head
        fast = head
        slow = dummy

        
        for _ in range(n):
            if fast:
                fast = fast.next
            else:
                return head  
        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next  
