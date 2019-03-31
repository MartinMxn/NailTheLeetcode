/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 
 Monotonic stack
 from end to start order
 smaller than peek, peek is res[i]
 greater than peek, pop until find greater one, if not found
 push list.get(i) to stack
 */
class Solution {
    public int[] nextLargerNodes(ListNode head) {
        List<Integer> list = new ArrayList<>();
        for(ListNode n = head; n != null; n = n.next) list.add(n.val);
        int[] res = new int[list.size()];
        Stack<Integer> stack = new Stack<>();
        for(int i = res.length - 1; i >= 0; i--) {
            if(stack.isEmpty()) {
                stack.push(list.get(i));
                continue;
            }
            boolean found = false;
            while(!stack.isEmpty()) {
                if(stack.peek() <= list.get(i)) stack.pop();
                else {
                    res[i] = stack.peek();
                    stack.push(list.get(i));
                    found = true;
                    break;
                }
            }
            if(!found) stack.push(list.get(i));
        }
        return res;
    }
}
