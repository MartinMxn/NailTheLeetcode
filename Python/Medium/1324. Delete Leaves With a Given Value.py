# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def removeLeafNodes(self, root: TreeNode, x: int) -> TreeNode:
        if not root:
            return None
        
        # make left and right also none is child removed
        root.left = self.removeLeafNodes(root.left, x)
        root.right = self.removeLeafNodes(root.right, x)
        
        if root.val == x and not root.left and not root.right:
            return None
        
        return root
