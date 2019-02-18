/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class OK_E_21_MergeTwoSortedLists {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if(l1 == null) return l2;
        if(l2 == null) return l1;
        ListNode d = new ListNode(0);
        d.next = l1.val <= l2.val ? l1 : l2;
        ListNode cur = d;
        while(l1 != null && l2 != null) {
            if(l1.val <= l2.val) {
                cur.next = l1;
                cur = l1;
                l1 = l1.next;
                
            } else {
                cur.next = l2;
                cur = l2;
                l2 = l2.next;
            }
        }
        //! exhausted either list just append other list to the end
        cur.next = l1 != null ? l1 : l2; 
        return d.next;
    }
}
