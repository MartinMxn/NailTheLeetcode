package Java.Easy;

import java.util.HashSet;
import java.util.Set;

public class OK_E_141_LinkedListCycle {
    public boolean hasCycle(ListNode head) {
        //O(n) space
        // if(head == null) return false;
        // HashMap<ListNode, Integer> posVisted = new HashMap<>();
        // int pos = 0;
        // while(head.next != null){
        //     if(posVisted.containsKey(head)) return true;
        //     posVisted.put(head, pos);
        //     pos++;
        //     head = head.next;
        // }
        // return false;

        //O(1)
        if(head == null || head.next == null) return false;
        ListNode slow = head, fast = head;
        while(fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
            if(slow == fast) return true;
        }
        return false;
    }
}
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
        next = null;
    }
}
