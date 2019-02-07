/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        //iterate
        // ListNode dummy = null;
        // ListNode cur = head;
        // while(cur != null) {
        //     ListNode tmp = cur.next;
        //     cur.next = dummy;
        //     dummy = cur;
        //     cur = tmp;
        // }
        // return dummy;
        
        //recursion
        /*
        Assume from node nk+1 to nm had been reversed and you are at node nk.
        n1 → … → nk-1 → nk → nk+1 ← … ← nm
        We want nk+1’s next node to point to nk.
        So, nk.next.next = nk;
        */
        if(head == null || head.next == null) return head;
        ListNode node = reverseList(head.next);
        head.next.next = head;
        head.next = null;
        return node;
    }
}
