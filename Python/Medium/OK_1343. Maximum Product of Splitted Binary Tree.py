# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        # 1. compute every node's sum and find the largest one
        sums = []
        
        def dfs(node):
            if not node: return 0
            cur_sum = node.val + dfs(node.left) + dfs(node.right)
            sums.append(cur_sum)
            return cur_sum
        
        total = dfs(root)
        return max(x * (total - x)for x in sums) % (10**9 + 7)
