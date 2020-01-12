# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    find all even(not odd)-valued grandparent
    """
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0
    
        def dfs(root, p=1, gp=1):
            nonlocal res
            if not root:
                return 
            if root.val % 2 == 0:
                if root.left and root.left.left: res += root.left.left.val
                if root.left and root.left.right: res += root.left.right.val
                if root.right and root.right.left: res += root.right.left.val
                if root.right and root.right.right: res += root.right.right.val
            dfs(root.left)
            dfs(root.right)
            
        dfs(root)
        return res
    
