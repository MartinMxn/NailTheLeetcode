# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
1. build dict to cache child:parent relation
2. cache the path to node p back to root and then track q until find common node(with hashtable)
"""
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack = [root]
        # node: parent
        parent_dict = {root: None}
        
        # add key-value pair until we find both of them
        while p not in parent_dict or q not in parent_dict:
            node = stack.pop()
            if node.left:
                parent_dict[node.left] = node
                stack.append(node.left)
            if node.right:
                parent_dict[node.right] = node
                stack.append(node.right)
        
        ancestor = set()
        
        while p:
            ancestor.add(p)
            p = parent_dict[p]
        
        while q not in ancestor:
            q = parent_dict[q]
        
        return q
