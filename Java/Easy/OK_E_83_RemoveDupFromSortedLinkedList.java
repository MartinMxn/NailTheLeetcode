package Java.Easy;

public class OK_E_83_RemoveDupFromSortedLinkedList {
    public ListNode deleteDuplicates(ListNode head) {
        // Set<Integer> set = new HashSet<>();
        // ListNode pre = new ListNode(-1);
        // ListNode node = head;
        // while(node != null){
        //     if(set.contains(node.val)){
        //         pre.next = node.next;
        //         node = node.next;
        //     }else{
        //         set.add(node.val);
        //         pre = node;
        //         node = node.next;
        //     }
        // }
        // return head;

        // because it's sorted, so it could be O(1) space, and faser
        ListNode node = head;
        while(node != null && node.next != null){
            if(node.val == node.next.val){
                node.next = node.next.next;
            }else{
                node = node.next;
            }
        }
        return head;
    }
}
