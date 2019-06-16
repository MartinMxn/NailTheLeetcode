class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        queue to store the all cur level nodes 
            3  ->  [[3]]
           / \
          9  20  -> [3, [9, 20]]
         / \ / \
         .....   -> 
        """
        if not root:
            return []
        
        res = []
        cur_l = [root]
        
        while cur_l:
            tmp_nodes = []
            tmp_vals = []
            for node in cur_l:
                tmp_vals.append(node.val)
                if node.left:
                    tmp_nodes.append(node.left)
                if node.right:
                    tmp_nodes.append(node.right)
            cur_l = tmp_nodes
            res.append(tmp_vals)
            
        return res
