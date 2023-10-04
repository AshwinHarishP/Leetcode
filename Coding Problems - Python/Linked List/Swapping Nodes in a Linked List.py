# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        List = []
        if not head:
            return None

        temp = head
        while temp:
            List.append(temp.val)
            temp = temp.next

        List[k - 1], List[-k] = List[-k], List[k - 1]

        new_head = ListNode(List[0])
        new_temp = new_head

        for i in range(1,len(List)):
            new_node = ListNode(List[i])
            new_temp.next = new_node
            new_temp = new_temp.next
        return new_head

