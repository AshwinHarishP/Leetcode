# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        l1_ele, l2_ele = "", ""

        while l1:
            l1_ele += (str(l1.val))
            l1 = l1.next
        
        while l2:
            l2_ele += str(l2.val)
            l2 = l2.next

        Sum = map(int,str(sum(map(int,l1_ele.split(" ")) + map(int,l2_ele.split(" ")))))
        
        head = ListNode(-1)
        temp = head
        
        for i in Sum:
            temp.next = ListNode(i)
            temp = temp.next
        return head.next


        


        
