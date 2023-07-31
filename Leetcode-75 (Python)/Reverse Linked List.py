# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        else:
            Stack = []
            temp = head
            while temp != None:
                Stack.append(temp)
                temp = temp.next


            head = Stack.pop()
            temp = head

            while len(Stack) != 0:
                temp.next = Stack.pop()
                temp = temp.next
            temp.next = None

        return head
