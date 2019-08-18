# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        """
        find the node and store the number of parent path node
        and continue to find the child node number
        get the max of these three and check whether beyond the half
        """
        count = [0, 0]
        def dfs(node):
            if not node:
                return 0
            left, right = dfs(node.left), dfs(node.right)
            if node.val == x:
                count[0], count[1] = left, right
            return left + right + 1
        # n - sum(count) - 1
        # whole subnode number of that node minus itself
        dfs(root)
        return max(max(count), n - sum(count) - 1) > n / 2
