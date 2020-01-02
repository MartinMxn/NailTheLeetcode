# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q = [root]
        res = 0
        
        while q:
            pre = q
            q = [child for node in q for child in [node.left, node.right] if child]
        
        return sum(map(lambda x: x.val, pre))
        
        
