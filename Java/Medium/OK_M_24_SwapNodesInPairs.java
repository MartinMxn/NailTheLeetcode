/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
//start from the node before pairsa
class OK_M_24_SwapNodesInPairs {
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        swap(dummy);
        return dummy.next;
    }
    
    private void swap(ListNode node) {
        if(node.next == null || node.next.next == null) return;
        ListNode a = node.next;
        ListNode b = node.next.next;
        a.next = b.next;
        b.next = a;
        node.next = b;
        swap(a);
    }
}
