# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        def find_max(node):
            nonlocal res
            if not node:
                return 0
            left = max(find_max(node.left), 0) # !
            right = max(find_max(node.right), 0)
            cur = left + right + node.val
            res = max(res, cur)
            return node.val + max(left, right)
        
        res = float('-inf')
        find_max(root)
        return res
