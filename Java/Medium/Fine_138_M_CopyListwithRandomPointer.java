/*
// Definition for a Node.
class Node {
    public int val;
    public Node next;
    public Node random;

    public Node() {}

    public Node(int _val,Node _next,Node _random) {
        val = _val;
        next = _next;
        random = _random;
    }
};
*/
class Solution {
    public Node copyRandomList(Node head) {
//         //1.O(n) space HashMap
//         if (head == null) return null;
//         HashMap<Node, Node> mapToCopy = new HashMap<>();
//         //create copy and put into map
//         Node cur = head;
//         while (cur != null) {
//             Node copyTmp = new Node(cur.val, null, null);
//             mapToCopy.put(cur, copyTmp);
//             cur = cur.next;
//         }
        
//         //copy both next and random
//         cur = head;
//         Node resHead = mapToCopy.get(cur);
//         while (cur != null) {
//             Node copyTmp = mapToCopy.get(cur);
//             copyTmp.next = mapToCopy.get(cur.next);
//             copyTmp.random = mapToCopy.get(cur.random);
//             cur = cur.next;
//         }
        
//         return resHead;
        
        //2.O(1)space
        // ! make clone node insert into original list
        // 1->1'->2-2'....
        // first go through for next, and second time for random
        // random: copy.next = ori.random.next
        if (head == null) return null;
        Node cur = head;
        
        // create copyNode and copy next
        while (cur != null) {
            Node copyNode = new Node(cur.val, null, null);
            copyNode.next = cur.next;
            cur.next = copyNode;
            cur = copyNode.next;
        }

        cur = head;
        //copy random
        while (cur != null) {
            cur.next.random = cur.random == null ? null : cur.random.next;
            cur = cur.next.next;
        }
        
        //divide the copy chain
        Node oriCur = head;
        Node copyCur = head.next;
        Node copyHead = copyCur;
        while (oriCur != null) {
            oriCur.next = oriCur.next.next;
            copyCur.next = oriCur.next == null ? null : oriCur.next.next;
            oriCur = oriCur.next;
            copyCur = copyCur.next;
        }
        
        return copyHead;
    }
}
