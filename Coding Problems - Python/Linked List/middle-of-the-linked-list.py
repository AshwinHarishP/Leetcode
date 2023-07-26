# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Finding length of linked list
        temp = head
        length = 1
        while temp != None:
            length += 1
            temp = temp.next

        if length %2 != 0:
            mid = length//2 + 1
        else:
            mid = length // 2 + 1

        pos = head
        for i in range(mid+1,length+1):
            pos = pos.next
        return pos
