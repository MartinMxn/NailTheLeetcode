# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        """
        1. build connect map
        2. bfs search k time to see what kind fo node we could reach
        """
        con = collections.defaultdict(list);
        # 1 build map
        def dfs(parent, child):
            if parent and child:
                con[parent.val].append(child.val)
                con[child.val].append(parent.val)
            if child.left: dfs(child, child.left)
            if child.right: dfs(child, child.right)
        dfs(None, root)
        
        res = [target.val]
        seen = set(res)
        for i in range(K):
            res = [neigh for node in res for neigh in con[node] if neigh not in seen]
            seen = set(res) | seen
            
        return res
            
