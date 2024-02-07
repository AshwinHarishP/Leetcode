# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        Q = deque()
        if not head or not head.next:
            return 

        temp = head
        while temp:
            Q.append(temp)
            temp = temp.next
        
        head = Q.popleft()

        while Q:
            head.next = Q.pop()
            head = head.next
            if Q:
                head.next = Q.popleft()
                head = head.next
        head.next = None
