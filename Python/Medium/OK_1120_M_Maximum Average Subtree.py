# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.res = 0
        
        def helper(root):
            if not root:
                return (0, 0)
            ln, ls = helper(root.left)
            rn, rs = helper(root.right)
            
            n = ln + rn + 1
            s = ls + rs + root.val
            self.res = max(self.res, s / n)
            return (n, s)
        
        helper(root)
        return self.res
