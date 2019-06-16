# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = float('-inf')
        self.calcu(root)
        return self.res
        
    def calcu(self, root):
        if not root:
            return 0
        left = max(0, self.calcu(root.left))
        right = max(0, self.calcu(root.right))
        self.res = max(self.res, left + right + root.val)
        return max(left, right) + root.val
        

        
