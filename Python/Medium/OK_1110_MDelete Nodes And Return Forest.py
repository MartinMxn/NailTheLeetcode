# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = []
        to_delete = set(to_delete)
        
        def helper(root, parent_exist):
            if not root:
                return None
            if root.val in to_delete:
                root.left = helper(root.left, False)
                root.right = helper(root.right, False)
            else:
                if not parent_exist:    # if parent not exist, the current node will generate a new tree and add to res
                    res.append(root)
                root.left = helper(root.left, True)
                root.right = helper(root.right, True)
                return root
            
        helper(root, False)
        return res
                
