/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public void reorderList(ListNode head) {
        if(head == null || head.next == null) return;
        Deque<ListNode> Q = new LinkedList<>();
        ListNode temp = head;

        while(temp != null){
            Q.offerLast(temp);
            temp = temp.next;
        }
        head = Q.pollFirst();

        while(head != null){
            head.next = Q.pollLast();
            head = head.next;
            if (!Q.isEmpty()){
                head.next = Q.pollFirst();
                head = head.next;
            }
        }

    }
}
