# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        # find max sum and try all sub_sum possible
        
        sums = []
        
        def dfs(node):
            if not node:
                return 0
            cur_sum = node.val + dfs(node.left) + dfs(node.right)
            sums.append(cur_sum)
            return cur_sum
    
        total = dfs(root)
        return max(s * (total - s) for s in sums) % (10 ** 9 + 7)
            
