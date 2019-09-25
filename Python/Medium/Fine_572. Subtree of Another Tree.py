# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    preorder 
    O(m*n)
    """
#     def same_tree(self, s, t):
#         if not s and not t:
#             return True
#         if not s or not t:
#             return False
#         if s.val == t.val:
#             return self.same_tree(s.left, t.left) and self.same_tree(s.right, t.right)
#         return False
        
#     def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
#         if not s and t:
#             return False
#         if self.same_tree(s, t): return True
    
#         return self.isSubtree(s.left, t) or self.isSubtree(s.right, t) 
    """
    O(m + n)
    by serialized two tree
    and string serach
    """
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        def serialize(node):
            if not node:
                return '#'
            l = serialize(node.left)
            r = serialize(node.right)
            node.se = '^' + str(node.val) + '$' + l + r
            return node.se
        
        
        return serialize(t) in serialize(s)
