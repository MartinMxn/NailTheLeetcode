class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists == null || lists.length == 0) return null;
        PriorityQueue<ListNode> pq = new PriorityQueue<>((a,b) -> {
            return a.val - b.val;
        });

        for (ListNode node : lists) {
            if(node != null) {
                pq.add(node);
            }
        }

        ListNode head = new ListNode(-1);
        ListNode dummuy = head;

        while (!pq.isEmpty()) {
            ListNode tmp = pq.poll();
            dummuy.next = tmp;
            dummuy = dummuy.next;
            if (tmp.next != null) {
                pq.add(tmp.next);
            }
        }

        return head.next;
    }
}
