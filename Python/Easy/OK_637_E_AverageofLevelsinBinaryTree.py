# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import statistics
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        """
        level order traverse and calculate the avg
        """
        if not root:
            return []
        res = []
        cur_nodes = [root]
        
        while cur_nodes:
            tmp_nodes = []
            tmp_vals = []
            for node in cur_nodes:
                tmp_vals.append(node.val)
                if node.left:
                    tmp_nodes.append(node.left)
                if node.right:
                    tmp_nodes.append(node.right)
            cur_nodes = tmp_nodes
            res.append(sum(tmp_vals)/len(tmp_vals))
        
        return res
