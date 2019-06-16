# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        """
        level order reverse version
        """
        if not root:
            return []
        res = []
        cur_nodes = [root]
        
        while cur_nodes:
            cur_vals = []
            tmp_nodes = []
            
            for node in cur_nodes:
                if node:
                    cur_vals.append(node.val)
                if node and node.left:
                    tmp_nodes.append(node.left)
                if node and node.right:
                    tmp_nodes.append(node.right)
            cur_nodes = tmp_nodes
            res.append(cur_vals)

        return res[::-1]
