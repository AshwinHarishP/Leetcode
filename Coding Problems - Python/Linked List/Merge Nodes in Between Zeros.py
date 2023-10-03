# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if not head:
            return head
        temp = head

        List = []
        while temp:
            List.append(temp.val)
            temp = temp.next

        Sum = 0
        res = []
        for i in range(1,len(List)):
            Sum += List[i]

            if List[i] == 0:
                res.append(Sum)
                Sum = 0
        
        head1 = ListNode(0)
        temp1 = head1
        for i in res:
            temp1.next = ListNode(i)
            temp1 = temp1.next
        return head1.next
        
