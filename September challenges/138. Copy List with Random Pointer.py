"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        
        # Creating a new weaved list of original and copied nodes.
        pointer = head
        while pointer:
            # Cloned Node
            new_node = Node(pointer.val, None, None)
            
            new_node.next = pointer.next
            pointer.next = new_node
            pointer = new_node.next
        
        pointer = head
        
        while pointer:
            pointer.next.random = pointer.random.next if pointer.random else None
            pointer = pointer.next.next
            
        pointer_old_list = head
        pointer_new_list = head.next
        head_new = head.next
        while pointer_old_list:
            pointer_old_list.next = pointer_old_list.next.next
            pointer_new_list.next = pointer_new_list.next.next if pointer_new_list.next else None
            pointer_old_list = pointer_old_list.next
            pointer_new_list = pointer_new_list.next
        return head_new
