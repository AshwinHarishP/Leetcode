# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        List = []
        temp = head
        n = 0
        while temp:
            List.append(temp.val)
            n += 1
            temp = temp.next

        maximum = float("-inf")
        for i in range(n//2):
            element = n - 1 - i
            Sum = List[i] + List[element]
            maximum = max(maximum,Sum)
        return maximum
        
