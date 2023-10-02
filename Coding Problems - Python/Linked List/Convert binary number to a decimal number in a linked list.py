# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        value = ""

        temp = head
        while temp is not None:
            value += str(temp.val)
            temp = temp.next
            
        return(int(value,2))

        
