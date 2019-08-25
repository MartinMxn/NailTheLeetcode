# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        cur = dummy = ListNode(0)
        dummy.next = head
        seen = collections.OrderedDict()
        prefix = 0
        
        while cur:
            prefix += cur.val
            node = seen.get(prefix, cur) # the node we get here is actually the node before the first node we need to remove
            while prefix in seen: # pop the nodes between
                seen.popitem()
            seen[prefix] = node # update map, the node here make sure get the first node appeared
            cur = cur.next
            node.next = cur
            
        return dummy.next
