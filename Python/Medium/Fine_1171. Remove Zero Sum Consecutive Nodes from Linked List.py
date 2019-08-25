# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prefix = 0
        seen = collections.OrderedDict()
        cur = dummy
        
        while cur:
            prefix += cur.val
            node = seen.get(prefix, cur) # get the seen[prefix], if not just cur
            print(prefix)
            while prefix in seen:
                print('pop', seen.popitem()[0])
            seen[prefix] = node
            cur = cur.next
            node.next = cur
        
        return dummy.next
        
