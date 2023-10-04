# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        self.head = head
        

    def getRandom(self):
        """
        :rtype: int
        """
        if self.head and self.head.next is None:
            return self.head.val

        temp = self.head
        result = None
        count = 0

        while temp:
            if (random.randint(0,count) == 0):
                result = temp.val
            temp = temp.next
            count += 1
        return result
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
