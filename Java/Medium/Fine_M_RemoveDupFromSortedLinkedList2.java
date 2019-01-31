package Java.Medium;

public class Fine_M_RemoveDupFromSortedLinkedList2 {
    //key: if pre.next == node
    public ListNode deleteDuplicates(ListNode head) {
        if(head == null) return null;
        ListNode dummy = new ListNode(Integer.MAX_VALUE);
        dummy.next = head;
        ListNode pre = dummy;
        ListNode node = head;
        while(node != null){
            while(node.next != null && node.val == node.next.val) node = node.next;
            if(pre.next == node){
                pre = pre.next;
            }else{
                pre.next = node.next;
            }
            node = node.next;
        }
        return dummy.next;
    }
}
