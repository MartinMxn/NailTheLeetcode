package Java.Medium;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    //find last non-9 digits
    public ListNode plusOne(ListNode head) {
        ListNode dummy = new ListNode(1);
        dummy.next = head;
        
        ListNode lastNon9 = dummy;
        ListNode go = head;
        while(go != null){
            if(go.val < 9) lastNon9 = go;
            go = go.next;
        }
        
        if(lastNon9.next != null){
            //6-7-9-9
            //  ^
            if(lastNon9 == dummy){   //9-9-9
                while(lastNon9.next != null){
                    lastNon9.next.val = 0;
                    lastNon9 = lastNon9.next;
                }
                return dummy;
            }else{  //1-2-9-9
                lastNon9.val++;
                while(lastNon9.next != null){
                    lastNon9.next.val = 0;
                    lastNon9 = lastNon9.next;
                }
                return head;
            }
        }else{  //1-9-8
            lastNon9.val++;
            return head;
        }
    }
}

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}
