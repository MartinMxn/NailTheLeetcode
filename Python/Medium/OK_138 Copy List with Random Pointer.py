"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""

class Solution:
    """
    create mapping realtion by dict for each node
    if there's not clone node in dic, create the cloned one with val, copy, and random pointer
    O(n) time
    O(n) space
    """ 
#     def __init__(self):
#         self.m = {}
      
#     def get_clone_node(self, node):
#         if node:
#             if node in self.m:
#                 return self.m[node] 
#             else:
#                 clone_node = Node(node.val, node.next, node.random)
#                 self.m[node] = clone_node
#                 return clone_node
            
#         return None
        
#     def copyRandomList(self, head):
#         if not head:
#             return head
        
#         cur = head
#         new_node = Node(cur.val, None, None)
#         self.m[cur] = new_node
        
#         while cur:
#             new_node.random = self.get_clone_node(cur.random)
#             new_node.next = self.get_clone_node(cur.next)
#             new_node = new_node.next
#             cur = cur.next
        
#         return self.m[head]
    """
    O(1) space by inserting node between original nodes
    clarification: random pointer is always exist?
    c1 - cl1 - c2 - cl2 - c3 - cl3
    """
    def copyRandomList(self, head):
        cur = head
        
        # insert clone nodes
        while cur:
            nxt = cur.next
            clone_node = Node(cur.val, nxt, None)
            cur.next = clone_node
            cur = nxt
            
        # add random pointer to clone nodes
        cur = head
        while cur:
            cl = cur.next
            cl.random = cur.random.next if cur.random else None # ! random pointer may not exist
            cur = cur.next.next
        
        # build clone node list
        dummy = Node(0, None, None)
        p1, p2 = dummy, head
        while p2:
            p1.next = p2.next
            p1 = p1.next
            p2.next = p2.next.next
            p2 = p2.next
        
            
        return dummy.next
