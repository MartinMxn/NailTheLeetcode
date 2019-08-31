# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def rob(self, root: TreeNode) -> int:
        # misunderstanding, not level skip, but connection
#         if not root:
#             return 0
#         cur_r, cur_nr = root.val, 0
#         q = deque()
#         q.append(root)
#         while q:
#             pre_r = cur_r
#             for i in range(len(q)):
#                 cur = q.popleft()
#                 if cur.left: 
#                     q.append(cur.left)
#                 if cur.right: 
#                     q.append(cur.right)
#             cur_r = max(cur_nr, cur_nr + sum([i.val for i in q]))
#             cur_nr = max(cur_nr, pre_r)
        
#         return max(cur_r, cur_nr)
        
        # r, nr for each option
        # O(logn) 
        # O(logn)
        def dfs(root):
            if not root:
                return 0, 0
            left_r, left_nr = dfs(root.left)
            right_r, right_nr = dfs(root.right)
            cur_r = root.val + left_nr + right_nr
            cur_nr = max(left_r, left_nr) + max(right_r, right_nr) 
            # ! two max compare rob here, since we don't know the left/right rob or not which is better
            return cur_r, cur_nr
            
        return max(dfs(root))
