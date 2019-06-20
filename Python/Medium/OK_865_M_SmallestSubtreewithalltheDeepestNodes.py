# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        """
        one-pass
        for each node, compared with global variable max_dep and record the node
        **we dont know the max_depth until come back to root, so need to return node, cur_max_depth**
        if left dep return == right dep, update node
        else return deeper one
        """
        
        def dfs(node):
            if not node:
                return None, 0
            left, right = dfs(node.left), dfs(node.right)
            
            if left[1] == right[1]:
                return node, left[1] + 1
            elif left[1] > right[1]:
                return left[0], left[1] + 1
            else:
                return right[0], right[1] + 1
            
        return dfs(root)[0]
                
            
            
