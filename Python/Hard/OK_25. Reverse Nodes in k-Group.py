# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    1 - 2 - 3 - 4 - 5
    1 ->2 ->3 ->4 ->5
               
    1 <-2 <-3 
            pre cur
               end will be deal with valid_count, if valid_count < k, reverse the interval
    """
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        valid_count = 0
        cur_node = head
        while cur_node and valid_count < k:
            cur_node = cur_node.next
            valid_count += 1
        if valid_count < k: # not enough node left
            return head
        
        def reverse(haed, count):
            prev, cur = None, head
            while count > 0:
                count -= 1
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return cur, prev
        
        new_head, prev = reverse(head, valid_count)
        head.next = self.reverseKGroup(new_head, k)
        
        return prev
        
                
                
            
            
