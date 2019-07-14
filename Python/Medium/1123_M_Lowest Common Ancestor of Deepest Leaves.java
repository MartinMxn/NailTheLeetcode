# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        
        # return (depth, node)
        def helper(root):
            if not root:
                return 0, None
            ld, ln = helper(root.left)
            rd, rn = helper(root.right)
            
            if ld == rd:
                return ld + 1, root
            elif ld > rd: 
                return ld + 1, ln
            else:
                return rd + 1, rn
        
        return helper(root)[1]
