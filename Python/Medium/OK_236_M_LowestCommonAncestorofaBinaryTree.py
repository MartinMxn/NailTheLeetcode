# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        """
        idea: trace back from p and q to find the lca, so need a parent map
        1 build a relation map for each node, like {node: parent}
        2 try to trace back p to root and record the path with a set
        3 and then trace back from q to root until find 1st node in p's path set
        """
        # 1 build map
        r = {root: None}
        
        def build(node):
            if not node:
                return
            if node.left:
                r[node.left] = node
            if node.right:
                r[node.right] = node
            left = build(node.left)
            right = build(node.right)
        
        build(root)
        
        path = set()
        # 2 track p back to root and record path
        while p:
            path.add(p)
            p = r[p]
        # 3 from q
        while q:
            if q in path:
                return q
            q = r[q]
