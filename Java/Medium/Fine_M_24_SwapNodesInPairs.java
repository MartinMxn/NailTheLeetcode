package Java.Medium;

public class Fine_M_24_SwapNodesInPairs {
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode cur = dummy;
        while(cur.next!= null && cur.next.next != null){
            cur = swap(cur);
        }
        return dummy.next;
    }

    private ListNode swap(ListNode node) {
        ListNode a = node.next;
        ListNode b = node.next.next;
        a.next = b.next;
        b.next = a;
        node.next = b;
        return a;
    }
}
