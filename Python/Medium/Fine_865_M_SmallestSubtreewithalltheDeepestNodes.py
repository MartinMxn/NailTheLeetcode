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
        find the max depth nodes
        depth_list = [
            [3], # depth 0
            [5, 1] # depth 1
        ]
        track each node back until find the common ancestor
        
        one-pass:
        return 2 value, based on the depth of left and right
        if equal return 
        """
        Res = collections.namedtuple("Res", ("node", "dep"))
        def dfs(node):
            if not node:
                return Res(None, 0)
            l, r = dfs(node.left), dfs(node.right)
            if l.dep == r.dep:
                return Res(node, l.dep + 1)
            if l.dep > r.dep:
                return Res(l.node, l.dep + 1)
            else:
                return Res(r.node, r.dep + 1)
        return dfs(root).node
            
