# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        min_v = root.val
        self.ans = float('inf')
        
        def dfs(node):
            if not node:
                return
            if min_v < node.val < self.ans:
                self.ans = node.val
            dfs(node.right)
            dfs(node.left)
            
        dfs(root)
        return self.ans if self.ans != float('inf') else -1
