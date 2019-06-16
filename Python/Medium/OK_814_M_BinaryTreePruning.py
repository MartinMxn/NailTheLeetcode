# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def prune(node):
            if not node:
                return False
            left = prune(node.left)
            right = prune(node.right)
            if not left:
                node.left = None
            if not right:
                node.right = None
            if not left and not right and node.val != 1:
                return False
            return True
        
        prune(root)
        return root
